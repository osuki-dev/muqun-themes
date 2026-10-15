# Artwork provenance

`assets/cloud-courier.png` is original AI-generated artwork created for this theme using OpenAI's built-in image generation tool on 2026-10-10. It depicts an original adult cloud courier and illustrator. No existing anime character is depicted, and the supplied reference image is not included in the package. Theme manifest and gallery composition are original work; released under CC0-1.0 to the extent rights can be waived.

`assets/preview.png` is a 1024×640 local gallery composition using the theme's own foreground and authored light/dark surfaces. It is an illustrative catalogue preview, not a captured application screenshot. Seven original coordinated template icons are supplied; all chrome uses solid materials. Home uses the default Muqun title with its logo hidden.

## Generation prompt

Use case: illustration-story. Asset type: transparent foreground hero for a calm blue-white Muqun theme called Sky Letter Atelier. Create an ORIGINAL adult woman cloud courier and illustrator, age 25, in refined Japanese anime cel-shaded style with delicate linework, high-key cyan, pearl white, touches of butter yellow. Shoulder-length dusty turquoise hair swept into a loose low side ponytail, round amber eyes, white beret with tiny brass envelope pin, white practical cropped windbreaker over sky-blue linen jumpsuit, modest adult proportions, white sneakers, little crossbody cyan mail satchel holding rolled drawings. She stands in an easy three-quarter pose and holds one illustrated sealed letter; her other hand carries a slim sketchbook. A few soft small clouds and two drifting blank envelopes cluster around her feet, like a floating cloud delivery studio. Full complete figure head to soles, comfortably inside image, centered with generous transparent air around silhouette, crisp readable silhouette. Actual transparent background, no rectangular backdrop, no scene gradient. No text, no logos, no watermark, no interface, no halo, no weapon, no school uniform. Elegant original adult character, no existing anime characters or distinctive franchise costume. Artwork usable against both pale cyan and deep navy.

The generated PNG's genuine alpha channel is preserved, with no background removal or recoloring. Both mode and device entries explicitly contain the full silhouette. Startup uses an independent edited letter-opening portrait. Mode-specific backgrounds use restrained original cloud contour motifs to keep the delicate sky illustration readable.

## Vector artwork

All wallpaper, control decoration, empty-state and icon PNGs are original code-native vector designs rasterized locally with Sharp. SVG sources are not packaged. Cloud contours, envelopes and paper-plane accents are coordinated with the courier story. No external stock, fonts or reference images are bundled.

## Startup artwork

`assets/launch.png` is an original transparent image edit generated using OpenAI built-in image generation from this theme’s own cloud courier illustration on 2026-10-10. The altered pose and waist-up framing are an independent startup scene, not a crop.

Startup edit prompt:

Edit the provided original adult cloud courier illustration into a distinctly different startup composition. Preserve her identity: age 25, dusty turquoise side ponytail, amber eyes, white beret with brass envelope pin, white windbreaker and blue linen jumpsuit. New composition: waist-up three-quarter portrait, smiling gently while opening an illustrated envelope with both hands, a small paper airplane and two fluffy clouds float beside her shoulder; sketchbook and mail satchel partially visible at waist. Delicate anime cel-shaded linework and pearl white, sky cyan and tiny gold details. Balanced landscape composition, subject slightly right of center, transparent breathing room on left, complete beret and hands inside frame. Genuine transparent background, no backdrop rectangle or gradient, no text, no logo, no UI, no existing character. This is an independent startup illustration, not the full-body pose cropped.

## Home composer local preview

`assets/home-composer-accent.png`: original theme-specific artwork generated with OpenAI imagegen, no third-party reference image. `assets/icon-parameters.png`: reused from Pine and Parchment in this repository, CC0-1.0.

## Continuity update

- `assets/environment-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.
- `assets/gallery-continuity.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.
- `assets/launch-complete.png`: original OpenAI built-in image generation for Muqun Theme Collection, 2026-10-13, under this theme's declared license.

No third-party reference images or marks were used. See CONTINUITY-PROMPTS.md for constraints and source-review limits.

- `assets/home-cover-light.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.
- `assets/home-cover-dark.png`: original identity-preserving environment expansion and matching lighting variant with OpenAI built-in image generation, 2026-10-13, under this theme's declared license.

## 2026-10-15 startup and parameter artwork repair

Pack `sky-letter-atelier` version `1.0.5`.

Startup artwork was completed from this theme's existing character using built-in OpenAI imagegen edits. The face, hair, upper clothing, pose and props were used as preservation constraints; the missing lower body and feet were supplied. These are original derivative assets under this theme's existing license, with no new external sources. Exact edit prompts and original inputs are recorded in [LAUNCH-COMPLETION-PROMPTS.md](LAUNCH-COMPLETION-PROMPTS.md).

- `assets/launch-complete.png`: complete transparent startup figure; replaces the incomplete launch-only image.

The new full silhouettes, complete feet, clothing and props were inspected in a source contact sheet. One completed startup image is shared by both appearance modes. This is artwork inspection, not a device startup capture.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with envelope handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"home-composer-accent","fit":"contain","opacity":0.58,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| light | regular | `{"asset":"home-composer-accent","fit":"contain","opacity":0.58,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | compact | `{"asset":"home-composer-accent","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |
| dark | regular | `{"asset":"home-composer-accent","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
