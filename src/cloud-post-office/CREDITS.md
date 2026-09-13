# Cloud Post Office

Original Japanese anime fantasy theme created locally on 2026-09-13 using the built-in image_gen tool. No external artwork or named franchise was used as a reference. Night and portrait variants reference only images generated for this theme.

## Local development

Version: 1.0.0. License: All rights reserved; no public distribution license selected for this local development version. No publishing or application is performed by this source folder.

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

