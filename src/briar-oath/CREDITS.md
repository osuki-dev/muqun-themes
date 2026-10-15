# Artwork credits

All six character and wallpaper assets were generated specifically for Briar Oath using OpenAI image generation on 2026-09-26, art-directed by Muqun. Source: https://openai.com/policies/terms-of-use/. Original fictional mature knight and enchanted environments; no third-party characters or existing artwork used. Released by Muqun under CC0-1.0.

The seven PNG icons are original Muqun vector drawings rasterized for the theme, combining briar notches and heraldic shields with recognizable UI semantics. CC0-1.0. The preview uses only this theme artwork.

Home uses a close three-quarter portrait. Launch is independently composed as a complete knight with shield, scabbard and both boots. Dark character lighting and the midnight forest are separately generated. Four foreground images retain true alpha transparency.

## Composer continuity

Sparse transparent theme-specific input ornaments generated with OpenAI imagegen; exact prompt is recorded in ENVIRONMENT-PROMPTS.md. No character duplication, opaque input plate, or enclosing frame.

## 2026-10-15 startup and parameter artwork repair

Pack `briar-oath` version `1.0.4`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with shield handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
