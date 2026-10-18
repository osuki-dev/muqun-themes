# Christmas Snow Post

Version 1.0.2. A grand alpine Christmas snow village replaces the sleigh foreground. Compact square and regular landscape cover paintings in each mode keep the illuminated tree central, with quiet sky above and snowy path below. Dedicated transparent launch/empty artwork depicts a snow-laden illuminated evergreen and three connected chalets.

Launch uses explicit compact/regular contain declarations in both modes. The App startup resolver selects the asset URI and uses its own contain box, so the composition and alpha padding are authored in the actual image rather than relying on focalPoint to repair it. Measured 10% alpha bounds: `1070x1126+100+52` on `1254x1254`.

Native snow is enabled, with intensity 0.4 light / 0.5 dark, speed 0.75, density 0.85, size 1.2 and downward travel. Light uses the cool info role and dark uses the pale text role. No falling snow is baked into the paintings. The App owns pause, reduced-motion and post-launch visibility. minAppVersion 3.0.0 follows the released 3.0 schema with snow controls (App commit 64092cd4, 2026-09-25; App Store release 2026-09-25).

Home title/logo remain hidden; composer background and decoration resolve to null in light/dark × compact/regular. No outset is authored. UI and terminal fill opacity stay 1. Eight template icons, independent parameters shape and icon directions are unchanged.

## Review coverage

Dedicated launch images and source Home paintings were visually inspected. Small 200px light/dark launch composites and compact/regular cover crops are source-art review, not native screenshots. CLI validation, contrast and full source packaging are checked separately. No mobile-dev, native device automation or native transition/keyboard acceptance is claimed.
