# Gentian above the Clouds

Original AI-generated artwork for Muqun Theme Collection. All rights reserved.

Artwork and chrome glyphs generated with OpenAI image generation; prompts are in PROMPTS.md.

Home hero (`assets/home-hero.png`): original AI-generated artwork created with the built-in image generation tool for Muqun Theme Collection. Swiss Alps, a violet-and-ivory mountain railway locomotive crossing a small curved stone viaduct above soft layered clouds, miniature alpine chalet beside one end. The scene is an imaginative illustration, not a precise location reconstruction. Covered by this theme’s existing license.

## Native adaptation 1.1.4

`assets/icon-create.png`, `assets/icon-scan.png`, `assets/icon-settings.png`, and `assets/icon-arrow.png` are original vector glyphs authored for this theme and rasterized to transparent 128×128 PNG with ImageMagick. Angular alpine edges with a small mountain peak. No third-party source or reference artwork was used. Covered by the theme’s existing license. Existing illustrations are unchanged. `home.arrow` visibly points up-right; its direction metadata declares that source orientation.

`assets/preview.png` is a deterministic light/dark gallery composition of the existing foreground artwork, final palette and native control glyphs. It is a concept preview, not a device screenshot.

## Contemporary character redraw 1.1.5

The previous miniature scenery and wallpaper assets were retired. `assets/home-scene.png` and `assets/launch-traveler.png` are original built-in image_gen illustrations. Home was generated from an original authored scene brief; independent startup used that original generated Home character as its only identity reference. No third-party visual inputs were used. Both packaged PNGs preserve generated RGBA alpha and are copied without crop, painting or recoloring. Original SVG control glyphs were authored for this theme and rasterized to transparent PNG: back/send/attach/create/scan/settings/arrow. Template tint follows the palette; arrow visibly points up-right and declares that source direction. Artwork and glyphs are covered by the theme’s existing license. The 1024×640 gallery preview is fictional, composed from final assets and palette, not an App screenshot. Full image prompts are in PROMPTS.md.

## Parameters glyph (1.1.8)

`assets/icon-parameters.png` reuses the original transparent adjustments glyph
from Pine & Parchment (`src/pine-and-parchment/assets/icon-parameters.png`).
Creator: Muqun. Source: [Muqun Theme Collection](https://github.com/osuki-dev/muqun-themes/tree/main/src/pine-and-parchment).
Source artwork license: CC-BY-4.0; reused within the collection for this
theme update. The packaged bytes and alpha are unchanged. This is a dedicated
`chrome.parameters` template asset; the existing settings glyph stays separate.

## Continuity review additions

`assets/scenery-light-continuity.png`: original scenery companion generated with OpenAI built-in image generation on 2026-10-13; theme-owned reference artwork only.

`assets/scenery-dark-continuity.png`: original scenery companion generated with OpenAI built-in image generation on 2026-10-13; theme-owned reference artwork only.

`assets/composer-corner-continuity.png`: original transparent theme-specific corner ornament generated with OpenAI built-in image generation on 2026-10-13. The central draft and bottom control areas are clear.

Existing character, startup, glyph, palette, and gallery artwork were retained from the current published source. New artwork was copied without scripted image modification.

## 2026-10-15 startup and parameter artwork repair

Pack `gentian-above-the-clouds` version `1.1.10`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with mountain handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.24,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"composer-corner-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
