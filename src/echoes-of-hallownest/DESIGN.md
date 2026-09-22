# Echoes of Hallownest

Silver-bone mist and cold steel-blue ink create a quiet underground fairytale. Architectural detail gathers at the outside edges of four separately composed wallpapers. Home has a contained Knight illustration; shared conversation wallpaper stays at 22 percent artwork strength while Home uses 48 percent. UI planes remain 97 percent opaque and terminal planes 98 percent.

A nail blade points back, a wing points forward to send, and a gothic arch paperclip indicates attachment. All three use template alpha so their colors follow the palette. Muqun name and logo remain default.

Ten original generated assets include a 1024x640 paired gallery cover. Artwork and alpha were inspected, with control glyphs reviewed tinted at 17px and 34px. CLI 1.9.0 validates the source and packed round-trip; source catalogue check passes. Both shared opacity floors are 93 percent, below the authored values.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
