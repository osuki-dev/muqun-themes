# Mushroom Daybreak

Original pixel-art landscapes reinterpret the Mushroom Kingdom as a calm panorama of red-brick platforms, rounded hills and green pipes. Cream and brick-red controls accompany the sky-blue daylight artwork; midnight cobalt surfaces and butter-yellow controls accompany the night scene.

Light compact layouts use their own portrait illustration. Dark compact and regular layouts share the night panorama, with a right-side focal point retaining Mario in compact framing. The shared wallpaper uses 24% strength to protect conversation text. Default Muqun identity remains intact.

The control glyphs reinterpret a pipe mouth as a back arrow, a moving shell as send and a pipe loop as attachment. The 1024 x 640 gallery cover diagrams the actual light and dark surfaces and accent palettes, with light on the left and dark on the right. A contained pixel garden supplies the empty-state illustration; a separate castle-and-moat composition supplies the Home hero. Both use transparent margins and complete centered silhouettes.

## Checks

CLI 1.9.0 validation, contrast, package round trip and full source checks pass. This theme has no warnings. Shared interface opacity floor is 95%; terminal is 89%, below the authored 96% surface opacity. The three template icons were inspected tinted at 17px and 34px in both modes.

The official browser preview was visually reviewed for light and dark Phone Home, Conversation and Terminal, plus Tablet Home and Terminal. Text and controls remain readable over the subdued wallpaper, and the contained Home scene appears above cards without covering controls. Native-device import was not tested.

Version 1.0.4 wires the existing transparent castle and moat scene into both Classic and Editorial Home, with explicit compact and regular mappings in each mode. It also gives Home explicit wallpaper mappings that preserve the established light portrait, light landscape, and dark focal treatments. The palette, identity, materials, and opacity remain unchanged; the mushroom garden remains the separate empty-state illustration.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
