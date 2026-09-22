# Raincoat Courier

## Direction

a playful rainy delivery route. The interface uses safety yellow, rain teal, concrete mist. Light and dark variants are separately illustrated and art-directed rather than mechanically recolored.

## Home

The home identity uses a short Japanese slogan. The hero is a full-body courier in a yellow raincoat, composed with generous transparent padding for both the home view and the app launch screen.

## Chrome

Back, send, and attach are custom monochrome template icons matched to the theme's line weight.

## Version 1.1.0 — Editorial Home

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
