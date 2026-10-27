# 01 · dev-life · 克码人生

程序员日常主题 · 20 个动态表情，Clawd 主演。规矩沿用 [Qisi3344/clawd-moji](https://github.com/Qisi3344/clawd-moji) 的 01-movie-night：眼睛是两个小黑方块（偶尔眯成 ^ ^ 或 > <），不画嘴，戏全靠动作和道具。

![preview](preview.png)

| # | 名字 | 动图 | 小剧情 |
|---|---|---|---|
| 1 | 思克中 Thinking | <img src="gif/thinking.gif" width="120"> | 头顶转着 Claude Code 的 ✻ 小星星，点点点一个个冒出来，歪头托腮 |
| 2 | 上下文压克 /compact | <img src="gif/compact.gif" width="120"> | 一块写着 /compact 的铁板压下来，> < 压成一张饼，弹回来 ^ ^，然后头顶冒出一个「？」——忘了刚才在干嘛 |
| 3 | 克隆 git clone | <img src="gif/clone.gif" width="120"> | 敲下 git clone，憋气发抖，噗一下分出两个小克，三只轮流蹦，再合回一只 |
| 4 | 合并冲克 Merge Conflict | <img src="gif/conflict.gif" width="120"> | `<<<<<<<` 和 `>>>>>>>` 两只小克顶着脑袋互推冒火花，弹开，互相瞪 |
| 5 | rm -rf 克 | <img src="gif/rmrf.gif" width="120"> | 一个字一个字敲完 rm -rf /，回车，自己从脚开始被删光，只剩一双眼睛，然后从终端里重新掉出来 |
| 6 | hello, 克 | <img src="gif/hello.gif" width="120"> | 一边打出 hello, world 一边 ^ ^ 挥手——打招呼专用 |
| 7 | LGTM 克 | <img src="gif/lgtm.gif" width="120"> | 双手举起印章，啪地盖下一个歪歪的红色 LGTM——同意 / 收到 / 没问题 |
| 8 | 测试通克 | <img src="gif/passed.gif" width="120"> | 紧张盯着，一个绿色大对勾画出来，彩纸落下，蹦蹦跳 |
| 9 | 报克 Error | <img src="gif/error.gif" width="120"> | 头顶红色 Error 闪烁，抱头 > <，然后四脚朝天翻过去，腿乱蹬、头上冒星星，再翻回来 |
| 10 | 续克 | <img src="gif/coffee.gif" width="120"> | 困得眯眼晃，端起蓝色马克杯一口闷，眼睛瞬间瞪大，满血复活 |
| 11 | 周五上克 | <img src="gif/deploy.gif" width="120"> | 头顶写着 friday deploy，捧三炷香闭眼连拜三下，烟袅袅 |
| 12 | 在我电脑上能跑 | <img src="gif/works.gif" width="120"> | 抱着自己的笔记本耸肩 ^ ^，works on my machine，抱着电脑冒爱心 |
| 13 | 抓克 Bug | <img src="gif/bug.gif" width="120"> | 眼睛跟着一只小虫，起跳一屁股坐下去，得意——结果虫从另一边溜走了 > < |
| 14 | 摸克鱼 | <img src="gif/fish.gif" width="120"> | 怀里抱着一条蓝色小鱼慢慢摸，鱼尾巴摇，冒小爱心 |
| 15 | 下克班 | <img src="gif/offwork.gif" width="120"> | 盯着时钟 17:59 → 18:00，一个蹲起冲出画面，只剩烟尘；然后时间又倒回 17:59，蔫蔫地走回来 |
| 16 | 加克班 | <img src="gif/overtime.gif" width="120"> | 深夜 02:00，月亮星星，趴在桌前打瞌睡往下沉，一个激灵惊醒，又慢慢闭眼 |
| 17 | 晚克 | <img src="gif/sleep.gif" width="120"> | 戴蓝色睡帽闭眼呼吸，一串 z 慢慢飘上去——晚安专用 |
| 18 | 404 克不到 | <img src="gif/notfound.gif" width="120"> | 写着 404 的纸箱里冒出半个脑袋左右张望，发现被看到了，嗖地缩回去，留下一个「？」 |
| 19 | 死循克 while(true) | <img src="gif/loop.gif" width="120"> | 在仓鼠轮里狂奔，跑着跑着眼睛变成 > <，汗都甩飞了 |
| 20 | 强克 git push --force | <img src="gif/forcepush.gif" width="120"> | 顶着写着 main 的大方块使劲推，咻地推飞，^ ^ 欢呼——然后方块又被推回来把它挤走 |

## 下载 / 在微信里用

- `gif/`：原尺寸 276×288，透明背景
- `wechat/`：240×240、每张 ≤100KB，透明背景（个别帧数多的做了抽帧）

想在微信里用：把 `wechat/` 里的 GIF 发到「文件传输助手」，点开长按 →「添加到表情」就好啦。

## 自己生成

```bash
cd src
pip install pillow
python clawd_dev.py            # 全部 20 个
python clawd_dev.py compact    # 只生成一个
```

不需要额外字体，命令行文字用的是代码里自带的 3×5 小像素字。

## 致谢

思路和画法来自 [@Qisi3344](https://github.com/Qisi3344) 的 [clawd-moji](https://github.com/Qisi3344/clawd-moji)，`src/clawd_dev.py` 里的绘图工具函数改编自原作的生成代码。
