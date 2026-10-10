# Graphite Daydream

Warm ivory paper, graphite manga contours and small sepia accents surround an original adult artist. Dark mode becomes a quiet charcoal studio. The Home portrait holds a closed sketchbook; independent startup artwork shows the same artist drawing in an open book.

## Recommended composition

Editorial Cover is authored intentionally (`homePresentation.header: cover`), with the default Muqun title and hidden logo. The portrait is narrow and tall: standard Editorial's width/2 band would make its face too small. Cover's width×0.9 band provides a useful portrait scale while leaving a quiet left title/utility column. Home uses contain-fit, x=0.82 and y=0 for the phone and Pad; the source's top edge stays intact and the app's bottom feather merges the waist into the action rail. The portrait is decorative; no control or essential text is baked into it. Classic remains supported through the shared contained foreground, but Editorial Cover is the intended presentation.

Both modes explicitly define compact and regular overrides for every slot. Startup is independently composed and centered at x=0.5/y=0.4. Solid navigation, composer and actions keep labels readable. Decorative chrome rules appear at 7–10% opacity; the low-strength wallpaper contributes quiet fiber marks without competing with sessions.

## Slot matrix

| Slot | Artwork | Treatment |
| --- | --- | --- |
| shell.wallpaper | paper-light / paper-dark | tiled quiet paper fibers, 80% |
| home.wallpaper | paper-light / paper-dark | matching Home paper, 80% |
| home.artwork | artist | independent standing portrait; contain, right aligned |
| navigation.background | chrome-light / chrome-dark | double pencil rule, 10% |
| composer.background | chrome-light / chrome-dark | double pencil rule, 9% |
| actions.background | chrome-light / chrome-dark | double pencil rule, 9% |
| cards.decoration | card-rule | short corner mark and bottom rule, 8% |
| buttons.primary.background | button-hatch | small right-edge diagonal hatching, 7% |
| tabs.background | tab-rule | low pencil underline, 8% |
| empty.artwork | empty-book | small closed sketchbook/pencil symbol, contain |
| launch.artwork | launch | distinct open-sketchbook artist pose, contain |

All seven chrome/Home icons use coherent 128px transparent pencil-stroke shapes in template mode; the app supplies mode and state colors. Back points left, Send points right, and Home arrow points up-right, declared through top-level `iconDirections`. Functional silhouettes stay conventional and thick enough for 17pt rendering.

The 1024×640 gallery preview shows light left/dark right, matching controls and a startup sample. It is a designed gallery composition, not an app screenshot.

## Authoring and validation

Local CLI 2.3.0 `list --search graphite-daydream` found no published match. CLI `init graphite-daydream --dir tmp/graphite-daydream-scaffold` created a scaffold; its 17 palette roles and 16 ANSI entries were compared with the original authored manifest, and its placeholders are not included. Source has 18 declared assets, 7 icon mappings and all 11 slots. `validate` succeeds, `contrast` reports no full-opacity failures, and `pack` round-trips successfully (about 1.06 MiB optimized). The only size warnings are the two 1024×1536 original character images exceeding the recommended 1024px longest edge.

Shared readability floors are 89% for interface and 92% for terminal; authored surfaces and terminal are fully opaque. Light floors are 89%/92%, dark 87%/90%. Credits and exact generation prompts are in CREDITS.md.
