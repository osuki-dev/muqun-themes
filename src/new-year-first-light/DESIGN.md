# New Year First Light

Version 1.0.2. The mode-specific compact/regular fireworks Home covers and quiet city wallpapers are retained. Startup now has its own transparent three-bloom fireworks, riverbank and arched bridge vignette instead of displaying the rectangular Home painting. The new square cutout is also reused in empty states.

Launch uses explicit compact/regular contain declarations in both modes. The App startup resolver selects the asset URI and uses its own contain box, so the composition and alpha padding are authored in the actual image rather than relying on focalPoint to repair it. Measured 10% alpha bounds: `1032x1123+112+67` on `1254x1254`.

Home scene, gallery and palette bytes are unchanged. No ambient effect is added.

Home title/logo remain hidden; composer background and decoration resolve to null in light/dark × compact/regular. No outset is authored. UI and terminal fill opacity stay 1. Eight template icons, independent parameters shape and icon directions are unchanged.

## Review coverage

Dedicated launch images and source Home paintings were visually inspected. Small 200px light/dark launch composites and compact/regular cover crops are source-art review, not native screenshots. CLI validation, contrast and full source packaging are checked separately. No mobile-dev, native device automation or native transition/keyboard acceptance is claimed.
