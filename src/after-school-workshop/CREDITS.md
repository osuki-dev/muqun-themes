# After School Workshop artwork credits

All rights reserved. Original assets created for Muqun Theme Collection.

Full youthful 2D editorial redraw on 2026-10-11. `assets/home-story.png` is original AI-generated story illustration, and `assets/launch-character.png` is separately generated startup character art. Both used OpenAI built-in image generation with genuine transparent output; deterministic trim, resize and transparent padding only. Full prompts are in PROMPTS.md.

`assets/paper-light.png`, `assets/paper-dark.png`, and edge textures are original geometric artwork authored for this theme. Seven native line glyphs reuse the original Muqun Theme Collection geometric family authored during the 2026 Clockwork Harlequin redraw, under the same ownership and rights. Directions: left back, up send, up-right Home arrow.

`assets/preview.png` is an original gallery composition of the final theme art and UI palette, not a device screenshot. No old machinery, diorama or miniature prop art is retained. No external stock image or third-party brand assets are bundled.

## Composer preview additions

`assets/composer-accent-compact.png` and `assets/composer-accent-regular.png` are original OpenAI built-in imagegen illustrations generated for this theme with real transparency. Only proportional resizing and metadata removal followed generation. Existing Home art and palette remain unchanged. `assets/icon-parameters.png` reuses the collection-owned Pine and Parchment rounded sliders template glyph, under the collection rights above. The rejected generated sliders candidate is not bundled.

## Home lower-silhouette repair

`assets/home-story.png` was subsequently edited with OpenAI built-in imagegen to complete interrupted lower anatomy and scene edges, preserving the original character/style/pose. It is a real-alpha vignette retaining a diffuse semi-transparent halo. Original launch artwork remains unchanged. The local preview remains the previous composition pending the parent review; no gallery files changed.

## Composer composition revision

New original built-in imagegen artwork introduces a distinct composer arrangement. Tiny Workshop and Mint Soda Interlude add a separate transparent overhang, proportionally resized and padded so the rim is at 75% canvas height. After School Workshop and Graphite Daydream replace the corner accent with side/lower stationery. No artwork was programmatically drawn. Home repairs and launch art remain preserved.

## Gallery refresh

The gallery preview is now an original built-in imagegen pure-art composition of the complete courtyard scene and both sneakers, light left/dark right. It is1024×640, no app UI, commands, developer logs or test output. Proportional resizing and one-pixel edge padding achieved exact dimensions without stretching.

## Continuity update

- `assets/environment-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.
- `assets/gallery-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.

No third-party reference images or marks were used. See CONTINUITY-PROMPTS.md for constraints and source-review limits.

- `assets/home-cover-light.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.
- `assets/home-cover-dark.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.

## 2026-10-15 startup and parameter artwork repair

Pack `after-school-workshop` version `1.1.13`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-full.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with notebook handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
