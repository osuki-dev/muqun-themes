# Atlantic in Azulejo

Portugal / Lisbon. Painted ceramic tilework connects coastal waves, stepped facades and lemon-yellow trams. The palette pairs warm porcelain with saturated cobalt; dark mode uses a deep glazed blue and lemon actions. This sunny, ornamental ceramic treatment is distinct from the cold engraved winter of Silver on the Neva.

Solid materials, 94% UI planes and 96% terminal backgrounds support legibility above detailed tilework.

## Verification

CLI 1.9.0 validation and packing passed. Contrast floors remain light 91% and dark 86% for interface surfaces, and light 88% and dark 75% for terminal surfaces. Authored opacity exceeds these floors.

The official preview at https://muqun.dev/themes/preview/?source=http://127.0.0.1:4184/ was visually inspected in both modes on 2026-09-14: Phone Home, Conversation and Terminal, plus Tablet Home and Terminal. Wallpaper crops, text, cards and template icons rendered without clipping or missing assets. Icons were separately reviewed at 17px and 34px on light/dark surfaces. The independent cover and transparent vignette were inspected locally. These are browser gallery checks, not a native-device import test.

Cultural references (research only; no source artwork reused):
- https://www.visitportugal.com/en/content/country-tiles
- https://www.visitportugal.com/en/content/top-10-lisbon


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
