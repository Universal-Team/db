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
    size: 14875872
    size_str: 14 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.3/CPyMO.for.Nintendo.3DS.3dsx
  CPyMO.for.Nintendo.3DS.cia:
    size: 11195328
    size_str: 10 MiB
    url: https://github.com/Strrationalism/CPyMO/releases/download/v1.1.3/CPyMO.for.Nintendo.3DS.cia
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
update_notes: '<h1 dir="auto">平台支持</h1>

  <h2 dir="auto">PSP平台支持</h2>

  <ul dir="auto">

  <li>新增SDL 1.2后端</li>

  <li>SDL2后端版本提升至第一梯队，并使其支持ffmpeg以支持全部音频功能</li>

  <li>SDL2后端版本对话历史数量调到24</li>

  <li>更新图标、启动声音和启动背景图</li>

  <li>修正键位定义</li>

  <li>设置PSP工作在333MHz CPU和167MHz总线下</li>

  <li>已关闭masktrans功能以使其运行流畅</li>

  </ul>

  <h2 dir="auto">PSV平台支持</h2>

  <ul dir="auto">

  <li>为减少存储卡IO，不再支持自动存档功能</li>

  <li>在PSV2000日版和Vita3K上正常工作</li>

  <li>设置了图标和背景图</li>

  <li>调整键位以使得它和PSP版本一致</li>

  <li>开启强制居中模式</li>

  <li>开启444MHz CPU/222MHz Bus/222MHz GPU/166MHz GPUXBar模式</li>

  </ul>

  <h2 dir="auto">Wii平台支持</h2>

  <ul dir="auto">

  <li>Wii平台可以实机启动并正常运行</li>

  <li>Wii平台现在打包了元数据和图标</li>

  </ul>

  <h1 dir="auto">新功能</h1>

  <ul dir="auto">

  <li>设置界面增加调整值的加减按钮</li>

  <li>修改文字大小后会立刻反映到设置界面上</li>

  <li>允许定义<code class="notranslate">DONT_PASS_PATH_TO_FFMPEG</code>以阻止FFmpeg直接使用路径加载文件</li>

  <li>CG界面将会对过长的CG进行滚动显示</li>

  <li>CG界面支持显示CG名称</li>

  <li>创建CG界面缩略图时将会根据画面比例对图片进行剪裁</li>

  <li>支持UWP ARM64</li>

  <li>支持通过宏<code class="notranslate">DISABLE_AUTOSAVE</code>来关闭自动存档槽位并将其设置为手动存档槽位0</li>

  <li>SDL2默认makefile在设置<code class="notranslate">DISALBE_AUDIO</code>环境变量为1时将会禁止播放声音</li>

  <li>多层UI堆叠</li>

  <li>msgbox允许设置关闭时回调</li>

  <li>SDL1.2后端支持使用SDL_ttf进行字体渲染</li>

  <li>SDL1.2后端支持使用SDL_image进行图片加载</li>

  <li>Switch、PSV支持+键/Start键快速退出</li>

  <li>只有一个游戏时将会直接启动该游戏而不会启动游戏选择器</li>

  <li>现在可以通过定义<code class="notranslate">DISABLE_MASKTRANS</code>宏来禁用masktrans</li>

  <li>尽管不能通过编译，但还是增加了WiiU的Makefile，日后WiiU Homebrew开发工具可用时可立刻使用</li>

  </ul>

  <h1 dir="auto">工具</h1>

  <ul dir="auto">

  <li>修改<code class="notranslate">pymo-convert-audio-to-ogg</code>为<code class="notranslate">pymo-convert-audio</code>使其通用</li>

  <li><code class="notranslate">pymo-convert</code>现在对特殊平台启用强制音频转换以提升音频兼容性</li>

  <li><code class="notranslate">pymo-convert</code>现在可以完美支持目标为psp的输出</li>

  </ul>

  <h1 dir="auto">Bug修正</h1>

  <ul dir="auto">

  <li>触屏和滚轮操作列表UI时选中项混乱</li>

  <li>SDL2后端上的强制居中功能现在将会缩放图像到合适大小</li>

  <li>部分平台上SDL2后端文本图像会在另一端冒出来一两像素的问题</li>

  <li>修复Switch上不能正确识别<code class="notranslate">pymogames</code>目录的问题</li>

  <li>SDL2后端上播放视频将尽可能利用屏幕空间</li>

  <li>3DS上视频播放长宽比不正确的问题</li>

  <li>视频播放器上存在av_frame未被av_frame_unref而产生泄露</li>

  <li>album界面增加绘制边缘选中提示，并且可以关闭加亮模式，以解决SDL1.2在不支持半透明方块混合的情况下不能正常显示CG界面的问题</li>

  <li>由于O3DS播放视频过于卡顿，已关闭O3DS上的视频播放功能</li>

  <li>播放视频时第一帧产生花屏问题</li>

  <li>修正UI模式下错误的刷新行为</li>

  <li>修正charas不能被即时清理导致skip时内存占用暴涨的问题</li>

  <li>当<code class="notranslate">cpymo_backend_image_load</code>从<code class="notranslate">cpymo_assetloader_load_image_with_mask</code>调用时会产生UB的问题</li>

  <li>恢复支持Windows ARM64</li>

  <li>恢复支持UWP ARM</li>

  <li>cpymo-tool中存在的warning</li>

  <li>修复宏<code class="notranslate">LEAKCHECK</code>失效的bug</li>

  <li>尝试修复cpymo-tool中的内存泄漏问题</li>

  <li>CG鉴赏缩略图生成器内存泄漏Bug修正</li>

  <li>修正stb_truetype下字体后端可能存在的写越界问题</li>

  <li>PSV版本修改了TITLE_ID</li>

  <li>修复Switch版不显示标题的Bug</li>

  </ul>

  <h1 dir="auto">优化</h1>

  <ul dir="auto">

  <li>当滑动List UI时将会隐藏选中项高亮框</li>

  <li>安卓和iOS版本在游戏中退出现在将会退回到游戏选择器而非直接退出</li>

  <li>现在BGM音量大小同时也会被作为视频音量大小</li>

  <li>将所有的<code class="notranslate">NDEBUG</code>宏修改为<code class="notranslate">!DEBUG</code>宏</li>

  <li>仅在鼠标/触摸不移动时才会触发长按动作</li>

  <li>rmenu中的字体大小现在跟随设置中的字体大小</li>

  <li>延长logo1和logo2的显示时长</li>

  <li>game selector翻页尽可能保守</li>

  <li>3DS的视频播放器现在采用硬件加速的YUV到RGB转换过程</li>

  <li>禁用了3DS和PSP版中不必要依赖的编译过程</li>

  <li>3DS版改用64MB内存模式，以避免重启进入大内存模式</li>

  <li>隐藏不必要公开的结构体</li>

  <li><code class="notranslate">LOW_FRAME_RATE</code>宏启动的情况下不再允许设置对话速度</li>

  <li>重写<code class="notranslate">cpymo_textbox</code>使其拥有更好的性能</li>

  <li>优化纹理加载失败时3DS后端<code class="notranslate">cpymo_backend_image_create</code>返回的错误信息</li>

  </ul>'
updated: '2022-12-31T15:59:12Z'
version: v1.1.3
version_title: CPyMO v1.1.3
wiki: https://github.com/Strrationalism/CPyMO/wiki
---
