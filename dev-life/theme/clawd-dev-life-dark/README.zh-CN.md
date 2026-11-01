# Clawd Dev Life (Dark)

[English](README.md) | 简体中文

[clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) 主题：让 Clawd 演出开发者的日常。

- **作者**：alwinecor
- **版本**：1.0.0
- **主题 ID**：`clawd-dev-life-dark`
- **源仓库**：<https://github.com/alwinecor/clawd-stickers>

## 安装

把本文件夹复制到 clawd-on-desk 的主题目录，然后在 **Settings... → Theme** 中选择本主题。

| 系统 | 主题目录 |
| --- | --- |
| Windows | `%APPDATA%/clawd-on-desk/themes/` |
| macOS | `~/Library/Application Support/clawd-on-desk/themes/` |
| Linux | `~/.config/clawd-on-desk/themes/` |

## 支持的能力

- 全部 agent 状态，包括思考、工作、子代理、压缩上下文、报错和完整入睡流程等
- 2 个会话与 3 个及以上会话的专用动画，含多只 Clawd
- 待机时眼睛跟随、随机待机动画、走动、拖拽和点击反应

## 已知限制

- 不支持迷你模式。
- 已关闭桌宠染色。
- 无专属音效。
- 已在 Windows 上的 clawd-on-desk 1.5.0 测试，macOS 和 Linux 尚未测试。

## 全部动画

本主题共 47 个动画。同一时机列出多个动画时，会播放其中一个。大部分动画来自[克码人生表情包](https://github.com/alwinecor/clawd-stickers/blob/main/dev-life/README.zh-CN.md)，具体内容说明请见那里。

### 工作

<table>
<tr><th>触发时机</th><th colspan="4">动画</th></tr>
<tr>
<td>提交提示词</td>
<td align="center"><img src="assets/thinking.apng" width="96"><br><b>思考中</b><br>Thinking</td>
<td align="center"><img src="assets/ultrathink.apng" width="96"><br><b>深度思考</b><br>ultrathink</td>
<td align="center"><img src="assets/plan.apng" width="96"><br><b>计划模式</b><br>Plan Mode</td>
<td></td>
</tr>
<tr>
<td rowspan="2">使用工具（1 个会话）</td>
<td align="center"><img src="assets/todo.apng" width="96"><br><b>待办清单</b><br>Todo List</td>
<td align="center"><img src="assets/simple.apng" width="96"><br><b>很简单</b><br>It's Simple</td>
<td align="center"><img src="assets/bug.apng" width="96"><br><b>抓虫</b><br>Bug Hunt</td>
<td align="center"><img src="assets/loop.apng" width="96"><br><b>死循环</b><br>while(true)</td>
</tr>
<tr>
<td align="center"><img src="assets/deadline.apng" width="96"><br><b>赶工</b><br>Deadline</td>
<td colspan="3"></td>
</tr>
<tr>
<td>使用工具（2 个会话）</td>
<td align="center"><img src="assets/team2.apng" width="96"><br><b>两人组</b><br>Team of Two</td>
<td align="center"><img src="assets/conflict.apng" width="96"><br><b>合并冲突</b><br>Merge Conflict</td>
<td colspan="2">两人组里，两只小克并排工作：一只写代码，一只跑测试，测试失败时慌成一团。</td>
</tr>
<tr>
<td>使用工具（3 个及以上会话）</td>
<td align="center"><img src="assets/team3.apng" width="96"><br><b>三人组</b><br>Team of Three</td>
<td colspan="3">第三只小克站到屏幕上，边喝咖啡边看另外两只干活。</td>
</tr>
<tr>
<td>子代理运行中</td>
<td align="center"><img src="assets/subagents.apng" width="96"><br><b>子代理</b><br>Subagents</td>
<td colspan="3"></td>
</tr>
<tr>
<td>压缩上下文</td>
<td align="center"><img src="assets/compact.apng" width="96"><br><b>上下文压缩</b><br>/compact</td>
<td colspan="3"></td>
</tr>
<tr>
<td>创建 worktree</td>
<td align="center"><img src="assets/clone.apng" width="96"><br><b>克隆</b><br>git clone</td>
<td colspan="3"></td>
</tr>
<tr>
<td>权限请求或提醒</td>
<td align="center"><img src="assets/proceed.apng" width="96"><br><b>疯狂同意</b><br>Yes, Proceed</td>
<td colspan="3"></td>
</tr>
<tr>
<td>任务完成</td>
<td align="center"><img src="assets/passed_long.apng" width="96"><br><b>测试通过（加长版）</b><br>Tests Passed (extended)</td>
<td align="center"><img src="assets/lgtm.apng" width="96"><br><b>批准</b><br>LGTM</td>
<td colspan="2"></td>
</tr>
<tr>
<td>工具调用失败</td>
<td align="center"><img src="assets/error.apng" width="96"><br><b>报错</b><br>Error</td>
<td colspan="3"></td>
</tr>
</table>

### 待机

<table>
<tr><th>触发时机</th><th colspan="4">动画</th></tr>
<tr>
<td>没有活动</td>
<td align="center"><img src="assets/idle.svg" width="96"><br><b>待机</b><br>Idle</td>
<td colspan="3"></td>
</tr>
<tr>
<td>自由走动</td>
<td align="center"><img src="assets/roam.svg" width="96"><br><b>走动</b><br>Walk</td>
<td colspan="3"></td>
</tr>
<tr>
<td rowspan="4">空闲时随机播放</td>
<td align="center"><img src="assets/fish.apng" width="96"><br><b>摸鱼</b><br>Slacking Off</td>
<td align="center"><img src="assets/coffee.apng" width="96"><br><b>咖啡续命</b><br>Coffee Break</td>
<td align="center"><img src="assets/duck.apng" width="96"><br><b>小黄鸭调试</b><br>Rubber Duck</td>
<td align="center"><img src="assets/works.apng" width="96"><br><b>在我电脑上能跑</b><br>Works on My Machine</td>
</tr>
<tr>
<td align="center"><img src="assets/blame.apng" width="96"><br><b>甩锅</b><br>git blame</td>
<td align="center"><img src="assets/deploy.apng" width="96"><br><b>周五上线</b><br>Friday Deploy</td>
<td align="center"><img src="assets/overtime.apng" width="96"><br><b>加班</b><br>Overtime</td>
<td align="center"><img src="assets/offwork.apng" width="96"><br><b>下班</b><br>Clock Out</td>
</tr>
<tr>
<td align="center"><img src="assets/leak.apng" width="96"><br><b>内存泄漏</b><br>Memory Leak</td>
<td align="center"><img src="assets/overflow.apng" width="96"><br><b>栈溢出</b><br>Stack Overflow</td>
<td align="center"><img src="assets/cherry.apng" width="96"><br><b>摘樱桃</b><br>cherry-pick</td>
<td align="center"><img src="assets/esc.apng" width="96"><br><b>急停</b><br>Esc</td>
</tr>
<tr>
<td align="center"><img src="assets/forcepush.apng" width="96"><br><b>强推</b><br>Force Push</td>
<td align="center"><img src="assets/stash.apng" width="96"><br><b>藏起来</b><br>git stash</td>
<td align="center"><img src="assets/clear.apng" width="96"><br><b>清空上下文</b><br>/clear</td>
<td align="center"><img src="assets/bye_long.apng" width="96"><br><b>拜拜（加长版）</b><br>/exit (extended)</td>
</tr>
</table>

### 互动

<table>
<tr><th>触发时机</th><th colspan="4">动画</th></tr>
<tr>
<td>被拖拽</td>
<td align="center"><img src="assets/drag.svg" width="96"><br><b>拖拽</b><br>Drag</td>
<td colspan="3"></td>
</tr>
<tr>
<td>双击</td>
<td align="center"><img src="assets/hello.apng" width="96"><br><b>你好，世界</b><br>hello, world<br>点击左侧。</td>
<td align="center"><img src="assets/right.apng" width="96"><br><b>您说得对</b><br>You're Absolutely Right!<br>点击右侧。</td>
<td align="center"><img src="assets/notfound.apng" width="96"><br><b>找不到</b><br>404 Not Found<br>有一半概率触发。</td>
<td></td>
</tr>
<tr>
<td>快速连点四下</td>
<td align="center"><img src="assets/rmrf.apng" width="96"><br><b>删库</b><br>rm -rf</td>
<td align="center"><img src="assets/detached_long.apng" width="96"><br><b>头掉了（加长版）</b><br>detached HEAD (extended)</td>
<td align="center"><img src="assets/banned_long.apng" width="96"><br><b>封号（加长版）</b><br>Banned (extended)</td>
<td></td>
</tr>
<tr>
<td>鼠标绕着小克转圈</td>
<td align="center"><img src="assets/dizzy.apng" width="96"><br><b>晕眩</b><br>Dizzy</td>
<td colspan="3"></td>
</tr>
</table>

### 睡眠

<table>
<tr><th>触发时机</th><th colspan="4">动画</th></tr>
<tr>
<td>入睡</td>
<td align="center"><img src="assets/yawn.apng" width="96"><br><b>打哈欠</b><br>Yawn</td>
<td colspan="3"></td>
</tr>
<tr>
<td>睡着</td>
<td align="center"><img src="assets/sleep.apng" width="96"><br><b>晚安</b><br>Good Night</td>
<td colspan="3"></td>
</tr>
<tr>
<td>醒来</td>
<td align="center"><img src="assets/wake.apng" width="96"><br><b>醒来</b><br>Wake</td>
<td colspan="3"></td>
</tr>
</table>

## 许可

见 [LICENSE](LICENSE)。本主题是非官方粉丝作品，与 Anthropic 无关联，也未获得其背书。
