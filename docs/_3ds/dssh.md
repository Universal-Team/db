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
    size: 15297552
    size_str: 14 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.3.0/3dssh.3dsx
  DSSH.cia:
    size: 14701504
    size_str: 14 MiB
    url: https://github.com/Fishason/DSSH/releases/download/v1.3.0/DSSH.cia
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
stars: 89
systems:
- 3DS
title: DSSH
unique_ids:
- '0xFF55C'
update_notes: '<p dir="auto">DSSH 的第一个社区贡献版本 🎉 本次合并了 <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/hedykan/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/hedykan">@hedykan</a>
  和 <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/cadl/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cadl">@cadl</a>
  两位贡献者的全部功能 PR（<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="4802917222" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/5/hovercard"
  href="https://github.com/Fishason/DSSH/pull/5">#5</a>、<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4861310221" data-permission-text="Title
  is private" data-url="https://github.com/Fishason/DSSH/issues/6" data-hovercard-type="pull_request"
  data-hovercard-url="/Fishason/DSSH/pull/6/hovercard" href="https://github.com/Fishason/DSSH/pull/6">#6</a>、<a
  class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="4863407029"
  data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/7"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/7/hovercard"
  href="https://github.com/Fishason/DSSH/pull/7">#7</a>），感谢你们！</p>

  <h2 dir="auto">新功能</h2>

  <h3 dir="auto">SELECT 键断线重连（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4802917222" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/5/hovercard"
  href="https://github.com/Fishason/DSSH/pull/5">#5</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/hedykan/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/hedykan">@hedykan</a>）</h3>

  <p dir="auto">合盖休眠会冻结 TCP 导致 SSH 硬断开，以前只能退出重进。现在按 <strong>SELECT</strong> 即可原地重连、秒回原来的
  tmux 会话。</p>

  <h3 dir="auto">蟹蟹吉祥物 6 个新状态（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4802917222" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/5/hovercard"
  href="https://github.com/Fishason/DSSH/pull/5">#5</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/hedykan/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/hedykan">@hedykan</a>）</h3>

  <p dir="auto">重连中张望、成功欢呼、失败沮丧、录音、思考、打字——蟹蟹现在会跟着应用状态卖萌了。</p>

  <h3 dir="auto">语音打字机流式输出（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4802917222" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/5"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/5/hovercard"
  href="https://github.com/Fishason/DSSH/pull/5">#5</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/hedykan/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/hedykan">@hedykan</a>）</h3>

  <p dir="auto">语音转写文本改为逐字流式回传（延迟自适应），不再一次性整段 dump。</p>

  <h3 dir="auto">macOS Keychain 自动解锁（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4861310221" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/6"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/6/hovercard"
  href="https://github.com/Fishason/DSSH/pull/6">#6</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/cadl/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cadl">@cadl</a>）</h3>

  <p dir="auto">连接 macOS 时自动解锁登录 Keychain，Claude Code 可以直接复用已有登录凭据，不用每次重新 login。在
  <code class="notranslate">config.ini</code> 中配置：</p>

  <div class="highlight highlight-source-ini" dir="auto"><pre class="notranslate"><span
  class="pl-k">macos_keychain_password</span> = <span class="pl-s"><span class="pl-pds">"</span>你的
  macOS 登录密码<span class="pl-pds">"</span></span></pre></div>

  <p dir="auto"><g-emoji class="g-emoji" alias="warning">⚠️</g-emoji> 密码以明文保存在 SD
  卡上，默认关闭，请自行评估风险。</p>

  <h3 dir="auto">fish / Kitty 键盘协议渲染修复（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4861310221" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/6"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/6/hovercard"
  href="https://github.com/Fishason/DSSH/pull/6">#6</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/cadl/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cadl">@cadl</a>）</h3>

  <p dir="auto">修复了 fish 等 shell 下输入一直卡在屏幕第一行、内容错乱的问题；补充了终端查询响应和正确的初始 PTY 尺寸。</p>

  <h3 dir="auto">原生 Tailscale 支持（<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="4863407029" data-permission-text="Title is private" data-url="https://github.com/Fishason/DSSH/issues/7"
  data-hovercard-type="pull_request" data-hovercard-url="/Fishason/DSSH/pull/7/hovercard"
  href="https://github.com/Fishason/DSSH/pull/7">#7</a>，by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/cadl/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cadl">@cadl</a>）</h3>

  <p dir="auto">3DS 可以直接加入你的 tailnet，通过 Tailscale IPv4 或 MagicDNS 名称连接 SSH。传输层由 <a
  href="https://github.com/cadl/libts3ds">libts3ds</a> 提供（实验性）。在 <code class="notranslate">config.ini</code>
  中配置 <code class="notranslate">tailscale_auth_key</code> 即可启用。</p>

  <h2 dir="auto">安装</h2>

  <ul dir="auto">

  <li><code class="notranslate">.3dsx</code>：放到 SD 卡 <code class="notranslate">/3ds/</code>
  目录，用 Homebrew Launcher 启动</li>

  <li><code class="notranslate">DSSH.cia</code>：用 FBI 安装</li>

  <li>私钥仍需 <code class="notranslate">ssh-keygen -m PEM</code> 格式（mbedtls 2.28 限制）</li>

  </ul>

  <h2 dir="auto">致谢</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/hedykan/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/hedykan">@hedykan</a>
  — SELECT 重连、吉祥物状态、语音打字机</li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/cadl/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cadl">@cadl</a>
  — Keychain 解锁、fish 渲染修复、Tailscale 支持及 libts3ds</li>

  </ul>

  <p dir="auto">两位的功能均经过各自真机验证；合并后的组合构建通过了全部主机端回归测试（config / terminal / IME）。</p>'
updated: '2026-08-13T10:38:08Z'
version: v1.3.0
version_title: DSSH v1.3 — 社区贡献版：重连 / Keychain / Tailscale
---
