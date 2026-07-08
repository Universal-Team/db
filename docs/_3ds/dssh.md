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
    size: 14920776
    size_str: 14 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.2.0/3dssh.3dsx
  DSSH.cia:
    size: 14468032
    size_str: 13 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.2.0/DSSH.cia
github: Fishason/DSSH
icon: https://raw.githubusercontent.com/Fishason/DSSH/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/Fishason/DSSH/refs/heads/main/icon.png
image_length: 1188
layout: app
license: other
license_name: Other
llm_generation: 'yes'
qr:
  DSSH.cia: https://db.universal-team.net/assets/images/qr/dssh-cia.png
source: https://github.com/Fishason/DSSH
stars: 52
systems:
- 3DS
title: DSSH
unique_ids:
- '0xFF55C'
update_notes: '<p dir="auto">两个小但都很有用的改动：终端 Shift+Tab 在软键盘上能打出来了，语音识别从 Whisper 换到
  Qwen3-ASR-Flash 解决稳定性 + 中文标点更地道。</p>

  <hr>

  <h2 dir="auto">⇥ Shift+Tab on the soft keyboard</h2>

  <p dir="auto">按住物理 <strong>L</strong>（Shift）同时点软键盘 <strong>tab</strong> → 输出 <code
  class="notranslate">\x1b[Z</code>（CSI Z，terminal 标准的"光标后退一个 tab"）。普通点 tab 仍然是 <code
  class="notranslate">\t</code> 不变。</p>

  <p dir="auto">实用场景：</p>

  <ul dir="auto">

  <li><strong>vim/zsh 补全候选反向走</strong>：补全菜单里前一项</li>

  <li><strong>tmux Ctrl-B q 后窗口编号反向切</strong></li>

  <li><strong>lazyvim 的部分 plugin</strong> 用 Shift+Tab 退出嵌套菜单</li>

  </ul>

  <p dir="auto">修改面：<code class="notranslate">source/softkb.c</code> 的 KIND_SEQ dispatch
  加 4 行——只对 <code class="notranslate">\t</code> 特判，其他 KIND_SEQ binding 不受影响。</p>

  <h2 dir="auto">🎙️ ASR 从 Whisper → Qwen3-ASR-Flash</h2>

  <p dir="auto"><code class="notranslate">OPENROUTER_AUDIO_MODEL</code> 常量从 <code
  class="notranslate">openai/whisper-large-v3-turbo</code> 切到 <strong><code class="notranslate">qwen/qwen3-asr-flash-2026-02-10</code></strong>。</p>

  <h3 dir="auto">为什么换：</h3>

  <ul dir="auto">

  <li><strong>稳定性</strong>：OpenRouter 的 Whisper Turbo provider 偶尔对某些 IP 段限速 / 阻断，同一段音频走
  Qwen 始终成功</li>

  <li><strong>中文标点更地道</strong>：

  <ul dir="auto">

  <li>Whisper：<code class="notranslate">你好世界,今天天气不错</code></li>

  <li>Qwen3：<code class="notranslate">你好，世界。今天天气不错。</code></li>

  </ul>

  </li>

  <li><strong>没有协议改动</strong>：OpenRouter 的 <code class="notranslate">/v1/audio/transcriptions</code>
  endpoint 对 Whisper 和 Qwen3 用<strong>完全相同</strong>的 JSON 请求 / 响应格式——服务器端 shim 改一个常量就完事，3DS
  端代码 0 修改</li>

  </ul>

  <h3 dir="auto">代价：</h3>

  <ul dir="auto">

  <li>单价从 ~$0.067/音频小时 → ~$0.13/音频小时（约 2 倍）。个人用一个月仍是几美分级别，可忽略</li>

  </ul>

  <h3 dir="auto">升级方式：</h3>

  <p dir="auto">OpenRouter API key 不变（同一把 key 同时能调 Whisper 和 Qwen）。重跑 install 脚本或者手动
  `git pull` 即可：</p>

  <div class="highlight highlight-source-shell" dir="auto"><pre class="notranslate"><span
  class="pl-c1">cd</span> <span class="pl-k">~</span>/dssh-repo <span class="pl-k">&amp;&amp;</span>
  git pull

  bash tools/install_whisper_api.sh   <span class="pl-c"><span class="pl-c">#</span>
  已有 key 不会再问，只刷新 shim</span></pre></div>

  <hr>

  <h2 dir="auto">📦 安装 / 升级</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>想要的</th>

  <th>下载</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td>Homebrew Launcher 启动</td>

  <td><a href="https://github.com/Fishason/DSSH/releases/latest/download/3dssh.3dsx">`3dssh.3dsx`</a></td>

  </tr>

  <tr>

  <td>HOME 菜单图标启动（推荐）</td>

  <td><a href="https://github.com/Fishason/DSSH/releases/latest/download/DSSH.cia">`DSSH.cia`</a></td>

  </tr>

  <tr>

  <td>完整 1m42s 演示视频（v1.0 拼音 IME 录的，v1.2 兼容）</td>

  <td><a href="https://github.com/Fishason/DSSH/releases/latest/download/demo.mp4">`demo.mp4`</a></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <h3 dir="auto">从 v1.1 升级</h3>

  <ul dir="auto">

  <li><strong>3DS</strong>：装新 `.cia` 即可（覆盖安装）。Shift+Tab 立刻生效</li>

  <li><strong>服务器</strong>：`cd ~/dssh-repo &amp;&amp; git pull &amp;&amp; bash tools/install_whisper_api.sh`——shim
  会刷新成 Qwen3 版本。下次按 START 自动用新模型</li>

  </ul>

  <h3 dir="auto">新用户从零安装</h3>

  <p dir="auto">按 README 的<a href="https://github.com/Fishason/DSSH/blob/main/README.zh.md#%E8%AF%AD%E9%9F%B3%E8%BE%93%E5%85%A5">语音输入章节</a>走
  OpenRouter + DeepSeek 两把 key 的一键安装，全套服务器端 ~30 KB、~1 分钟搞定。</p>'
updated: '2026-05-31T03:11:50Z'
version: v1.2.0
version_title: DSSH v1.2 — Shift+Tab + Qwen3 ASR Flash
---
