# Art direction

A welcoming shrine attendant in ivory and vermilion watercolor, quiet garden scenery, and restrained midnight lantern bloom. Separate wordless artwork and wallpaper for both Home layouts.

## Production prompts

- Foreground: a natural, expressive adult character in finely inked editorial watercolor. Portrait 2:3, subject toward the right, whole face inside the frame, transparent alpha background and softly fading lower hem. No writing, labels, symbols, logos, interface, or baked-in title.
- Light wallpaper: warm ivory paper with restrained architectural watercolor limited to the lower and right edges; large quiet upper and left areas. No people or writing.
- Dark wallpaper: the same setting interpreted in quiet midnight colors, with tiny warm lights and restrained paper texture. No people or writing.

## Layout contract

A single shared transparent foreground occupies home.artwork. Home and shell wallpapers are separate scenery assets; empty.artwork reuses the foreground. Startup inherits Home artwork. No duplicate launch asset is needed. Compact and regular focal points preserve the face. Native layout renders the Home title and control glyphs.

## Effects

Light mode disables ambient effects. Dark mode uses bloom at intensity 0.12 and speed 0.35. Effects are nonessential; the static composition remains complete when reduced motion disables them.
