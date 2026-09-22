# Fern and Fiord

A Fiordland landscape interpreted as layered carved pigment: vertical cliff striations meet finely cut fern silhouettes and long silver reflections. The light interface uses blue-grey mist and mineral teal; the dark interface moves into cold slate shadow with glacier-cyan controls. Greenstone and fern greens stay in the artwork, separating the cool interface from the forest. This is an original landscape interpretation rather than an exact landmark reconstruction.

Four independently composed wallpapers serve light/dark and compact/regular layouts. The foreground fern-and-stone illustration is isolated on transparency. The back glyph is a leafy direction stem, send is a kayak crossing the fiord, and attachment is an unfurling stem shaped as a paperclip. All three tint with the interface palette. Default Muqun home identity is preserved.

The gallery cover pairs the theme's own light artwork on the left with dark artwork on the right, at 1024 × 640. UI and terminal surfaces use 96% authored opacity for restrained atmosphere.

## Landscape reference

The Department of Conservation describes Fiordland's ice-carved fiords, rainforests and cascading waterfalls. Used as factual landscape context only; no reference artwork is reproduced.

- https://www.doc.govt.nz/parks-and-recreation/places-to-go/fiordland/places/fiordland-national-park/

## Validation

CLI 1.8.0 validation, contrast, package round trip, and source checks pass. The shared interface opacity floor is 94%; terminal is 93%, below the authored 96% values. This theme has no validation warnings. Artwork and transparent glyphs were inspected, including tinted glyphs at 17px and 34px in both modes.

The CLI browser preview loaded the theme and exposed the dark device previews in its accessibility tree. Browser screenshot capture failed and input commands timed out, so the full device visual review remains unverified.


## Unified Home artwork

Classic and Editorial resolve one `home.artwork` foreground, using the manifest’s light/dark and compact/regular overrides. `home.background` remains the independent wallpaper. The layout positions the foreground; it never stacks a second Home illustration. `homeIdentity.artwork` controls default visibility. Startup reuses the same foreground unless an explicit `launch.artwork` preserves a distinct launch composition. Existing artwork filenames are retained; they do not identify rendering slots.

## Toolbar surfaces

Toolbar controls use the normal theme surface. This theme does not force a transparent or specially translucent toolbar; readers can adjust surface opacity in the app.
