# Cloud Post Office — Design and review

Original anime fantasy with blue/ivory day and night palettes, dedicated phone and wide compositions, and a paper courier empty state. The default home name and logo are retained.

## Version 1.2.0 / Editorial Home

Editorial Home uses the cover header with a dedicated 2:1 transparent foreground. The sky-postwoman and cloud mailbox sit to the right, leaving the upper-left controls unobstructed and the lower edge quiet for the native work-card rail. The existing day/night wallpapers remain the background, preserving the theme's palette and setting in both modes. Toolbar backgrounds are removed so the controls sit lightly over the cover; their native hit targets and theme colors remain unchanged.

Classic Home keeps the existing square `home.hero`, while Editorial resolves only the new `home.decoration`. The foreground is intentionally nonessential, contains no text or controls, and uses the same asset at compact and regular widths because its composition already reserves responsive negative space.

## Version 1.1.0 / CLI 1.7.0

Folded-paper back arrow, origami courier send, and add-envelope attachment.

The three theme-specific generated glyphs replace the rejected generic geometric draft. Each is a 128×128 transparent PNG used in template mode. Local 17px and 34px checks cover silhouette and contrast; browser preview remains a separate gate. Palettes and home identity are unchanged.

## Gallery preview

A dedicated illustrated cover is referenced by `preview`. It represents the theme atmosphere and is separate from app wallpaper and UI screenshots. Validated using CLI 1.7.1.
