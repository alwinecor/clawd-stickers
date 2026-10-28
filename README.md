# clawd-stickers

English | [简体中文](README.zh-CN.md)

A collection of pixel-art stickers starring Clawd, the Claude Code mascot. Each set has its own theme, and every sticker is generated with code.

> [!NOTE]
> Clawd belongs to Anthropic. This is an unofficial fan project for non-commercial use only. See [LICENSE](LICENSE).

<p align="center"><img src="01-dev-life/preview.png" width="640" alt="01 · Dev Life preview"></p>

## How to use

Open a set, pick a sticker you like, and right-click or long-press to save the GIF. For WeChat, use the smaller versions in that set's `wechat/` folder: send one to "File Transfer", open it, long-press, and choose "Add to Stickers".

## Sets

| # | Theme | Contents | Status |
|---|---|---|---|
| 01 | [Dev Life · 克码人生](01-dev-life/) | 30 stickers about a programmer's everyday life | Done |

## Structure

Each set lives in its own folder:

- `gif/`: finished GIFs at full size (276×288)
- `wechat/`: WeChat-sized versions (240×240, ≤100KB)
- `preview.png`: an overview image of the set
- `src/`: the code that generates the set
- `README.md` / `README.zh-CN.md`: the sticker list and the story behind each one

## Credits

- The idea, Clawd's pixel style and the set structure all come from [clawd-moji](https://github.com/Qisi3344/clawd-moji) by [@Qisi3344](https://github.com/Qisi3344): the 15×16 body grid, black-square eyes with no mouth, one theme per set, and the `gif/` + `wechat/` + `src/` layout.
- The drawing helpers in `01-dev-life/src/clawd_dev.py` (`base`, `xform`, `squash`, `kf`, `face`, `render`, `save` and others) are adapted from that project's `clawd_movies.py` and `clawd_movies_more.py`.
- Clawd belongs to [Anthropic](https://www.anthropic.com).
