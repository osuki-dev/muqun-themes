# Paris, After the Rain — Credits and provenance

## Identity

- Theme ID: `paris-after-rain`
- Collection: Muqun Theme Collection
- Country: France
- Place: Paris
- Version: 1.1.0
- Author / attribution label: Muqun Theme Collection
- Created: 2026-09-13
- License: All rights reserved. See LICENSE.md.

## Artwork origin

All five assets were generated for this theme with OpenAI's built-in image_gen tool. The initial wide daylight scene and transparent vignette were generated from text. The night scene uses the generated daylight scene as its edit target; the portrait daylight scene uses the same generated wide scene as its composition/style reference; the portrait night scene uses only this theme's generated portrait and night images. No third-party photographs, downloaded artwork, screenshots, logos, or existing poster designs were supplied as visual inputs.

These are artistic interpretations, not documentary records or geographically exact reconstructions. The theme is not affiliated with any tourism authority, monument operator, artist, cafe, or cultural institution. No ownership or exclusive rights are claimed over depicted landmarks, historical styles or cultural symbols. AI-generated origin is disclosed; the attribution label does not assert that every generated pixel has independent copyright protection.

## Cultural research — text references only

- Paris tourism office, Art Nouveau: https://parisjetaime.com/eng/article/art-nouveau-a232
- RATP, Guimard heritage: https://www.ratp.fr/decouvrir/patrimoine/hector-guimard

These links informed the choice of cultural elements. None of the sites' photographs or illustrations are included, copied or licensed into this pack.

## Asset ledger

| File | Creation | Final format |
| --- | --- | --- |
| assets/scene-wide-light.webp | Text-generated original scene | 1536×1024, WebP quality 85 |
| assets/scene-wide-dark.webp | Night edit of generated wide scene | 1536×1024, WebP quality 85 |
| assets/scene-light.webp | Dedicated portrait composition from generated scene | 1024×1536, WebP quality 85 |
| assets/scene-dark.webp | Night edit of generated portrait | 1024×1536, WebP quality 85 |
| assets/vignette.png | Text-generated transparent vignette | 768×768, PNG with alpha preserved |

Wallpapers were converted without cropping. The vignette was downscaled to fit its UI slot; its generated alpha was preserved. SHA-256 digests in theme.json cover the actual final source bytes. Local review packages use --no-optimize so the transparent PNG remains unchanged. No scripts, research images or machine information are included in the theme pack.

## Exact prompt set

### scene-wide-light.webp

```text
Use case: stylized-concept
Asset type: landscape wallpaper 1536x1024 for a premium France-inspired app theme named Paris, After the Rain.
Primary request: an original exquisite French Belle Epoque Art Nouveau travel lithograph, NOT Japanese anime, NOT photorealistic. A Paris riverside after a gentle rain: elegant cream limestone Haussmann facades, a distant Eiffel Tower in natural daylight, a curved Seine embankment, a foreground burgundy cafe awning and delicate original botanical wrought-iron curves. Express France through local architectural proportions and elegant printmaking, not a flag collage.
Composition: main cafe detail and awning frame far right and bottom; river and distant architecture form lower third; a large quiet champagne paper sky across center and upper half for readable app content. Asymmetric editorial composition with restrained sweeping botanical ornament in corners, no enclosing border. Fine engraved lines, subtle lithographic grain, elegant flat color shapes, gorgeous nuanced hand printing. Palette limited to champagne ivory, deep burgundy, antique gold, warm limestone and graphite; avoid blue as a dominant color, avoid green as dominant. Soft warm daylight reflections on wet pavement, sophisticated and calm. No text, signage, logos, signatures, watermarks, UI. No replicas of an existing poster. One single full-bleed original artwork.
```

### scene-wide-dark.webp

```text
Use case: lighting-weather
Asset type: dark-mode landscape wallpaper 1536x1024, Paris, After the Rain.
Edit target: generated daylight Paris lithograph. Preserve the exact architecture, Eiffel Tower silhouette, cafe, wet pavement, composition, botanical ornament and lithographic print texture. Change to an intimate rainy evening with deep wine/black-cherry sky, graphite-plum shadows, soft antique-gold cafe lamps and reflections, muted rose limestone. The distant Eiffel Tower stays a plain unlit silhouette, no sparkling or special light installation. Maintain quiet low-detail middle/upper sky for UI. Dominant burgundy and warm charcoal, no blue night sky, no emerald. Fine original French Art Nouveau illustration, no text, logos, watermark or UI.
```

### scene-light.webp

```text
Use case: stylized-concept
Asset type: portrait phone wallpaper 1024x1536, Paris, After the Rain.
Input image is a style and scene reference, not a crop target. Create a dedicated tall composition of the same original French Art Nouveau Paris riverside print: burgundy cafe awning and botanical ironwork along right edge, limestone buildings and Seine bridge across bottom third, distant Eiffel Tower visible in lower central area, wet pavement reflections. Keep upper 55 percent quiet champagne sky with restrained fine botanical linework only in extreme corners. Elegant lithographic grain, delicate engraved architecture, warm champagne, burgundy, antique gold, graphite palette. Not anime, not photography. Preserve cultural architectural identity without copying an existing poster. No text, signage, logo, watermark, UI or enclosing border.
```

### scene-dark.webp

```text
Use case: lighting-weather
Asset type: dark portrait phone wallpaper 1024x1536.
Image 1 is edit target, tall daylight Paris Art Nouveau print. Image 2 is lighting and palette reference for evening. Preserve image 1 composition, tower position, cafe, plant ornament, river, architecture and tall quiet upper sky. Change only to image 2's warm black-cherry/burgundy evening palette, charcoal-plum shadows, antique-gold cafe lamps and soft wet reflections. The distant Eiffel Tower remains a plain unlit silhouette with no light show. Keep upper middle calm. Fine lithographic texture, no blue-dominant sky, no text, logo, signature or UI.
```

### vignette.png

```text
Use case: stylized-concept
Asset type: square transparent PNG empty-state vignette for Paris, After the Rain app theme, 1024x1024.
Original elegant French Art Nouveau lithographic vignette: a small ivory porcelain cafe cup and saucer with burgundy rim, curled steam merging into slender antique-gold botanical wrought-iron flourishes, one small folded burgundy umbrella lying alongside. Exquisite engraved lines and softly textured print pigments, cohesive restrained silhouette, generous fully transparent margin. Champagne, burgundy, antique gold and dark graphite outlines readable on light and dark backgrounds. Not anime, not 3D, not a flat emoji. No lettering, text, logos, watermark, solid background rectangle or checkerboard. Truly transparent alpha background.
```

## Theme-specific generated glyphs, version 1.1.0

Generated with the built-in image_gen tool and resized to 128×128 PNG with transparency preserved. These replace the discarded geometric draft icons.

### icon-back.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original BACK navigation glyph for a French Art Nouveau Paris theme: bold arrow pointing LEFT, its horizontal shaft is one graceful sweeping vine ending in a single simple leaf at the far right, while its left arrowhead is unmistakable and large. Restrained botanical curve, no thin filigree, no tiny veins. Flat solid BLACK filled silhouette, clear at 17 pixels. Centered square with 15 percent genuinely transparent margin. No text, logo, gradients, shadow, border or white rectangle. One isolated icon.
```

### icon-send.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original monochrome app SEND glyph for a French Art Nouveau Paris theme. A graceful diagonal fountain-pen feather quill pointing upper right, its streamlined nib and forward tip suggest a send arrow. ONE sweeping curved silhouette with only two broad feather cuts and a distinct nib opening, elegant asymmetry and clear direction. Minimal bold flat BLACK filled silhouette, no fine barbs, no filigree. Must be immediately readable at 17 pixels, not an ornate illustration. Centered square with 15 percent transparent margin. Truly transparent alpha background, no white square, no checkerboard, no text, no logo, no gradients, no shadow, no border. One isolated glyph.
```

### icon-attach.png

```text
Use case: stylized-concept
Asset type: transparent PNG theme UI pictogram, 1024x1024.
A single original monochrome app ATTACH FILE glyph for a French Art Nouveau theme. Two overlapping small stationery sheets held by a graceful leaf-shaped document clip at upper right. The outer contour of the clip is a simple curled Art Nouveau leaf; the two sheets keep the add-document meaning obvious. Bold flat BLACK silhouette with only three broad negative-space cuts, no veins or miniature filigree. Sophisticated broad curves, immediately readable at 17 pixels. Centered square with 15 percent transparent margin. Genuinely transparent alpha background, no white rectangle, no text, no logo, no shadows or gradients. One isolated icon.
```

## Gallery cover

Generated with the built-in image generation tool. Encoded as a 1024 px WebP.

```text
Use case: ads-marketing
Create one exquisite standalone theme gallery cover, landscape 3:2, for "Paris, After the Rain". French Art Nouveau lithograph: rainy Paris Seine, distant Eiffel silhouette, burgundy cafe awning and botanical wrought iron, cream paper and black-cherry night with golden lamps. Original polished illustration with sophisticated editorial composition, distinctive cultural craft texture. Show the theme's day and night atmosphere as one coherent scene. Center focal subjects within middle 65 percent for thumbnail cropping. No text, typography, watermark, logo, borders, phones or fabricated app interfaces. Full bleed finished artwork.
```

## home-hero

Create one original standalone app Home hero illustration. An elegant Parisian Seine footbridge with an ornate curved iron railing and one antique streetlamp, a flowering chestnut tree rising behind and a tiny rain-reflecting cobblestone landing. No coffee cup or umbrella. Art Nouveau lithographic illustration, graceful botanical lines, champagne limestone, burgundy and antique gold. One coherent compact scene, not a collection of unrelated objects. Square PNG with genuinely transparent alpha background. Complete contained silhouette, every detail inside the canvas, generous transparent margins of at least 12 percent on every side. Beautiful polished illustration readable at 180 pixels high. No text, lettering, logos, border, frame, background rectangle, checkerboard, cast shadow outside scene or cropped elements. This is a new distinct Home scene, not an empty-state icon.
