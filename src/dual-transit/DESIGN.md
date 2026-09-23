# Dual Transit

An original pair of adult urban couriers in expressive manga ink and watercolor. The light edition pairs warm paper, vermilion accents and a detailed sunset railway. The dark edition uses neutral charcoal, copper and amber; it has no blue cast.

## Artwork and layouts

`home.artwork` uses dedicated close-up transparent illustrations. `launch.artwork` uses separate complete figures, including shoes, with contain fitting. Changing launch proportions never changes Home's scale. The wallpapers contain architecture only, so characters appear once. Both wallpaper slots use full opacity; opaque cream or charcoal surfaces provide readable controls without washing out the scene.

Classic and Editorial own their geometry. This package does not define a new layout. Seven template icons cover every currently supported icon slot: back, send, attach, create, scan, settings, and Home arrow. Their alpha shapes inherit the active control color.

## Ambient effects

Light: dust, intensity 0.18, density 0.75, size 1, speed 0.45, upward direction, using the `textMuted` and `warning` palette roles.

Dark: embers, intensity 0.25, density 0.65, size 1, speed 0.35, upward direction, using the `primary` and `warning` palette roles.

These are palette roles rather than fixed effect colors. The renderer owns the particle-count cap, motion and reduced-motion behavior. The package requires the updated Muqun 3.0.0 build with the expanded effect contract; older strict effect schemas cannot import it. Distribution is held until coordinated App, CLI and website validation and user review are complete.
