# Notices

This project is an unofficial fan work. It uses or refers to the third-party material below, which is not covered by [LICENSE](LICENSE) or [LICENSE-ART](LICENSE-ART) except where stated.

## Clawd character

The Clawd character belongs to [Anthropic](https://www.anthropic.com). This project is not affiliated with or endorsed by Anthropic, and its licences grant no rights in the character.

## clawd-moji

The drawing helpers in `dev-life/src/clawd_dev.py`, such as `base`, `xform`, `squash`, `kf`, `face` and `render`, are adapted from `clawd_movies.py` and `clawd_movies_more.py` in [Qisi3344/clawd-moji](https://github.com/Qisi3344/clawd-moji).

Status: to be confirmed. The clawd-moji README says the code in each set's `src/` uses MIT and the sticker images are for personal, non-commercial use, while its LICENSE file limits all repository content to personal, non-commercial use. This project treats the adapted code as MIT, following that README, until Qisi3344 confirms the intended terms. No clawd-moji image files are included here.

## clawd-on-desk

The desktop pet themes are built for [clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk), whose artwork is not covered by its AGPL-3.0 source licence and is all rights reserved. The themes contain none of that artwork. `idle.svg`, `roam.svg` and `drag.svg` show the same Clawd body shape as clawd-on-desk's artwork because both depict the same character.

| Theme file | Source |
| --- | --- |
| `idle.svg` | Breathing and blinking follow this project's stickers. The `eyes-js`, `body-js` and `shadow-js` ids and the eye tracking settings in `theme.json` follow the clawd-on-desk theme format. |
| `roam.svg`, `drag.svg` | Drawn from this project's stickers, including their arm poses and eyes, with their own animation. |

Earlier versions of `idle.svg` reused the breathing and blinking timing, keyframes and layering of `clawd-idle-follow.svg`. This was replaced on 2026-11-01, and this project's licences do not cover that animation in those earlier versions.
