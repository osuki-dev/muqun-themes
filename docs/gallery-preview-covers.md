# UI-independent gallery covers

The gallery displays the static image named by `theme.json`'s `preview` asset.
The CLI copies the packed image to `dist/previews/`; it does not render a Home
screen. Old session buttons and workspace labels were baked into source PNGs.
Changing a browser preview template cannot remove them.

`scripts/generate-preview-covers.py` replaces that one-off composition process
with an intentionally UI-independent cover. It only reads local, declared
artwork and palette colours. There are no fonts, names, sample text, session
cards, toolbars, model selectors or action buttons in its drawing operations.

## Composition

- 1024x640, light on the left and dark on the right.
- Each half starts with its variant's opaque background colour. A declared
  Home wallpaper (or shell fallback) composites on top with its authored
  opacity and fit. Only the canonical `home.wallpaper` and `shell.wallpaper`
  slot names are recognised; explicit null disables a layer.
- Home foreground artwork, with launch/empty artwork as fallback only when
  absent, is contain-fit within 464x520. This preserves an entire portrait or
  landscape subject, including transparent margins. The cover intentionally
  does not reproduce any App layout's cropping or size.
- Six plain rectangular paint samples show surface, raised surface, text,
  primary, success and warning colours. They have no labels or interaction.
- Missing artwork slots produce a palette-only cover. A declared missing
  file is an error, not a silent substitute for a broken theme package.

Mode-specific artwork, compact overrides, alpha and explicit zero opacity
are respected. Wallpaper cover crops use focal points; contain never
stretches a subject. Tiled wallpaper stays tiled. Transparent areas reveal
the variant background, never a checkerboard.

## Commands

Requires Python 3.9+ and ImageMagick 7 (`magick` on PATH); no Python packages,
network access, fonts, browser, simulator or image-generation API is needed.

```sh
python scripts/generate-preview-covers.py sugar-circuit
python scripts/generate-preview-covers.py sugar-circuit --write
python scripts/generate-preview-covers.py --all --write --jobs 4
python -m unittest discover -s scripts -p 'test_*.py'
```

Outputs go to ignored `dist/cover-previews/` by default. PNG and lossless WebP
retain each theme's declared preview path/format. `--write` changes only that
asset, its SHA-256 and the manifest patch version. It skips these writes when
the generated image is identical. Run validation and the source repository's
normal packing gate afterwards. The generator does not publish or change the
release index. Asset composition may differ after an ImageMagick upgrade;
review a representative sample before updating a collection.

For another worktree, use `--source-root /path/to/worktree/src --output
/path/to/worktree/dist/cover-previews`, and name only the themes owned by that
worktree. Do not overwrite another agent's sources.

## Review boundaries

This is a gallery cover, not proof of App readability, contrast, clipping or
interaction. Test those independently on actual layouts. The compositor
does not erase text already drawn into a source illustration; such an asset
needs a separately authored text-free version. Never use an old flattened
preview as a foreground asset, or fake UI will be reproduced.

Source illustrations remain untouched. They retain their existing credits;
the preview is a deterministic composition of those same licensed assets.
