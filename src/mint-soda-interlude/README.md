# Mint Soda Interlude

Complete original cafe theme using mint, cream and peach with deep botanical night mode.

Initialization evidence: `bun ../cli/lib/cli.js init mint-soda-interlude` ran from `themes/` before authoring, reporting 11 decoration slots and 20 placeholder images. The scaffold was adapted and every placeholder replaced.

## Slot matrix

| Slot | Light / dark asset | Purpose |
| --- | --- | --- |
| shell.wallpaper | paper-light / paper-dark | Quiet edge bubbles |
| home.wallpaper | paper-light / paper-dark | Matching calm ground |
| home.artwork | barista | Standing original adult barista |
| navigation.background | rail-light / rail-dark | Subtle edge bubbles |
| composer.background | stationery-light / stationery-dark | Fine stationery rule |
| actions.background | rail-light / rail-dark | Coordinated chrome bubbles |
| cards.decoration | card-light / card-dark | Corner stationery mark |
| buttons.primary.background | button-light / button-dark | Subtle on-primary circles |
| tabs.background | stationery-light / stationery-dark | Coordinated rule |
| empty.artwork | empty | Soda glass and peach coaster |
| launch.artwork | launch | New waist-up serving gesture |

Seven original 96px alpha PNG template icons replace chrome.back, chrome.send, chrome.attach, chrome.create, chrome.scan, chrome.settings and home.arrow. Rounded 7px strokes remain visible at 17pt. Top-level iconDirections declares back left and send/home arrow right.

## Layout rationale

Read actual app home-editorial-artwork.tsx, home-editorial-layout.tsx and hero-feather.ts. Cover is chosen because standard Editorial limits artwork to width/2 height; cover offers width×0.9 and better displays this tall silhouette. Its lower mask begins at 68%, preserving face and soda while the skirt dissolves. Classic uses proportional native feathering.

Both modes explicitly contain compact and regular foregrounds. Home focal x=0.56 compact / 0.60 regular gently biases art away from leading utilities; y=0.10 / 0.05 aligns vertical slack near the top. Launch stays centered x=0.5, y=0.20 / 0.05. Contain preserves every source pixel; focal points position slack rather than crop. The app owns title width fitting, action placement and missing-art fallback. Default Home name remains visible with logo hidden. Chrome is solid and motifs are at 12–15% opacity.

Preview is a 1024×640 catalogue composition with actual palette, original art, icon strip and independent launch miniature. No native device import or screenshot is claimed.
