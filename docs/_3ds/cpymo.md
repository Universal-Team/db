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
    size: 15224140
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.0/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11367360
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.0/CPyMO.for.Nintendo.3DS.cia
github: Strrationalism/CPyMO
icon: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/icon.png
icon_index: 203
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

  <li>解决了O3DS上cia版本不能启动的问题。</li>

  <li>PSP上采用16位色帧缓存。</li>

  <li>在Wii和PSP上流式加载图片。</li>

  <li>优化Wii体验。</li>

  <li>Wii上可以按需刷新了。</li>

  <li>Wii上现在支持音频播放。</li>

  <li>SDL1后端上将会在srcrect和dstrect中绘制区域大小不同时进行居中处理。</li>

  <li>SDL1后端现在可以自由选择字体渲染质量更偏向质量还是性能。</li>

  <li>SDL2后端现在可以修改帧缓存格式。</li>

  <li>移动了自动存档的发生时机，使其看起来更加流畅。</li>

  <li>移除了多余的刷新。</li>

  <li>已修复当使用CR换行符时CPyMO出现的未定义行为。</li>

  <li>已修复gameconfig.txt中gametitle为空时的未定义行为。</li>

  <li>定义<code class="notranslate">DISABLE_IMAGE_SCALING</code>宏即可阻止图片组件的缩放行为。</li>

  <li>重启CPyMO游戏的时候不会再打印cpymo的logo。</li>

  <li>将会尝试在包中查找长度超过31的长文件名。</li>

  <li>由小涂增加的适用于Android平台的TTS音频视障帮助。</li>

  <li>视障帮助中，退出backlog时不会阅读当前文本的问题已经解决。</li>

  <li>新增CPyMO Text后端，它将仅在控制台上输出游戏文本。</li>

  <li>mo2pymo补丁不能正常读取游戏名称的bug修正。</li>

  <li>mo2pymo补丁不能正常生成<code class="notranslate">crs</code>命令的实现的问题。</li>

  <li>mo2pymo补丁现在将会处理秋之回忆1中的<code class="notranslate">#goto _END</code>找不到标签的问题。</li>

  <li>pymo2ykm不能正常处理<code class="notranslate">chara_pos</code>的问题。</li>

  <li>改进了CMake和NMake的配置文件，现在它自动扫描源代码并编译，而不再需要手动指定。</li>

  <li>整理gitignore。</li>

  <li>为SDL1和SDL2的makefile提供了DEBUG选项。</li>

  </ul>'
updated: '2022-07-17T02:35:16Z'
version: v1.1.0
version_title: CPyMO 1.1.0
---
