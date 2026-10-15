# Fern and Fiord artwork credits

All rights reserved. Original assets created for Muqun Theme Collection.

Full youthful 2D editorial redraw on 2026-10-11. `assets/home-story.png` is original AI-generated story illustration, and `assets/launch-character.png` is separately generated startup character art. Both used OpenAI built-in image generation with genuine transparent output; deterministic trim, resize and transparent padding only. Full prompts are in PROMPTS.md.

`assets/paper-light.png`, `assets/paper-dark.png`, and edge textures are original geometric artwork authored for this theme. Seven native line glyphs reuse the original Muqun Theme Collection geometric family authored during the 2026 Clockwork Harlequin redraw, under the same ownership and rights. Directions: left back, up send, up-right Home arrow.

`assets/preview.png` is an original gallery composition of the final theme art and UI palette, not a device screenshot. No old machinery, diorama or miniature prop art is retained. No external stock image or third-party brand assets are bundled.

## Full-page environment revision

New environment illustrations are original fictional artwork generated for Muqun Theme Collection with the OpenAI built-in image generation tool, using this theme artwork as reference. No third-party imagery or marks introduced. License: All rights reserved. See generation prompts and DESIGN-REVIEW.md for review limits.

## 2026-10-15 startup and parameter artwork repair

Pack `fern-and-fiord` version `1.1.9`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-full.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with paddle handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | none | none |
| light | regular | none | none |
| dark | compact | none | none |
| dark | regular | none | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
