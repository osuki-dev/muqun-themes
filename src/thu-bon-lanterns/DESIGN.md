# Lanterns on the Thu Bon — Design and review

Country: Vietnam. Public-facing metadata is English.

## Direction

Original Vietnamese silk-and-lacquer-inspired illustration: Hoi An ochre shophouses, handcrafted lanterns, wooden river boat and quiet jade water. The scene is an artistic interpretation of the Thu Bon riverside.

## Palette reservation

| Role | Light | Dark |
| --- | --- | --- |
| Background | #F4F4E8 | #0B211B |
| Surface | #FCF9EE | #112D24 |
| Raised surface | #E7EDDF | #1A382D |
| Text | #142F27 | #FFF5D9 |
| Primary | #165843 | #B4E3C4 |
| Warning / gold accent | #71520D | #FFE1A1 |

Reserve jade / rice-paper / ochre for this theme. Avoid the blue/cream family of Cloud Post Office and the burgundy/champagne family of Paris, After the Rain.

Semantic colors and all 16 ANSI entries were authored separately for this palette; native home identity and chrome icons remain default. Decorative artwork occupies the shared wallpaper and empty state. Controls use colored surfaces so text and states retain hierarchy.

UI opacity: 90%. Terminal opacity: 92%. Both exceed the CLI contrast floor. Shared interface floor: 86%; terminal: 85%. No full-opacity failures were reported by contrast.

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
bunx @osuki-dev/muqun-theme@1 validate thu-bon-lanterns
bunx @osuki-dev/muqun-theme@1 contrast thu-bon-lanterns
bunx @osuki-dev/muqun-theme@1 check --sources
bunx @osuki-dev/muqun-theme@1 pack thu-bon-lanterns --no-optimize
bunx @osuki-dev/muqun-theme@1 preview thu-bon-lanterns --port 4175 --no-open
```

Keep this theme in its own branch and PR. Only src/thu-bon-lanterns/ belongs in the PR; dist/ and index.json are generated. Do not merge or publish as part of a local review.
