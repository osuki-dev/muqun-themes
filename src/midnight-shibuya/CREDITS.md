# Credits

- Art direction, palette, manifest, icons, and compositing: Muqun
- Background and hero artwork: generated with OpenAI image generation
- Preview: composed from the included light and dark artwork

No third-party images, trademarks, or fonts are included.

## Native adaptation 1.1.3

`assets/icon-create.png`, `assets/icon-scan.png`, `assets/icon-settings.png`, and `assets/icon-arrow.png` are original vector glyphs authored for this theme and rasterized to transparent 128×128 PNG with ImageMagick. Quiet rounded urban linework matching the original white template glyphs. No third-party source or reference artwork was used. Covered by the theme’s existing license. Existing illustrations are unchanged. `home.arrow` visibly points up-right; its direction metadata declares that source orientation.

`assets/preview.png` is a deterministic light/dark gallery composition of the existing foreground artwork, final palette and native control glyphs. It is a concept preview, not a device screenshot.

## 2026-10-15 startup and parameter artwork repair

Pack `midnight-shibuya` version `1.1.7`.

`assets/icon-parameters.png` is an original transparent geometric glyph exported from a vector drawing for this theme: two adjustment rails with umbrella handles. It replaces the generic glyph while keeping the parameters control recognizable at small sizes. Its existing independent `chrome.parameters` declaration and `template` tinting remain; no settings fallback or other icon was changed. Light and dark tinted source previews were inspected.

Home input artwork is unchanged. Resolved mode/width declarations (responsive images replace the entire base image):

| Mode | Width | Background (asset, fit, opacity, focal point, outset) | Overhang |
| --- | --- | --- | --- |
| light | compact | none | none |
| light | regular | none | none |
| dark | compact | none | none |
| dark | regular | none | none |

Omitted outset edges resolve to zero. Missing background/overhang paints nothing. Classic and Editorial share these slots. Source integrity, schema/asset validation, contrast and in-memory source packing are checked separately from visual inspection. Native phone/Pad checks in both layouts and modes (long drafts, keyboard, parameters open/closed and voice-to-text) remain unperformed; no theme was imported or auto-applied.
