> Historical design record retained for provenance. See [REVISION.md](REVISION.md) for the current artwork and validation status.

# Asset provenance

## Home continuity candidate 1.2.3

The generated home-cover-continuity and home-paper continuity images are original fictional OpenAI image-generation artwork made on 2026-10-13 for Muqun Theme Collection. Cover references are this theme's own collection illustration. Wallpaper generation uses no third-party reference. License: the existing theme license. No script image editing was used. HOME-CONTINUITY.md records source review, responsive resolution, startup props and limitations. Published parameters/composer additions retain their original collection provenance.


All assets in this refreshed package are original and distributed under CC-BY-4.0.

- `assets/home-artwork.png`: original fictional adult scene generated for Muqun Theme Collection with OpenAI built-in image generation on 2026-10-11.
- `assets/launch.png`: independently generated centered fictional adult portrait, same tool/date. The launch is a separate composition, not a Home crop.
- `assets/empty.png`, seven `assets/icon-*.png`, four quiet wallpaper assets and six chrome decorations: original deterministic vector drawings authored for Muqun Theme Collection, rasterized with librsvg.
- `assets/preview.png`: authored representative Editorial Home composition from the final package artwork and light/dark tokens; not an App screenshot or a promise of layout selection.

Exact prompts and any targeted refinements are in ARTWORK.md. All refinement references are this commission's own generated art; no external reference imagery or third-party marks are included. Proportional resizing and small transparent edge margins are used for package sizing. Superseded miniature scenery and object illustrations are absent.

## 2026-10-15 startup and parameter artwork repair

Pack `the-last-reading-room` version `1.2.5`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with book handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"home-composer-compact","fit":"contain","opacity":0.38,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":4}}` | none |
| light | regular | `{"asset":"home-composer-regular","fit":"contain","opacity":0.38,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":4}}` | none |
| dark | compact | `{"asset":"home-composer-compact","fit":"contain","opacity":0.5,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":4}}` | none |
| dark | regular | `{"asset":"home-composer-regular","fit":"contain","opacity":0.5,"focalPoint":{"x":0.5,"y":1},"outset":{"left":0,"right":0,"bottom":4}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.

- `assets/hero-compact-wide.png`: OpenAI built-in image generation edit of this pack's original `hero.png`, 2026-10-28; original subject/style retained, centered complete composition on wide transparent canvas. Prompt: Technical reframing only; preserve complete bodies, feet, props, faces and style; wide 2:1 genuine-alpha canvas, central 48% subject width, large transparent side margins, no crop, no backdrop, no new subjects. Generated source: `exec-98b4bf3d-9267-4ae5-b58b-c5608194c197.png`.
