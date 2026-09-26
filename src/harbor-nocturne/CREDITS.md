# Harbor Nocturne artwork

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
