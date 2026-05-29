---
author: Fish
avatar: https://avatars.githubusercontent.com/u/147747767?v=4
categories:
- app
- utility
color: '#f8e3c6'
color_bg: '#807566'
created: '2026-05-01T05:16:15Z'
description: Nintendo 3DS SSH client with on-screen pinyin IME, RSA auth, citro2d
  ANSI terminal, and a crab
download_filter: (cia|3dsx)
download_page: https://github.com/Fishason/DSSH/releases
downloads:
  3dssh.3dsx:
    size: 14920704
    size_str: 14 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.1.0/3dssh.3dsx
  DSSH.cia:
    size: 14468032
    size_str: 13 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.1.0/DSSH.cia
github: Fishason/DSSH
icon: https://raw.githubusercontent.com/Fishason/DSSH/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/Fishason/DSSH/refs/heads/main/icon.png
image_length: 1188
layout: app
license: other
license_name: Other
llm_usage: undisclosed
qr:
  DSSH.cia: https://db.universal-team.net/assets/images/qr/dssh-cia.png
source: https://github.com/Fishason/DSSH
stars: 38
systems:
- 3DS
title: DSSH
update_notes: "<p dir=\"auto\">v1.0 把语音输入做完了；v1.1 加了一条<strong>与 SSH 平行的语音 AI 问答通道</strong>——按住\
  \ <strong>L+START</strong> 说一句问题，底屏弹出问答 modal，DeepSeek 答案直接出现，<strong>不打扰</strong>顶屏正在跑的\
  \ yazi / vim / tmux / claude-code。</p>\n<hr>\n<h2 dir=\"auto\">\U0001F3A4 → \U0001F916\
  \ Voice AI ask（v1.1 新增）</h2>\n<pre class=\"notranslate\"><code class=\"notranslate\"\
  >[L + START] 录音 32 秒上限\n   │\n   ▼ 16 kHz PCM → 服务器 shim --ask\n[Whisper Turbo]\
  \ 转写\n   │\n   ▼ 转出来的中文 → DeepSeek-Chat（带 history）\n[DeepSeek] 回答（6-15 句，markdown）\n\
  \   │\n   ▼ JSON 返回 3DS\n[底屏 modal 0.5s 淡入]\n   │\n   ├─ A 关闭 + 保留 history（追问）\n\
  \   └─ B / 触屏 关闭 + 清空 history（新对话）\n</code></pre>\n<h3 dir=\"auto\">用户体验：</h3>\n\
  <ul dir=\"auto\">\n<li><strong>顶屏 SSH 完全不动</strong>——问 AI 不打断 yazi / vim 状态</li>\n\
  <li><strong>Markdown 渲染</strong>：<code class=\"notranslate\"># 标题</code> 黄色、<code\
  \ class=\"notranslate\">`code`</code> 青色、<code class=\"notranslate\">- 列表</code>\
  \ → <code class=\"notranslate\">• 列表</code>、<code class=\"notranslate\">**bold**</code>\
  \ 隐式 strip 不丢内容</li>\n<li><strong>History 追问</strong>：A 关 modal 时保留当前 Q&amp;A，下次\
  \ L+START 接续；B 重置开新对话；上限 5 轮 FIFO</li>\n<li><strong>录音上限从 8 秒升到 32 秒</strong>——多句话问题也塞得下</li>\n\
  <li><strong>触发手势</strong>：L+START（区别于普通 START 的语音 IME）</li>\n</ul>\n<h3 dir=\"auto\"\
  >服务器端配置——还是一条命令</h3>\n<p dir=\"auto\">需要<strong>两把 API key</strong>（OpenRouter +\
  \ DeepSeek，均有免费额度）：</p>\n<div class=\"highlight highlight-source-shell\" dir=\"\
  auto\"><pre class=\"notranslate\">git clone https://github.com/Fishason/DSSH.git\
  \ <span class=\"pl-k\">~</span>/dssh-repo\nbash <span class=\"pl-k\">~</span>/dssh-repo/tools/install_whisper_api.sh\n\
  <span class=\"pl-c\"><span class=\"pl-c\">#</span> ↑ 交互式提示输入两把 key</span></pre></div>\n\
  <p dir=\"auto\">或者非交互式：</p>\n<div class=\"highlight highlight-source-shell\" dir=\"\
  auto\"><pre class=\"notranslate\">OPENROUTER_API_KEY=<span class=\"pl-s\"><span\
  \ class=\"pl-pds\">\"</span>sk-or-v1-...<span class=\"pl-pds\">\"</span></span>\
  \ \\\nDEEPSEEK_API_KEY=<span class=\"pl-s\"><span class=\"pl-pds\">\"</span>sk-...<span\
  \ class=\"pl-pds\">\"</span></span> \\\nbash <span class=\"pl-k\">~</span>/dssh-repo/tools/install_whisper_api.sh</pre></div>\n\
  <markdown-accessiblity-table><table role=\"table\">\n<thead>\n<tr>\n<th>Key</th>\n\
  <th>申请地址</th>\n<th>用途</th>\n<th>必需性</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td><strong>OpenRouter</strong></td>\n\
  <td><a href=\"https://openrouter.ai/settings/keys\" rel=\"nofollow\">openrouter.ai/settings/keys</a></td>\n\
  <td>Whisper Turbo（语音→文字）</td>\n<td><strong>必需</strong></td>\n</tr>\n<tr>\n<td><strong>DeepSeek</strong></td>\n\
  <td><a href=\"https://platform.deepseek.com/api_keys\" rel=\"nofollow\">platform.deepseek.com/api_keys</a></td>\n\
  <td>DeepSeek-Chat（AI 回答）</td>\n<td>L+START 必需，纯语音 IME 不需要</td>\n</tr>\n</tbody>\n\
  </table></markdown-accessiblity-table>\n<p dir=\"auto\">费用：Whisper Turbo `$0.04/音频小时`\
  \ + DeepSeek `~$0.0001/次问答`，个人用月成本几美分。</p>\n<p dir=\"auto\">详细安装文档见 <a href=\"https://github.com/Fishason/DSSH/blob/main/README.zh.md#%E8%AF%AD%E9%9F%B3%E8%BE%93%E5%85%A5\"\
  >README — 语音输入</a>。</p>\n<hr>\n<h2 dir=\"auto\">\U0001F6E0 其它改动（自 v1.0）</h2>\n<ul\
  \ dir=\"auto\">\n<li><strong>modal 渲染 z-order 修复</strong>：之前 `renderer_draw_text_px`\
  \ 内部硬编码 z=0.5，比 modal bg z=0.51 低，文字被背景覆盖看不见。新增 `renderer_draw_text_px_z(x, y, z,\
  \ text, rgba)` API 让 modal 用 z=0.62 画文字稳压 bg</li>\n<li><strong>Aux channel drain\
  \ loop</strong>：voice.c phase 2 改成单帧内 drain 完所有 readable bytes 再判 EOF，避免分包到达时 EOF\
  \ 早判导致 JSON 截断</li>\n<li><strong>shim --ask 模式</strong>：每条 error path 都走兜底 JSON\
  \ 输出，3DS 永不收到完全空 reply</li>\n<li><strong>诊断日志</strong>：`/tmp/dssh-ai-debug.log`\
  \ 记录每次 L+START 的 PCM 长度 / 转写文本 / DeepSeek 回答 / 输出 JSON，调试一目了然</li>\n</ul>\n<h2 dir=\"\
  auto\">\U0001F4E6 安装</h2>\n<markdown-accessiblity-table><table role=\"table\">\n\
  <thead>\n<tr>\n<th>想要的</th>\n<th>下载</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>Homebrew\
  \ Launcher 启动</td>\n<td><a href=\"https://github.com/Fishason/DSSH/releases/latest/download/3dssh.3dsx\"\
  >`3dssh.3dsx`</a></td>\n</tr>\n<tr>\n<td>HOME 菜单图标启动（推荐）</td>\n<td><a href=\"https://github.com/Fishason/DSSH/releases/latest/download/DSSH.cia\"\
  >`DSSH.cia`</a></td>\n</tr>\n<tr>\n<td>v1.0 拼音 IME 演示视频（v1.1 兼容）</td>\n<td><a href=\"\
  https://github.com/Fishason/DSSH/releases/latest/download/demo.mp4\">`demo.mp4`</a></td>\n\
  </tr>\n</tbody>\n</table></markdown-accessiblity-table>\n<h2 dir=\"auto\">\U0001F504\
  \ 从 v1.0 升级</h2>\n<p dir=\"auto\">3DS 端：直接用新 `.cia` 覆盖。</p>\n<p dir=\"auto\">服务器端：</p>\n\
  <p dir=\"auto\">```bash<br>\ncd ~/dssh-repo &amp;&amp; git pull<br>\nbash tools/install_whisper_api.sh</p>\n\
  <h1 dir=\"auto\">已有 OpenRouter key 不会再问；新提示输入 DeepSeek key</h1>\n<p dir=\"auto\"\
  >```</p>\n<p dir=\"auto\">旧的纯语音 IME 仍然可用，只是 L+START 多了一个 AI 问答路径。如果不想用，跳过 DeepSeek\
  \ key 就行——L+START 会优雅 fail（modal 显示 \"no API key\" 错误）。</p>\n<h2 dir=\"auto\">\U0001F41B\
  \ 已知边界</h2>\n<ul dir=\"auto\">\n<li>modal 答案区约 14 行 × 50 字符；超长答案末尾自动 `...` 截断</li>\n\
  <li>`<strong>bold</strong>` 在 6×12 像素字体下没法做加粗效果——syntax 隐去、内容仍显示，但<strong>没有视觉强调</strong></li>\n\
  </ul>"
updated: '2026-05-07T11:00:19Z'
version: v1.1.0
version_title: DSSH v1.1 — 语音问 AI（L+START）
---
