---
author: Wheat
avatar: https://avatars.githubusercontent.com/u/102208097?v=4
categories:
- utility
color: '#0fb740'
color_bg: '#0a802d'
created: '2026-08-26T02:16:26Z'
description: '任天堂 3DS 第三方电子邮件 homebrew 客户端：多账户、IMAP 收件、中文邮件解码、SD 卡本地缓存，非官方项目。 \n  A
  third-party email homebrew client for the hacked Nintendo 3DS: multi-account, IMAP,
  Chinese mail decoding & SD-card cache. Unofficial.'
download_page: https://github.com/BladeWheat/Mail3DS/releases
downloads:
  Mail3DS.3dsx:
    size: 24165792
    size_str: 23 MiB
    url: https://github.com/BladeWheat/Mail3DS/releases/download/v1.1.0/Mail3DS.3dsx
  Mail3DS.cia:
    size: 23966656
    size_str: 22 MiB
    url: https://github.com/BladeWheat/Mail3DS/releases/download/v1.1.0/Mail3DS.cia
github: BladeWheat/Mail3DS
icon: https://raw.githubusercontent.com/BladeWheat/Mail3DS/master/icon.png
image: https://raw.githubusercontent.com/BladeWheat/Mail3DS/master/cia_build/banner_256x128.png
image_length: 14454
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  Mail3DS.cia: https://db.universal-team.net/assets/images/qr/mail3ds-cia.png
source: https://github.com/BladeWheat/Mail3DS
stars: 2
systems:
- 3DS
title: Mail3DS
unique_ids:
- '0x3A170'
update_notes: '<h2 dir="auto">Mail3DS v1.1.0</h2>

  <p dir="auto">本次更新主要修复长邮件显示问题与若干操作体验问题。</p>

  <h3 dir="auto">🐛 问题修复</h3>

  <ul dir="auto">

  <li><strong>修复长邮件正文内容缺失</strong>：旧版正文自动换行按字节处理，会把一个汉字（UTF-8 占 3 字节）从中间切断或直接丢字，导致长邮件段落残缺、内容不完整。现改为按完整汉字逐字换行（英文按单词换行），任何文字都不会丢失，长邮件可完整阅读。</li>

  <li><strong>修复 HTML 邮件换行偶发乱码</strong>：HTML 正文的自动换行同样改为汉字安全，不再把多字节字符切坏。</li>

  <li><strong>修复邮件列表标题末尾出现问号</strong>：标题/发件人/预览过长被截断时，可能把汉字切成半截显示成“???”，现改为按完整字符截断并补省略号“…”。</li>

  </ul>

  <h3 dir="auto">⚡ 优化</h3>

  <ul dir="auto">

  <li><strong>左摇杆与十字键逻辑完全统一</strong>：列表、菜单、正文阅读中，摇杆上下左右的行为与十字键完全一致；正文阅读时按一下滚动 3 行，不再出现摇杆单独平滑滚动、重复滚动的问题。</li>

  <li>正文最大排版行数提升至 1500 行，可完整显示数万字的超长邮件。</li>

  </ul>

  <h3 dir="auto">ℹ️ 其他</h3>

  <ul dir="auto">

  <li>“设置 → 关于”版本号更新为 v1.1.0。</li>

  </ul>'
updated: '2026-08-26T17:42:11Z'
version: v1.1.0
version_title: v1.1.0
---
