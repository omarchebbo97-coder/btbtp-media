# BTBTP build tools
- Videos: `python3 make2.py episode.json` (needs ffmpeg, node + playwright, fonts from `npm i @fontsource/readex-pro @fontsource/source-sans-3 @fontsource-variable/source-serif-4` in a folder named tpl/ next to v2/). Captions at top, colour per speaker (Wadad pink, Souad green, New kidney gold, guests slate), long lines split, end card in the tail.
- Stories: `node story.js spec.json out.jpg` -> 1080x1920 awareness story (top card + question card), e.g. st04.json / st05.json.
- Carousels: `node render2.js spec.json outdir` -> IG 1080x1350 (EN first) + TikTok 1080x1920 (AR first). `"swipe": true` adds the swipe cue on slides 1-2 (swipe test from C01 on). No progress badge.
- Character refs in /refs (masters). ElevenLabs flow misJK7gxgwM7tegJUBra.
- Baydat scene from 25 Oct: refs/baydat_xray.jpg (Omar's X-ray pick, outside the body). Use refs/baydat_xray_tall.jpg (9:16 with headroom) for slides/videos: text goes in the top dark area, character stays clear of the swipe pill.
- From 25 Oct 2026 Lebanon is on winter time: Buffer dueAt uses +02:00 (until DST returns end of March).
- Every Instagram image post: tag @omar_chebbo on the first image (userTags x0.5 y0.5). Buffer has no collab-invite.
- TikTok safe zones (29 Oct): text panels start at y=300, right margin 150, handle and swipe pill sit above y=1450 (TikTok's caption covers the bottom ~470px, the search bar the top ~250px). Swipe pill on TikTok is left-aligned. Use photo_tt in a slide spec for a TikTok-only image (e.g. refs/baydat_xray_tiktok.jpg).
