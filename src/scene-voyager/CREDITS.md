# Artwork provenance

Original illustrations generated for Muqun with OpenAI image generation on 2026-09-22, with expanded launch compositions on 2026-09-23. Released by the author under CC0-1.0. No external photographs, branded marks, fonts, or interface screenshots are bundled.

- `assets/artwork-light.png`: the existing close-up courier, laptop, and cream Tokyo/Fuji circular vignette for Home.
- `assets/artwork-dark.png`: the existing close-up astronaut, laptop, and orbital vignette for Home.
- `assets/launch-light.png`: the same visual direction expanded to a complete courier and bicycle, including both wheels and shoes, with transparent outer space.
- `assets/launch-dark.png`: a complete astronaut including helmet and both boots, with transparent outer space.
- `assets/preview.png`: the retained 1024 × 640 gallery composition of the Home illustrations.
- `assets/icon-attach.png` and `assets/icon-create.png`: existing original template glyphs. The other five supported glyphs are original manga-stroke vector drawings exported as template PNGs.

The supplied Scene study was a visual direction reference only. Home continues to use exactly one unchanged `home.artwork` layer. Distinct complete launch images use `launch.artwork` with contain fitting; they are never an additional Home foreground. Existing Classic and Editorial layouts own all geometry and controls.

## 2026-09-24 wallpaper extension

`assets/wallpaper-light.png` is an original OpenAI-generated, wordless cream-paper Tokyo and Fuji screenprint scene. `assets/wallpaper-dark.png` is a matching night edit of that image, preserving the composition and converting the sun to an antique-gold moon. The source prompts specified no characters, brands, interface, or lettering. Both images are included under the theme's CC0-1.0 licence.

## 2026-10-15 startup and parameter artwork repair

Pack `scene-voyager` version `1.0.8`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with compass handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | none | none |
| light | regular | none | none |
| dark | compact | none | none |
| dark | regular | none | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
