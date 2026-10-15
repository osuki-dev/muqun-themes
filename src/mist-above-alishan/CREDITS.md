# Mist above Alishan

## Home continuity candidate 1.1.7

The generated home-cover-continuity and home-paper continuity images are original fictional OpenAI image-generation artwork made on 2026-10-13 for Muqun Theme Collection. Cover references are this theme's own collection illustration. Wallpaper generation uses no third-party reference. License: the existing theme license. No script image editing was used. HOME-CONTINUITY.md records source review, responsive resolution, startup props and limitations. Published parameters/composer additions retain their original collection provenance.


Original AI-generated artwork created with OpenAI image generation for the Muqun Theme Collection. All rights reserved. Prompts are recorded in PROMPTS.md.

The illustrations interpret Alishan tea terraces, cypress forests, mist and the forest railway. They are original stylized landscapes, not location photographs or maps.

Landscape research: [Alishan National Scenic Area](https://www.ali-nsa.net/en/) and [Alishan Forest Railway](https://recreation.forest.gov.tw/en/Forestry/FR?typ=11&typ_id=0900041). No third-party imagery is bundled.

The standalone Home hero is original AI-generated artwork created with OpenAI image generation. It is a separate composition from the preserved empty-state illustration. Its creative brief is recorded in PROMPTS.md.

## Native adaptation 1.1.3

`assets/icon-create.png`, `assets/icon-scan.png`, `assets/icon-settings.png`, and `assets/icon-arrow.png` are original vector glyphs authored for this theme and rasterized to transparent 128×128 PNG with ImageMagick. Rounded botanical strokes with one tea leaf. No third-party source or reference artwork was used. Covered by the theme’s existing license. Existing illustrations are unchanged. `home.arrow` visibly points up-right; its direction metadata declares that source orientation.

`assets/preview.webp` is a deterministic light/dark gallery composition of the existing foreground artwork, final palette and native control glyphs. It is a concept preview, not a device screenshot.

## Contemporary redraw 1.1.4

The previous miniature Home, empty and scenic wallpaper assets were retired from this package. The two new original illustrations (`assets/home-railway.png` and `assets/launch-train.png`) were created with the built-in image_gen tool on 2026-10-11 without third-party visual inputs. Both contain genuine RGBA transparency. Covered by the theme’s existing license. Source generations were copied without crop, recoloring or painting. Full prompts are in PROMPTS.md. Startup is an independent square illustration; Home is an independent 1536×1024 landscape scene. Gallery preview is a deterministic composition of these final assets and palette, not a native screenshot.

Final redraw revision: the packaged Home/startup illustrations were drawn by the built-in image_gen tool from this theme’s own original generated scene drafts. Their scene composition is retained with visibly drawn outlines, cel shading and simplified color planes. No third-party images were used. The earlier detailed drafts were rejected and are not packaged. Full final prompts are in PROMPTS.md.

## Integrated Home and composer update

The new cover/sky/composer and gallery artwork is original fictional artwork generated with the OpenAI built-in image generation tool, using this collection’s existing artwork as the reference. Exact prompts are in COVER-PROMPTS.md. No third-party source was added. License: All rights reserved.

## 2026-10-15 startup and parameter artwork repair

Pack `mist-above-alishan` version `1.1.9`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with rail handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-accent","fit":"contain","opacity":0.18,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-accent","fit":"contain","opacity":0.18,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-accent","fit":"contain","opacity":0.18,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-accent","fit":"contain","opacity":0.18,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
