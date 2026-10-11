#!/usr/bin/env python3
"""Compose UI-independent gallery covers from existing theme art (ImageMagick 7)."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MISSING = object()


def run(*args):
    return subprocess.run(["magick", *map(str, args)], check=True, capture_output=True).stdout


def decoration(theme, mode, names):
    base = theme.get("decoration") or {}
    variant = (theme.get("variantDecorations") or {}).get(mode) or {}
    for name in names:
        spec = variant.get(name, base.get(name, MISSING))
        if spec is MISSING:
            continue
        if spec is None:
            return None
        compact = spec.get("compact", MISSING)
        return spec if compact is MISSING else compact
    return None


def asset_path(directory, theme, asset):
    path = (directory / theme["assets"][asset]["path"]).resolve()
    if not path.is_relative_to(directory.resolve()) or not path.is_file():
        raise ValueError(f"Invalid local asset path: {asset}")
    return path


def layer(directory, theme, spec, width, height, output, foreground=False):
    source = asset_path(directory, theme, spec["asset"])
    # Gallery foregrounds always contain the complete artwork; this is not Home geometry.
    fit = "contain" if foreground else spec.get("fit", "cover")
    args = [source, "-auto-orient", "-colorspace", "sRGB"]
    if fit == "tile":
        args = ["-size", f"{width}x{height}", f"tile:{source}"]
    else:
        args += ["-resize", f"{width}x{height}" + ("^" if fit == "cover" else "")]
        # Center the complete foreground. Wallpaper crops follow the authored focal point.
        if fit == "cover":
            size = run(*args, "-format", "%w %h", "info:").decode().split()
            focal = spec.get("focalPoint", {"x": 0.5, "y": 0.5})
            x = round((int(size[0]) - width) * focal["x"])
            y = round((int(size[1]) - height) * focal["y"])
            args += ["-crop", f"{width}x{height}+{x}+{y}", "+repage"]
        args += ["-gravity", "center", "-background", "none", "-extent", f"{width}x{height}"]
    args += ["-alpha", "on", "-channel", "A", "-evaluate", "multiply", str(spec.get("opacity", 1)), "+channel", output]
    run(*args)


def render(directory, theme, output):
    with tempfile.TemporaryDirectory(prefix="muqun-cover-") as temp:
        temp = Path(temp)
        halves = []
        for mode in ("light", "dark"):
            colors = theme["variants"][mode]["colors"]
            half = temp / f"{mode}.png"
            run("-size", "512x640", f"xc:{colors['background']}", half)
            wallpaper = decoration(theme, mode, ("home.wallpaper", "shell.wallpaper"))
            if wallpaper:
                image = temp / f"{mode}-wallpaper.png"
                layer(directory, theme, wallpaper, 512, 640, image)
                run(half, "-colorspace", "sRGB", image, "-compose", "over", "-composite", half)
            art = decoration(theme, mode, ("home.artwork", "launch.artwork", "empty.artwork"))
            if art:
                image = temp / f"{mode}-art.png"
                layer(directory, theme, art, 464, 520, image, foreground=True)
                run(half, "-colorspace", "sRGB", image, "-geometry", "+24+24", "-compose", "over", "-composite", half)
            # Six flat paint samples, deliberately not cards, buttons, text or toolbar glyphs.
            args = [half]
            for index, role in enumerate(("surface", "surfaceRaised", "text", "primary", "success", "warning")):
                x = 24 + index * 78
                args += ["-fill", colors[role], "-draw", f"rectangle {x},588 {x+73},611"]
            run(*args, half)
            halves.append(half)
        output.parent.mkdir(parents=True, exist_ok=True)
        args = [*halves, "+append", "-strip"]
        if output.suffix.lower() == ".webp":
            args += ["-define", "webp:lossless=true"]
        else:
            args += ["-define", "png:exclude-chunks=date,time"]
        run(*args, output)


def generate(directory, output_dir, write=False):
    manifest_path = directory / "theme.json"
    theme = json.loads(manifest_path.read_text())
    preview = theme["assets"][theme["preview"]]
    target = asset_path(directory, theme, theme["preview"])
    output = output_dir / (theme["id"] + target.suffix)
    render(directory, theme, output)
    data = output.read_bytes()
    changed = data != target.read_bytes()
    if write and changed:
        version = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", theme["version"])
        if not version:
            raise ValueError(f"Cannot increment version: {theme['version']}")
        major, minor, patch = version.groups()
        theme["version"] = f"{major}.{minor}.{int(patch)+1}"
        preview["sha256"] = hashlib.sha256(data).hexdigest()
        shutil.copyfile(output, target)
        manifest_path.write_text(json.dumps(theme, ensure_ascii=False, indent=2) + "\n")
    return f"{theme['id']}: {'updated' if write and changed else 'unchanged' if not changed else 'previewed'} {output}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("themes", nargs="*", help="Theme directory names under src/")
    parser.add_argument("--all", action="store_true", help="Select all existing source themes")
    parser.add_argument("--write", action="store_true", help="Replace declared previews, update hashes, bump changed versions")
    parser.add_argument("--source-root", type=Path, default=ROOT / "src", help="Source directory in this or another isolated worktree")
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "cover-previews")
    parser.add_argument("--jobs", type=int, default=4)
    options = parser.parse_args()
    if not shutil.which("magick"):
        parser.error("ImageMagick 7 (magick) is required")
    if options.all == bool(options.themes):
        parser.error("Choose theme names or --all")
    names = sorted(p.parent.name for p in options.source_root.glob("*/theme.json")) if options.all else options.themes
    if any(not re.fullmatch(r"[a-z][a-z0-9-]*", name) for name in names):
        parser.error("Theme names must be source directory IDs")
    if not 1 <= options.jobs <= 8:
        parser.error("--jobs must be between 1 and 8")
    with ThreadPoolExecutor(max_workers=options.jobs) as pool:
        for message in pool.map(lambda name: generate(options.source_root / name, options.output, options.write), names):
            print(message, flush=True)


if __name__ == "__main__":
    main()
