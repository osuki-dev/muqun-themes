# Ocarina of Dawn

A quiet, unofficial Zelda-inspired watercolor theme. Original forest ruins, mossy sword pedestals, a blue ceramic ocarina and delicate ferns evoke a woodland adventure. Mist, sage and pale gold give way to deep forest tones at night. All compositions are newly generated rather than copied from game artwork.

Leaf, fletched-arrow and grappling-loop glyphs replace back, send and attach as alpha templates. Each was reviewed at 17 px and 34 px in both palette tints. The full UI and terminal palettes pass CLI 1.9.0 contrast checks: shared floors are 90% for surfaces and 91% for terminal, below authored 95% and 97% defaults.

## Preview review

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
