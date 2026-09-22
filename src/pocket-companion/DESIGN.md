# Pocket Companion

An original cocoa-furred otter with a cream muzzle and apricot neckerchief rests among smooth river pebbles. Soft pencil detail and tactile paper create a warm, quiet companion. Oat surfaces and cocoa text define the light variant; cocoa surfaces and apricot controls define the dark variant.

The template glyphs interpret a tail as a back arrow, a folded cloth pocket as a paper-plane send action, and a rounded clip as the attachment control. The cover is 1024 x 640 with light on the left and dark on the right. Version 1.0.4 adds the responsive Home hero mapping; it introduces no new artwork.

## Checks

CLI 1.8.1 validation, contrast, package round trip, and full source checks pass. This theme has no validation warnings. The shared interface opacity floor is 94%; terminal is 91%, below the authored 96% values. Transparent illustrations and glyphs were inspected, including template tints at 17px and 34px in both modes.

The official browser preview was visually reviewed in both light and dark modes: Phone Home, Conversation and Terminal, plus Tablet Home and Terminal. The contained pocket banner stays separate from navigation and composer controls. This verifies the gallery-rendered layouts, not a native-device import.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
