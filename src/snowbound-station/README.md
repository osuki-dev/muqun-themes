# Snowbound Station

A little railway station and bookshop become a warm refuge in heavy snow. The
daylight palette uses icy blue and snow cream; blue hour keeps amber windows
against midnight blue. All displayed text is English.

## Composition

The wallpaper is the world: distant snowy houses, receding rails, buried platform,
and three depths of falling flakes. It contains no person. The transparent Home
vignette adds a small scarf-wrapped adult, snow-covered bench, rail and lantern
on the right, leaving the title side quiet. Classic and Editorial share this one
foreground. The independent startup illustration is a centered transparent cutout of the
traveler, station doorway and snowy bench. Its irregular alpha silhouette fits
the native square contain-fit launch slot without an opaque rectangular backdrop.

Both modes explicitly fill all 11 decoration slots. Compact wallpapers preserve
the station shelter and bookshop window; regular wallpapers retain the panorama.
All slots explicitly declare compact/regular behavior, contain-fit preserves the
foreground and square empty-state notebook/ticket, and chrome details stay faint.
Seven transparent template glyphs cover Back, Send, Attach, Create, Scan, Settings,
and Home Arrow. Their direction metadata describes the actual drawing.

## Ambient snow

Light: intensity 0.48, speed 1.2, density 1, size 1.8, textMuted palette.
Dark: intensity 0.72, speed 1.3, density 1, size 2, text palette.
Both fall down-left. Light flakes therefore have a subtle blue-gray tint; dark
flakes are snowy white. Dense static snowfall belongs to the scenic artwork;
the actual Home effect adds at most 16 moving flakes. It pauses when inactive and
respects reduced motion. Startup has static snow because Home motion begins
after startup settles. The gallery image depicts static snowfall.

Requires a Muqun 3.1.0 build with the expanded ambient-effect runtime and
Muqun Theme CLI 2.3.1 or newer. The minimum version matches the App main
branch manifest and its snow/density/size/palette/direction schema. Store
distribution was not verified; older 3.1.0 builds may lack these controls.

## Verification

Created using the local CLI `list --search snow` and `init snowbound-station`.
Run `bun ../cli/lib/cli.js validate snowbound-station`, `contrast snowbound-station`,
and `pack snowbound-station` from the themes repository. The complete source has
21 declared assets; all 20 scaffold placeholders were replaced or removed.
The PNG split preview is 1024 by 640. Artwork provenance and prompts are in
CREDITS.md. Source delivery is this directory; local dist files are generated.
