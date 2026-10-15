# Graphite Daydream artwork credits

- `assets/artist.png`: original AI-generated artwork made for this theme with OpenAI's built-in image generation tool on 2026-10-10, then refined through a targeted edit. Creator: Muqun Project with OpenAI image generation. No external illustration is bundled. Licence: All rights reserved.
- `assets/preview.png`: gallery composition of the theme's original artist and its authored light/dark palette; created locally by Muqun Project. Licence: All rights reserved. It is a design preview, not an app screenshot.

The user-supplied reference was examined only for warm paper and confident pencil linework; its character, pose, costume and signature were not reused, and the reference is not packaged.

## Initial generation prompt

Additional original code-native UI graphics: seven pencil-stroke template icons, paper fiber wallpaper plates, restrained chrome rules, card corners, button hatching, tab rules, and the empty-state sketchbook symbol. These are authored by Muqun Project, rasterized to PNG, with no third-party assets. Licence: All rights reserved.

`assets/launch.png`: independent OpenAI imagegen edit of the original artist into a seated pose with open sketchbook. Same creator and licence as the Home portrait.

## Independent launch generation prompt

Use case: illustration-story. Edit the original Graphite Daydream artist into a genuinely independent STARTUP illustration, keeping her identity: adult woman age26 with expressive manga face, round glasses, tousled brown bob, modest ivory blouse and taupe cardigan, graphite contour and sparse sepia crosshatching. Change the pose and framing: waist-up artist seated, facing slightly left, looking down warmly at an OPEN sketchbook, one hand supporting the open book and the other holding a pencil over the page. Both hands clearly drawn and anatomically correct. Wide gentle arc silhouette; entire head, book and hands within the frame, generous transparent margin. No desk rectangle or background objects, no text or sketch writing. Flat warm ivory opaque character fills for both light/dark backgrounds. True transparent alpha outside subject, absolutely no shadow/glow/haze/paper rectangle, isolated anime pencil illustration. This is different from the standing portrait holding a closed book.

Use case: illustration-story. Asset type: transparent foreground for Muqun anime theme Graphite Daydream. Create an original adult woman artist, age 26, charming lively expression, round wire-rim glasses, short tousled brown bob, cream modest collared blouse and loose warm taupe cardigan, holding a closed ivory sketchbook against her chest with one arm and a graphite pencil in the other hand. Three-quarter waist-up portrait, entire head/hair/hands/sketchbook included with generous clear alpha padding all around, gently angled posture, smiling thoughtful gaze. Premium hand-drawn manga graphite contour illustration: confident expressive dark pencil linework with delicate crosshatching, warm ivory solid fills within the character so it reads over dark backgrounds, a few restrained sepia watercolor touches, tactile paperlike texture ONLY inside painted subject, no rectangular paper background. Keep strong silhouette and refined attractive adult face, anatomically correct hands. Transparent background, isolated subject, no scene, no writing, no UI, no logos, no watermark, no rabbit ears, no bunny costume, no lingerie.

## Refinement prompt

undefined

## Full-page environment revision

New environment illustrations are original fictional artwork generated for Muqun Theme Collection with the OpenAI built-in image generation tool, using this theme artwork as reference. No third-party imagery or marks introduced. License: All rights reserved. See generation prompts and DESIGN-REVIEW.md for review limits.

## 2026-10-15 startup and parameter artwork repair

Pack `graphite-daydream` version `1.0.5`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with pencil handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
