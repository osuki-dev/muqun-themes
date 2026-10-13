# Sakura, in Passing design review

Version: 1.2.3. Decision: repair.

Retain the integrated bicycle riverbank cover; add cherry banks, bridge and river town. Rebuild launch with both full bicycle wheels, frame, saddle, basket and handlebar.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `home-environment-compact-light` / cover / 0.42 | `composer-compact` / contain / 0.34 | `{"left": 0, "right": 0, "bottom": 0}` | `composer-overhang` / contain / 0.85 |
| light | regular | `home-environment-regular-light` / cover / 0.52 | `composer-regular` / contain / 0.34 | `{"left": 0, "right": 0, "bottom": 0}` | `composer-overhang` / contain / 0.85 |
| dark | compact | `home-environment-compact-dark` / cover / 0.68 | `composer-compact` / contain / 0.42 | `{"left": 0, "right": 0, "bottom": 0}` | `composer-overhang` / contain / 0.85 |
| dark | regular | `home-environment-regular-dark` / cover / 0.68 | `composer-regular` / contain / 0.42 | `{"left": 0, "right": 0, "bottom": 0}` | `composer-overhang` / contain / 0.85 |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.
