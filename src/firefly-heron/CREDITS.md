# Firefly Heron artwork

All artwork was created for Muqun with OpenAI's built-in image generation tool on 2026-09-26. No third-party characters, photographs, logos, or stock illustrations were used. The original generated artwork and original icon designs are distributed with this theme under CC0-1.0.

| Files | Creator / source | License |
| --- | --- | --- |
| `assets/home.webp` | Muqun, original OpenAI image generation and transparency/framing edits, https://openai.com/index/image-generation/ | CC0-1.0 |
| `assets/launch.webp` | Muqun, independently generated OpenAI illustration with transparency extraction, https://openai.com/index/image-generation/ | CC0-1.0 |
| `assets/wallpaper-light.webp`, `assets/wallpaper-dark.webp` | Muqun, two independent original OpenAI background paintings, https://openai.com/index/image-generation/ | CC0-1.0 |
| `assets/icon-*.png` | Muqun, original hand-authored vector geometry rasterized to PNG | CC0-1.0 |
| `assets/preview.png` | Muqun, composition of this theme's own artwork | CC0-1.0 |

## Art direction and prompts

- Home: original Japanese anime film wildlife illustration of a silver heron, S-curved neck, lifted wings, individual feather detail, jade shadows, warm golden rim lighting, tiny fireflies, isolated on transparent alpha. A targeted extraction removed diffuse background glow; a framing correction preserved the entire left wing and both feet.
- Launch: independently composed full flying heron, wings in an upward V, trailing complete legs and toes, five fireflies, transparent alpha. A targeted extraction removed the original opaque background and its broad glow. This is not a crop of Home.
- Light wallpaper: cinematic Japanese wetland at golden dawn, reflective river, emerald reeds, ancient willow trees, atmospheric distant mountains and peach sunlight, full-bleed gouache detail. No people, birds, lettering or logos.
- Dark wallpaper: cinematic midnight wetland, charcoal forest and bronze-olive reeds, warm ivory moon, amber fireflies and reflected moonlight. No dominant blue, no birds, people, lettering or logos.

## Coverage and verification

The complete current replaceable icon set is included: `chrome.back`, `chrome.send`, `chrome.attach`, `chrome.create`, `chrome.scan`, `chrome.settings`, and `home.arrow`. The Home arrow's authored direction is `up-right`. Assets use template rendering so their color follows the selected theme and state. Other App glyphs are outside the current theme icon contract.

Home and launch use the same neutral silver rendering in light and dark modes; wallpaper and UI palettes are mode-specific. Static artworks have a maximum edge of 1024 pixels. The source preview is 1024 by 640. Transparent Home and launch were inspected over white and dark backgrounds; no rectangular background is retained. CLI 2.3.1 validation, contrast and package round-trip passed. Native App installation is not claimed here.
