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

## Pad grounding correction 1.0.7

Actual iPad Editorial light/dark screenshots of 1.0.6 showed the isolated foreground floating above unrelated environment geometry. The regular Home wallpaper now uses a purpose-composed full scene with visible ground contact; regular Home artwork is null to prevent duplicate subjects. The compact foreground and wallpaper, shell wallpaper, launch, empty state, composer and icons remain byte-for-byte/configuration unchanged. New light/dark scenes preserve original subjects and place faces in the left content area. Gallery preview still represents the unchanged compact artwork. Source visual inspection and CLI checks are not native acceptance: this new regular composition requires iPad retest, including additional layouts/orientations not represented in the initial Editorial portrait captures.

The 1.0.7 pilot uses one original day scene for both modes, with regular wallpaper contain fit and left-center focal point (0, 0.5). Landscape keeps the scene in the left artwork region while the native theme base color fills the work column; portrait has only narrow side slack. This is a wallpaper, never an opaque foreground. Actual two-orientation review must assess whether the remaining base-color area feels intentional; no acceptance is inferred from contain geometry.

## Rejected pilot and restoration 1.0.8

Actual 1.0.7 iPad portrait/landscape light/dark captures showed proper grounding, but the landscape New terminal row overlapped the riders’ foreheads and part of the left upper face. This tradeoff is rejected. Version 1.0.8 restores the complete 1.0.6 rendering configuration and assets, changing only version; the original illustrated foreground reserves readable face space. The 1.0.7 artifact is preserved for audit but is not the final candidate. No four-pose pass is claimed for 1.0.7.
