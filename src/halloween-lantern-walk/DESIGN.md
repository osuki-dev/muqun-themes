# Halloween Lantern Walk

Version 1.0.0. Original festive storybook character with matching light/night environments. Home uses one transparent, contain-fit character with generous canvas margins; the character-free wallpaper extends behind the status bar. No duplicated figure is painted into the background. Home name/logo are hidden so typography cannot cover the face. Launch and empty states use the complete standalone figure, including both feet.

Compact and regular resolve explicitly to the same square, contain-fit Home drawing (opacity 1, focal point 0.5,0). Only the character-free environment is cover-cropped. The square character is never stretched or cover-cropped. Both appearance modes share the character identity, with separately painted day/night environments.

## Input and controls

In light/dark and compact/regular, `home.composer.background` and `home.composer.decoration` are null: no artwork, no outset/overhang and no obstruction of text, attachment, parameters or send. Surface and terminal background opacity are 1. The parameters glyph is declared independently from settings and uses template tint.

## Verification

CLI 2.4.1 focused validation and package round trip passed; all 97 source themes and required previews passed the full source check. Palette opacity/contrast floors were inspected. Character, Home spacing, both environments and gallery artwork were visually inspected as source images. The generated alpha channels and declared hashes are preserved.

Native acceptance was not completed; device automation was stopped at the user's direction. No claim is made for a complete phone/Pad layout matrix, long draft, keyboard, voice, iOS or live sending test. Only a disposable QA emulator was used; no user device or real paired workspace was automated.
