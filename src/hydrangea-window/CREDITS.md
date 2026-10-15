# Asset provenance

All assets in this refreshed package are original and distributed under CC-BY-4.0.

- `assets/home-artwork.png`: original fictional adult scene generated for Muqun Theme Collection with OpenAI built-in image generation on 2026-10-11.
- `assets/launch.png`: independently generated centered fictional adult portrait, same tool/date. The launch is a separate composition, not a Home crop.
- `assets/empty.png`, seven `assets/icon-*.png`, four quiet wallpaper assets and six chrome decorations: original deterministic vector drawings authored for Muqun Theme Collection, rasterized with librsvg.
- `assets/preview.png`: authored representative Editorial Home composition from the final package artwork and light/dark tokens; not an App screenshot or a promise of layout selection.

Exact prompts and any targeted refinements are in ARTWORK.md. All refinement references are this commission's own generated art; no external reference imagery or third-party marks are included. Proportional resizing and small transparent edge margins are used for package sizing. Superseded miniature scenery and object illustrations are absent.

- `assets/home-composer-compact.png` and `assets/home-composer-regular.png`: original transparent edge artwork generated with OpenAI built-in image generation on 2026-10-12 for this theme; proportionally resized and arranged on transparent phone/Pad canvases. CC-BY-4.0.
- `assets/icon-parameters.png`: existing repository original sliders drawing reused from Pine and Parchment; transparent template rendering, CC-BY-4.0.

- `assets/home-artwork-complete.png`: original Home lower-edge completion using OpenAI built-in image editing of this commission’s own source on 2026-10-12, CC-BY-4.0.

- Revised composer assets: independent OpenAI built-in generated original artwork on 2026-10-12, CC-BY-4.0; proportional resizing and transparent layout only.

- `assets/home-artwork-compact.png`, `assets/home-artwork-regular.png`: independent OpenAI built-in imagegen recompositions of this commission’s completed Home on 2026-10-12; original fictional face/style preserved, transparent quiet-left phone/Pad composition, CC-BY-4.0.
- `assets/preview.png`: original pure-art palette cover regenerated from this commission’s current completed Home using built-in OpenAI imagegen on 2026-10-12, CC-BY-4.0; light left/dark right, no simulated App UI or text.

## Continuity review additions

`assets/scenery-light-continuity.png`: original scenery companion generated with OpenAI built-in image generation on 2026-10-13; theme-owned reference artwork only.

`assets/scenery-dark-continuity.png`: original scenery companion generated with OpenAI built-in image generation on 2026-10-13; theme-owned reference artwork only.

Existing character, startup, glyph, palette, and gallery artwork were retained from the current published source. New artwork was copied without scripted image modification.

## 2026-10-15 startup and parameter artwork repair

Pack `hydrangea-window` version `1.2.4`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with petal handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"home-composer-compact","fit":"contain","opacity":0.36,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"home-composer-overhang","fit":"contain","opacity":0.9,"focalPoint":{"x":1,"y":0}}` |
| light | regular | `{"asset":"home-composer-regular","fit":"contain","opacity":0.36,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"home-composer-overhang","fit":"contain","opacity":0.9,"focalPoint":{"x":1,"y":0}}` |
| dark | compact | `{"asset":"home-composer-compact","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"home-composer-overhang","fit":"contain","opacity":0.94,"focalPoint":{"x":1,"y":0}}` |
| dark | regular | `{"asset":"home-composer-regular","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"home-composer-overhang","fit":"contain","opacity":0.94,"focalPoint":{"x":1,"y":0}}` |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
