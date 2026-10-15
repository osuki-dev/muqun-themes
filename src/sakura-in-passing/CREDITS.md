# Sakura, in Passing — artwork credits

All currently declared illustrations are original fictional2D anime/editorial artwork generated for Muqun Theme Collection with OpenAI built-in image generation. Home is an illustrated natural activity scene; launch is an independently generated transparent character composition. No third-party artwork or software marks are included. Original geometric template glyphs and subtle edge/contour patterns were authored deterministically for this collection.

License: All rights reserved.

Retired miniature scenery and previous poster/diorama art are no longer distributed. See PROMPTS.md for the exact generation prompts.

## Integrated Home and composer update

The new cover/sky/composer and gallery artwork is original fictional artwork generated with the OpenAI built-in image generation tool, using this collection’s existing artwork as the reference. Exact prompts are in COVER-PROMPTS.md. No third-party source was added. License: All rights reserved.

## Full-page environment revision

New environment illustrations are original fictional artwork generated for Muqun Theme Collection with the OpenAI built-in image generation tool, using this theme artwork as reference. No third-party imagery or marks introduced. License: All rights reserved. See generation prompts and DESIGN-REVIEW.md for review limits.

## 2026-10-15 startup and parameter artwork repair

Pack `sakura-in-passing` version `1.2.5`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with blossom handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-compact","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| light | regular | `{"asset":"composer-regular","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | compact | `{"asset":"composer-compact","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | regular | `{"asset":"composer-regular","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
