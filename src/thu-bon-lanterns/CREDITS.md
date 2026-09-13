# Lanterns on the Thu Bon — Credits and provenance

## Identity

- Theme ID: `thu-bon-lanterns`
- Collection: Muqun Theme Collection
- Country: Vietnam
- Place: Hoi An / Thu Bon River
- Version: 1.0.0
- Author / attribution label: Muqun Theme Collection (AI-assisted)
- Created: 2026-09-13
- License: All rights reserved. See LICENSE.md.

## Artwork origin

All five assets were generated for this theme with OpenAI's built-in image_gen tool. The initial wide daylight scene and transparent vignette were generated from text. The night scene uses the generated daylight scene as its edit target; the portrait daylight scene uses the same generated wide scene as its composition/style reference; the portrait night scene uses only this theme's generated portrait and night images. No third-party photographs, downloaded artwork, screenshots, logos, or existing poster designs were supplied as visual inputs.

These are artistic interpretations, not documentary records or geographically exact reconstructions. The theme is not affiliated with any tourism authority, monument operator, artist, cafe, or cultural institution. No ownership or exclusive rights are claimed over depicted landmarks, historical styles or cultural symbols. AI-generated origin is disclosed; the attribution label does not assert that every generated pixel has independent copyright protection.

## Cultural research — text references only

- Vietnam Tourism, Hoi An culture and Thu Bon: https://www.vietnam.travel/things-to-do/7-things-to-do-hoi-an
- Vietnam Tourism, Hoi An experiences: https://www.vietnam.travel/things-to-do/top-things-to-do-hoi-an

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
Asset type: landscape wallpaper 1536x1024 for a premium Vietnam-inspired app theme named Lanterns on the Thu Bon.
Primary request: an exquisite original Vietnamese silk-and-lacquer inspired contemporary illustration of Hoi An beside the Thu Bon River in daylight. Ochre-yellow historic shophouses with dark timber shutters and terracotta roofs, handmade silk lanterns of elongated and rounded shapes, a slender wooden river boat, delicate bougainvillea at edge. Culturally grounded central Vietnam, no Chinese pagoda mashup, no Japanese torii, no generic tropical resort.
Composition: shophouses and a few silk lanterns on far left and lower-left, river curves across lower third toward distant roofs; spacious pale celadon atmospheric sky and quiet water through center-right for app content. Carefully hand-drawn architecture, tactile silk grain, layered lacquer-like flat pigment shapes with delicate ink contours and selective golden highlights. Luminous humid morning, elegant and contemplative. Palette: jade/emerald, warm ochre yellow, pale rice-paper cream, tiny cinnabar lantern accents. Not anime, not European poster, not photorealistic. No text, signage glyphs, logos, watermark, UI, flags or frame. Single original full-bleed illustration.
```

### scene-wide-dark.webp

```text
Use case: lighting-weather
Asset type: dark-mode landscape wallpaper 1536x1024, Lanterns on the Thu Bon.
Edit target: generated daytime Hoi An river illustration. Preserve architecture, roof silhouettes, boat, flowers, lantern positions, broad quiet center-right space, tactile silk-and-lacquer pigment style. Change to a lantern-lit evening: deep jade/emerald-black sky and river, warm ochre shop walls softly lit from within, luminous amber and small cinnabar silk lanterns, restrained broken golden river reflections. No blue dominant night palette, no wine/plum dominant palette. Do not add dense crowds or extra buildings. Elegant original Vietnamese illustration, not anime, no text, signage glyphs, logos, watermark or UI.
```

### scene-light.webp

```text
Use case: stylized-concept
Asset type: portrait phone wallpaper 1024x1536, Lanterns on the Thu Bon.
Input image is a reference for the same Hoi An scene and silk/lacquer art style, not a crop target. Recompose specifically for a tall phone: ochre-yellow shophouses with dark timber shutters and tiled roofs hug left edge, a few handmade elongated silk lanterns and bougainvillea in upper-left corner, a small wooden boat at lower-left, jade river sweeping through lower portion. Tall quiet pale celadon atmosphere occupies upper center and right, ample restful space for UI. Tactile silk grain, subtle gold pigment accents and fine ink contours, Vietnamese architectural specificity, luminous warm daylight. No Chinese/Japanese architectural substitutions, no text, signage, logos, watermark, border or UI.
```

### scene-dark.webp

```text
Use case: lighting-weather
Asset type: dark portrait phone wallpaper 1024x1536.
Image 1 is edit target tall daytime Hoi An print. Image 2 is lighting and palette reference for lantern evening. Preserve image 1 architecture, lantern locations, flowers, boat, river curve, tall quiet center-right and silk/lacquer texture. Change only to image 2's deep emerald-black sky and jade water, ochre walls lit softly within, amber and restrained cinnabar lantern glow with slender broken gold reflections. No extra structures or crowd. No blue dominant sky, no burgundy dominant palette. No text, logo, watermark, border or UI.
```

### vignette.png

```text
Use case: stylized-concept
Asset type: square transparent PNG empty-state vignette for Lanterns on the Thu Bon app theme, 1024x1024.
Original refined Vietnamese silk-and-lacquer inspired illustration: two handcrafted Hoi An silk lanterns, one warm ochre elongated lantern and one small cinnabar round lantern with delicate tassels, suspended above a tiny slender dark wooden river boat and three stylized jade ripples. Restrained fine ink contours, tactile silk pigment detail, subtle gold highlights, airy coherent compact silhouette with generous fully transparent margin. Traditional central Vietnamese lantern shapes, not a Chinese pagoda, no text or signage. Rich jade, ochre, tiny cinnabar, ivory details. Not anime, not photorealism, not a flat emoji. No logo, watermark, solid backdrop or checkerboard. Truly transparent alpha background.
```
