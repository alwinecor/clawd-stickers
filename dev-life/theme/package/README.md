# {name}

English | [简体中文](README.zh-CN.md)

A [clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) theme in which Clawd acts out everyday developer life.

- **Author**: alwinecor
- **Version**: {version}
- **Theme ID**: `{id}`
- **Source**: <https://github.com/alwinecor/clawd-stickers>

## Install

Copy this folder into your clawd-on-desk themes folder, then pick the theme under **Settings... → Theme**.

| System | Themes folder |
| --- | --- |
| Windows | `%APPDATA%/clawd-on-desk/themes/` |
| macOS | `~/Library/Application Support/clawd-on-desk/themes/` |
| Linux | `~/.config/clawd-on-desk/themes/` |

## Supports

- Every agent state, including thinking, working, subagents, context compaction, errors, the full sleep sequence and more
- Separate animations for two and for three or more active sessions, with several Clawds on screen
- Eye tracking while idle, random idle animations, roaming, dragging and click reactions

## Known limitations

- Mini mode is not supported.
- Pet tint is turned off.
- No custom sound effects.
- Tested with clawd-on-desk 1.5.0 on Windows. macOS and Linux are untested.

## Animations

The theme has 47 animations. Where a moment lists several, one of them plays. Most come from the [Dev Life stickers](https://github.com/alwinecor/clawd-stickers/blob/main/dev-life/README.md), where you can read more about each one.

### Working

<table>
<tr><th>When</th><th colspan="4">Animation</th></tr>
<tr>
<td>A prompt is submitted</td>
<td align="center"><img src="assets/thinking.apng" width="96"><br><b>Thinking</b></td>
<td align="center"><img src="assets/ultrathink.apng" width="96"><br><b>ultrathink</b></td>
<td align="center"><img src="assets/plan.apng" width="96"><br><b>Plan Mode</b></td>
<td></td>
</tr>
<tr>
<td rowspan="2">Using tools, one session</td>
<td align="center"><img src="assets/todo.apng" width="96"><br><b>Todo List</b></td>
<td align="center"><img src="assets/simple.apng" width="96"><br><b>It's Simple</b></td>
<td align="center"><img src="assets/bug.apng" width="96"><br><b>Bug Hunt</b></td>
<td align="center"><img src="assets/loop.apng" width="96"><br><b>while(true)</b></td>
</tr>
<tr>
<td align="center"><img src="assets/deadline.apng" width="96"><br><b>Deadline</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Using tools, two sessions</td>
<td align="center"><img src="assets/team2.apng" width="96"><br><b>Team of Two</b></td>
<td align="center"><img src="assets/conflict.apng" width="96"><br><b>Merge Conflict</b></td>
<td colspan="2">In Team of Two, two Clawds share the desk: one writes code, the other runs tests and panics when one fails.</td>
</tr>
<tr>
<td>Using tools, three or more sessions</td>
<td align="center"><img src="assets/team3.apng" width="96"><br><b>Team of Three</b></td>
<td colspan="3">A third Clawd joins them, standing on top of the screens and sipping coffee.</td>
</tr>
<tr>
<td>A subagent is active</td>
<td align="center"><img src="assets/subagents.apng" width="96"><br><b>Subagents</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Compacting context</td>
<td align="center"><img src="assets/compact.apng" width="96"><br><b>/compact</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Creating a worktree</td>
<td align="center"><img src="assets/clone.apng" width="96"><br><b>git clone</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Permission request or alert</td>
<td align="center"><img src="assets/proceed.apng" width="96"><br><b>Yes, Proceed</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Task completed</td>
<td align="center"><img src="assets/passed_long.apng" width="96"><br><b>Tests Passed (extended)</b></td>
<td align="center"><img src="assets/lgtm.apng" width="96"><br><b>LGTM</b></td>
<td colspan="2"></td>
</tr>
<tr>
<td>Tool failure</td>
<td align="center"><img src="assets/error.apng" width="96"><br><b>Error</b></td>
<td colspan="3"></td>
</tr>
</table>

### Idle

<table>
<tr><th>When</th><th colspan="4">Animation</th></tr>
<tr>
<td>No activity</td>
<td align="center"><img src="assets/idle.svg" width="96"><br><b>Idle</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Free roam</td>
<td align="center"><img src="assets/roam.svg" width="96"><br><b>Walk</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td rowspan="4">Random idle scene</td>
<td align="center"><img src="assets/fish.apng" width="96"><br><b>Slacking Off</b></td>
<td align="center"><img src="assets/coffee.apng" width="96"><br><b>Coffee Break</b></td>
<td align="center"><img src="assets/duck.apng" width="96"><br><b>Rubber Duck</b></td>
<td align="center"><img src="assets/works.apng" width="96"><br><b>Works on My Machine</b></td>
</tr>
<tr>
<td align="center"><img src="assets/blame.apng" width="96"><br><b>git blame</b></td>
<td align="center"><img src="assets/deploy.apng" width="96"><br><b>Friday Deploy</b></td>
<td align="center"><img src="assets/overtime.apng" width="96"><br><b>Overtime</b></td>
<td align="center"><img src="assets/offwork.apng" width="96"><br><b>Clock Out</b></td>
</tr>
<tr>
<td align="center"><img src="assets/leak.apng" width="96"><br><b>Memory Leak</b></td>
<td align="center"><img src="assets/overflow.apng" width="96"><br><b>Stack Overflow</b></td>
<td align="center"><img src="assets/cherry.apng" width="96"><br><b>cherry-pick</b></td>
<td align="center"><img src="assets/esc.apng" width="96"><br><b>Esc</b></td>
</tr>
<tr>
<td align="center"><img src="assets/forcepush.apng" width="96"><br><b>Force Push</b></td>
<td align="center"><img src="assets/stash.apng" width="96"><br><b>git stash</b></td>
<td align="center"><img src="assets/clear.apng" width="96"><br><b>/clear</b></td>
<td align="center"><img src="assets/bye_long.apng" width="96"><br><b>/exit (extended)</b></td>
</tr>
</table>

### Interaction

<table>
<tr><th>When</th><th colspan="4">Animation</th></tr>
<tr>
<td>Dragged</td>
<td align="center"><img src="assets/drag.svg" width="96"><br><b>Drag</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Double-click</td>
<td align="center"><img src="assets/hello.apng" width="96"><br><b>hello, world</b><br>Left side.</td>
<td align="center"><img src="assets/right.apng" width="96"><br><b>You're Absolutely Right!</b><br>Right side.</td>
<td align="center"><img src="assets/notfound.apng" width="96"><br><b>404 Not Found</b><br>A 50% chance.</td>
<td></td>
</tr>
<tr>
<td>Four rapid clicks</td>
<td align="center"><img src="assets/rmrf.apng" width="96"><br><b>rm -rf</b></td>
<td align="center"><img src="assets/detached_long.apng" width="96"><br><b>detached HEAD (extended)</b></td>
<td align="center"><img src="assets/banned_long.apng" width="96"><br><b>Banned (extended)</b></td>
<td></td>
</tr>
<tr>
<td>Mouse circled around Clawd</td>
<td align="center"><img src="assets/dizzy.apng" width="96"><br><b>Dizzy</b></td>
<td colspan="3"></td>
</tr>
</table>

### Sleep

<table>
<tr><th>When</th><th colspan="4">Animation</th></tr>
<tr>
<td>Falling asleep</td>
<td align="center"><img src="assets/yawn.apng" width="96"><br><b>Yawn</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Asleep</td>
<td align="center"><img src="assets/sleep.apng" width="96"><br><b>Good Night</b></td>
<td colspan="3"></td>
</tr>
<tr>
<td>Waking up</td>
<td align="center"><img src="assets/wake.apng" width="96"><br><b>Wake</b></td>
<td colspan="3"></td>
</tr>
</table>

## License

See [LICENSE](LICENSE). This is an unofficial fan theme, not affiliated with or endorsed by Anthropic.
