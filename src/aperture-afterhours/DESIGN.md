# Aperture Afterhours

Clinical industrial spatial scenes pair chalk white and chilled blue with orange portal accents. Dark mode uses deep slate and pale blue controls. Four independently composed backgrounds serve phone and tablet. Home retains full artwork and a contained Companion Cube hero; shared content wallpaper uses 35% strength to keep conversation and terminal calm. Default Muqun name and logo remain.

The back arrow emerges from an oval portal; Send is a dart with a portal-shaped cutout; Attach uses interlinked oval rings. All three use template alpha for mode-aware tint. The cover pairs light on the left and dark on the right.

## Verification

CLI 1.9.0 validation and packing passed. Contrast floors are 90% light and 87% dark for interface surfaces, and 87% light and 75% dark for terminal surfaces.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
