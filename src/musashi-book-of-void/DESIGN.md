# 宮本武蔵｜空の巻

The theme translates the restraint of *The Book of Five Rings* into a quiet interface: aged washi and a vermilion dawn in light mode; moonlit blue-black ink in dark mode; iron-red actions and indigo information accents. Each mode has its own scenery background and transparent swordsman Hero. Three brush-shaped template icons complete the chrome.

Artwork is intentionally nonessential. Both modes remain complete and readable if decoration is unavailable.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
