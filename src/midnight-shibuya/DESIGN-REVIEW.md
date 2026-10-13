# 渋谷、午前零時 design review

Version: 1.1.6. Decision: retain.

Retain continuous rainy city environment and two complete umbrellas, including canopy, stem and curved handle.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `background-light` / cover / 0.62 | None | `{}` | None |
| light | regular | `background-light` / cover / 0.62 | None | `{}` | None |
| dark | compact | `background-dark` / cover / 0.68 | None | `{}` | None |
| dark | regular | `background-dark` / cover / 0.68 | None | `{}` | None |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.
