# Paris, After the Rain — Design and review

## Current Home continuity candidate 1.2.8

Rainy Paris limestone facades, cafe awnings and tree canopy extend through the cover top; the photographer and cafe remain one complete scene. A faint architectural paper wallpaper continues the street down the page.

This section supersedes the older wallpaper-omission notes below. The new opaque 1322×1190 Home cover is painted through both upper edges. All light/dark and compact/regular Home artwork resolutions use cover fit, opacity 1 and top-center focal points. Cover presentation, toolbar surfaces, identity, launch/empty art and palettes are preserved. The nearly square source fits the phone cover band more closely than the former wide painting. Native bottom feathering blends it into the independent wallpaper.

Four independently generated Home wallpaper assets provide light/dark and compact/regular resolutions: 887×1774 phone sources and 1024×1536 regular sources. They use cover fit and top-center focal points, at opacity 0.42 light / 0.35 dark. Scene forms stay at the outer edges; the central 70% and the lower reading region remain quiet paper. No hero subject is repeated. The explicit null shell wallpaper is preserved; Home wallpaper may still serve the App's shell-sheet fallback.

Composer resolution matrix: light compact, light regular, dark compact and dark regular all resolve the existing transparent composer-accent image, contain fit, top-center focal point, Home opacity 0.18 / ordinary composer opacity 0.12, outset omitted (zero), Home overhang decoration absent. The central draft and lower controls remain transparent. These are inspected source resolutions, not native long-draft screenshots. The published chrome.parameters template glyph is restored independently of chrome.settings.

Generated heroes, all four wallpaper sources and existing composer artwork were visually inspected. The App's current Editorial artwork sizing/resolution code was read. CLI validate and contrast passed for this version; resource warnings remain for the existing gallery, launch and composer sources and the new cover exceeding 1024px. Existing gallery source is 1586×992, larger than the recommended 1024×640 export. Isolated three-theme source packaging is recorded in the final report.

Native phone/Pad, Classic/Editorial, light/dark, keyboard, long drafts, parameters open/closed, voice-to-text and landscape tablet clipping remain unverified. No device run or publication was performed. Generation briefs and provenance are recorded in SCENERY-PROMPTS.md.

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

Semantic colors and all 16 ANSI entries were authored separately for this palette; native home identity and home identity remains default; chrome icons use the version 1.1.0 set. Decorative artwork occupies the shared wallpaper and empty state. Controls use colored surfaces so text and states retain hierarchy.

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
bunx @osuki-dev/muqun-theme@1.7.0 validate paris-after-rain
bunx @osuki-dev/muqun-theme@1.7.0 contrast paris-after-rain
bunx @osuki-dev/muqun-theme@1.7.0 check --sources
bunx @osuki-dev/muqun-theme@1.7.0 pack paris-after-rain --no-optimize
bunx @osuki-dev/muqun-theme@1.7.0 preview paris-after-rain --port 4174 --no-open
```

Keep this theme in its own branch and PR. Only src/paris-after-rain/ belongs in the PR; dist/ and index.json are generated. Do not merge or publish as part of a local review.

## Version 1.1.0 / CLI 1.7.0

Botanical back arrow, quill send, and leaf-clipped stationery attachment.

The three theme-specific generated glyphs replace the rejected generic geometric draft. Each is a 128×128 transparent PNG used in template mode. Local 17px and 34px checks cover silhouette and contrast; browser preview remains a separate gate. Palettes and home identity are unchanged.

## Gallery preview

A dedicated illustrated cover is referenced by `preview`. It represents the theme atmosphere and is separate from app wallpaper and UI screenshots. Validated using CLI 1.7.1.

## Version 1.2.0 — Editorial Home

## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.wallpaper` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.

## Toolbar surfaces

Toolbar controls use the normal theme surface. This theme does not force a transparent or specially translucent toolbar; readers can adjust surface opacity in the app.
