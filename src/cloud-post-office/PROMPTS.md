# Cloud Post Office

Original Japanese anime fantasy theme created locally on 2026-09-13 using the built-in image_gen tool. No external artwork or named franchise was used as a reference. Night and portrait variants reference only images generated for this theme.

## Local development

Version: 1.1.0. License: All rights reserved; no public distribution license selected for this local development version. No publishing or application is performed by this source folder.

The default Muqun home name, logo and chrome icons are retained. The shared wallpaper and empty-state illustration carry the visual story; control surfaces intentionally use the palette without additional artwork so labels and states remain clear.

## Asset processing

Four wallpapers are 1536×1024 or 1024×1536. The square paper courier was resized from 1254×1254 to 768×768, preserving transparency. The four opaque wallpapers were encoded to static WebP at quality 85. The transparent paper courier is retained as PNG to avoid artifacts observed in the local WebP conversion. No other local image edits were made. The manifest contains SHA-256 digests of the final asset bytes. Initial town-and-sky explorations were discarded and are not packaged.

## Exact generation prompts

### scene-wide-light.webp

```text
Use case: stylized-concept
Asset type: final landscape wallpaper for an inventive original Japanese anime app theme, 1536x1024.
Primary request: The Cloud Post Office, an imaginative Japanese anime world. A tiny charming sky-blue and cream Japanese postal kiosk on a floating railway platform above an immense luminous cloud sea, thin brass postal tubes curling into sky, a few floating envelopes turning into tiny paper birds. One original adult anime postwoman with short ink-blue bob, cream cape jacket, teal messenger satchel and coral hair ribbon stands near the kiosk looking toward the sky. No existing franchise.
Composition: beautifully composed wide establishing shot, kiosk and small readable full-body character in lower-right quarter, floating platform curves along bottom edge, expansive quiet pale sky and softly painted clouds across center and left for app content. Strong crafted silhouette, fine cel-shaded character drawing, richly hand-painted 2D background, airy cinematic daylight, powder blue and warm ivory with restrained coral accents, subtle whimsical detail. Avoid generic photoreal scenery. No text, letters, signage glyphs, logos, watermark, UI or border. One cohesive illustration.
```

### scene-wide-dark.webp

```text
Use case: lighting-weather
Asset type: dark-mode landscape wallpaper for The Cloud Post Office anime theme.
Input: edit target, the daylight cloud post office illustration.
Preserve exactly the original adult postwoman's face, bob haircut, costume and anatomy, kiosk design, brass transparent mail tubes, floating railways, buildings and landscape framing. Transform the same world into a magical star-mail night shift: deep ink-blue and muted violet cloud sea, soft moonlight, warm amber lamps, floating envelopes and paper birds gently glowing like constellations, very subtle star trails near upper edge. Rich hand-painted Japanese anime background, restrained contrast in center-left behind app content. No text, logos, watermark or UI. Landscape 1536x1024.
```

### scene-light.webp

```text
Use case: stylized-concept
Asset type: portrait phone wallpaper 1024x1536 for Cloud Post Office.
Input reference: wide daylight Cloud Post Office, preserve original adult postwoman appearance, cream cape, ink-blue bob, coral ribbon, blue satchel, kiosk architecture and rich Japanese anime art style.
Recompose scene for a tall phone instead of cropping. Tiny floating postal station and full-body postwoman occupy lower-right third; curve of suspended train track sweeps along bottom; large pale blue sky and soft luminous clouds occupy upper two-thirds, sparse envelopes turning into paper birds near top edge. Whimsical brass mail tubes integrated into station; floating islands only in distance. Center must be restful for UI. Exquisite hand-painted 2D anime background, warm ivory daylight and airy blues. No text, logos, watermark, UI, borders.
```

### scene-dark.webp

```text
Use case: lighting-weather
Asset type: portrait dark-mode Cloud Post Office phone wallpaper 1024x1536.
Input image 1 is edit target portrait daylight; image 2 is supporting reference for night lighting.
Preserve image 1 composition, character identity, face, clothes, anatomy, kiosk, mail tubes, railway and tall aspect ratio. Change daylight to magical star-mail night shift matching image 2: midnight ink blue and muted violet clouds, warm amber lamps and gently glowing mail envelopes/paper birds, sparse delicate stars. Keep upper middle restful, no large new objects. Original hand-painted Japanese anime illustration. No text, logos, watermark or UI.
```

### paper-courier.png

```text
Use case: stylized-concept
Asset type: square transparent-background empty-state illustration for Cloud Post Office Japanese anime app theme, 1024x1024.
Primary request: a charming ivory origami swallow delivering a tiny sealed cream envelope with a coral wax seal, circling above a little fluffy cloud and a tiny blue brass-trimmed postal satchel. Clear whimsical anime illustration, fine ink-blue outlines, restrained soft cel shading, small warm gold star sparkles, clean elegant shape language matching an anime floating post office. Compact centered silhouette with generous transparent margin. Truly transparent background alpha, no white rectangle, no checkerboard drawn in, no scenery, no text, no logo, no watermark, no interface. Must remain readable on both pale ivory and dark midnight backgrounds.
```

## Theme-specific generated glyphs, version 1.1.0

Generated with the built-in image_gen tool and resized to 128×128 PNG with transparency preserved. These replace the discarded geometric draft icons.

### icon-back.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original BACK navigation glyph for Cloud Post Office: a bold left-pointing chevron built from two folded paper wing shapes, one broad negative-space diagonal fold makes it feel like a folded letter. Clearly a left arrow first, paper craft second. No bird head or extra object. Flat solid BLACK silhouette with generous clear cutouts. Readable at 17 pixels. Centered square with 15 percent genuinely transparent margin. No text, logo, gradients, shadow, border or white rectangle. One isolated icon.
```

### icon-send.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original monochrome app SEND glyph for Cloud Post Office. Compact silhouette of an origami swallow flying toward upper right while carrying a tiny sealed envelope, the pointed forward wing and beak form a clear directional send arrow. Minimal bold flat BLACK filled shapes, three or four large readable shapes maximum, generous negative-space cuts, no thin feathers, no tiny ornament. Elegant playful folded paper language matching an illustrated floating post office. Must be immediately readable at 17 pixels. Centered inside a square with 15 percent transparent margin. Truly transparent alpha background, no white square, no checkerboard, no text, no logo, no gradients, no shadow, no border. One isolated glyph, not a sheet.
```

### icon-attach.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original monochrome app ATTACH FILE glyph for Cloud Post Office. A closed square postal envelope with one distinct round wax seal at center, with a large simple PLUS cutout inside the seal. Envelope outline is thick with a broad triangular flap cutout. Compact 3-shape silhouette reads as add a letter or attachment. Playful folded paper, not standard paperclip. Bold flat BLACK silhouette, broad transparent cutouts, no feather details. Readable at 17 pixels. Centered square, 15 percent transparent margin. Genuinely transparent background, no white rectangle, no text, no watermark, no gradients. One icon only.
```

## Gallery cover

Generated with the built-in image generation tool. Encoded as a 1024 px WebP.

```text
Use case: ads-marketing
Create one exquisite standalone theme gallery cover, landscape 3:2, for "Cloud Post Office". Japanese anime illustrated floating postal railway above clouds, original young courier with ink-blue bob, cream cape, coral ribbon and leather satchel; brass postal tubes, folded envelopes and origami swallow. Powder-blue daylight blending into ink-navy stars. Original polished illustration with sophisticated editorial composition, distinctive cultural craft texture. Show the theme's day and night atmosphere as one coherent scene. Center focal subjects within middle 65 percent for thumbnail cropping. No text, typography, watermark, logo, borders, phones or fabricated app interfaces. Full bleed finished artwork.
```

## Distinct Home hero

Create a NEW standalone square Home hero illustration, 1024x1024, intended to resize to768px. Original anime illustration of a cheerful young adult sky-postwoman with ink-blue bob haircut, cream cape, coral ribbon, small brass goggles and blue satchel, seated on a crescent-shaped cloud sorting three sealed letters beside a tiny brass mailbox. Airy sky blue and cream with coral accents. Full contained character composition. No paper bird. One cohesive central composition fitting within80% of canvas, generous transparent margins on all four sides. GENUINELY TRANSPARENT background with real alpha, no checkerboard texture, no colored rectangular backdrop, no white paper backdrop, no frame, no text, no logo. Beautiful readable contained illustration at180px display height. Subtle dark and light outlines keep subject legible on both light and dark app surfaces.

## Editorial Home foreground, version 1.2.0

Generated with the built-in image generation tool as a transparent 1536×1024 source. It was center-cropped to 1536×768 and resized to 1024×512 with alpha preserved for the final 2:1 `home.decoration` asset. No other image edits were made.

### home-decoration.png

```text
Use case: stylized-concept
Asset type: transparent foreground artwork for the Muqun Editorial Home cover, wide 2:1 banner.
Primary request: Create a NEW original anime illustration for the established Cloud Post Office theme: a cheerful young adult sky-postwoman with short ink-blue bob hair, cream cape jacket, coral ribbon, small brass goggles and deep blue postal satchel, standing beside a tiny brass cloud-mailbox while releasing three folded envelopes that become origami swallows. Match the existing theme's refined hand-painted Japanese anime look, airy powder blue, warm ivory, brass gold, restrained coral, and ink-blue outlines.
Composition/framing: one cohesive contained foreground silhouette across a wide 2:1 canvas. Place the character and mailbox primarily in the right-middle 55 percent, with the character's face away from the upper-left utility controls. Let paper birds arc gently through the upper center. Keep the left 30 percent mostly open transparent space. Keep the entire bottom 22 percent sparse and quiet so native action cards can overlap it. All artwork must fit within the canvas with generous transparent margins; no crop at head, hands, feet, birds, mailbox, or satchel.
Style/medium: polished original 2D anime illustration, delicate cel shading, subtle paper and watercolor texture, strong readable silhouette at phone size, sophisticated rather than chibi.
Constraints: genuinely transparent alpha background; no scenery, no sky rectangle, no white backdrop, no checkerboard, no frame. No text, letters, signage, logos, watermark, buttons, interface elements, or baked UI. No paper courier bird matching the empty-state asset; use simple folded-envelope swallows. Must remain legible over both pale cloud daylight and deep midnight cloud backgrounds.
```
