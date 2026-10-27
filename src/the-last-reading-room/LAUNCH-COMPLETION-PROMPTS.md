> Historical design record retained for provenance. See [REVISION.md](REVISION.md) for the current artwork and validation status.

# Startup character completion

Built-in OpenAI imagegen edit, 2026-10-15. The existing character image is the edit target; complete only its missing lower body while preserving the upper character, pose, clothing and props. Transparent output; no layout or App code changes.

## launch.png

Input: `assets/launch.png` at the previous theme version.

Use-case: identity-preserve. Perform local completion/outpainting of this supplied existing Muqun startup character. Preserve the existing upper-body character illustration: same exact identity, face, hair, pose, colors, clothing, linework, props and accessories as closely as possible. Keep exact brown bun, looking-up female face, sage headphones around neck, navy sweater, open cream book and both hands holding it. Continue sweater hem into relaxed charcoal trousers, full legs and soft casual loafers. Only complete missing lower body, not a redesign. Deliver entire head-to-toe silhouette, both feet completely visible with generous transparent margins, no waist fade or amputated edge. Match original illustration/anime style. Genuinely transparent PNG background, no new people, scenery, text or floor. Save output locally for repo integration.
