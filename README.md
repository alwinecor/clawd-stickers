# clawd-stickers

A collection of pixel-art stickers starring Clawd, the Claude Code mascot. Each set has its own theme, and every sticker is generated with code.

> Claude Code 吉祥物 Clawd 的像素表情包合集。一套一个主题，全部用代码生成。

> [!NOTE]
> Clawd belongs to Anthropic. This is an unofficial fan project for non-commercial use only. See [LICENSE](LICENSE).
>
> Clawd 角色属于 Anthropic。本仓库是粉丝创作，非官方、非商用，详见 [LICENSE](LICENSE)。

<p align="center"><img src="01-dev-life/preview.png" width="640" alt="01 · Dev Life preview"></p>

## How to use · 怎么用

Open a set, pick a sticker you like, and right-click or long-press to save the GIF. For WeChat, use the smaller versions in that set's `wechat/` folder: send one to "File Transfer", open it, long-press, and choose "Add to Stickers".

> 挑一套点开，选一个喜欢的，右键或长按保存 GIF 就能用。在微信里用的话，拿各套 `wechat/` 文件夹里的小尺寸版，发到「文件传输助手」，点开长按 →「添加到表情」。

## Sets · 套装

| # | Theme 主题 | Contents 内容 | Status 状态 |
|---|---|---|---|
| 01 | [Dev Life · 程序员日常](01-dev-life/) | 20 stickers about a programmer's everyday life<br>程序员日常 · 20 个 | Done 完成 |

## Structure · 结构

Each set lives in its own folder:

- `gif/`: finished GIFs at full size (276×288)
- `wechat/`: WeChat-sized versions (240×240, ≤100KB)
- `preview.png`: an overview image of the set
- `src/`: the code that generates the set
- `README.md`: the sticker list and the story behind each one

> 每套一个文件夹：`gif/` 放原尺寸动图，`wechat/` 放微信尺寸版，`preview.png` 是总览图，`src/` 是生成代码，`README.md` 是这套的清单和小剧情。

## Credits · 致谢

- The idea, Clawd's pixel style and the set structure all come from [clawd-moji](https://github.com/Qisi3344/clawd-moji) by [@Qisi3344](https://github.com/Qisi3344): the 15×16 body grid, black-square eyes with no mouth, one theme per set, and the `gif/` + `wechat/` + `src/` layout.
- The drawing helpers in `01-dev-life/src/clawd_dev.py` (`base`, `xform`, `squash`, `kf`, `face`, `render`, `save` and others) are adapted from that project's `clawd_movies.py` and `clawd_movies_more.py`.
- Clawd belongs to [Anthropic](https://www.anthropic.com).

> - 项目思路、Clawd 的像素画法和套装结构都来自 [@Qisi3344](https://github.com/Qisi3344) 的 [clawd-moji](https://github.com/Qisi3344/clawd-moji)：15×16 的身体网格、黑方块眼睛不画嘴、一套一个主题，以及 `gif/` + `wechat/` + `src/` 的目录结构。
> - `01-dev-life/src/clawd_dev.py` 里的绘图工具函数（`base`、`xform`、`squash`、`kf`、`face`、`render`、`save` 等）改编自原作的 `clawd_movies.py` 和 `clawd_movies_more.py`。
> - Clawd 角色属于 [Anthropic](https://www.anthropic.com)。
