# Clawd Stickers

English | [简体中文](README.zh-CN.md)

A collection of pixel-art animated stickers starring **Clawd**, the Claude Code mascot. Characters, props and frame-by-frame animation are drawn in Python, with ready-to-use GIFs included.

The collection currently contains **40 animated stickers** with the theme **Dev Life · 克码人生**.

> [!NOTE]
> This is an unofficial fan project, unaffiliated with and not endorsed by Anthropic. Content whose copyright is held by this project's contributors is [MIT-licensed](LICENSE) by default. Third-party rights, including the Claude Code mascot, are excluded.

## Contents

- [Features](#features)
- [Sticker preview](#sticker-preview)
- [Download and use](#download-and-use)
- [Generate locally](#generate-locally)
- [Repository structure](#repository-structure)
- [License and usage](#license-and-usage)
- [Credits](#credits)

## Features

- **Developer life and programmer jokes**: includes classics such as hello world, git clone and rubber duck debugging, alongside everyday scenes like slacking off, clocking out and bug hunting. There are also plenty of Claude Code references, including thinking, context compaction, usage limits and even a ban joke.
- **Consistent pixel style**: fan art based on Clawd's pixel design.
- **Ready-to-use GIFs**: every sticker is 288×288 with a transparent background and loops continuously. Download and use them directly, with no development environment needed.
- **Light and dark sets**: the dark set brightens text and outlines and darkens ground shadows for dark-mode chats.
- **Generated with code**: the Python script uses Pillow, with no extra fonts to download. Generate all stickers or selected ones locally.

## Sticker preview

The collection currently includes 40 stickers with the theme **Dev Life · 克码人生**. See the [set guide](dev-life/README.md) for details.

<table>
  <tr><td align="center" width="20%"><b>hello, world</b></td><td align="center" width="20%"><b>Thinking</b></td><td align="center" width="20%"><b>ultrathink</b></td><td align="center" width="20%"><b>Plan Mode</b></td><td align="center" width="20%"><b>Todo List</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/hello.gif" width="110" alt="hello, world"></td><td align="center"><img src="dev-life/gif/thinking.gif" width="110" alt="Thinking"></td><td align="center"><img src="dev-life/gif/ultrathink.gif" width="110" alt="ultrathink"></td><td align="center"><img src="dev-life/gif/plan.gif" width="110" alt="Plan Mode"></td><td align="center"><img src="dev-life/gif/todo.gif" width="110" alt="Todo List"></td></tr>
  <tr><td align="center" width="20%"><b>It's Simple</b></td><td align="center" width="20%"><b>Subagents</b></td><td align="center" width="20%"><b>Yes, Proceed</b></td><td align="center" width="20%"><b>LGTM</b></td><td align="center" width="20%"><b>You're Absolutely Right!</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/simple.gif" width="110" alt="It's Simple"></td><td align="center"><img src="dev-life/gif/subagents.gif" width="110" alt="Subagents"></td><td align="center"><img src="dev-life/gif/proceed.gif" width="110" alt="Yes, Proceed"></td><td align="center"><img src="dev-life/gif/lgtm.gif" width="110" alt="LGTM"></td><td align="center"><img src="dev-life/gif/right.gif" width="110" alt="You're Absolutely Right!"></td></tr>
  <tr><td align="center" width="20%"><b>/compact</b></td><td align="center" width="20%"><b>/clear</b></td><td align="center" width="20%"><b>Usage Limit</b></td><td align="center" width="20%"><b>Esc</b></td><td align="center" width="20%"><b>Banned</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/compact.gif" width="110" alt="/compact"></td><td align="center"><img src="dev-life/gif/clear.gif" width="110" alt="/clear"></td><td align="center"><img src="dev-life/gif/limit.gif" width="110" alt="Usage Limit"></td><td align="center"><img src="dev-life/gif/esc.gif" width="110" alt="Esc"></td><td align="center"><img src="dev-life/gif/banned.gif" width="110" alt="Banned"></td></tr>
  <tr><td align="center" width="20%"><b>git clone</b></td><td align="center" width="20%"><b>git stash</b></td><td align="center" width="20%"><b>cherry-pick</b></td><td align="center" width="20%"><b>Merge Conflict</b></td><td align="center" width="20%"><b>Force Push</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/clone.gif" width="110" alt="git clone"></td><td align="center"><img src="dev-life/gif/stash.gif" width="110" alt="git stash"></td><td align="center"><img src="dev-life/gif/cherry.gif" width="110" alt="cherry-pick"></td><td align="center"><img src="dev-life/gif/conflict.gif" width="110" alt="Merge Conflict"></td><td align="center"><img src="dev-life/gif/forcepush.gif" width="110" alt="Force Push"></td></tr>
  <tr><td align="center" width="20%"><b>git blame</b></td><td align="center" width="20%"><b>rm -rf</b></td><td align="center" width="20%"><b>detached HEAD</b></td><td align="center" width="20%"><b>404 Not Found</b></td><td align="center" width="20%"><b>Error</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/blame.gif" width="110" alt="git blame"></td><td align="center"><img src="dev-life/gif/rmrf.gif" width="110" alt="rm -rf"></td><td align="center"><img src="dev-life/gif/detached.gif" width="110" alt="detached HEAD"></td><td align="center"><img src="dev-life/gif/notfound.gif" width="110" alt="404 Not Found"></td><td align="center"><img src="dev-life/gif/error.gif" width="110" alt="Error"></td></tr>
  <tr><td align="center" width="20%"><b>Bug Hunt</b></td><td align="center" width="20%"><b>Rubber Duck</b></td><td align="center" width="20%"><b>while(true)</b></td><td align="center" width="20%"><b>Stack Overflow</b></td><td align="center" width="20%"><b>Memory Leak</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/bug.gif" width="110" alt="Bug Hunt"></td><td align="center"><img src="dev-life/gif/duck.gif" width="110" alt="Rubber Duck"></td><td align="center"><img src="dev-life/gif/loop.gif" width="110" alt="while(true)"></td><td align="center"><img src="dev-life/gif/overflow.gif" width="110" alt="Stack Overflow"></td><td align="center"><img src="dev-life/gif/leak.gif" width="110" alt="Memory Leak"></td></tr>
  <tr><td align="center" width="20%"><b>Works on My Machine</b></td><td align="center" width="20%"><b>Tests Passed</b></td><td align="center" width="20%"><b>Friday Deploy</b></td><td align="center" width="20%"><b>Deadline</b></td><td align="center" width="20%"><b>Overtime</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/works.gif" width="110" alt="Works on My Machine"></td><td align="center"><img src="dev-life/gif/passed.gif" width="110" alt="Tests Passed"></td><td align="center"><img src="dev-life/gif/deploy.gif" width="110" alt="Friday Deploy"></td><td align="center"><img src="dev-life/gif/deadline.gif" width="110" alt="Deadline"></td><td align="center"><img src="dev-life/gif/overtime.gif" width="110" alt="Overtime"></td></tr>
  <tr><td align="center" width="20%"><b>Coffee Break</b></td><td align="center" width="20%"><b>Slacking Off</b></td><td align="center" width="20%"><b>Clock Out</b></td><td align="center" width="20%"><b>Good Night</b></td><td align="center" width="20%"><b>/exit</b></td></tr>
  <tr><td align="center"><img src="dev-life/gif/coffee.gif" width="110" alt="Coffee Break"></td><td align="center"><img src="dev-life/gif/fish.gif" width="110" alt="Slacking Off"></td><td align="center"><img src="dev-life/gif/offwork.gif" width="110" alt="Clock Out"></td><td align="center"><img src="dev-life/gif/sleep.gif" width="110" alt="Good Night"></td><td align="center"><img src="dev-life/gif/bye.gif" width="110" alt="/exit"></td></tr>
</table>

## Download and use

### Save a single sticker

1. Choose a sticker from the preview above or open the [set guide](dev-life/README.md).
2. Click its GIF to open the original, then right-click to save the `.gif` file.

### Download the whole set

Select **Code → Download ZIP** on the repository home page, extract the archive and open [`dev-life/gif/`](dev-life/gif/) to find the whole sticker collection for light backgrounds. The dark-background set is in [`dev-life/gif-dark/`](dev-life/gif-dark/). You can also clone the repository with the Git commands below.

### Add and use stickers in chat apps

Saved GIFs can be sent directly in chat apps such as WeChat, Xiaohongshu and WhatsApp. If the app supports custom stickers, you can also add them manually. All GIFs are 288×288 with a transparent background and loop continuously.

## Generate locally

Run the included Python script to edit animations or regenerate GIFs.

### Requirements

- Python 3 and pip.
- The Pillow image library.
- Git if cloning the repository; downloading a ZIP is also supported.

### Get the repository and install dependencies

```bash
git clone https://github.com/alwinecor/clawd-stickers.git
cd clawd-stickers
python -m pip install Pillow
```

### Generate stickers

Run these commands from the repository root:

```bash
# Generate all 40 stickers
python dev-life/src/clawd_dev.py

# Generate only the context-compaction sticker
python dev-life/src/clawd_dev.py compact

# Generate several selected stickers
python dev-life/src/clawd_dev.py thinking compact clear

# Generate the dark-background set (combines with the arguments above)
python dev-life/src/clawd_dev.py --dark
```

Output is saved to [`dev-life/gif/`](dev-life/gif/), or [`dev-life/gif-dark/`](dev-life/gif-dark/) with `--dark`, replacing GIFs with the same names. The dark colour swaps are listed in the `DARK` table at the top of the script. The script prints each sticker's name, frame count and file size.

Arguments generally match GIF filenames without the `.gif` extension, such as `thinking`, `compact` and `clear`. Browse the output directory for the full list. The script's `ALL` list and `FILE` mapping define the generator entry points and output names; `clear` maps to the `clear_ctx()` function.

## Repository structure

```text
clawd-stickers/
├── README.md                  # English project guide
├── README.zh-CN.md            # Chinese project guide
├── LICENSE                    # Standard MIT License
└── dev-life/                  # Dev Life sticker set
    ├── README.md              # English sticker content guide
    ├── README.zh-CN.md        # Chinese sticker content guide
    ├── gif/                   # 40 finished GIFs
    ├── gif-dark/              # 40 finished GIFs (dark background)
    ├── promo/                 # Share images (3:4, 20 stickers per page)
    │   ├── covers/            # Animated pages and stills, dark and light
    │   └── make_covers.py     # Share image generator
    └── src/
        └── clawd_dev.py       # Drawing, animation and GIF export
```

## License and usage

Except for third-party material and rights otherwise noted, this project's code, documentation and original artistic contributions are licensed under the [MIT License](LICENSE), to the extent that contributors hold the relevant copyright. This includes original contributions to the sticker artwork.

- **Content covered by MIT**: use, modification, distribution and commercial use are permitted. Retain applicable copyright and license notices when distributing copies or substantial portions, including attribution for adapted upstream code.
- **Third-party material and rights**: The Claude Code mascot belongs to Anthropic.

## Credits

- Thanks to [@Qisi3344](https://github.com/Qisi3344) and [clawd-moji](https://github.com/Qisi3344/clawd-moji) for the drawing tools and creative inspiration used in this project!
- Drawing helpers in this repository's [`clawd_dev.py`](dev-life/src/clawd_dev.py), including `base`, `xform`, `squash`, `kf`, `face` and `render`, are adapted from that project's `clawd_movies.py` and `clawd_movies_more.py`.
- [Anthropic](https://www.anthropic.com) owns the Clawd character.
