# Poolside Prism design review

Version: 1.0.4. Decision: repair.

Replace ripple-only paper with pool tiles, garden, pergola and caustics. Retain researcher reading action with complete notebook and life buoy.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `home-environment-light` / cover / 0.34 | `home-composer-accent` / contain / 0.58 | `{"left": 0, "right": 0, "bottom": 0}` | `empty-buoy` / contain / 0.85 |
| light | regular | `home-environment-light` / cover / 0.34 | `home-composer-accent` / contain / 0.58 | `{"left": 0, "right": 0, "bottom": 0}` | `empty-buoy` / contain / 0.85 |
| dark | compact | `home-environment-dark` / cover / 0.65 | `home-composer-accent` / contain / 0.48 | `{"left": 0, "right": 0, "bottom": 0}` | `empty-buoy` / contain / 0.85 |
| dark | regular | `home-environment-dark` / cover / 0.65 | `home-composer-accent` / contain / 0.48 | `{"left": 0, "right": 0, "bottom": 0}` | `empty-buoy` / contain / 0.85 |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.
