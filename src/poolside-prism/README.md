# Poolside Prism

A complete cyan poolside theme with crisp navy and white surfaces, a marine researcher, and a quiet ripple vocabulary. Initialized with the local Muqun CLI 2.3.0 (`init poolside-prism`); every scaffold placeholder was removed and replaced with original assets.

## Layout recommendation

Editorial Cover is recommended for this portrait silhouette. The native cover artwork band is up to 0.9 times content width rather than Standard's half-width band, preserving a useful character scale. Classic remains supported. The theme selects Cover only within Editorial; it does not change the user's layout preference.

Home uses `contain` and focal point (0.5, 0.12) explicitly on phone and tablet in both modes. This preserves the entire portrait and biases vertical slack toward the top. Native Editorial feathering starts at 68% of the band; the lower water and ledge may dissolve while the face and notebook remain above the transition. Classic feathers its own contained image bounds. Launch is a distinct horizontal half-body composition, also contained. Wallpapers never duplicate either character. The default Muqun title remains; the logo is hidden. Utility button surfaces stay enabled.

Source review: app HomeEditorialArtwork, HomeEditorialLayout, and hero-feather geometry. No app code changed. Preview is an authoring composition, not an actual device capture; native import and device rendering are not claimed.

## Complete slot matrix

| Slot | Artwork | Treatment |
| --- | --- | --- |
| shell.wallpaper | mode-specific caustic lines | quiet full-bleed |
| home.wallpaper | mode-specific offset concentric ripples | quiet full-bleed |
| home.artwork | original seated researcher | contain, opacity 1 |
| launch.artwork | independently generated researcher startup vignette | contain, opacity 1 |
| navigation.background | sparse water contour | opacity .06 |
| composer.background | sparse water contour | opacity .045 |
| actions.background | sparse water contour | opacity .05 |
| cards.decoration | sparse water contour | opacity .055 |
| buttons.primary.background | sparse water contour | opacity .06 |
| tabs.background | sparse water contour | opacity .045 |
| empty.artwork | buoy and waterproof notebook | contain, opacity .85 |

All slots have explicit light/dark compact/regular entries. Seven coordinated 96px template-alpha icons use rounded strokes and familiar functional silhouettes: back, send, attach, create, scan, settings, and home arrow. Icon directions declare their authored orientations. Solid native surfaces and opacity 1 protect readability; all decorations remain nonessential.

Artwork provenance and prompts are in CREDITS.md. Local validation, contrast and package roundtrip are run before delivery. Gallery preview is 1024×640, light on the left and dark on the right.
