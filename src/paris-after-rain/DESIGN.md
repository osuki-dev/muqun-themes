# Paris, After the Rain — Design and review

Country: France. Public-facing metadata is English.

## Direction

Original French Art Nouveau lithograph: rain-washed Seine, limestone facades, cafe awning and botanical ironwork. This is an illustrated Paris interpretation, not an exact location rendering.

## Palette reservation

| Role | Light | Dark |
| --- | --- | --- |
| Background | #F8F1E7 | #21151C |
| Surface | #FFF9F0 | #2B1C24 |
| Raised surface | #EEE4DA | #34252D |
| Text | #2B1922 | #FFF4E8 |
| Primary | #70233E | #F3C0D2 |
| Warning / gold accent | #715019 | #F5D8A4 |

Reserve burgundy / champagne / black-cherry for this theme. Avoid the blue/cream family of Cloud Post Office and the jade/ochre family of Lanterns on the Thu Bon.

Semantic colors and all 16 ANSI entries were authored separately for this palette; native home identity and chrome icons remain default. Decorative artwork occupies the shared wallpaper and empty state. Controls use colored surfaces so text and states retain hierarchy.

UI opacity: 90%. Terminal opacity: 92%. Both exceed the CLI contrast floor. Shared interface floor: 84%; terminal: 83%. No full-opacity failures were reported by contrast.

## Local review matrix

- [x] Inspect generated day/night wide and portrait compositions.
- [x] Dedicated phone compositions instead of automatic wide-image crops.
- [x] Keep generated images free of labels and watermarks; English manifest text.
- [x] Run validate and contrast; no errors or warnings for this theme.
- [ ] Browser light / phone, light / wide, dark / phone, dark / wide visual review.
- [ ] Browser empty state and terminal visual review.
- [ ] Native Muqun import and device review.

Browser review is currently blocked: the browser tool cannot verify the admin-enforced security policy for muqun.dev. Do not count launching the CLI server as a completed visual review.

## Reproduce

From this worktree:

```sh
bunx @osuki-dev/muqun-theme@1 validate paris-after-rain
bunx @osuki-dev/muqun-theme@1 contrast paris-after-rain
bunx @osuki-dev/muqun-theme@1 check --sources
bunx @osuki-dev/muqun-theme@1 pack paris-after-rain --no-optimize
bunx @osuki-dev/muqun-theme@1 preview paris-after-rain --port 4174 --no-open
```

Keep this theme in its own branch and PR. Only src/paris-after-rain/ belongs in the PR; dist/ and index.json are generated. Do not merge or publish as part of a local review.
