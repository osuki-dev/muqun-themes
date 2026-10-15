# Asset provenance

All assets in this refreshed package are original and distributed under CC-BY-4.0.

- `assets/home-artwork.png`: original fictional adult scene generated for Muqun Theme Collection with OpenAI built-in image generation on 2026-10-11.
- `assets/launch.png`: independently generated centered fictional adult portrait, same tool/date. The launch is a separate composition, not a Home crop.
- `assets/empty.png`, seven `assets/icon-*.png`, four quiet wallpaper assets and six chrome decorations: original deterministic vector drawings authored for Muqun Theme Collection, rasterized with librsvg.
- `assets/preview.png`: authored representative Editorial Home composition from the final package artwork and light/dark tokens; not an App screenshot or a promise of layout selection.

Exact prompts and any targeted refinements are in ARTWORK.md. All refinement references are this commission's own generated art; no external reference imagery or third-party marks are included. Proportional resizing and small transparent edge margins are used for package sizing. Superseded miniature scenery and object illustrations are absent.

## Home composer additions (1.1.2)

- `assets/home-composer-light.png` and `assets/home-composer-dark.png`: original
  transparent cafe windowsill illustrations generated for Muqun Theme Collection
  with OpenAI's built-in image generation tool on 2026-10-12. The dark image is an
  evening-lighting edit of the commissioned light image; no third-party reference
  is used. Proportionally resized to 1024×341 for delivery, preserving alpha.
- `assets/icon-parameters.png`: original deterministic three-row adjustment glyph
  authored for Muqun Theme Collection and rasterized with librsvg.

Creator: Muqun Theme Collection. Source: this repository and the generation prompts
in ARTWORK.md; no external source URL. License: CC-BY-4.0, matching this theme.

## Continuity update

- `assets/environment-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.
- `assets/gallery-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.

No third-party reference images or marks were used. See CONTINUITY-PROMPTS.md for constraints and source-review limits.

- `assets/home-cover-light.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.
- `assets/home-cover-dark.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.

## 2026-10-15 startup and parameter artwork repair

Pack `kissaten-after-rain` version `1.1.5`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"home-composer-light","fit":"contain","opacity":0.72,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| light | regular | `{"asset":"home-composer-light","fit":"contain","opacity":0.6,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| dark | compact | `{"asset":"home-composer-dark","fit":"contain","opacity":0.66,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| dark | regular | `{"asset":"home-composer-dark","fit":"contain","opacity":0.56,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
