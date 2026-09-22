# Papyrus on the Nile

Egypt / Nile Valley interpreted through papyrus-inspired gouache: lapis water, copper sandstone, ivory lateen sails and papyrus stems. The scenes are artistic compositions rather than reconstructions of a specific landmark.

Light mode uses warm paper surfaces and lapis actions. Dark mode uses deep mineral blue surfaces and pale copper actions. Back is a reed arrow, send is a streamlined triangular felucca sail, and attach is a paperclip with a scroll curl. All three are alpha-template glyphs with mode-specific tinting. Default Muqun home name and logo are preserved.

Four independently generated wallpapers cover light/dark and phone/tablet formats. A transparent felucca vignette fills the empty state. The 1024 × 640 gallery diptych places light on the left and dark on the right.

## Reference

[Experience Egypt: cruising and sailing](https://www.experienceegypt.eg/en/attraction/15/cruising-sailing) describes feluccas on the Nile. [Experience Egypt: Aswan](https://www.experienceegypt.eg/en/city/9/aswan-abu-simbel) informed the river setting. These sources supplied context only; no third-party imagery is packaged.

## Review

Artwork and gallery cover inspected for composition and clean rendering. Template glyphs inspected at 17 px and 34 px in both palette tints. CLI 1.8.0 validation and contrast checks passed; shared readable floors are 89% for surfaces and 90% for terminal. Authored opacity is 94% and 96%, respectively.

The live CLI preview loaded its theme data and exposed the dark phone Home, Conversation and Terminal and tablet Home and Terminal views. Browser screenshot capture failed, so full visual device verification remains pending.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.
