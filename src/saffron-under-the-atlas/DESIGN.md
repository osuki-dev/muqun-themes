# Saffron under the Atlas

Earthen architecture and oasis palms become woven silhouettes beneath distant Atlas peaks. Saffron cream and clay pink create the daylight world; midnight indigo and woven gold stars create its night counterpart.

The palette uses dark indigo text and burnt saffron actions in light mode, with warm ivory text and pale saffron actions in dark mode. UI and terminal planes use 96% opacity to keep dense woven texture behind readable text. Phone and tablet use independently composed portrait and landscape art.

Ribbon back, flying-carpet send and woven-loop attachment silhouettes retain familiar action directions. All three use template tinting. The default Muqun name and logo remain. Only the shared wallpaper and contained empty illustration are decorated.

## Editorial Home

## Validation

CLI 1.9.0 source validation, package round trip and package validation passed with 11 assets; the packed theme is 2.84 MiB. Contrast floors remain light interface 86%, terminal 90%; dark interface 84%, terminal 78%. Authored opacity is 96% in both modes. The CLI warns that its published build does not yet read the app's new `homePresentation` field; the field is intentionally retained for the matching app release.

All seven illustrations and the three glyphs were inspected as local raster images, including the transparent 1024 × 512 Editorial composition. Glyph tint was reviewed at 17px and 34px in both palettes. The gallery preview loaded the theme and device labels, but screenshot capture and browser interaction were unavailable; visual device review remains pending.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.

## Toolbar surfaces

Toolbar controls use the normal theme surface. This theme does not force a transparent or specially translucent toolbar; readers can adjust surface opacity in the app.
