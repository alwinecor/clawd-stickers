# clawd-stickers

English | [简体中文](README.zh-CN.md)

A collection of pixel-art animated stickers starring **Clawd**, the Claude Code mascot. Each set follows a theme, with characters, props and frame-by-frame animation drawn in Python and ready-to-use GIFs included.

The collection currently contains **1 set and 40 animated stickers**, together forming **Dev Life · 克码人生**.

> [!NOTE]
> This is an unofficial fan project, unaffiliated with and not endorsed by Anthropic. Clawd belongs to Anthropic. Repository contents are for personal, non-commercial use only. See [LICENSE](LICENSE).

## Contents

- [Features](#features)
- [Sticker preview](#sticker-preview)
- [Download and use](#download-and-use)
- [Sticker sets](#sticker-sets)
- [Generate locally](#generate-locally)
- [Repository structure](#repository-structure)
- [Contributing](#contributing)
- [License and usage](#license-and-usage)
- [Credits](#credits)

## Features

- **Inspired by developer life**: merge conflicts, context compaction, slacking off and clocking out become little animated stories.
- **Consistent pixel style**: Clawd keeps its 15×16 body grid, black-square eyes and mouthless design, expressing emotion through movement and props.
- **Ready-to-use GIFs**: every sticker is 288×288 with a transparent background and loops continuously. No development environment is needed to use them.
- **Generated with code**: the Python script uses Pillow and a built-in 3×5 pixel font, with no extra fonts to download. Generate the whole set or selected stickers.
- **Organized by theme**: each set has its own finished GIFs, generator code and documentation in English and Chinese.

## Sticker preview

All 40 stickers from **Dev Life · 克码人生** are shown below, ordered to keep related scenes together. See the [set guide](01-dev-life/README.md) for each sticker's story.

<table>
  <tr><td align="center" width="20%"><b>hello, world</b></td><td align="center" width="20%"><b>Thinking</b></td><td align="center" width="20%"><b>ultrathink</b></td><td align="center" width="20%"><b>Plan Mode</b></td><td align="center" width="20%"><b>Todo List</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/hello.gif" width="110" alt="hello, world"></td><td align="center"><img src="01-dev-life/gif/thinking.gif" width="110" alt="Thinking"></td><td align="center"><img src="01-dev-life/gif/ultrathink.gif" width="110" alt="ultrathink"></td><td align="center"><img src="01-dev-life/gif/plan.gif" width="110" alt="Plan Mode"></td><td align="center"><img src="01-dev-life/gif/todo.gif" width="110" alt="Todo List"></td></tr>
  <tr><td align="center" width="20%"><b>It's Simple</b></td><td align="center" width="20%"><b>Subagents</b></td><td align="center" width="20%"><b>Yes, Proceed</b></td><td align="center" width="20%"><b>LGTM</b></td><td align="center" width="20%"><b>You're Absolutely Right!</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/simple.gif" width="110" alt="It's Simple"></td><td align="center"><img src="01-dev-life/gif/subagents.gif" width="110" alt="Subagents"></td><td align="center"><img src="01-dev-life/gif/proceed.gif" width="110" alt="Yes, Proceed"></td><td align="center"><img src="01-dev-life/gif/lgtm.gif" width="110" alt="LGTM"></td><td align="center"><img src="01-dev-life/gif/right.gif" width="110" alt="You're Absolutely Right!"></td></tr>
  <tr><td align="center" width="20%"><b>/compact</b></td><td align="center" width="20%"><b>/clear</b></td><td align="center" width="20%"><b>Usage Limit</b></td><td align="center" width="20%"><b>Esc</b></td><td align="center" width="20%"><b>Banned</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/compact.gif" width="110" alt="/compact"></td><td align="center"><img src="01-dev-life/gif/clear.gif" width="110" alt="/clear"></td><td align="center"><img src="01-dev-life/gif/limit.gif" width="110" alt="Usage Limit"></td><td align="center"><img src="01-dev-life/gif/esc.gif" width="110" alt="Esc"></td><td align="center"><img src="01-dev-life/gif/banned.gif" width="110" alt="Banned"></td></tr>
  <tr><td align="center" width="20%"><b>git clone</b></td><td align="center" width="20%"><b>git stash</b></td><td align="center" width="20%"><b>cherry-pick</b></td><td align="center" width="20%"><b>Merge Conflict</b></td><td align="center" width="20%"><b>Force Push</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/clone.gif" width="110" alt="git clone"></td><td align="center"><img src="01-dev-life/gif/stash.gif" width="110" alt="git stash"></td><td align="center"><img src="01-dev-life/gif/cherry.gif" width="110" alt="cherry-pick"></td><td align="center"><img src="01-dev-life/gif/conflict.gif" width="110" alt="Merge Conflict"></td><td align="center"><img src="01-dev-life/gif/forcepush.gif" width="110" alt="Force Push"></td></tr>
  <tr><td align="center" width="20%"><b>git blame</b></td><td align="center" width="20%"><b>rm -rf</b></td><td align="center" width="20%"><b>detached HEAD</b></td><td align="center" width="20%"><b>404 Not Found</b></td><td align="center" width="20%"><b>Error</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/blame.gif" width="110" alt="git blame"></td><td align="center"><img src="01-dev-life/gif/rmrf.gif" width="110" alt="rm -rf"></td><td align="center"><img src="01-dev-life/gif/detached.gif" width="110" alt="detached HEAD"></td><td align="center"><img src="01-dev-life/gif/notfound.gif" width="110" alt="404 Not Found"></td><td align="center"><img src="01-dev-life/gif/error.gif" width="110" alt="Error"></td></tr>
  <tr><td align="center" width="20%"><b>Bug Hunt</b></td><td align="center" width="20%"><b>Rubber Duck</b></td><td align="center" width="20%"><b>while(true)</b></td><td align="center" width="20%"><b>Stack Overflow</b></td><td align="center" width="20%"><b>Memory Leak</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/bug.gif" width="110" alt="Bug Hunt"></td><td align="center"><img src="01-dev-life/gif/duck.gif" width="110" alt="Rubber Duck"></td><td align="center"><img src="01-dev-life/gif/loop.gif" width="110" alt="while(true)"></td><td align="center"><img src="01-dev-life/gif/overflow.gif" width="110" alt="Stack Overflow"></td><td align="center"><img src="01-dev-life/gif/leak.gif" width="110" alt="Memory Leak"></td></tr>
  <tr><td align="center" width="20%"><b>Works on My Machine</b></td><td align="center" width="20%"><b>Tests Passed</b></td><td align="center" width="20%"><b>Friday Deploy</b></td><td align="center" width="20%"><b>Deadline</b></td><td align="center" width="20%"><b>Overtime</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/works.gif" width="110" alt="Works on My Machine"></td><td align="center"><img src="01-dev-life/gif/passed.gif" width="110" alt="Tests Passed"></td><td align="center"><img src="01-dev-life/gif/deploy.gif" width="110" alt="Friday Deploy"></td><td align="center"><img src="01-dev-life/gif/deadline.gif" width="110" alt="Deadline"></td><td align="center"><img src="01-dev-life/gif/overtime.gif" width="110" alt="Overtime"></td></tr>
  <tr><td align="center" width="20%"><b>Coffee Break</b></td><td align="center" width="20%"><b>Slacking Off</b></td><td align="center" width="20%"><b>Clock Out</b></td><td align="center" width="20%"><b>Good Night</b></td><td align="center" width="20%"><b>/exit</b></td></tr>
  <tr><td align="center"><img src="01-dev-life/gif/coffee.gif" width="110" alt="Coffee Break"></td><td align="center"><img src="01-dev-life/gif/fish.gif" width="110" alt="Slacking Off"></td><td align="center"><img src="01-dev-life/gif/offwork.gif" width="110" alt="Clock Out"></td><td align="center"><img src="01-dev-life/gif/sleep.gif" width="110" alt="Good Night"></td><td align="center"><img src="01-dev-life/gif/bye.gif" width="110" alt="/exit"></td></tr>
</table>

## Download and use

### Save a single sticker

1. Open the [set guide](01-dev-life/README.md) and choose a sticker.
2. Click its GIF to open the original, then right-click or long-press to save the `.gif` file.
3. Send it or add it as a custom sticker in a chat app that supports GIFs.

### Download the whole set

Select **Code → Download ZIP** on the repository home page, extract the archive and open [`01-dev-life/gif/`](01-dev-life/gif/) to find all finished stickers. You can also clone the repository with the Git commands below.

### Add stickers in WeChat

Send the saved GIF as a file to **File Transfer**, open it in WeChat, then long-press and choose **Add to Stickers**. The exact menu may vary by WeChat client.

## Sticker sets

| # | Theme | Contents | Stickers | Status |
| --- | --- | --- | --- | --- |
| 01 | [Dev Life · 克码人生](01-dev-life/README.md) | A developer's work and life | 40 | Complete |

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
python 01-dev-life/src/clawd_dev.py

# Generate only the context-compaction sticker
python 01-dev-life/src/clawd_dev.py compact

# Generate several selected stickers
python 01-dev-life/src/clawd_dev.py thinking compact clear
```

Output is saved to [`01-dev-life/gif/`](01-dev-life/gif/), replacing GIFs with the same names. The script prints each sticker's name, frame count and file size.

Arguments generally match GIF filenames without the `.gif` extension, such as `thinking`, `compact` and `clear`. Browse the output directory for the full list. The script's `ALL` list and `FILE` mapping define the generator entry points and output names; `clear` maps to the `clear_ctx()` function.

## Repository structure

```text
clawd-stickers/
├── README.md                  # English project guide
├── README.zh-CN.md            # Chinese project guide
├── LICENSE                    # License and usage terms
└── 01-dev-life/               # Dev Life sticker set
    ├── README.md              # English sticker list and stories
    ├── README.zh-CN.md        # Chinese sticker list and stories
    ├── gif/                   # 40 finished GIFs (288×288)
    └── src/
        └── clawd_dev.py       # Drawing, animation and GIF export
```

## Contributing

Suggest new themes or stickers, or report problems through [Issues](https://github.com/alwinecor/clawd-stickers/issues). Pull requests improving animations, generator code and documentation are welcome.

When adding or changing stickers:

1. Keep Clawd's existing pixel design and the set's visual style.
2. Add a generator function for each new animation and register it in `ALL`. Add a `FILE` mapping if its output name differs.
3. Generate the GIF and check playback, transparency and output dimensions.
4. Update the set's English and Chinese lists. Add a link to the root guides when introducing a new set.
5. Preserve source attribution and credits, and follow the usage terms in [LICENSE](LICENSE).

## License and usage

This repository uses a custom fan-project usage statement. See [LICENSE](LICENSE) for its full text:

- Clawd belongs to Anthropic.
- This is an unofficial fan project, unaffiliated with and not endorsed by Anthropic.
- Repository contents are for personal, non-commercial use only. Commercial use is prohibited.

## Credits

- [clawd-moji](https://github.com/Qisi3344/clawd-moji) by [@Qisi3344](https://github.com/Qisi3344), especially its [01-movie-night](https://github.com/Qisi3344/clawd-moji/tree/main/01-movie-night) set, inspired the project concept, Clawd's pixel style and the directory structure organized by theme.
- Drawing helpers in this repository's [`clawd_dev.py`](01-dev-life/src/clawd_dev.py), including `base`, `xform`, `squash`, `kf`, `face` and `render`, are adapted from that project's `clawd_movies.py` and `clawd_movies_more.py`.
- [Anthropic](https://www.anthropic.com) owns the Clawd character.
