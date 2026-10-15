# Credits

- `assets/background-light.png` and `assets/background-dark.png` — separate dawn and moonlit environment layers created for Muqun; no external source artwork used.
- `assets/hero-light.png` and `assets/hero-dark.png` — separate transparent, contain-fit character layers created for Muqun and relit for their respective modes.
- `assets/icon-back.png`, `assets/icon-send.png`, and `assets/icon-attach.png` — original brush-shaped template glyphs created for this theme.
- `assets/preview.png` — composed from the generated banner and the theme's own palette.

## 2026-09-24 interface extension

The new `icon-*.png` files are original vector drawings exported to transparent template PNGs, with details tailored to this pack. `chrome-light.png` and `chrome-dark.png` are original geometric vector chrome accents. No outside source art was used for these additions.

## Parameters glyph (1.1.7)

`assets/icon-parameters.png` reuses the original transparent adjustments glyph
from Pine & Parchment (`src/pine-and-parchment/assets/icon-parameters.png`).
Creator: Muqun. Source: [Muqun Theme Collection](https://github.com/osuki-dev/muqun-themes/tree/main/src/pine-and-parchment).
Source artwork license: CC-BY-4.0; reused within the collection for this
theme update. The packaged bytes and alpha are unchanged. This is a dedicated
`chrome.parameters` template asset; the existing settings glyph stays separate.

## Continuity review additions

`assets/composer-corner-continuity.png`: original transparent theme-specific corner ornament generated with OpenAI built-in image generation on 2026-10-13. The central draft and bottom control areas are clear.

Existing character, startup, glyph, palette, and gallery artwork were retained from the current published source. New artwork was copied without scripted image modification.

## 2026-10-15 startup and parameter artwork repair

Pack `musashi-book-of-void` version `1.1.9`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with ink-diamond handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
