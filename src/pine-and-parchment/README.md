# Pine & Parchment

An original young adult field-sketch courier wears a cream hoodie, a soft pine utility vest and modern sneakers. Daylight uses warm parchment and deep green ink; night uses pine surfaces and soft sage accents. Brass appears in small illustration details and warning states, keeping the palette restrained. All text roles and the terminal's sixteen ANSI foregrounds were designed for full-opacity readable surfaces.

## Native layout composition

Editorial cover is intentional. A single transparent seated character is the Home foreground. The right-aligned contain fit leaves space on the phone's upper left for native utilities; top alignment preserves the complete hair and youthful face. The sketchpad and folded paper-map plane overlap the outfit to supply near/middle depth, while distant faint pines and contour lines live only on Home wallpaper. No character is duplicated between wallpaper and foreground. The map and coat occupy the lower feather region; the face is near the top. Classic uses the same unified artwork and lets the app own its banner geometry.

Both compact and regular overrides are explicit in each mode. Regular retains the complete portrait with right alignment; the wide diagonal landscape foreground spreads across a wider Pad pane; the 1200px square wallpaper covers the background and spreads the contour landscape independently of the portrait. The app's cover Pad column offsets and native title layering remain responsible for final placement. The Home name is hidden and the default logo retained, reducing title collisions. Artwork contains no UI, essential text or device frames. Missing art retains the app's normal fallback. No real-device import test is claimed.

Startup has an independent centered waist-up composition: the same character shares a freshly drawn botanical sketch toward the viewer. It is not a crop or duplicate of the Home picture. The empty illustration is a square map/compass drawn specifically for this theme.

## Slot map

| Slot | Artwork | Treatment |
| --- | --- | --- |
| shell.wallpaper | wallpaper-light / wallpaper-dark | quiet mode-specific contour field |
| home.wallpaper | home-wallpaper-light / home-wallpaper-dark | faint distant pine silhouettes and contours |
| home.artwork | home-artwork | transparent single character; contain, right/top |
| launch.artwork | launch-artwork | independent map-opening pose; contain, centered |
| navigation.background | navigation | subtle brass contour/branch motif |
| composer.background | composer | subtle brass contour/branch motif |
| actions.background | actions | subtle brass contour/branch motif |
| cards.decoration | cards | subtle brass contour/branch motif |
| buttons.primary.background | buttons | subtle brass contour/branch motif |
| tabs.background | tabs | subtle brass contour/branch motif |
| empty.artwork | empty | square map/compass; contain |

All six chrome motifs use 8% slot opacity, subordinate to labels. The seven 128px template glyphs are rounded 8px strokes with transparent backgrounds. Back points left, Home arrow points right, send points up-right; top-level iconDirections records these drawn orientations. Create is a plus, scan is framed corners, attach is a paperclip, and settings is a gear. At 17pt they stay semantic and consistent.

The 1024x640 gallery image shows daylight and night, a startup inset, UI color samples and the complete icon strip. It is an authored palette composition, not a device screenshot.

## Local checks

Created with the local CLI init scaffold after a catalogue search for pine. All placeholders were replaced. Validate and contrast pass; surfaces and terminal are authored at opacity 1. Pack creates the ignored distribution file with a successful importer round trip. The root maintainer runs the shared source/preview check with the other themes.

## Home composer (1.0.2)

The courier's botanical map returns as a small desk still life at the bottom of
the Home input: folded parchment, pine needles, a pinecone and a brass drafting
compass. It is a transparent, irregular island rather than a second input frame.
There is no extra character on the upper-right rim and no baked background plate.
The existing surface colors and authored background opacity remain unchanged;
the reader's saved opacity continues to control the App's field fill.

| Mode | Compact | Regular | Artwork opacity | Image outset |
| --- | --- | --- | --- | --- |
| Light | home-composer-botanical, contain, center/bottom | same asset, contain, center/bottom | 0.82 | left/right 12 dp, bottom 8 dp |
| Dark | home-composer-botanical, contain, center/bottom | same asset, contain, center/bottom | 0.62 | left/right 12 dp, bottom 8 dp |

All four responsive declarations repeat the full image settings. The Pad uses
the same low central island without stretching it across the wider input. The
outset is an image envelope, not a promise that artwork fills every margin.
`home.composer.decoration` is explicitly disabled in both modes. The template
`chrome.parameters` glyph uses three circular adjustment handles, consistent
with the other rounded line icons and distinct from Settings.

CLI 2.4.1 source validation, contrast analysis and package round trip are the
local authoring checks. They do not establish native phone/Pad acceptance;
Classic/Editorial, keyboard, long drafts and inline dictation still require the
App's coordinated visual review. The existing gallery cover remains pure
artwork and palette, without a simulated input field.
