# Native adaptation notes

Standard Editorial header keeps the title outside foreground overlap. Classic always contains Home art inside its 180pt compact / 132pt regular band; both assets are intentionally landscape. Home assets are trimmed to their complete alpha bounds plus24px transparent margins; compact and regular share the complete composition at up to1024px width, avoiding the formerly oversized regular canvas. Editorial standard also contains art in min(280,width/2). Alpha silhouettes are nonessential; disabling art removes the band. Long identity names and large text remain native App responsibilities.

Launch is an independent 1024-square centered alpha illustration. No launch fit or opacity assumption is made because native launch consumes asset URI only.

Wallpapers contain only a sparse bottom/right contour or coastal glaze accent; no baked title, repeated foreground or software-logo cards. The 6 chrome/control slots use quiet transparent edge/rail motifs with empty label centers and authored opacity0.08–0.14. Native attenuation may reduce them further. Seven transparent template glyphs use consistent7px strokes; arrows visually inspected: back left, send up, Home arrow up-right.

Gallery preview uses final source art and palette; it is a deterministic UI composition, not a native screenshot. CLI validate/contrast/pack were run; actual device import, launch handoff and interactions were not tested in this task.

Editorial scale refinement: previous extra canvas reduced Alpha occupancy to about69%/46% (Atlas compact/regular) and80%/53% (Atlantic). Trim-plus24pxmargin preserves complete silhouettes and raises artwork scale within actual measured Editorial geometry. Standard header remains intentional: title stays outside art; Classic bottom-third overlap is accepted App behavior, not reason to shrink foreground. Independent launch unchanged.
