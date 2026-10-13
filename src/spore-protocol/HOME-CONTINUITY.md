# Spore Protocol — Home continuity 1.2.3

quiet lush fern forest trail under connected canopy and soft misty light, small mushroom edges and pale dawn gaps; preserve adult short blue-haired hiker, green jacket and backpack

The Home cover is a new complete opaque scene with connected upper sky, architecture or canopy. It preserves this theme's central identity and art style. It uses the same home.artwork asset for Classic and Editorial, with explicit light/dark and compact/regular cover fit and top focal points. Native layout and bottom feathering own its placement. The main subject is not copied into page wallpaper. Existing palette, card fills/borders/material choices and clear utility backgrounds are preserved; no shared card template was imposed.

Home wallpaper is separately generated for light and dark, with real low-contrast environment shapes and paper fibers. The center and lower reading region remain quiet. It resolves explicit compact/regular cover-fit objects at opacity 0.42 light / 0.35 dark. Both width classes intentionally share the 1024×1536 mode source with complete responsive image objects and top-center position; native landscape Pad clipping has not been inspected.

## Startup and input review

Startup is preserved as its existing transparent source and contain-fit override. Full hiker, book and backpack are present. Both action completeness and the source canvas were reviewed, not merely file existence/alpha. The App launch resolver uses the explicit launch artwork before Home artwork, and the opening drawing uses containedImageRect. No opaque Home rectangle was substituted for these startup cutouts. Native animation and landing crop remain unverified.

Home composer background/overhang settings were preserved from the published baseline (or the existing original three-theme candidate). The mode/width records below include each image's own fit, opacity, focal point and outset; null means no drawing. Declared transparent composer sources for the four published composer themes were visually inspected, with center/control clearance retained. Source inspection does not prove native long-draft readability.

```json
{
  "light": {
    "home.composer.background": {
      "asset": "home-composer-compact",
      "fit": "contain",
      "opacity": 0.38,
      "focalPoint": {
        "x": 0,
        "y": 0
      },
      "outset": {
        "left": 6,
        "right": 0,
        "bottom": 0
      },
      "compact": {
        "asset": "home-composer-compact",
        "fit": "contain",
        "opacity": 0.38,
        "focalPoint": {
          "x": 0,
          "y": 0
        },
        "outset": {
          "left": 6,
          "right": 0,
          "bottom": 0
        }
      },
      "regular": {
        "asset": "home-composer-regular",
        "fit": "contain",
        "opacity": 0.38,
        "focalPoint": {
          "x": 0,
          "y": 0
        },
        "outset": {
          "left": 6,
          "right": 0,
          "bottom": 0
        }
      }
    },
    "home.composer.decoration": null
  },
  "dark": {
    "home.composer.background": {
      "asset": "home-composer-compact",
      "fit": "contain",
      "opacity": 0.5,
      "focalPoint": {
        "x": 0,
        "y": 0
      },
      "outset": {
        "left": 6,
        "right": 0,
        "bottom": 0
      },
      "compact": {
        "asset": "home-composer-compact",
        "fit": "contain",
        "opacity": 0.5,
        "focalPoint": {
          "x": 0,
          "y": 0
        },
        "outset": {
          "left": 6,
          "right": 0,
          "bottom": 0
        }
      },
      "regular": {
        "asset": "home-composer-regular",
        "fit": "contain",
        "opacity": 0.5,
        "focalPoint": {
          "x": 0,
          "y": 0
        },
        "outset": {
          "left": 6,
          "right": 0,
          "bottom": 0
        }
      }
    },
    "home.composer.decoration": null
  }
}
```

## Provenance and validation

The new cover and paper wallpaper are original fictional artwork generated/edited with the built-in OpenAI image generation tool for Muqun Theme Collection on 2026-10-13, under this theme's existing license. Cover edits used only this theme's existing illustration. Paper scenes were independently generated; no other theme/group's character or scene was reused. Final output bytes were copied directly; no script image edits, resizes or alpha changes. Deployment Atlas's first two paper candidates were rejected because their historical villages did not match the abstract infrastructure world, then regenerated in dimensional cut paper.

Published parameters glyphs and composer patches were preserved from pinned collection main 98ebc1e7a054d26c0dff9f3fa5857d61b32f56a9. Candidate 1.2.3 exceeds published 1.2.2. CLI source validation/contrast/pack checks are reported by the final review matrix. Remaining gaps: native phone and Pad in both layouts/modes, launch, long multiline text, keyboard, parameters open/closed and voice-to-text. Existing gallery remains separate visual artwork; no interface was baked into new assets. No commit or publication was performed.
