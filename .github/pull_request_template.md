## Theme

<!-- id, name, and a sentence on the look. A screenshot or two helps. -->

## Checklist

- [ ] One theme in this PR, and only its source: `src/<id>/` (no `dist/`, no `index.json`; CI builds those)
- [ ] `bunx @osuki-dev/muqun-theme check --sources --require-preview` passes with no errors
- [ ] Placeholder artwork from `init` is replaced or deliberately kept as flat tints
- [ ] `assets/preview.png` is a real cover, 1024×640, light look on the left half and dark on the right
- [ ] `name`, `author`, `license`, `description` and `tags` are set in `theme.json`
- [ ] `version` in `theme.json` was bumped if this changes an existing theme

## Rights

- [ ] I hold the copyright to this theme, and the `license` in `theme.json` is the licence I grant
- [ ] Every image in `assets/` is my own work, **or** is listed in `src/<id>/CREDITS.md` with its creator, source URL and licence, compatible with the theme's licence
