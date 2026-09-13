# muqun-themes

Themes for [Muqun](https://github.com/osuki-dev/muqun-app). Sources are
reviewed here; packages are built here.

```
main                        what people write and review
  src/<id>/theme.json         a theme as it is authored, beside its assets/

release                     what CI builds from main after every merge
  dist/<id>.muqun-theme       each theme, packed and ready to install
  index.json                  the catalogue of everything in dist/ -- what `list` and the gallery read
```

A pull request carries one thing: `src/<id>/`. CI checks that it validates and
packs. After the merge, CI packs every source, regenerates the catalogue, and
publishes both to the `release` branch, rebuilt whole every time. Nobody
commits a package or an index by hand.

## Making a theme with an agent

Most themes here will be made by an agent, and one thing decides whether it
produces an installable theme or a plausible-looking mockup: **whether it read
the skill first.**

The skill is the authoring contract from the Muqun app: the workflow, the
resource and surface rules, the boundaries, the full JSON Schema, a complete
starter manifest, and how to check the result. It lives in the CLI repository
and ships with every CLI version. Install it into this checkout once:

```sh
bunx skills add osuki-dev/muqun-theme-cli
```

That puts it where Codex, Claude Code, Cursor and the rest look. `AGENTS.md`
tells an agent to read it before touching a theme. Run the same command again
to pick up a newer version.

Then ask for the theme. Attach reference images if you have them, name the id,
and say where the result goes:

> Create a Muqun theme with id `grand-voyage` from the attached references.
> Author it in `src/grand-voyage`, including the 1024×640 preview cover, and
> make `bunx @osuki-dev/muqun-theme check --sources --require-preview` pass.

Review what comes back the same way you would a human's: run the check, look at
the artwork, read the PR. The skill makes an agent produce a valid theme; it
does not make it produce a good one.

## Requirements

**Bun 1.4 or newer.** The toolchain is
[`@osuki-dev/muqun-theme`](https://www.npmjs.com/package/@osuki-dev/muqun-theme).
Nothing to install; `bunx` fetches it, and it knows this repository's layout:
run from the repository root, a bare id is enough.

```sh
bunx @osuki-dev/muqun-theme --help
```

## Making a theme by hand

Pick an id: lowercase letters, digits and dashes, starting with a letter. It
names the directory, the package and the theme inside the app, so choose it
once. Read the skill too; it is written for an agent, but it is the same
contract you are working to.

**1. Scaffold.** A complete, installable theme with placeholder artwork, so you
discover the format by editing and deleting rather than by reading the schema.

```sh
bunx @osuki-dev/muqun-theme init grand-voyage      # writes src/grand-voyage/
```

**2. Edit.** Open `src/grand-voyage/theme.json`. Set `name`, `author` and
`license`, and a `description` and `tags` for the gallery. Work through both
`variants` (light and dark are separate, with no inheritance). Replace the flat
tints in `assets/` with real artwork, or delete the slots you do not want.
Every placeholder carries a marker, and the tools tell you which ones are still
in place.

**3. Check as you go.** Neither command needs a packed file.

```sh
bunx @osuki-dev/muqun-theme contrast grand-voyage  # what the palette costs in translucency
bunx @osuki-dev/muqun-theme validate grand-voyage  # everything the app checks on import
```

`validate` exits `0` when the theme is usable. Warnings are advice; errors mean
the app would refuse it.

**4. Make the cover.** `assets/preview.png` is what the website and the app
show before anyone downloads the pack, so it is required: 1024×640, the light
look on the left half and the dark look on the right, made from the theme's
own artwork or its surfaces and palette. `init` leaves a flat placeholder
there; replace it and keep it named in the manifest's `preview` field.

**5. Run what CI runs.**

```sh
bunx @osuki-dev/muqun-theme check --sources --require-preview
```

That validates every source, packs it in memory to prove it can be, and
refuses a theme without a cover. If you
want to see the package itself, `bunx @osuki-dev/muqun-theme pack grand-voyage`
writes `dist/grand-voyage.muqun-theme`; it is gitignored, so pack as much as
you like.

To edit an existing theme, work in its `src/` directory and bump `version` in
`theme.json`. The next build repacks it.

## Submitting a theme

Themes arrive as pull requests, one theme per PR.

1. Branch from `main`: `git switch -c theme/grand-voyage`.
2. Add `src/grand-voyage/`. Nothing else: `dist/` and `index.json` are built
   by CI and are ignored by git on `main`.
3. Run `bunx @osuki-dev/muqun-theme check --sources --require-preview` from
   the repository root. It is exactly what CI runs on the PR.
4. Open the pull request. The template lists what a reviewer looks for.

What gets a theme merged:

- The check passes with **no errors**. Warnings are discussed in the PR, not
  blocked on.
- No placeholder artwork left from `init`, unless a slot is deliberately a flat
  tint. The preview cover is never a placeholder.
- The `id` is not already taken by another theme in `src/`.
- `name`, `author` and `license` are set, and the rights below are in order.

Once merged, the build workflow packs it and publishes it to `release` within
a minute or two; it then appears in `list` and on the website.

## Copyright and third-party artwork

**A theme belongs to the person who submits it.** Merging it here transfers
nothing: you keep the copyright, and the `license` field in `theme.json` is the
licence you grant readers who install it. Choose one you mean.

The repository itself, meaning everything that is not a theme (the workflows,
the documentation, the templates), is under the Apache License 2.0 in
`LICENSE`. That licence does not apply to anything under `src/<id>/`; each
theme carries its own.

**You must hold the rights to everything in `assets/`**, either because you
made it or because its licence lets you redistribute it under yours. If any
image is not your own work, it has to be marked:

- Add `src/<id>/CREDITS.md` listing, for each third-party image: the file, the
  creator, where it came from (a URL), and its licence. That file stays in the
  source and is never packed, so it costs the theme nothing.
- Make sure the theme's `license` is compatible with every licence you list.
  A CC BY image inside an all-rights-reserved theme is not.
- Artwork you are not allowed to redistribute, or whose origin you cannot
  state, does not go in. That includes screenshots of other people's work and
  images generated from a prompt naming a living artist's style.

A pull request that cannot answer "where did this image come from" is not
merged, however good the theme looks.

## Installing a theme

Browse the themes on the website, or list them from a terminal:

```sh
bunx @osuki-dev/muqun-theme list
bunx @osuki-dev/muqun-theme list --search sea
```

Download the `.muqun-theme` file from the
[`release` branch](https://github.com/osuki-dev/muqun-themes/tree/release/dist)
and import it in the Muqun app. The app performs the same checks `validate`
does, so a package that passed here installs there.

## Format reference

The format itself, every field and every limit, is documented in the toolchain's
[README](https://github.com/osuki-dev/muqun-theme-cli#the-muqun-theme-format).
Where the two disagree, the app is right and the tool has drifted; please open
an issue there.
