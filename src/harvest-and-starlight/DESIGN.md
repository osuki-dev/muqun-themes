# Harvest & Starlight

A farm storybook in carefully clustered 2D pixels: honey harvest light, cornflower sky, lavender hills and plum starlight. The chicken, watering can and Junimo provide a recognizable Stardew Valley fan-art focal point without recreating an in-game screen.

Light mode pairs warm honey-paper surfaces with cornflower actions and plum text. Dark mode reverses into a deep plum room with pale cornflower actions and cream text. Both terminal palettes retain meaningful distinct ANSI roles.

Four separately composed wallpapers cover phone and tablet aspect ratios. Shared content wallpaper is intentionally restrained at 18%; Home uses 50% and a separate contain-fit hero, leaving conversation and terminal reading areas quiet. UI opacity is 96%, terminal 97%. Default Muqun name and logo are preserved.

Editorial Home uses the cover header and reuses the transparent chicken, pumpkin, watering-can, and Junimo vignette as its foreground in both compact and regular widths. The same asset remains the Classic Home hero and startup artwork, so the established identity and launch handoff are unchanged. The cover toolbar stays visually open over the pixel-art foreground while native controls retain their theme colors and hit targets.

The back arrow carries wheat grains, send uses a leaf folded into an arrow, and attach is a sprouting paperclip. Their template silhouettes follow stepped pixel contours. The empty-state illustration is a watering can and seed tray. A split gallery preview shows daylight left and starlight right.

## Validation

CLI validation, contrast, package round trip and the 60-theme source check with required previews pass. The current published CLI reports the newer `homePresentation` field as an ignored compatibility warning. Shared contrast floors are 90% for interface surfaces and 86% for the terminal. The ten assets, alpha channels and tinted glyphs at 17px and 34px were visually reviewed.

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.

## Toolbar surfaces

Toolbar controls use the normal theme surface. This theme does not force a transparent or specially translucent toolbar; readers can adjust surface opacity in the app.
