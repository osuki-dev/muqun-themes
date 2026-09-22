# After School Workshop

Warm ivory and deep indigo frame a quiet neighborhood workshop, with cobalt print detail and small amber and coral accents. The custom Home name and hidden logo remain unchanged.

Version 1.1.0 adds Editorial Home artwork without changing the palette, identity, Classic hero, empty-state behavior, or responsive mappings.

## Verification

CLI 1.9.0 validation and packing passed. Contrast completed with interface floors of 91% light and 83% dark, and terminal floors of 94% light and 80% dark; the existing dark terminal palette reports one ANSI colour below 4.5:1.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
