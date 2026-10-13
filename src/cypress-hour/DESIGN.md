# Cypress Hour design review

Version: 1.1.3. Decision: repair.

Retain the integrated scooter terrace; replace sky-only paper with vineyards, villas, cypresses and olive edges. Complete helmet in launch portrait.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `home-environment-compact-light` / cover / 0.28 | `composer-compact` / contain / 0.72 | `{"left": 0, "right": 0, "bottom": 0}` | None |
| light | regular | `home-environment-regular-light` / cover / 0.42 | `composer-regular` / contain / 0.72 | `{"left": 0, "right": 0, "bottom": 0}` | None |
| dark | compact | `home-environment-compact-dark` / cover / 0.65 | `composer-compact` / contain / 0.82 | `{"left": 0, "right": 0, "bottom": 0}` | None |
| dark | regular | `home-environment-regular-dark` / cover / 0.65 | `composer-regular` / contain / 0.82 | `{"left": 0, "right": 0, "bottom": 0}` | None |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.
