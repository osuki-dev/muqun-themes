# Theme continuity review — cohort 0

All19 sources reviewed against published main `98ebc1e7a054d26c0dff9f3fa5857d61b32f56a9`. Existing current icons and composer fixes were synchronized before additional art changes. Source work remains a local candidate.

## Design and preservation

Distinct backgrounds were chosen for each theme. Good complete scene artwork is retained. Card surfaces preserve each theme's existing palette/material design; this change does not impose universal borders or opacity. Key startup props were examined visually, not merely checked for asset presence.

| Theme | Home scene and whole-page background | Composer | Startup |
| --- | --- | --- | --- |
| atlantic-in-azulejo | Integrated Lisbon scene extends to top; quiet sky; original traveller/tram retained. New Phone/Pad day/night coastal architecture, sea, azulejo and bougainvillea folio. | New quiet azulejo floral corners in Home/dock. | Reasonable traveller portrait and tram shoulder motif retained. |
| aegean-paperlight | Integrated Aegean scene extends to top; corrected complete bicycle/shoes; contain protects action props. New Phone/Pad day/night Greek architecture, coast, windmill and olive folio. | New far-left sea/olive and far-right shell accents in Home/dock. | Rebuilt startup rider with complete bicycle wheels/frame/pedals and shoes. |
| aperture-afterhours | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Complete robot pair/pedestal retained. |
| briar-oath | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Full knight, shield, sword and boots retained in both modes. |
| cover-courier | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Reasonable courier portrait/shoulder bag retained in both modes. |
| eclipse-archivist | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Complete wings, armillary object and boots retained. |
| glasshouse-prowler | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Complete kitten, watering can, fern and tail retained in both modes. |
| ink-over-jiangnan | Existing good subject/scene retained; cover hint respected. New transparent misty canal/bridge/willow environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole traveller, red umbrella and boots retained. |
| last-inning | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Full pitching pose, ball, glove and cleats retained in both modes. |
| midnight-operator | Existing good subject/scene retained; cover hint respected. New transparent rooftop antennas and urban navigation environment. | Latest published Home/dock accents preserved. | Complete independent radio icon retained. |
| mushroom-daybreak | Existing good subject/scene retained; cover hint respected. New transparent golden forest/mushroom/path environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole seated ranger, mushroom, staff and boots retained. |
| one-piece-grand-voyage | Existing good subject/scene retained; cover hint respected. Day/night ocean ship backgrounds edited to remove duplicate Luffy; both widths corrected. | Existing nautical map panel also mapped to Home. | Whole Luffy, sail, boat and waves retained. |
| pomegranate-court | Existing good subject/scene retained; cover hint respected. New transparent courtyard/fruit/fountain environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole seated guitarist, guitar neck/body and feet retained. |
| reef-reverie | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Whole swimming diver/fins and manta wings/tail retained in both modes. |
| saffron-under-the-atlas | Existing good subject/scene retained; cover hint respected. New transparent Atlas/kasbah/zellij environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole architectural blue door/stair cutout retained. |
| soft-machines | Existing good subject/scene retained; cover hint respected. New transparent pearl paper/material studio environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole kinetic sculpture and base retained. |
| terraces-of-the-sun | Existing good subject/scene retained; cover hint respected. New transparent Andean terraces/textile/native grass environment. | New sparse transparent environmental motif in Home and conversation dock. | Whole seated hiker and llama retained. |
| tiny-workshop | Existing good subject/scene retained; cover hint respected. New transparent skylight/plants/tool-shelf workshop environment. | Latest published Home/dock accents preserved. | Reasonable workshop portrait holds whole helmet; full Home bicycle scene retained. |
| velvet-signal | Existing good subject/scene retained; cover hint respected. Existing complete full-page scene/paper retained. | New sparse transparent environmental motif in Home and conversation dock. | Whole standing investigator, torch, notebook and boots retained in both modes. |

## Verification and limits

19 schema/image/reference validations and19 contrast checks passed.152 existing icon images are byte-identical to the published baseline. Every additional output was visually inspected; all14 new composer accent centers sampled have alpha0. Native imagegen dimensions remain intact and may exceed recommended1024px export sizes.

Both width classes and color modes resolve explicit supported artwork slots. Environmental details remain quiet at reading centers. Full-prop startup illustrations use contain. Phone/Pad and Classic/Editorial runtime QA remains pending because device automation is paused. Source checks cannot establish toolbar contrast or crop appearance on actual devices.

Conversation `composer.background` is consumed by the enclosing dock. The inner text field has no independent image slot in the inspected App contract. Home `home.composer.background` is separate; no palette transparency workaround was used.

## Published-background diagnosis

The actual Atlantic1.3.2 and Aegean1.2.3 packages matched catalogue SHA256. Their wallpaper art was nearly solid paper with only two faint lower lines, authored at Home opacity0.8. The App image layer preserves that opacity and renders above the base page color. These two examples support an authoring deficiency, not a proven missing-image or opacity-clamp renderer regression. Of94 published manifests,18 have no Home/Shell wallpaper, zero declare wallpaper opacity0, and zero referenced source files are missing in the pinned tree.

## Prompt provenance

Exact full-page/prop/composer generation prompts are recorded in each changed theme's `ENVIRONMENT-PROMPTS.md`. Original first-pass top-scene prompts remain in `COVER-PROMPTS.md` for Atlantic/Aegean. No other cohort artwork was reused.
