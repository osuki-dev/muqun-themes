# Asset provenance

All assets in this refreshed package are original and distributed under CC-BY-4.0.

- `assets/home-artwork.png`: generated specifically for this theme with OpenAI built-in image generation on 2026-10-10, commissioned by Muqun Theme Collection; no external reference artwork, third-party logos or source images used. Exact prompt is recorded in `ARTWORK.md`.
- `assets/launch.png`, `assets/empty.png`, seven `assets/icon-*.png`, four wallpaper resources, and six chrome decorations: original deterministic vector drawings authored for Muqun Theme Collection and rasterized with librsvg.
- `assets/preview.png`: original composition using the final package artwork and theme tokens.

Superseded third-party technology marks and previous illustrations are not included.

## 2026-10 full-page continuity

Additional environmental wallpaper and corrected full-prop artwork generated with OpenAI imagegen from the existing theme art. Exact prompts are recorded in ENVIRONMENT-PROMPTS.md. Existing subject artwork and published icon/composer provenance are retained.

## 2026-10-15 startup and parameter artwork repair

Pack `midnight-operator` version `1.2.5`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with circuit handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | `{"asset":"home-composer-accent","fit":"contain","opacity":0.58,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"launch","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| light | regular | `{"asset":"home-composer-accent","fit":"contain","opacity":0.58,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"launch","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | compact | `{"asset":"home-composer-accent","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"launch","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |
| dark | regular | `{"asset":"home-composer-accent","fit":"contain","opacity":0.48,"focalPoint":{"x":0.5,"y":0},"outset":{"left":0,"right":0,"bottom":0}}` | `{"asset":"launch","fit":"contain","opacity":0.85,"focalPoint":{"x":1,"y":0}}` |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
