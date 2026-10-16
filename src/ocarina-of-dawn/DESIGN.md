# Ocarina of Dawn Home composition

Version 1.1.8 repairs the artwork and framing shared by Classic and Editorial. The previous 1400×945 picture combined an opaque meadow and a chopped tree with transparent sky/margins. In a standard contain-fit band it read as an inset scenic cutout. Dark mode also reused its bright sunrise against a separate moonlit wallpaper.

The repair follows the collection's full-scene covers, including Aegean Paperlight and Acacia Afterglow. The same traveler, seated pose, green cloak, complete blue ocarina and meadow/valley remain. Environmental outpainting closes the top and side edges. Matching dawn and moonlit paintings keep the character readable in both modes.

| Mode | Width class | Home image | Size | Fit | Focal point |
| --- | --- | --- | --- | --- | --- |
| light | compact | `home-modern` | 1254×1254 | cover | 0.5, 0 |
| dark | compact | `home-modern-dark` | 1254×1254 | cover | 0.5, 0 |
| light | regular | `home-wide-light` | 1536×1024 | cover | 0.5, 0 |
| dark | regular | `home-wide-dark` | 1536×1024 | cover | 0.5, 0 |

`homePresentation.header` uses the existing cover composition. All four images have opaque upper/side edges, so the App classifies them as scenes and fills the available cover frame; the native bottom mask supplies the fade. Compact square and regular landscape variants preserve the face and instrument through different crops. These are width classes, not a theme-selected layout.

The Home title defaults to hidden, as on comparable complete scenic covers. Native review caught the previous large “Dawn” title covering the traveler's face after switching to cover framing. The gallery name remains Ocarina of Dawn. Existing toolbar backgrounds remain enabled. Home wallpaper opacity is reduced to 0.18 light / 0.20 dark so the landscape behind session text is quieter. Shell wallpaper, palette, interface fill opacity, icons, materials, startup and empty-state character remain unchanged.

## Home input resolution

Classic and Editorial use the same input slots. Compact/regular image objects replace the complete base image. Both width entries retain contain fit, focal point 0.5,0 and all-zero outsets; `home.composer.decoration` stays explicitly null.

| Mode | Width | Background asset | Opacity | Outset left/right/bottom | Overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | composer-corner-continuity | 0.24 | 0/0/0 | none |
| light | regular | composer-corner-continuity | 0.24 | 0/0/0 | none |
| dark | compact | composer-corner-continuity | 0.30 | 0/0/0 | none |
| dark | regular | composer-corner-continuity | 0.30 | 0/0/0 | none |

The separate transparent startup character remains contain-fit and is not replaced by a scenic rectangle. Missing/hidden Home artwork still follows the App's existing fallback behavior.

## Verification for 1.1.8

CLI 2.4.1 validation, contrast inspection, package round trip (17 assets, 3.85 MiB compressed), declared SHA-256 checks and the complete 94-theme source/preview check passed. App geometry checks covered nine widths from 320 to 1366 dp for both modes.

Native screenshots were inspected on a disposable Android API 36 emulator using the current App development build: phone 1080×2400 at 420 dpi and tablet 1600×1200 at 200 dpi, Classic/Editorial preferences, light/dark (eight cases). The traveler and ocarina remain visible, scene edges are complete, and the title no longer crosses the face. Tablet uses the App's shared Pad composition for both preferences. The App was restarted after changing emulator density to avoid stale Skia scale. The parameter glyph is visible, and its options panel opens.

This was an offline Home fixture with no real computer or conversation. iOS, live sending, editable long drafts, keyboard and voice states were not exercised. The composer assets/configuration, startup figure and icons are byte-for-byte unchanged; this review does not claim those untested interactions or other themes. Native screenshots remain separate QA evidence, not package/gallery artwork.
