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
    size: 15191800
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.9/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11301824
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.0.9/CPyMO.for.Nintendo.3DS.cia
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

  <li>修复当快进时循环音效不会被覆盖的问题。</li>

  <li>cpymo-tool在resize图片时，若比率为1, 1，则只转换格式而不进行缩放。</li>

  <li>修复pymo-converter在不存在chara目录的情况下报错的问题。</li>

  <li>立绘命令缓存增加到64个，以应对复杂的立绘情况。</li>

  <li>在图标不为57*57的情况下将会引发警告。</li>

  <li>在mask渐变加载失败时将会引发警告。</li>

  <li>修复找不到脚本文件时会引发UB的问题。</li>

  <li>修复进入album界面时需要点击一下界面才能操作的问题。</li>

  <li>INVALID_ARG不再会导致游戏卡住。</li>

  <li>libpymo中新增来自YukimiScript编译器的<code class="notranslate">if</code>语法。</li>

  <li>当播放视频时若找不到文件则不应当崩溃。</li>

  <li>修复了当<code class="notranslate">select</code>系命令的<code class="notranslate">init_position</code>超过选项数时会发生崩溃的问题。</li>

  <li>修复了文本框不正常的问题。</li>

  <li>libpymo中if_goto的实现不正确，所有的运算符都会被强制替换为eq。</li>

  <li>修复了在选择支关闭右键菜单时可能会引发崩溃的错误行为。</li>

  <li>菜单的鼠标选择和点击统一以最后一个选中的目标为准。</li>

  <li>优化album返回时可能会出现误操作的问题。</li>

  <li>已经修复pymo-convert在某些情况下不能正常使用的问题。</li>

  <li>pymo-convert可以自动生成目标目录。</li>

  <li>新增pymo-strip工具用于精简pymo游戏数据包。</li>

  </ul>'
updated: '2022-05-26T04:35:28Z'
version: v1.0.9
version_title: CPyMO 1.0.9
wiki: https://github.com/Strrationalism/CPyMO/wiki
---
