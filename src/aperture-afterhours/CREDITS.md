# Credits

Unofficial Portal fan art. Portal and its characters, imagery and trademarks belong to Valve Corporation. This theme is not affiliated with or endorsed by Valve.

All packaged images are original AI-generated interpretations created for this theme using OpenAI image generation, not game screenshots or extracted assets. Prompts: PROMPTS.md.

`assets/home-hero.png`: newly generated with OpenAI image generation for this theme; ATLAS and P-body on a compact testing platform. Existing franchise notices remain applicable.

## Native adaptation (2026)

Original native template glyphs: `assets/icon-create.png`, `assets/icon-scan.png`, `assets/icon-settings.png`, `assets/icon-arrow.png`. Created for this theme in 2026 using geometric linework; retain the theme license. Existing back/send/attach artwork is unchanged.

The 2026 `assets/preview.png` is an original palette and UI composition rendered from this theme’s declared artwork. It is a gallery illustration, not a native device screenshot.

## Composer continuity

Sparse transparent theme-specific input ornaments generated with OpenAI imagegen; exact prompt is recorded in ENVIRONMENT-PROMPTS.md. No character duplication, opaque input plate, or enclosing frame.

## 2026-10-15 startup and parameter artwork repair

Pack `aperture-afterhours` version `1.1.7`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with portal handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
