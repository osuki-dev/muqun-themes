# Cinder Canyon design review

Version: 1.0.3. Decision: retain.

Retain continuous canyon, road and cactus environment; preserve comic cowboy and walking launch with complete coiled rope.

Home uses `cover` with `toolbarBackground: false`, so native icons sit over the environment. Classic and Editorial consume the same theme slots. Original palette, material and card/border choices are preserved; the review does not impose filled or outlined cards. Latest published template `chrome.parameters` and composer overrides are retained. Wallpaper opacity softens scenery independently of the unchanged input fill.

| Mode | Width | Wallpaper | Composer background | Outset | Composer overhang |
| --- | --- | --- | --- | --- | --- |
| light | compact | `wallpaper-light` / cover / 1 | None | `{}` | None |
| light | regular | `wallpaper-light` / cover / 1 | None | `{}` | None |
| dark | compact | `wallpaper-dark` / cover / 1 | None | `{}` | None |
| dark | regular | `wallpaper-dark` / cover / 1 | None | `{}` | None |

Original Home, startup/fallback and light/dark environment artwork was visually inspected. Startup action props were checked. App code resolves launch per mode/width and contains the image (`containedImageRect`, `fit="contain"`); this is code inspection, not a startup screenshot.

CLI validation, contrast and isolated 19-theme source/pack check passed (`check ok 19 theme(s)`). Image-size and unused-asset warnings remain authoring notices.

Native QA remains: phone/Pad, Classic/Editorial, both modes, long multiline drafts, keyboard, parameters open/closed and voice-to-text; inspect icon legibility, header seam, startup reveal and controls. No device import, apply, commit or publication is claimed.

## Revised layered candidate 1.0.5

The prior hidden `home.artwork` selected the actual app's Stage `world` role, putting the riders behind native HUD/cards. This candidate declares visible opaque cover artwork, selecting the app's `sky` band (`home-stage-layers.ts`), and uses contain fitting in Classic/Editorial. This is an intentional adaptation of the full-scene guidance to the actual supported opaque cover-art path. It preserves that guidance's essential invariant: no duplicated subject. Home and shell wallpapers are the inspected subject-free canyon scenery, subdued to 0.28 opacity. New 1536x1024 regular artwork is a true horizontal recomposition with complete riders and bikes; compact retains the complete 1024x1536 source. Launch uses the same responsive art with contain fit. The eight original semantic glyphs were visually inspected and restored, with native computer control/failure fallback and up-right arrow metadata. Old cowboy foreground/launch remain removed because they conflict with the new adult motocross duo. No Home composer or empty artwork existed in this pack; they remain absent rather than fabricated.

CLI 2.4.1 validate, contrast and pack round-trip pass. Four longest-edge size warnings are advisory; each scene is 1.57 MP. Native Classic/Editorial/Stage phone/Pad light/dark acceptance is pending; contain and band selection alone do not establish freedom from native overlays or feathering.

## Native feedback and revised candidate 1.0.6

Android Stage light on 1.0.5 placed the faces behind the computer header. The opaque band candidate therefore failed and was not propagated to the other packs. Phone Editorial showed clear faces but cover cards overlapped lower legs; the Pad state showed complete figures but a warning covered part of the composer. These are limited observations, not acceptance.

Version 1.0.6 replaces Home's opaque scene with genuine generated transparent full-body figures, approximately 50% clear pixels at alpha <= 5%. This selects the actual Stage `figure` role and uses the app's contain behavior for cutouts in Classic and Editorial. Complete boots, hands and faces were inspected on a neutral background. The subject-free canyon remains behind them, avoiding duplicate people. Compact and regular launch keep the full source scenes with their corresponding aspect. Native 1.0.6 acceptance remains pending.

## Current composition 1.0.8

The theme retains the complete illustrated foreground and subject-free canyon used in 1.0.6. Version 1.0.8 preserves those rendering settings and artwork bytes. The foreground presentation reserves space for faces above the action controls.
