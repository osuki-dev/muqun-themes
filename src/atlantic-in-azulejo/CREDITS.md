# Atlantic in Azulejo — artwork credits

All currently declared illustrations are original fictional2D anime/editorial artwork generated for Muqun Theme Collection with OpenAI built-in image generation. Home is an illustrated natural activity scene; launch is an independently generated transparent character composition. No third-party artwork or software marks are included. Original geometric template glyphs and subtle edge/contour patterns were authored deterministically for this collection.

License: All rights reserved.

Retired miniature scenery and previous poster/diorama art are no longer distributed. See PROMPTS.md for the exact generation prompts.

## Integrated Home and composer update

The new cover/sky/composer and gallery artwork is original fictional artwork generated with the OpenAI built-in image generation tool, using this collection’s existing artwork as the reference. Exact prompts are in COVER-PROMPTS.md. No third-party source was added. License: All rights reserved.

## 2026-10 full-page continuity

Additional environmental wallpaper and corrected full-prop artwork generated with OpenAI imagegen from the existing theme art. Exact prompts are recorded in ENVIRONMENT-PROMPTS.md. Existing subject artwork and published icon/composer provenance are retained.

## 2026-10-15 startup and parameter artwork repair

Pack `atlantic-in-azulejo` version `1.4.2`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-full.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with tile handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-corners","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-corners","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-corners","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-corners","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
