---
author: Strrationalism Studio
avatar: https://avatars.githubusercontent.com/u/36921849?v=4
categories:
- emulator
color: '#c1b295'
color_bg: '#807662'
created: '2021-12-07T16:15:06Z'
description: PyMO AVG Game Engine implemention in C.
download_page: https://github.com/Strrationalism/CPyMO/releases
downloads:
  CPyMO.for.Linux.x64.zip:
    size: 8297228
    size_str: 7 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Linux.x64.zip
  CPyMO.for.Nintendo.3DS.3dsx:
    size: 15191248
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11301824
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Nintendo.3DS.cia
  CPyMO.for.Universal.Windows.Platform.zip:
    size: 26043356
    size_str: 24 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Universal.Windows.Platform.zip
  CPyMO.for.Windows.ARM.zip:
    size: 6148080
    size_str: 5 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Windows.ARM.zip
  CPyMO.for.Windows.ARM64.zip:
    size: 6509992
    size_str: 6 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Windows.ARM64.zip
  CPyMO.for.Windows.x64.zip:
    size: 7525584
    size_str: 7 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Windows.x64.zip
  CPyMO.for.Windows.x86.zip:
    size: 6516292
    size_str: 6 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.Windows.x86.zip
  CPyMO.for.macOS.Apple.Silicon.zip:
    size: 7347060
    size_str: 7 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.macOS.Apple.Silicon.zip
  CPyMO.for.macOS.x64.zip:
    size: 8389890
    size_str: 8 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/CPyMO.for.macOS.x64.zip
  libpymo.ykm:
    size: 10306
    size_str: 10 KiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/libpymo.ykm
  mo2pymo.ps1:
    size: 67012
    size_str: 65 KiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/mo2pymo.ps1
  pymo-convert-audio-to-ogg.ps1:
    size: 3418
    size_str: 3 KiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/pymo-convert-audio-to-ogg.ps1
  pymo-converter.ps1:
    size: 7690
    size_str: 7 KiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/pymo-converter.ps1
  pymo2ykm.ps1:
    size: 39574
    size_str: 38 KiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.7/pymo2ykm.ps1
github: Strrationalism/CPyMO
icon: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/icon.png
icon_index: 202
image: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/banner.png
image_length: 30736
layout: app
license: agpl-3.0
license_name: GNU Affero General Public License v3.0
qr:
  CPyMO.for.Nintendo.3DS.cia: https://db.universal-team.net/assets/images/qr/cpymo-for-nintendo-3ds-cia.png
source: https://github.com/Strrationalism/CPyMO
systems:
- 3DS
title: CPyMO
update_notes: '<h1 dir="auto">改进</h1>

  <ul dir="auto">

  <li>Emscripten现在可以使用FFmpeg播放音视频，并升到第二梯队</li>

  <li>Android现在可以使用FFmpeg播放音视频，并升到第二梯队</li>

  <li>Android最低版本要求从4.1提升到4.3</li>

  <li>Android上隐藏了状态栏</li>

  <li>Bug fixed: 桌面版不能正确加载3通道的icon.png问题</li>

  <li>Bug fixed: pymo-converter在PATH目录中工作时不能正常运行的问题</li>

  <li>Bug fixed: 当引擎启动失败时将不会创建save文件夹</li>

  <li>3DS版C摇杆死区扩大</li>

  <li>移动函数<code class="notranslate">cpymo_backend_text_render</code>到<code class="notranslate">cpymo_backend_font_render</code></li>

  <li>Bug fixed: 某些游戏正常退出时会产生<code class="notranslate">NO_MORE_CONTENT</code>错误输出</li>

  <li>PSV现在使用FFmpeg作为音视频后端，并且使用vpk安装包</li>

  <li>快进时不会播放非循环音效和语音以提升快进性能</li>

  <li>SDL2后端在脚本引起的崩溃中将会弹出错误对话框</li>

  <li>设置了全局存档的dirty检测，减少不必要的写入</li>

  <li>Bug fixed: SDL2后端播放视频改为适配屏幕而非拉伸</li>

  <li>PSP禁用语音通道以降低内存占用</li>

  <li>移动动画采用缓动曲线</li>

  </ul>

  <h1 dir="auto">工具</h1>

  <ul dir="auto">

  <li>增加<code class="notranslate">convert-audio-to-ogg</code>工具用于将游戏音频转换为ogg</li>

  <li>现在可以通过nmake和GNU Make来构建CPyMO和cpymo-tool</li>

  <li>pymo-converter现在可以转换音视频</li>

  <li>cpymo-tool现在可以将一组图片打包为单张图片用于<code class="notranslate">select_img</code>等命令</li>

  </ul>

  <h1 dir="auto">构建过程</h1>

  <ul dir="auto">

  <li>现在3DS和PSV平台的FFmpeg将会构建并安装到仓库内，不会污染开发环境</li>

  <li>不使用CMake的用户现在可以在Windows下使用nmake来构建cpymo和cpymo-tool</li>

  </ul>'
updated: '2022-05-07T07:24:22Z'
version: v1.0.7
version_title: CPyMO 1.0.7
---
