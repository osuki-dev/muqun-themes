# Neon Window Study

Two adult roommates listen to records on floor cushions with a sleepy dog in a dreamy blue and lilac lifestyle webtoon.

## One pack, three Home layouts

The existing Home artwork slot supplies one complete transparent foreground in contain fit. Classic, Editorial and Stage choose their own geometry; the manifest adds no layout selector. The complete foreground is also used at launch. No characters occur in wallpaper.

Compact uses the existing portrait scene. Regular now uses a separately recomposed 1536×1024 landscape scene that retains the architectural vista and foreground floor together. Light and dark have independently lit environments. Full-body foreground sources remain uncropped; native fades and control overlap need device review.

## Resolved decoration mapping

| Mode | Slot | Base | Compact | Regular |
| --- | --- | --- | --- | --- |
| light | home.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | home.wallpaper | background-light / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light-regular / cover / 0.38 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | shell.wallpaper | background-light / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-light-regular / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | launch.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| light | home.composer.background | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | home.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | home.wallpaper | background-dark / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark-regular / cover / 0.5 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | shell.wallpaper | background-dark / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} | background-dark-regular / cover / 0.12 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | launch.artwork | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} | foreground / contain / 1 / focal {'x': 0.5, 'y': 0.5} / outset {} |
| dark | home.composer.background | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} | neon-composer / contain / 0.18 / focal {'x': 0.5, 'y': 0.5} / outset {} |

## Controls and evidence

Eight themed semantic icon slots are present, with template tinting and native fallback if unavailable. Settings uses a gear independently from parameter sliders; directional arrows retain their declared direction. Computer selection retains native semantics. Restored accents preserve their original bounded placement. New camera/headphone accents use 0.18 Home input opacity; no outset is added.

Source validation and contrast are separate from native acceptance. Pending per-pack acceptance: Classic/Editorial/Stage × phone/Pad × light/dark, long computer titles and drafts, keyboard, parameters, voice, user opacity and theme switching. These source notes claim no screenshots.

## Version 1.0.7 compact framing correction

Home compact in both modes uses foreground-compact.webp: original1536×1024 drawing centered on2048×1024 transparent canvas with256px side margins. Fit contain, opacity and focal point unchanged. This compensates for native Stage overscan that clipped the seated silhouettes. Regular/Pad and launch art, wallpaper, controls and composer unchanged. Phone Editorial/Stage retest required.
