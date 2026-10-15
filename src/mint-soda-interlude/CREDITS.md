# Artwork and provenance

## Home continuity candidate 1.0.4

The generated home-cover-continuity and home-paper continuity images are original fictional OpenAI image-generation artwork made on 2026-10-13 for Muqun Theme Collection. Cover references are this theme's own collection illustration. Wallpaper generation uses no third-party reference. License: the existing theme license. No script image editing was used. HOME-CONTINUITY.md records source review, responsive resolution, startup props and limitations. Published parameters/composer additions retain their original collection provenance.


- `assets/mint-soda-barista.png`: original AI-generated illustration created for this theme using OpenAI built-in image generation on 2026-10-10. Theme and original artwork are released under CC0-1.0. No stock assets or existing characters are included.
- `assets/preview.png`: catalogue composition using this theme's own palette and original artwork. It is an illustrative composition, not an app capture.
- Two user-supplied references were inspected for airy pastel atmosphere and anime linework only. Their characters, branding and images are not distributed.

## Generation prompt

Use case: stylized-concept. Asset type: transparent foreground illustration for a quiet anime cafe app theme. Create an original adult woman barista, visibly mid-twenties, with short pale teal bob hair, a small peach blossom hair pin, gentle confident smile, tasteful loose cream blouse with collar and long sleeves, mint green apron over a calf-length peach skirt. She holds a clear tall glass of mint soda with tiny sparkling bubbles, ice and a mint leaf at chest level. Airy candy mint, cream and peach, high key refined anime cel shading with delicate graphite-pencil line detail, elegant adult proportions. Three-quarter length figure from head to mid calves, complete silhouette and hands with generous transparent margin on every edge. A few small floating bubbles beside the glass, no other scene elements. Clean editorial restraint, soft daylight. Genuine transparent background, no backdrop, no floor, no text, no logos, no UI, no watermark, no existing franchise character, no halo, no animal ears. Original design.

## Composition

The transparent original is preserved unaltered. Both modes explicitly use contain-fit artwork for compact and regular layouts. Solid mint-cream and deep botanical surfaces keep native chrome readable. Icons remain native. Home retains its default name with the logo hidden.

## Additional original assets

All paper, rail, stationery, card, button, icon and empty-state PNGs are original code-drawn raster illustrations released under CC0-1.0. Temporary vector instructions were rasterized, with no scripts or SVGs distributed.

`assets/mint-soda-launch.png` is a built-in OpenAI image-generation edit of this theme's original barista. The new serving gesture and waist-up framing distinguish it from Home. Alpha is preserved.

### Startup edit prompt

Edit this original barista illustration into a distinct startup composition for the same mint cafe theme. Preserve her adult identity, short pale teal bob, peach blossom pin, tasteful cream blouse and mint apron, delicate pencil anime linework, mint cream peach palette. Change the pose and framing: centered waist-up portrait, facing viewer, smiling gently, both hands offering the glass of sparkling mint soda forward on a small simple cream saucer, soda glass and tiny bubbles clearly visible. Complete head, arms and serving hands, generous transparent margin. New serving gesture, no full skirt or legs. Genuine transparent background, no environment, text, logo, watermark or UI.

## 2026-10-15 startup and parameter artwork repair

Pack `mint-soda-interlude` version `1.0.6`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/mint-soda-launch.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with bubble handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| light | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.34,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | compact | `{"asset":"composer-accent-compact","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | regular | `{"asset":"composer-accent-regular","fit":"contain","opacity":0.42,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"composer-overhang","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
