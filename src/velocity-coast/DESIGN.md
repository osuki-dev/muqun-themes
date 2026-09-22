# Velocity Coast

Crisp comic cel shading and diagonal coastal loops frame Sonic in cobalt, coral and white. The interface pairs clear blue daylight with marine night and warm coral action tint. Home retains full artwork and a contained hero; shared wallpaper is reduced to 12% to keep conversation text clear.

Four dedicated light/dark portrait/wide wallpapers, separate transparent hero and empty illustration, and speed-fin back/send plus track-loop attachment glyphs support the theme. Default Muqun identity remains intact.

## Review

CLI 1.9.0 validation, contrast, package round trip and full source check passed with all ten assets and no theme warnings. Shared opacity floors are 92% interface and 88% terminal; authored planes are 96%.

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
