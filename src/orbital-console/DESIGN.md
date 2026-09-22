# Orbital Console

Aerospace white, midnight navy and safety orange frame an original orbital station. Ceramic modules, segmented docking rings and solar wings form sculptural hardware at the image edges, leaving a generous clear center for the interface. The spacecraft is an artistic design, not a technical reconstruction.

Light mode pairs cool white surfaces with a deep orange action color; dark mode pairs layered navy surfaces with pale safety orange. Both include complete terminal palettes. Surface opacity is 94% and terminal opacity is 96%; CLI 1.8.1 reports shared readable floors of 90% and 89%, respectively.

Four independently generated wallpapers cover light/dark phone and tablet layouts. A transparent orbital probe illustrates the empty state. The 1024 × 640 gallery image shows light on the left and dark on the right. Back uses a chamfered wing arrow, send a spacecraft nose, and attach a docking-clamp loop, all alpha templates. Default Muqun home identity remains intact.

## Review

Original artwork, the diptych cover and transparent edges were inspected. All three icons were reviewed in both theme tints at 17 px and 34 px.

The browser preview was visually inspected in both modes: phone Home, Conversation and Terminal, plus tablet Home and Terminal. Labels and controls remained legible, the artwork loaded, and the terminal background remained subdued. The gallery does not expose a separate tablet Conversation view. This is browser gallery verification, not an on-device import test.

## Home illustration

A dedicated contained Home composition now accompanies the server list. The original empty-state illustration remains separate. The new 768 × 768 PNG retains transparent edges for both palettes.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
