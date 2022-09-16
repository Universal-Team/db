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
    size: 15224172
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.1/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11367360
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.1/CPyMO.for.Nintendo.3DS.cia
github: Strrationalism/CPyMO
icon: https://raw.githubusercontent.com/Strrationalism/CPyMO/main/cpymo-backends/3ds/icon.png
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
unique_ids:
- '0xF3098'
update_notes: '<h1 dir="auto">重要提示</h1>

  <p dir="auto">Android CPyMO已经更新签名，需要先卸载原有版本再安装新版本，卸载CPyMO不会造成存档丢失。</p>

  <h1 dir="auto">改进</h1>

  <ul dir="auto">

  <li>列表UI添加了滑动惯性。</li>

  <li>游戏界面向上滑动即可打开回想界面。</li>

  <li>优化长按手感。</li>

  <li>PSP现在可以实机启动

  <ul dir="auto">

  <li>更新PSP的构建环境</li>

  <li>重写PSP的Makefile使文件布局整洁</li>

  <li>重新映射PSP键位</li>

  </ul>

  </li>

  <li>SDL2后端更新

  <ul dir="auto">

  <li>允许自定义SDL2_Mixer音频后端的音频格式</li>

  <li>允许禁用stb库，以替换成SDL2_image和SDL2_ttf</li>

  <li>重新实现强制居中功能</li>

  <li>允许禁用鼠标</li>

  <li>同时按下ALT+ENTER切换全屏时现在不会引发ENTER键误触</li>

  </ul>

  </li>

  <li>新增<code class="notranslate">CPYMO_ARR_COUNT</code>和<code class="notranslate">CPYMO_FOREACH_ARR</code>宏用于简化数组操作</li>

  <li>视障帮助功能整理为<code class="notranslate">TEXT_EXTRACT</code>、<code class="notranslate">TEXT_EXTRACT_COPY_TO_CLIPBOARD</code>和<code
  class="notranslate">TEXT_EXTRACT_ANDROID_ACCESSIBILITY</code></li>

  <li>修正在多个album列表文件的情况下不能正确产生对应album ui界面图像的问题</li>

  <li>允许通过GNU工具链构建出具有自定义图标和不具有控制台窗口的Windows版CPyMO</li>

  <li>文字菜单在选中时产生微弱移动效果使得选中状态更加直观。</li>

  <li>Bug修正：<code class="notranslate">cpymo_utils_replace_cr</code>具有不正确的行为。</li>

  <li>增加<code class="notranslate">cpymo_assetloader_load_icon</code>及<code class="notranslate">cpymo_assetloader_load_icon_pixels</code>函数用于加载图标。</li>

  <li>在HDPI设备上修正了鼠标位置不正确的问题。</li>

  <li>pymo-convert支持在不支持的设备上剔除组件。</li>

  <li>pymo-convert可以显示更多信息。</li>

  <li>pymo-convert可以进行最大比例适配（并为3DS开启）。</li>

  <li>3DS现在可以等比例拉伸去黑边（以屏幕下端对齐）。</li>

  <li>cpymo-tool现在支持生成album UI缓存图片。</li>

  <li>3DS, PSV, Android, Emscripten上的ffmpeg已经升级到5.0.1。</li>

  <li>使得movie行为与pymo一致。</li>

  <li>CPyMO将会检查PyMO版本兼容性。</li>

  <li>3ds，psv，Emscripten将会从github安装ffmpeg。</li>

  </ul>'
updated: '2022-07-30T11:11:48Z'
version: v1.1.1
version_title: CPyMO v1.1.1
wiki: https://github.com/Strrationalism/CPyMO/wiki
---
