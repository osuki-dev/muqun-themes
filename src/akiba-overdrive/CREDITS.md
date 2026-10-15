# Artwork provenance

## Home composer update

The transparent `composer-edge-compact.png` and `composer-edge-regular.png` are original artwork generated for this theme with OpenAI image generation and supplied under the theme's CC0-1.0 license. Graphite rails, teal connectors and amber docking lights complement the urban architecture. Phone and tablet compositions preserve clear writing space. The parameter icon is an original template glyph matching the attachment and send controls. The gallery preview uses the theme's own artwork and palette without simulated App controls.

The foreground and two architectural wallpapers were newly generated for Muqun on 2026-09-23 using OpenAI image generation and released by the author under CC0-1.0. No external character franchise, photography, branded marks, fonts, or interface screenshots are bundled.

- `assets/figure.png`: original wordless watercolor character, transparent alpha; shared between light and dark modes.
- `assets/wallpaper-light.png` and `assets/wallpaper-dark.png`: original quiet architectural scenery without people or writing.
- `assets/preview.png`: 1024 × 640 light/dark gallery composition rendered from this theme's own assets and palette.
The seven supported control icons are original vector drawings exported as template PNGs for this theme. Their semantic shapes remain familiar at small sizes.

The previous poster lettering, foreground duplication, and old character/empty-state images have been removed. Native Home layout renders the theme title once; no words are baked into illustrations.

## 2026-09-24 interface extension

The new `icon-*.png` files are original vector drawings exported to transparent template PNGs, with details tailored to this pack. `chrome-light.png` and `chrome-dark.png` are original geometric vector chrome accents. No outside source art was used for these additions.

The 2026 `assets/preview.png` is an original palette and UI composition rendered from this theme’s declared artwork. It is a gallery illustration, not a native device screenshot.

## 2026-10-15 startup and parameter artwork repair

Pack `akiba-overdrive` version `1.0.10`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-full.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-edge-compact","fit":"cover","opacity":0.88,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| light | regular | `{"asset":"composer-edge-regular","fit":"cover","opacity":0.88,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| dark | compact | `{"asset":"composer-edge-compact","fit":"cover","opacity":0.8,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |
| dark | regular | `{"asset":"composer-edge-regular","fit":"cover","opacity":0.8,"focalPoint":{"x":0.5,"y":1},"outset":{"left":12,"right":12,"bottom":8}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
