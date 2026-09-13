# Working in muqun-themes

This repository holds Muqun theme sources under `src/<id>/`. The packed
`.muqun-theme` files and the `index.json` catalogue are built by CI after a
merge and published to the `release` branch; nobody commits them.

## Before creating or editing a theme

Read the `muqun-theme` skill in full, first. It is the authoring contract from
the Muqun app: the workflow, the resource and surface rules, the boundaries,
the complete JSON Schema, a complete starter manifest, and how to check the
result. If it is not installed in this checkout (`.agents/skills/muqun-theme/`
or `.claude/skills/muqun-theme/`), install it:

```sh
bunx skills add osuki-dev/muqun-theme-cli -y
```

Follow it as written. A theme that ignores it may look right and still be
refused by the app.

## Making a theme

The CLI needs Bun 1.4 or newer and nothing installed; run it from the
repository root and it knows the layout, so a bare id is enough:

```sh
bunx @osuki-dev/muqun-theme init <id>          # writes src/<id>/, a complete scaffold with placeholder art
bunx @osuki-dev/muqun-theme contrast <id>      # opacity floor and the pairs that set it
bunx @osuki-dev/muqun-theme validate <id>      # what the app checks on import
bunx @osuki-dev/muqun-theme check --sources    # what CI runs on the PR; must pass before you finish
```

- `<id>` is lowercase letters, digits and dashes, starting with a letter. It is
  the directory name and the theme's `id`; they must agree.
- Your deliverable is `src/<id>/` only. Do not commit anything under `dist/`
  or an `index.json`; both are gitignored here and built by CI.
  `bunx @osuki-dev/muqun-theme pack <id>` is fine for a local look at the
  package.
- Replace every placeholder image from `init` with real artwork, or delete the
  slot. `validate` names the placeholders still in place.
- Set `name`, `author`, `license`, `description` and `tags`. Bump `version`
  when changing an existing theme.
- Only use artwork the submitter holds the rights to. For any image that is not
  the submitter's own work, write `src/<id>/CREDITS.md` with the file, the
  creator, the source URL and the licence. If you cannot state where an image
  came from, do not use it.

## Before finishing

`bunx @osuki-dev/muqun-theme check --sources` must pass. Submit one theme per
pull request.
