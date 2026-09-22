# One Piece — Grand Voyage

Version 1.2.0 preserves the original fan-art scenes and ocean-adventure palette: turquoise daylight, moonlit navy, burgundy accents and straw-hat gold. The existing Grand Voyage Home name and hidden logo remain unchanged.

The contained Home hero depicts Luffy on a ship's bow; each mode's Chopper illustration remains dedicated to the empty state. Hero content is hidden by the app when the empty state is active. The four existing phone/tablet wallpapers retain their original compositions and focal points. Nautical map and woven action textures remain at restrained opacity. UI planes use 88% opacity and terminal planes 94% for steadier reading over the detailed seascapes.

Three template glyphs add a rope-arrow back control, a sailboat send control and a knotted-rope paperclip attachment control. Their alpha shapes follow the mode's primary color. Six supporting textures and illustrations are resized to 768px; the gallery preview is a 1024x640 PNG with light on the left and dark on the right. All assets include verified SHA-256 digests.

## Verification

The dedicated Home hero presents Luffy standing on a ship bow above curling turquoise waves. It is a separate transparent composition from the preserved empty-state illustration and is used in both modes and responsive sizes.

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
