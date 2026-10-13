# Atlantic in Azulejo

Version 1.4.0 expands the coastal tram illustration into a continuous daylight
and twilight cover. The corresponding sky wallpapers contain no character;
Home draws the traveller exactly once through `home.artwork`. The existing
identity choices, launch portrait and template chrome glyphs are preserved.

The cover hint changes Editorial presentation. Classic remains the reader's
independent layout choice and consumes the same artwork and composer slots.
Compact and regular image overrides are declared explicitly in both modes.

## Composer artwork

`home.composer.background` uses a transparent azulejo and bougainvillea corner
ornament at 0.26 opacity with contain fit. The middle is transparent and the
lower control lane has no enclosing border. No outset is declared, and
`home.composer.decoration` remains unset: there is no decorative overhang.
Light and dark inherit the same shape; compact and regular explicitly resolve
the same asset and fit. The field's own fill opacity remains unchanged.

`composer.background` applies the matching ornament at 0.14 opacity to the
conversation composer's enclosing chrome. In the current App, this slot does
not supply an independent image inside the conversation text field. Home's
input artwork does not implicitly fall back to this slot.

## Verification scope

The generated daylight and twilight covers, sky-only wallpapers and transparent
composer ornament were visually inspected as assets. Source validation and
palette contrast checks passed. These checks do not prove native layout or
artwork-over-text contrast.

Native review is still required on phone and Pad, in Classic and Editorial,
light and dark, with long drafts, keyboard visible, parameters open and closed,
and voice-to-text active. The Home artwork visibility override and long custom
identity label also require native review. No native screenshots are claimed.

Exact generation prompts are in [COVER-PROMPTS.md](COVER-PROMPTS.md).
