# Jasmine at Dusk

A laughing adult woman in cream linen and a coral scarf relaxes on a jasmine rooftop, captured in natural lifestyle photography.

## One pack, three Home layouts

The existing Home artwork slot supplies one complete transparent foreground in contain fit. Classic, Editorial and Stage choose their own geometry; the manifest adds no layout selector. The complete foreground is also used at launch. No characters occur in wallpaper.

Compact uses the existing portrait scene. Regular now uses a separately recomposed 1536×1024 landscape scene that retains the architectural vista and foreground floor together. Light and dark have independently lit environments. Full-body foreground sources remain uncropped; native fades and control overlap need device review.

## Resolved decoration mapping

| Mode | Slot | Base | Compact | Regular |
| --- | --- | --- | --- | --- |
| light | home.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | home.wallpaper | background-light / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light-regular / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | launch.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | empty.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | home.composer.background | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} |
| light | composer.background | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} |
| dark | home.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | home.wallpaper | background-dark / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark-regular / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | launch.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | empty.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | home.composer.background | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.18 / focal {'x': 0.5, 'y': 0} / outset {} |
| dark | composer.background | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} | composer-accent / contain / 0.12 / focal {'x': 0.5, 'y': 0} / outset {} |

## Controls and evidence

Eight themed semantic icon slots are present, with template tinting and native fallback if unavailable. Settings uses a gear independently from parameter sliders; directional arrows retain their declared direction. Computer selection retains native semantics. Restored accents preserve their original bounded placement. New camera/headphone accents use 0.18 Home input opacity; no outset is added.

Source validation and contrast are separate from native acceptance. Pending per-pack acceptance: Classic/Editorial/Stage × phone/Pad × light/dark, long computer titles and drafts, keyboard, parameters, voice, user opacity and theme switching. These source notes claim no screenshots.

## Version 1.0.16 provenance correction

Settings now uses the newly authored original geometric cog from Aperture 1.1.10. Template tint preserves this theme palette. Other artwork and responsive declarations are unchanged. Native review of this cog remains pending. See CREDITS.md.

## Version 1.0.17 empty-state canvas correction

Only empty.artwork now uses empty-square.webp: a1536×1536 transparent canvas centered around the unchanged full figure. Both light/dark, compact/regular retain contain fit and previous opacity/focal values. Home, launch, wallpaper, controls and composer declarations/asset bytes are unchanged.
