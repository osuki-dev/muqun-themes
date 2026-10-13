# Continuity artwork

All new raster artwork was authored with OpenAI built-in image generation on 2026-10-13 from this theme collection's original art or its theme brief. Each theme keeps its own subject, scene and visual medium.

## Authoring constraints

- Environmental wallpaper: recognizable scene details confined to outer edges, with a genuinely transparent center for reading. No duplicate foreground subject.
- Home cover (where present): preserve subject identity, pose and story props; extend its own environment into a square full-width scene, calm header region and genuinely transparent lower fade. Dark companion preserves composition while changing lighting.
- Gallery cover: theme art only, light on the left and dark on the right; no baked-in App controls or labels.
- Composer: transparent wide edge artwork; clear central draft area and low corner ornament weight, with explicit mode/width resolution.
- Startup repair (where present): keep portrait/pose while restoring complete story props or missing extremities.

## Added or replaced artwork

- `assets/environment-continuity.png`
- `assets/gallery-continuity.png`
- `assets/composer-continuity.png`

## Verification limits

Source inspection and CLI checks are distinct from real App review. Phone/Pad, both layouts, keyboard, long drafts and voice-to-text still require native review. Image generation output sizes are preserved; CLI packaging determines their admissibility.

## Home cover pair

- `assets/home-cover-light.png`
- `assets/home-cover-dark.png`

The Home cover uses `cover`, full opacity and top focal point in light/dark and compact/regular. Startup keeps `contain`. The original subject is preserved; the whole context is expanded. Obsolete declarations are retired after checking every remaining reference. Busy upper scenery keeps toolbar surfaces; open upper scenery opts them out.
