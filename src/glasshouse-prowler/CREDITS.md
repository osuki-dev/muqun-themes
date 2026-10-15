# Glasshouse Prowler artwork

All character and botanical conservatory illustrations were generated specifically for this original Muqun theme with OpenAI image generation on September 26, 2026. No third-party franchise characters, photographs, or reference artwork were used. Source: this authoring session; no public source URL. Released with this theme under CC0-1.0.

- `assets/home-light.webp`, `assets/home-dark.webp`: original cute cel-shaded silver tabby kitten portrait, preserved alpha.
- `assets/launch-light.webp`, `assets/launch-dark.webp`: independently generated complete playful anime kitten with watering can and fern, preserved alpha. Shared neutral fur artwork is intentional across both modes.
- `assets/wallpaper-light.webp`, `assets/wallpaper-dark.webp`: independently generated daylight and midnight botanical glasshouse paintings.
- `assets/icon-*.png`: seven original friendly rounded botanical vector glyphs authored for this theme and rasterized to transparent PNG, CC0-1.0.
- `assets/preview.png`: composited from this theme's own assets and palette, CC0-1.0.

The supported replacement roles are chrome.back, chrome.send, chrome.attach, chrome.create, chrome.scan, chrome.settings, and home.arrow. Other App glyphs retain the built-in rendering. The Home arrow points up-right and declares its source direction.

The kitten illustrations were regenerated as explicitly stylized Japanese-animation characters: rounded faces, expressive emerald eyes and simplified cel-shaded fur. They replace the earlier realistic cat studies, which are not shipped.

## Composer continuity

Sparse transparent theme-specific input ornaments generated with OpenAI imagegen; exact prompt is recorded in ENVIRONMENT-PROMPTS.md. No character duplication, opaque input plate, or enclosing frame.

## 2026-10-15 startup and parameter artwork repair

Pack `glasshouse-prowler` version `1.0.4`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with paw handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| light | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.3,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | compact | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |
| dark | regular | `{"asset":"composer-continuity","fit":"contain","opacity":0.26,"focalPoint":{"x":0.5,"y":0}}` | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
