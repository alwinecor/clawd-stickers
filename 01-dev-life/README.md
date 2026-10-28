# 01 · Dev Life · 克码人生

English | [简体中文](README.zh-CN.md)

30 animated stickers about a programmer's everyday life, starring Clawd. Clawd's eyes are two small black squares (sometimes squinting into ^ ^ or > <), and there's no mouth: every joke is told through movement and props. Stickers 21–30 are Claude Code specials. These rules follow [01-movie-night](https://github.com/Qisi3344/clawd-moji/tree/main/01-movie-night) from Qisi3344/clawd-moji.

| # | Name | Sticker | Story |
|---|---|---|---|
| 1 | **Thinking** | <img src="gif/thinking.gif" width="120"> | Claude Code's ✻ spinner turns above its head while dots appear one by one and it tilts its head, deep in thought. |
| 2 | **/compact** | <img src="gif/compact.gif" width="120"> | A plate labeled `/compact` presses down and flattens it into a pancake. It bounces back happy, then a "?" pops up: what was it doing again? |
| 3 | **git clone** | <img src="gif/clone.gif" width="120"> | Types `git clone`, strains and shakes, and splits into three. They take turns hopping, then merge back into one. |
| 4 | **Merge Conflict** | <img src="gif/conflict.gif" width="120"> | Under `<<<<<<<` and `>>>>>>>`, two Clawds push head to head with sparks flying, bounce apart, and glare at each other. |
| 5 | **rm -rf** | <img src="gif/rmrf.gif" width="120"> | Types `rm -rf /` and hits Enter. It gets deleted from the feet up until only its eyes are left, then drops back out of the terminal. |
| 6 | **hello, world** | <img src="gif/hello.gif" width="120"> | Types `hello, world` and waves. Good for saying hi. |
| 7 | **LGTM** | <img src="gif/lgtm.gif" width="120"> | Raises a rubber stamp and slams down a crooked red LGTM. Means "approved", "got it", or "sounds good". |
| 8 | **Tests Passed** | <img src="gif/passed.gif" width="120"> | Watches nervously as a big green check mark draws itself, then hops around in falling confetti. |
| 9 | **Error** | <img src="gif/error.gif" width="120"> | A red Error flashes overhead. It clutches its head, flips onto its back with legs kicking and stars circling, then flips back up. |
| 10 | **Coffee Break** | <img src="gif/coffee.gif" width="120"> | Sways half asleep, gulps down a blue mug of coffee, and snaps wide awake. |
| 11 | **Friday Deploy** | <img src="gif/deploy.gif" width="120"> | Under the words `friday deploy`, holds three incense sticks and bows three times with its eyes closed. |
| 12 | **Works on My Machine** | <img src="gif/works.gif" width="120"> | Hugs its laptop and shrugs, then cuddles it with hearts floating up. |
| 13 | **Bug Hunt** | <img src="gif/bug.gif" width="120"> | Tracks a little bug, jumps and sits right on it, feels proud, and then the bug sneaks out the other side. |
| 14 | **Slacking Off** | <img src="gif/fish.gif" width="120"> | Holds a little blue fish and gently pets it. The tail wags and small hearts float up. (In Chinese, "slacking off" is literally "petting fish".) |
| 15 | **Clock Out** | <img src="gif/offwork.gif" width="120"> | Stares at the clock until 17:59 turns 18:00, then dashes off screen. Time rewinds to 17:59 and it trudges back. |
| 16 | **Overtime** | <img src="gif/overtime.gif" width="120"> | 02:00 under the moon: nods off at the desk, jolts awake, then slowly drifts off again. |
| 17 | **Good Night** | <img src="gif/sleep.gif" width="120"> | Sleeps in a blue nightcap while a trail of z's floats up. |
| 18 | **404 Not Found** | <img src="gif/notfound.gif" width="120"> | Peeks out of a box marked 404, looks left and right, realizes it's been spotted, ducks back in, and leaves a "?". |
| 19 | **while(true)** | <img src="gif/loop.gif" width="120"> | Runs flat out in a hamster wheel until its eyes go > < and sweat goes flying. |
| 20 | **Force Push** | <img src="gif/forcepush.gif" width="120"> | Shoves a big block labeled `main` until it flies off and cheers. Then the block gets pushed back and squeezes it out. |
| 21 | **Yes, Proceed** | <img src="gif/proceed.gif" width="120"> | Permission dialogs keep popping up and it keeps hitting yes, faster and faster, until its eyes go > <. |
| 22 | **Esc** | <img src="gif/esc.gif" width="120"> | Charging ahead full speed when a giant Esc key slams down in front of it. It screeches to a stop, nose to the key. |
| 23 | **Usage Limit** | <img src="gif/limit.gif" width="120"> | Types away while a battery drains from green to red. At empty, `limit reached` appears and it melts flat until the battery recharges and it bounces back. |
| 24 | **Plan Mode** | <img src="gif/plan.gif" width="120"> | Puts on a hard hat, unrolls a blueprint and sketches a little house on it before writing any code. |
| 25 | **/clear** | <img src="gif/clear.gif" width="120"> | The terminal is overflowing and its eyes are spinning. Types `/clear`, everything wipes away, and it sparkles with relief. |
| 26 | **ultrathink** | <img src="gif/ultrathink.gif" width="120"> | `ultrathink` appears in rainbow letters. It thinks so hard it turns red and steams, then a light bulb goes on. |
| 27 | **Subagents** | <img src="gif/subagents.gif" width="120"> | Sends out three tiny Clawds that run off screen. They come back one by one with check marks, and it cheers. |
| 28 | **Todo List** | <img src="gif/todo.gif" width="120"> | Watches the todo list as each item turns orange, then gets checked off. When all four are done, confetti falls. |
| 29 | **You're Absolutely Right!** | <img src="gif/right.gif" width="120"> | Nods along eagerly as `You're absolutely right!` appears line by line, with sparkles. |
| 30 | **/exit** | <img src="gif/bye.gif" width="120"> | Types `/exit`, waves goodbye, then shrinks away into the terminal, leaving `bye!` behind. |

## Download / Use in WeChat

- `gif/`: full size, 276×288, transparent background
- `wechat/`: 240×240, ≤100KB each, transparent background (a few longer ones drop frames to fit)

To use them in WeChat, send a GIF from `wechat/` to "File Transfer", open it, long-press, and choose "Add to Stickers".

## Build it yourself

```bash
cd src
pip install pillow
python clawd_dev.py            # all 30
python clawd_dev.py compact    # just one
```

No extra font is needed: the command-line text uses a tiny 3×5 pixel font built into the script.

## Credits

The idea and drawing style come from [clawd-moji](https://github.com/Qisi3344/clawd-moji) by [@Qisi3344](https://github.com/Qisi3344). The drawing helpers in `src/clawd_dev.py` are adapted from that project's generator code.
