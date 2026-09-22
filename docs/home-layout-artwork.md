# Home layout artwork

Classic and Editorial are app layout preferences. A theme supplies shared artwork,
identity and colors; it does not select the user's layout. Browser preview parameters
`layout=classic|editorial`, `device=phone|tablet`, and `mode=light|dark` only select
preview compositions.

## One foreground, one background

| Manifest path | Role |
| --- | --- |
| `decoration["home.artwork"]` | The single Home foreground in either layout. |
| `decoration["home.wallpaper"]` | Wallpaper behind Home content. |
| `decoration["launch.artwork"]` | Optional distinct startup composition; otherwise startup reuses Home artwork. |
| `homeIdentity.artwork` | `default` or `hidden` author preference for Home artwork visibility. |
| `homeIdentity.name` | Custom, default, or hidden Home title. |
| `homeIdentity.logo` | Custom, default, or hidden Home mark. |

Never duplicate a foreground to obtain layering. Cover's character overlaps its
native title through layout ordering, while wallpaper remains behind both. The
foreground must not contain functional controls or essential text. Prefer transparent,
wordless illustrations with a quiet area around the title and utility controls.

`homePresentation.header` selects `standard` or `cover` within Editorial.
`homePresentation.toolbarBackground` defaults to enabled; explicit `false` removes
utility button surfaces. Custom names are independent of the package name. Cover
measures the title's rendered width and reduces its font size to fit its column.

## Responsive composition

Use explicit light/dark entries under `variantDecorations`, with `compact` and
`regular` overrides when phone and Pad need different crops. An omitted override
inherits; an object replaces the resolved image; `null` deliberately disables it.
Preserve the subject's face and silhouette using `fit` and `focalPoint`. Use `contain`
when the complete illustration matters. A missing or undecodable image must leave
no empty artwork frame.

The app determines foreground geometry from its layout and available content width.
Do not bake device frames, navigation, cards, titles or fixed pixel positioning into
artwork. Cover places the horizontal action rail at the lower foreground edge on
phones; wider content uses a cover column beside recent sessions and connections.
The rail's theme-tinted edge fades indicate remaining horizontally scrollable cards.

Startup normally reuses the resolved Home foreground. Declare `launch.artwork` only
when a separate startup image genuinely improves the composition, rather than copying
the same asset into another slot. Startup art and Home art are never rendered as two
foregrounds on Home.

## Package and review requirements

Keep manifests within 256 KiB, at most 32 assets, at most 8 MiB and 16 megapixels per
asset, and 25 MiB compressed / 50 MiB expanded per package. Gallery previews are
1024×640 images with light and dark treatments.

Review both layouts, phone and Pad, light and dark, long titles, absent artwork and
explicit null overrides. Foregrounds must not cover action labels or session content.
Check readable contrast over wallpapers and native surfaces. Preserve original image
provenance and filenames even when their authoring role changes.

This unified artwork contract requires CLI 2.x. CI and published authoring commands
use `@osuki-dev/muqun-theme@2`. During coordinated local development use the updated
local CLI:

```sh
bun ../cli/lib/cli.js check --sources --require-preview
bun ../cli/lib/cli.js build
```

Build output and `index.json` are generated artifacts; do not commit them.
