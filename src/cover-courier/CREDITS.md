# Cover Courier artwork

All packaged artwork was generated locally with OpenAI image generation on 2026-09-22 for this theme, using the user-approved COVER concept. The reference mockup itself is not packaged. Assets: cover-light.webp, cover-dark.webp, empty-state.webp, preview.webp. Preview resized to 1024 × 640; art encoded as static WebP. No remote assets, fonts, scripts, or private workspace data are included.

Generated artwork and authored palette: CC0-1.0, to the extent rights subsist. No claim of exclusive copyright in AI-generated material.

## Layered artwork revision (1.0.1)

The current package contains paper-light.webp and paper-dark.webp (quiet railway
wallpapers), courier-light.webp and courier-dark.webp (transparent character
artwork), and preview.webp (1024 x 640, light left / dark right). These were
generated with the built-in OpenAI image tool on 2026-09-22 from the approved
COVER character reference. Prompts requested subdued ivory/graphite railway
paper, an isolated courier with real alpha, a silver-haired dark variant, and
a two-mode gallery composition. Encoding and resizing preserve alpha. Previous
flattened banners remain local source alternatives and are not packaged.

## Native adaptation (2026)

Original native template glyphs: `assets/icon-create.png`, `assets/icon-arrow.png`. Created for this theme in 2026 using geometric linework; retain the theme license. Existing back/send/attach artwork is unchanged.

The 2026 `assets/preview.png` is an original palette and UI composition rendered from this theme’s declared artwork. It is a gallery illustration, not a native device screenshot.

## Composer continuity

Sparse transparent theme-specific input ornaments generated with OpenAI imagegen; exact prompt is recorded in ENVIRONMENT-PROMPTS.md. No character duplication, opaque input plate, or enclosing frame.

## 2026-10-15 startup and parameter artwork repair

Pack `cover-courier` version `1.0.12`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-full-light.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.
- `assets/launch-full-dark.png`: complete transparent startup figure; separate from the preserved shared Home/empty illustration.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet; both Cover Courier mode variants were reviewed. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with chevron handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
