"""Run with python -m unittest discover -s scripts -p 'test_*.py'."""

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("covers", Path(__file__).with_name("generate-preview-covers.py"))
covers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(covers)


class PreviewCoversTest(unittest.TestCase):
    def theme(self):
        colors = dict(background="#FFFFFF", surface="#DDDDDD", surfaceRaised="#CCCCCC",
                      text="#111111", primary="#2244FF", success="#00AA55", warning="#FFAA00")
        return dict(id="fixture", version="1.2.3", preview="preview",
                    assets={"preview": {"path": "preview.png"}},
                    variants={"light": {"colors": colors}, "dark": {"colors": {**colors, "background": "#000000"}}})

    def pixel(self, image, x, y):
        return covers.run(image, "-format", f"%[hex:p{{{x},{y}}}]", "info:").decode()[:6]

    def test_color_only_preview_and_idempotent_update(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            theme = self.theme()
            manifest = root / "theme.json"
            manifest.write_text(json.dumps(theme))
            covers.run("-size", "8x8", "xc:red", root / "preview.png")
            covers.generate(root, root / "output", write=True)
            first = manifest.read_bytes()
            updated = json.loads(first)
            image = root / "preview.png"
            self.assertEqual(covers.run(image, "-format", "%wx%h", "info:"), b"1024x640")
            self.assertEqual(self.pixel(image, 100, 100), "FFFFFF")
            self.assertEqual(self.pixel(image, 600, 100), "000000")
            self.assertEqual(self.pixel(image, 260, 600), "2244FF")
            self.assertEqual(updated["version"], "1.2.4")
            self.assertEqual(updated["assets"]["preview"]["sha256"], hashlib.sha256(image.read_bytes()).hexdigest())
            covers.generate(root, root / "output", write=True)
            self.assertEqual(manifest.read_bytes(), first)

    def test_foreground_contain_preserves_portrait_and_transparency(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            # Tall subject with uniquely coloured extremities; cover/stretch would lose/change them.
            covers.run("-size", "100x400", "xc:none", "-fill", "red", "-draw", "rectangle 25,0 74,39",
                       "-fill", "blue", "-draw", "rectangle 25,360 74,399", root / "art.png")
            theme = self.theme()
            theme["assets"]["art"] = {"path": "art.png"}
            covers.layer(root, theme, {"asset": "art", "fit": "cover"}, 400, 400, root / "layer.png", foreground=True)
            self.assertEqual(self.pixel(root / "layer.png", 200, 10), "FF0000")
            self.assertEqual(self.pixel(root / "layer.png", 200, 390), "0000FF")
            self.assertEqual(covers.run(root / "layer.png", "-format", "%[fx:p{0,0}.a]", "info:"), b"0")

    def test_explicit_null_and_mode_override(self):
        theme = {"decoration": {"home.artwork": {"asset": "base"}},
                 "variantDecorations": {"light": {"home.artwork": None}, "dark": {"home.artwork": {"asset": "dark"}}}}
        self.assertIsNone(covers.decoration(theme, "light", ("home.artwork",)))
        self.assertEqual(covers.decoration(theme, "dark", ("home.artwork",)), {"asset": "dark"})

    def test_unknown_wallpaper_alias_does_not_override_canonical_slot(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            covers.run("-size", "8x8", "xc:#00FF00", root / "wallpaper.png")
            for slot in ("home.wallpaper", "shell.wallpaper"):
                with self.subTest(slot=slot):
                    theme = self.theme()
                    theme["assets"]["wallpaper"] = {"path": "wallpaper.png"}
                    theme["decoration"] = {
                        "home.background": {"asset": "missing-legacy-home"},
                        "shell.background": {"asset": "missing-legacy-shell"},
                        slot: {"asset": "wallpaper"},
                    }
                    image = root / "cover.png"
                    covers.render(root, theme, image)
                    self.assertEqual(self.pixel(image, 100, 100), "00FF00")
                    self.assertEqual(self.pixel(image, 600, 100), "00FF00")

    def test_color_foreground_remains_colored_on_grayscale_backgrounds(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            covers.run("-size", "100x400", "xc:none", "-fill", "red", "-draw", "rectangle 25,0 74,39",
                       "-fill", "blue", "-draw", "rectangle 25,360 74,399", root / "art.png")
            theme = self.theme()
            theme["assets"]["art"] = {"path": "art.png"}
            theme["decoration"] = {"home.artwork": {"asset": "art"}}
            image = root / "cover.png"
            covers.render(root, theme, image)
            for x in (256, 768):
                self.assertEqual(self.pixel(image, x, 40), "FF0000")
                self.assertEqual(self.pixel(image, x, 520), "0000FF")


if __name__ == "__main__":
    unittest.main()
