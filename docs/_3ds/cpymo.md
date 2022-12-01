---
author: Strrationalism Studio
avatar: https://avatars.githubusercontent.com/u/36921849?v=4
categories:
- emulator
color: '#c1b295'
color_bg: '#807662'
created: '2021-12-07T16:15:06Z'
description: PyMO AVG Game Engine implemention in C.
download_filter: (\.3dsx|\.cia)
download_page: https://github.com/Strrationalism/CPyMO/releases
downloads:
  CPyMO.for.Nintendo.3DS.3dsx:
    size: 15238800
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.2/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11375552
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.2/CPyMO.for.Nintendo.3DS.cia
github: Strrationalism/CPyMO
icon: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/icon.png
image: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/banner.png
image_length: 28367
layout: app
license: agpl-3.0
license_name: GNU Affero General Public License v3.0
qr:
  CPyMO.for.Nintendo.3DS.cia: https://db.universal-team.net/assets/images/qr/cpymo-for-nintendo-3ds-cia.png
source: https://github.com/Strrationalism/CPyMO
systems:
- 3DS
title: CPyMO
unique_ids:
- '0xF3098'
update_notes: '<h1 dir="auto">新功能</h1>

  <ul dir="auto">

  <li><strong>支持iOS。</strong></li>

  <li>现在允许仅跳过已读部分，可以在游戏设置中开关此功能。</li>

  <li>已读内容变暗。</li>

  <li>增加<code class="notranslate">software</code>后端用于在脱离硬件和系统API的情况下进行软件渲染，将输出RGB帧缓冲。</li>

  <li>CPyMO ASCII Art现在支持rule图淡化过场。</li>

  <li>SDL2后端可以通过<code class="notranslate">DISABLE_VSYNC</code>宏关闭垂直同步以提升快进速度。</li>

  </ul>

  <h1 dir="auto">PyMO行为一致性</h1>

  <ul dir="auto">

  <li>现在say命令将会取消fade_out状态。</li>

  <li>goto和if goto失败时不会崩溃，而是继续执行。</li>

  <li>change不应该破坏调用栈。</li>

  </ul>

  <h1 dir="auto">Bug修正</h1>

  <ul dir="auto">

  <li>历史记录中<code class="notranslate">max_lines</code>字段没有进行初始化。</li>

  <li>已修正Win32与UWP平台下鼠标和触屏混合操作时List UI不灵敏的问题。</li>

  <li>修复List UI上可能崩溃的问题。</li>

  <li>加载带mask图像失败时可能会导致双重free。</li>

  </ul>

  <h1 dir="auto">体验改进</h1>

  <ul dir="auto">

  <li>桌面版CPyMO在使用时若游戏窗口大小超过屏幕大小，则直接创建最大化窗口，并且挑选一个合适的窗口大小。</li>

  <li>SDL2后端新增Menu键支持。</li>

  <li>支持在SDL 2.0.18及以上版本响应高精度触摸板的平滑滚动。</li>

  <li>支持在SDL2、SDL1后端上当用户即将关闭窗口时询问是否确定关闭。</li>

  <li>优化触屏长按操作手感，现在不再需要松开才能响应。</li>

  <li>CPyMO ASCII Art在Windows上的输出效率得到大幅优化，现在GitHub Action上提供Windows版CPyMO ASCII Art的二进制文件。</li>

  <li>rule图淡化方向现在与ONScripter一致。</li>

  <li>滚动列表要在页面还满的时候就停止滚动，而不是滚动到只有一行。</li>

  </ul>

  <h1 dir="auto">优化</h1>

  <ul dir="auto">

  <li>当使用call命令时，若该脚本已经被加载于其他的解释器，则直接调用其他解释器的脚本，而不是重新加载。</li>

  <li>使用<code class="notranslate">stb_ds</code>优化<code class="notranslate">cpymo_hash_flags</code>和<code
  class="notranslate">cpymo_vars</code>。</li>

  <li>使用柔性数组优化<code class="notranslate">cpymo_chara</code>。</li>

  <li>从<code class="notranslate">cpymo_interpreter</code>中拆分出<code class="notranslate">cpymo_script</code>。</li>

  <li><code class="notranslate">cpymo_parser_stream_span</code>改名为<code class="notranslate">cpymo_str</code>。</li>

  <li>backlog功能的存储被移动到了堆上以减少静态存储区占用过大导致的崩溃问题。</li>

  <li>使用<code class="notranslate">stb_leakcheck</code>进行内存泄漏检查。</li>

  <li>在<code class="notranslate">text</code>后端上禁用了图像加载功能以减少内存占用。</li>

  </ul>'
updated: '2022-09-26T16:55:33Z'
version: v1.1.2
version_title: CPyMO v1.1.2
wiki: https://github.com/Strrationalism/CPyMO/wiki
---
