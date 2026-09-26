# Alpine Dispatch artwork

All illustrations are original artwork generated for Muqun with OpenAI's built-in image generation tool on 2026-09-26. No existing franchise, artist reference, stock asset or third-party character is used. Distribution license: CC0-1.0. No external source URL applies to these original assets.

## Illustration prompt record

- `assets/home-light.webp`: Original lovable Japanese anime Shiba Inu alpine rescue companion, rounded plush cheeks, oversized sparkling amber eyes, small smiling muzzle, plump paws and simplified russet and cream cel-shaded fur, crimson windblown scarf, olive radio harness and brass beacon. Complete seated dog, alert gaze to the left, warm sunlight, premium hand-inked Japanese animation character design. A framing edit restored safe space around the ears and scarf; the generated figure has genuine alpha. This replaces the earlier realistic dog design.
- `assets/home-dark.webp`: Lighting-only edit of the same seated illustration, jade moon rim, amber beacon reflections and warm charcoal shadows. Anatomy, accessories and transparent silhouette preserved.
- `assets/launch-light.webp`: Independent standing pose of the same cute anime rescue dog with a coiled climbing rope and carabiner. Complete ears, paws, tail and scarf. Separate from the seated Home composition. The complete rope, backpack, short rounded paws, ears, scarf and curled tail are visible against genuine transparency.
- `assets/launch-dark.webp`: Night-lighting edit of the complete standing vignette. Jade moon rim and warm amber beacon, transparent alpha preserved.
- `assets/wallpaper-light.webp`: Original Japanese Alps rescue valley after snowstorm: monumental snow peaks, pine forests, red-roof rescue station, tiny amber beacons and pale gold sunrise clouds. Rich hand-painted anime environment, no people or lettering.
- `assets/wallpaper-dark.webp`: Independently generated midnight alpine rescue valley: dark fir forest, jade moonlight, restrained aurora and amber beacon trail. Warm black-green sky rather than a blue color filter.
- `assets/preview.png`: Deterministic 1024 x 640 side-by-side composition of the theme's own daylight and night wallpapers and seated dog illustrations.

Illustrations were generated and edited with the built-in image tool, then resized and converted to static WebP without altering their authored alpha. The longest illustration edge is 1024 pixels. The raw generation sources are retained outside the package.

## Original icon system

The seven `assets/icon-*.png` images are original geometric drawings by Muqun, rendered from paths at 128 x 128. Friendly rescue notation provides consistent rounded strokes with clear control semantics at 17 pt: a single left return arrow with curved endpoint, compass send, rope-loop attachment, circled create cross, rounded scanning reticle, circular settings dial and northeast waypoint arrow. They are template masks, so the App supplies the active theme tint in both modes. No SVG is included in the package.

All seven roles supported by the current authoring contract are populated: `chrome.back`, `chrome.send`, `chrome.attach`, `chrome.create`, `chrome.scan`, `chrome.settings`, `home.arrow`. The arrow's source orientation is explicitly `up-right`. Other native App glyphs remain native; this theme does not invent unsupported icon replacement slots.

## Presentation and checks

Home and launch are independent complete transparent dog illustrations. The generated RGB planes may contain unused colors under fully transparent pixels; those pixels are not visible when composited. Both light and dark figures were inspected over solid backgrounds to verify there is no scenic rectangle, ground plane or hard silhouette crop. Wallpapers own the environment.

Compact and regular foregrounds explicitly use contain. The native controls retain their solid readable surfaces. Snow uses the existing bounded effect with intensity 0.12, density 0.15 and speed 0.25. Theme validation and contrast checks passed with CLI 2.3.1. Native device installation is not claimed here.
