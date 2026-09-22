# Quiet Terminal

Graphite, fog blue and soft white keep the interface calm and precise. Separate light and dark ANSI palettes retain meaningful red, green, amber, blue, magenta and cyan families with restrained saturation.

Opaque solid planes keep Home, Conversation and Terminal visually quiet. Artwork appears only in the contained empty-state illustration: folded metal brackets and a single ceramic cursor block, rendered separately for each mode. All responsive sizes use the contained square composition. Default Muqun name and logo remain visible.

The back glyph recalls a carriage return, send combines an arrow with a cursor cell, and attachment follows squared monospaced bracket geometry. All three use template alpha so their tint follows the selected mode. The gallery preview pairs soft-white light mode on the left with graphite dark mode on the right.

## Home illustration

A dedicated contained Home composition now accompanies the server list. The original empty-state illustration remains separate. The new 768 × 768 PNG retains transparent edges for both palettes.

## Version 1.1.0 — Editorial Home

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
