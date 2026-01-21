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
    size: 15045848
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.9/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11281344
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.9/CPyMO.for.Nintendo.3DS.cia
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
stars: 141
systems:
- 3DS
title: CPyMO
unique_ids:
- '0xF3098'
update_notes: '<h1 dir="auto">停更说明</h1>

  <p dir="auto">鉴于本人因工作原因和健康原因，无力继续维护CPyMO，故跳过1.1.4~1.1.8版本，直接发布1.1.9版本，之后到2024年1月19日之前，CPyMO将会只进行Bug修正，此后不再对CPyMO主分支进行维护。</p>

  <h1 dir="auto">注意</h1>

  <p dir="auto"><strong>读取1.1.3及以前的存档时，将会出现立绘坐标错误、背景坐标错误、前景动画坐标错误的情况，在后面的场景中恢复正常后重新存档即可解决</strong></p>

  <p dir="auto"><em>引发这些问题的原因是此版本修改存档数据中坐标的表示方式，使其可以在各个不同分辨率大小的游戏之间通用</em></p>

  <h1 dir="auto">废弃</h1>

  <ul dir="auto">

  <li>移除PSP SDL 1.2后端支持</li>

  <li>移除GameCube Makefile</li>

  <li>移除WiiU Makefile</li>

  <li>消除宏</li>

  <li>移除<code class="notranslate">pymo-convert.ps1</code>和<code class="notranslate">pymo-convert-audio.ps1</code></li>

  </ul>

  <h1 dir="auto">新功能</h1>

  <ul dir="auto">

  <li>增加乐曲《Song of PyMO》以作为某些平台上的启动音乐使用</li>

  <li>在PSP平台上使用《Song of PyMO》作为启动音乐</li>

  <li>不同分辨率大小版本的游戏之间存档可以通用</li>

  <li>Auto模式</li>

  <li>CPyMO ASCII Art现在使用备用缓冲区并关闭光标</li>

  <li>CPyMO ASCII Art现在可以运行时动态改变终端大小</li>

  <li>使用<code class="notranslate">cpymo-tool strip</code>取代<code class="notranslate">pymo-strip.ps1</code></li>

  <li>使用<code class="notranslate">cpymo-tool convert</code>取代<code class="notranslate">pymo-convert.ps1</code>和<code
  class="notranslate">pymo-convert-audio.ps1</code></li>

  <li><code class="notranslate">cpymo-tool gen-album-cache</code>现在可以自动搜索<code class="notranslate">#album</code>命令，不再需要手动传入列表名称</li>

  </ul>

  <h1 dir="auto">Bug 修正</h1>

  <ul dir="auto">

  <li>修正了在对话点击后没有刷新屏幕的问题</li>

  <li>修正在定义了<code class="notranslate">GAME_SELECTOR_DIR_2</code>时，只能显示其中一个文件夹的游戏的Bug</li>

  <li>修正在<code class="notranslate">ENABLE_SCREEN_FORCE_CENTERED</code>状态中依然会在SDL2后端下设置逻辑渲染大小的Bug</li>

  <li>PSV在O3优化下会出现奇怪的行为，因此修改为O2优化级别</li>

  <li>修正背景效果层与Fade层的绘制顺序存在错误</li>

  <li>修正album界面在显示CG时退出会导致的内存泄漏</li>

  <li>修正在album中单张CG加载异常时产生的未定义行为</li>

  <li>修正在music和album中找不到列表文件的情况下产生的segmentation fault</li>

  <li>change命令在加载脚本失败时触发segmentation fault</li>

  <li>mo2pymo中对mo2的<code class="notranslate">GOTO_ENDING</code>命令解释有误</li>

  <li>秋之回忆2不能在结局部分正常跳回主界面的问题</li>

  <li>修复<code class="notranslate">namealign</code>字段不能被正确解释的问题</li>

  <li><code class="notranslate">cpymo-tool gen-album-ui</code>现在已经不会再覆盖已有的图像文件</li>

  </ul>

  <h1 dir="auto">优化</h1>

  <ul dir="auto">

  <li>

  <p dir="auto">现在允许对内存分配进行剪裁，当以下情况不能获取足够内存时，将会进行内存剪裁并重试：</p>

  <ul dir="auto">

  <li>加载背景时</li>

  <li>加载立绘时</li>

  <li>关键字符串无法创建</li>

  <li>需要播放BGM时</li>

  <li>使用scroll命令时</li>

  </ul>

  </li>

  <li>

  <p dir="auto">当使用BG_FADE或背景淡化时间为0时，则以低内存的方式加载背景后重试</p>

  </li>

  <li>

  <p dir="auto">当进入album界面时，将会卸载背景图以降低内存占用</p>

  </li>

  <li>

  <p dir="auto">更好用的文本提取API <code class="notranslate">cpymo_engine_extract_text</code></p>

  </li>

  <li>

  <p dir="auto">现在允许在确定取消对话框中响应取消操作</p>

  </li>

  <li>

  <p dir="auto">改进头文件的导入方式，现在不需要再配置<code class="notranslate">-I</code>选项手动指定各种头文件了</p>

  </li>

  <li>

  <p dir="auto">优化右键菜单背景的缩放比例，使得右键菜单文字一般不会溢出到背景之外</p>

  </li>

  </ul>'
updated: '2023-08-14T15:24:56Z'
version: v1.1.9
version_title: CPyMO Aria v1.1.9
---
