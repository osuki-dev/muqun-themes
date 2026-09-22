# Neon Pellet Run

The back glyph combines a maze chevron and pellet, send uses a directional open-chevron shape, and attachment uses a loop with a pellet end. All use template tinting.

## Validation

CLI validation, contrast and package round trip passed with ten assets. Shared interface and terminal floors are 89% and 88%; authored opacity is 97%. Artwork and glyphs were inspected locally, including 17px and 34px tint checks.

Browser preview previously loaded the theme and device labels, including the Classic Home hero declaration. The Editorial declaration is contract-validated but has not been claimed as device-tested.

The dedicated Home artwork presents Pac-Man and two ghosts circling a violet maze arc. It is a separate transparent composition from the preserved empty-state illustration and is used in both modes and responsive sizes. Editorial contains the whole image instead of cropping it, so the native masthead, actions, and long labels remain app-rendered and unobstructed.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
