# Layered artwork revision

The youthful direction and original new full scenes are preserved. Complete figures are authored as a genuine-alpha square foreground, separated from subject-free daylight/night environments. This prevents the same character appearing twice and allows the existing Classic, Editorial and Stage foreground layout to position figures. Both width classes explicitly resolve foreground and wallpaper; original phone and tablet scenes remain in responsive launch artwork. Empty states use the complete square foreground. Eight semantic icons and their direction contract remain unchanged.

Restored decoration slots: home.composer.background. These are small non-character motifs and keep the draft area clear.

## Retired assets

The following original assets depict the superseded character or location or preview; they were not restored because they conflict with the new art direction. Their historical documentation is retained.

- `assets/home-scene.png`
- `assets/launch-traveler.png`
- `assets/scenery-dark-continuity.png`
- `assets/scenery-light-continuity.png`

## Generation provenance

Generated with the built-in OpenAI image generation tool. Foreground edit referenced the new compact daylight scene; daytime environment referenced that scene; night environment referenced the generated daytime environment.

### hero

Extract the foreground subjects from this reference into a genuinely transparent background PNG. Preserve exact original art style, adult identities, clothing, meaningful interaction, complete head-to-toe bodies and all shoes/feet. Include necessary support bench/stool for seated people; include snowboard for snow pair; include drumkit/bass and cat for musicians; include reader's cat and book. Remove ALL environment, sky, architecture, ground and scenery. Compose clean isolated full figures with natural support props within square1024x1024 canvas, no cropping, 6% padding. Do not add new characters, text, logos or watermark. True alpha background.

### environment-light

Create a SUBJECT-FREE environment wallpaper derived from this exact reference. Remove ALL people and animals and foreground personal props/instruments. Keep original drawing style, palette, location, warm daylight and environmental details. Broad subdued central forms, restrained contrast behind phone UI, rich edges; no enormous empty blank band. Recompose landscape1536x1024 so central crop also works portrait. No text labels logos UI watermark. Fully opaque background.

### environment-dark

Edit only lighting of this exact empty environment into quiet blue nighttime with subtle warm practical lamps. Keep architecture and composition exactly unchanged. No people or animals; no text logos UI. Landscape1536x1024.

## Acceptance

Source images inspected for complete bodies, genuine alpha, subject-free environments and coherent props. CLI and contrast results are reported separately. Native Classic/Editorial/Stage phone/tablet validation remains pending with the parent QA agent; source validity is not visual acceptance.

## 1.1.13 compact Stage framing

Native iPhone Stage 1.1.12 cropped the snowboard and outer arm/boot. Compact now uses a separate 2:1 centered transparent foreground with complete figures and board. Regular art and all other slots stay unchanged. Native recheck is pending.

## 1.1.14 Home and launch composition roles

Home now uses the previous launch scene, with explicit light/dark and phone/Pad
images. Home foreground is disabled so the snowboard friends appear only once.
The launch images deterministically combine the previous subject-free Home
mountains and complete transparent friends, retaining the muted environment
and full snowboard. Compact canvases remain 1024x1536; regular canvases remain
1536x1024. Existing source images, icons, composer decoration and palettes are
unchanged. The new composites are static WebP images; no new artwork was generated.

Manifest validation, contrast, packaging and full source checks are recorded in
the follow-up PR. Native launch and Classic/Editorial/Stage phone/Pad acceptance
must be reported separately; source previews are not device screenshots.
