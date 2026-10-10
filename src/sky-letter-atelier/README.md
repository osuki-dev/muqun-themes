# Sky Letter Atelier

Recommended layout: Editorial Cover. The theme supplies artwork; the app retains the user's Classic/Editorial preference. Home keeps the Muqun name and hides the logo.

## Geometry

The full-body transparent courier is contain-fit, aligned at x=0.92 on compact widths and x=1 on regular widths. The Editorial cover's height is min(640, width × 0.9); this keeps the complete portrait in its allocated band while leaving the left utility column clear. The native title precedes the foreground with a measured 35% title-height overlap. The bottom 32% fades into the action rail, so the face, hands and letter remain above the softened lower silhouette. The tablet cover is already anchored right by the native layout; the right-aligned contain override reinforces its open leading edge. Classic uses the same nonessential foreground with native feathering.

The independent startup portrait changes the pose and framing, showing the courier opening a letter, rather than repeating or cropping the Home asset. It is contain-fit and centered. No wallpaper or control image duplicates either portrait.

## Slot matrix

| Slot | Treatment |
| --- | --- |
| shell.wallpaper | Mode-specific pearl cyan / blue-hour navy with sparse cloud contour motifs |
| home.wallpaper | Same coordinated sky field, background only |
| home.artwork | Full-body courier, right-aligned transparent foreground |
| launch.artwork | Independently generated waist-up letter-opening scene |
| empty.artwork | Original envelope resting above a cloud, square contained illustration |
| navigation.background | Hairline horizon and trailing cloud, 12% |
| composer.background | Small paper plane and cloud at trailing edge, 12% |
| actions.background | Trailing cloud with quiet horizon line, 10% |
| cards.decoration | Small envelope at trailing lower corner, 10% |
| buttons.primary.background | Fine white paper plane at trailing edge, 12% |
| tabs.background | Low undulating horizon and trailing cloud, 12% |

All slots resolve in both modes with explicit compact/regular image entries; inherited control motifs use the same alpha artwork in each mode. Solid navigation, composer and action materials preserve labels. Background and terminal opacity are authored at 1.

Seven 96×96 template glyphs follow a 24-unit grid and consistent 1.8-unit rounded stroke: back, send, attach, create, scan, settings and Home arrow. Send is a paper plane; the other controls preserve conventional semantics for readability at 17pt. Top-level iconDirections declares actual arrow orientation.

## Review

Created using CLI 2.3.0 init, replacing all 20 scaffold placeholders. The catalogue preview is a local 1024×640 light-left/dark-right composition with control samples, seven-icon strips and startup miniatures; it is not a device screenshot. Schema validation, opacity/ANSI contrast analysis and package round trip run locally. No actual-device import, rendering or application is claimed.
