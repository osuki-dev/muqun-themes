# Halloween Lantern Walk

Version 1.0.2. The Home broom-riding witch and autumn wallpapers are retained. A separate compact, foreshortened broom pose now serves launch/empty. Its nearly square silhouette uses the startup box more effectively than the previous horizontal Home-style illustration; the complete hat, lantern, cat and boots remain inside the transparent canvas.

Launch uses explicit compact/regular contain declarations in both modes. The App startup resolver selects the asset URI and uses its own contain box, so the composition and alpha padding are authored in the actual image rather than relying on focalPoint to repair it. Measured 10% alpha bounds: `1164x1149+60+54` on `1254x1254`.

Home remains the existing safe-margin square contain image in both widths and modes; its bytes are unchanged. No ambient effect is added.

Home title/logo remain hidden; composer background and decoration resolve to null in light/dark × compact/regular. No outset is authored. UI and terminal fill opacity stay 1. Eight template icons, independent parameters shape and icon directions are unchanged.

## Review coverage

Dedicated launch images and source Home paintings were visually inspected. Small 200px light/dark launch composites and compact/regular cover crops are source-art review, not native screenshots. CLI validation, contrast and full source packaging are checked separately. No mobile-dev, native device automation or native transition/keyboard acceptance is claimed.
