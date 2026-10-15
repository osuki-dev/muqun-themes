# Harbor Nocturne artwork

## Home continuity candidate 1.0.3

The generated home-cover-continuity and home-paper continuity images are original fictional OpenAI image-generation artwork made on 2026-10-13 for Muqun Theme Collection. Cover references are this theme's own collection illustration. Wallpaper generation uses no third-party reference. License: the existing theme license. No script image editing was used. HOME-CONTINUITY.md records source review, responsive resolution, startup props and limitations. Published parameters/composer additions retain their original collection provenance.


All illustrations are original artwork generated for Muqun using OpenAI's built-in image generation tool on 2026-09-26. No external character, franchise, artist reference, stock image, or third-party artwork is included. Distribution license: CC0-1.0. Icons are original geometric drawings by Muqun, rasterized to PNG; no SVG is packaged.

## Assets and prompt record

- `assets/home-light.webp`: Original mature Japanese male acoustic cellist, windswept black hair, ivory linen overshirt, black shirt and vermilion scarf. Seated playing an amber cello, full instrument, bow, stool and boots, cinematic Japanese anime ink and painterly cel shading. Warm harbor sunlight. Genuine transparent alpha, complete silhouette, no text. A follow-up background-extraction edit preserved the figure and removed every background plane.
- `assets/home-dark.webp`: Lighting-only edit of the Home figure: warm amber rim light, copper highlights, soft plum shadows, ivory becomes pale warm taupe; no blue, original silhouette and transparent alpha preserved.
- `assets/launch-light.webp`: Independent standing cellist composition, complete cello upright, bow in other hand, vintage case and coiled harbor rope. Full figure and all props, cinematic original anime, warm golden light, transparent alpha, no scene or rectangular backdrop and no lettering. This is not a crop of the Home image.
- `assets/launch-dark.webp`: Night lighting edit of the independent launch vignette; warm amber light and copper reflections, transparent alpha preserved.
- `assets/wallpaper-light.webp`: Original working Japanese harbor environment without people: towering cream-gold afternoon clouds, vermilion dock cranes, ferries, distant mountains and sparkling water. Rich pigment and quiet upper sky, wordless.
- `assets/wallpaper-dark.webp`: Original nighttime working harbor without people: warm charcoal sky, amber moon, red cranes, dock lamps reflected in dark water, copper and plum, no blue or lettering.
- `assets/preview.png`: Deterministic side-by-side composition of the theme's own Home artwork over the corresponding wallpapers.
- `assets/icon-*.png`: Seven semantic template icons, designed from stroked geometric paths. Template rendering allows native theme tinting in both modes.

## Presentation and verification

Home and launch are separate transparent illustrations; wallpapers own the environment. The Home foreground deliberately contains no scenic rectangle and the launch pose includes the entire cello, case, rope, boots and bow. Native UI text and controls remain native; the theme contains no embedded text. Compact and regular size classes use explicit contained foregrounds. The low-density dust effect uses existing bounded App rendering with intensity 0.12 and speed 0.25.

The current 2.3.1 authoring contract supports seven custom icon roles: chrome.back, chrome.send, chrome.attach, chrome.create, chrome.scan, chrome.settings and home.arrow. Other UI glyphs retain the App's native rendering; this package does not pretend unsupported slots are customizable.

## 2026-10-15 startup and parameter artwork repair

Pack `harbor-nocturne` version `1.0.5`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with note handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | none | none |
| light | regular | none | none |
| dark | compact | none | none |
| dark | regular | none | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
