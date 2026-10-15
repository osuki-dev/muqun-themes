# Credits

Original AI-generated fan artwork created with OpenAI image generation for Muqun Theme Collection. All bundled scenes and glyphs were newly generated; no game screenshots or extracted assets are included.

Hollow Knight and its characters belong to Team Cherry. This is an unofficial fan theme, not endorsed by Team Cherry. No rights to the underlying game are granted. [Official game website](https://www.hollowknight.com/).

See PROMPTS.md for art direction.

## Native adaptation (2026)

Original native template glyphs: `assets/icon-create.png`, `assets/icon-scan.png`, `assets/icon-settings.png`, `assets/icon-arrow.png`. Created for this theme in 2026 using geometric linework; retain the theme license. Existing back/send/attach artwork is unchanged.

The 2026 `assets/preview.png` is an original palette and UI composition rendered from this theme’s declared artwork. It is a gallery illustration, not a native device screenshot.

## Composer parameters (1.1.6)

`assets/icon-parameters.png` is an existing original Muqun template glyph reused
from lunar-aquarium. Creator: Muqun. Source:
https://github.com/osuki-dev/muqun-themes/tree/main/src/lunar-aquarium/assets/icon-parameters.png
Icon license: CC0-1.0. The rest of this theme retains its existing licensing.

The two open circular knobs match the delicate linework and concentric settings ring. This transparent sliders mask is
independently declared as `chrome.parameters`, with template tinting in both
light and dark modes. It does not replace or fall back to `chrome.settings`.
No illustration, palette, surface opacity or composer decoration is changed.

## Continuity review additions

`assets/composer-corner-continuity.png`: original transparent theme-specific corner ornament generated with OpenAI built-in image generation on 2026-10-13. The central draft and bottom control areas are clear.

Existing character, startup, glyph, palette, and gallery artwork were retained from the current published source. New artwork was copied without scripted image modification.

## 2026-10-15 startup and parameter artwork repair

Pack `echoes-of-hallownest` version `1.1.8`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with horn handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
