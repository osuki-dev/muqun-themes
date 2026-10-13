# Rhythm of Dessau design review

Version: 1.0.10. Decision: retain.

Retain Bauhaus architectural paper and primary geometric print. Complete architectural sculpture is launch fallback, preserving its non-character identity.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `portrait-light` / cover / 1 | None | `{}` | None |
| light | regular | `wide-light` / cover / 1 | None | `{}` | None |
| dark | compact | `portrait-dark` / cover / 1 | None | `{}` | None |
| dark | regular | `wide-dark` / cover / 1 | None | `{}` | None |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.
