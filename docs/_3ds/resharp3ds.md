---
author: Saysaa
avatar: https://avatars.githubusercontent.com/u/112180175?v=4
categories:
- app
color: '#3c4037'
color_bg: '#3c4037'
created: '2026-06-01T16:33:12Z'
description: C# runtime and SDK for Nintendo 3DS
download_page: https://github.com/saysaa/ReSharp3DS/releases
downloads:
  ReSharp3DS.3dsx:
    size: 364260
    size_str: 355 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v2.1.3/ReSharp3DS.3dsx
  ReSharp3DS.cia:
    size: 634304
    size_str: 619 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v2.1.3/ReSharp3DS.cia
  mscorlib.pe:
    size: 31028
    size_str: 30 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v2.1.3/mscorlib.pe
github: saysaa/ReSharp3DS
icon: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/icon.png
image: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/banner.png
image_length: 34706
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: none
qr:
  ReSharp3DS.cia: https://db.universal-team.net/assets/images/qr/resharp3ds-cia.png
script_message: Remember to create a folder named “ReSharp3DS” at the root of your
  SD card
source: https://github.com/saysaa/ReSharp3DS
stars: 14
systems:
- 3DS
title: ReSharp3DS
unique_ids:
- '0x23400'
update_notes: "<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/0679d3d4-de8a-40ea-a5ec-483944f435e7\"\
  ><img width=\"600\" height=\"600\" alt=\"image\" src=\"https://github.com/user-attachments/assets/0679d3d4-de8a-40ea-a5ec-483944f435e7\"\
  \ style=\"max-width: 100%; height: auto; max-height: 600px;; aspect-ratio: 600 /\
  \ 600; background-color: var(--bgColor-muted); border-radius: 6px\" class=\"js-gh-image-fallback\"\
  ></a>\n<h2 dir=\"auto\">ReSharp3DS SDK Update</h2>\n<ul dir=\"auto\">\n<li>Input.IsAPressedOnce\
  \ / IsBPressedOnce / etc.</li>\n<li>Graphics.DrawLine</li>\n<li>Graphics.DrawCircle</li>\n\
  <li>Graphics.FillCircle</li>\n<li>Graphics.DrawSprite</li>\n<li>Graphics.DrawSprite(path,\
  \ x, y, width, height)</li>\n<li>Math3DS.Clamp / Abs / Lerp</li>\n<li>Color.RGB\
  \ + couleurs constantes</li>\n<li>Debug.Log / LogInt</li>\n<li>File.GetSize</li>\n\
  <li>Directory.ListFiles</li>\n<li>Directory.ListFolders</li>\n<li>Runtime.Exit</li>\n\
  <li>Runtime.Restart</li>\n<li>Runtime.GetVersion</li>\n<li>Runtime.GetFps</li>\n\
  <li>App.Exists</li>\n<li>App.ReadText</li>\n<li>App.WriteText</li>\n<li>Audio.PauseMusic</li>\n\
  <li>Audio.ResumeMusic</li>\n<li>Audio.SetMusicLoop</li>\n<li>Audio.PlaySfx</li>\n\
  <li>UI.MessageBox</li>\n<li>UI.DrawButton</li>\n<li>UI.DrawProgressBar</li>\n</ul>\n\
  <h3 dir=\"auto\">Exemple</h3>\n<div class=\"highlight highlight-source-cs\" dir=\"\
  auto\"><pre class=\"notranslate\"><span class=\"pl-k\">namespace</span> <span class=\"\
  pl-v\">ReSharp3DS</span>\n<span class=\"pl-kos\">{</span>\n    <span class=\"pl-k\"\
  >public</span> <span class=\"pl-k\">class</span> <span class=\"pl-smi\">Program</span>\n\
  \    <span class=\"pl-kos\">{</span>\n        <span class=\"pl-k\"><span class=\"\
  pl-k\">static</span></span> <span class=\"pl-smi\">bool</span> <span class=\"pl-s1\"\
  >initialized</span> <span class=\"pl-c1\">=</span> <span class=\"pl-c1\">false</span><span\
  \ class=\"pl-kos\">;</span>\n        <span class=\"pl-k\"><span class=\"pl-k\">static</span></span>\
  \ <span class=\"pl-smi\">int</span> <span class=\"pl-s1\">x</span> <span class=\"\
  pl-c1\">=</span> <span class=\"pl-c1\">150</span><span class=\"pl-kos\">;</span>\n\
  \        <span class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"\
  pl-smi\">int</span> <span class=\"pl-s1\">y</span> <span class=\"pl-c1\">=</span>\
  \ <span class=\"pl-c1\">110</span><span class=\"pl-kos\">;</span>\n        <span\
  \ class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"pl-smi\"\
  >int</span> <span class=\"pl-s1\">lastSaveTime</span> <span class=\"pl-c1\">=</span>\
  \ <span class=\"pl-c1\">0</span><span class=\"pl-kos\">;</span>\n\n        <span\
  \ class=\"pl-k\">public</span> <span class=\"pl-k\"><span class=\"pl-k\">static</span></span>\
  \ <span class=\"pl-smi\">void</span> <span class=\"pl-en\">Main</span><span class=\"\
  pl-kos\">(</span><span class=\"pl-kos\">)</span>\n        <span class=\"pl-kos\"\
  >{</span>\n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-c1\">!</span><span class=\"pl-s1\">initialized</span><span class=\"\
  pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n               \
  \ <span class=\"pl-s1\">initialized</span> <span class=\"pl-c1\">=</span> <span\
  \ class=\"pl-c1\">true</span><span class=\"pl-kos\">;</span>\n\n               \
  \ <span class=\"pl-s1\">Console</span><span class=\"pl-kos\">.</span><span class=\"\
  pl-en\">Clear</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n                <span class=\"pl-s1\">Debug</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">Log</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-s\">\"ReSharp3DS full API demo\"</span><span class=\"\
  pl-kos\">)</span><span class=\"pl-kos\">;</span>\n                <span class=\"\
  pl-s1\">Debug</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">Log</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-s1\">Runtime</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">GetVersion</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n\n                <span class=\"pl-s1\">Audio</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">Init</span><span class=\"pl-kos\">(</span><span class=\"\
  pl-kos\">)</span><span class=\"pl-kos\">;</span>\n                <span class=\"\
  pl-s1\">Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">SetSfxVolume</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-c1\">80</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n                <span class=\"pl-s1\"\
  >Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">SetMusicVolume</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-c1\">60</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n\n                <span class=\"pl-s1\"\
  >x</span> <span class=\"pl-c1\">=</span> <span class=\"pl-s1\">Save</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">GetInt</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-s\">\"last_x\"</span><span class=\"pl-kos\">,</span> <span\
  \ class=\"pl-s1\">x</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n                <span class=\"pl-s1\">y</span> <span class=\"pl-c1\"\
  >=</span> <span class=\"pl-s1\">Save</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">GetInt</span><span class=\"pl-kos\">(</span><span class=\"pl-s\"\
  >\"last_y\"</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">y</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n            <span class=\"\
  pl-kos\">}</span>\n\n            <span class=\"pl-s1\">x</span> <span class=\"pl-c1\"\
  >+=</span> <span class=\"pl-s1\">Input</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">CirclePadX</span><span class=\"pl-kos\">(</span><span class=\"\
  pl-kos\">)</span> <span class=\"pl-c1\">/</span> <span class=\"pl-c1\">25</span><span\
  \ class=\"pl-kos\">;</span>\n            <span class=\"pl-s1\">y</span> <span class=\"\
  pl-c1\">-=</span> <span class=\"pl-s1\">Input</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">CirclePadY</span><span class=\"pl-kos\">(</span><span class=\"\
  pl-kos\">)</span> <span class=\"pl-c1\">/</span> <span class=\"pl-c1\">25</span><span\
  \ class=\"pl-kos\">;</span>\n\n            <span class=\"pl-s1\">x</span> <span\
  \ class=\"pl-c1\">=</span> <span class=\"pl-s1\">Math3DS</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">Clamp</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">x</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\"\
  >0</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">Screen</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-s1\">BottomWidth</span> <span class=\"\
  pl-c1\">-</span> <span class=\"pl-c1\">12</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n            <span class=\"pl-s1\">y</span> <span class=\"\
  pl-c1\">=</span> <span class=\"pl-s1\">Math3DS</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">Clamp</span><span class=\"pl-kos\">(</span><span class=\"pl-s1\"\
  >y</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\">0</span><span class=\"\
  pl-kos\">,</span> <span class=\"pl-s1\">Screen</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-s1\">BottomHeight</span> <span class=\"pl-c1\">-</span> <span class=\"\
  pl-c1\">12</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n\
  \n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">Touch</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >IsPressed</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n     \
  \           <span class=\"pl-s1\">x</span> <span class=\"pl-c1\">=</span> <span\
  \ class=\"pl-s1\">Touch</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >X</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"\
  pl-kos\">;</span>\n                <span class=\"pl-s1\">y</span> <span class=\"\
  pl-c1\">=</span> <span class=\"pl-s1\">Touch</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">Y</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n            <span class=\"pl-kos\">}</span>\n\
  \n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">Input</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >IsAPressedOnce</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n     \
  \           <span class=\"pl-s1\">Audio</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">Beep</span><span class=\"pl-kos\">(</span><span class=\"pl-s1\"\
  >Notes</span><span class=\"pl-kos\">.</span><span class=\"pl-s1\">C5</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-c1\">100</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n            <span class=\"pl-kos\">}</span>\n\
  \n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">Input</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >IsBPressedOnce</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n     \
  \           <span class=\"pl-s1\">Save</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">SetInt</span><span class=\"pl-kos\">(</span><span class=\"pl-s\"\
  >\"last_x\"</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">x</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n                <span\
  \ class=\"pl-s1\">Save</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >SetInt</span><span class=\"pl-kos\">(</span><span class=\"pl-s\">\"last_y\"</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-s1\">y</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n                <span class=\"pl-s1\"\
  >lastSaveTime</span> <span class=\"pl-c1\">=</span> <span class=\"pl-s1\">Time</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">Milliseconds</span><span class=\"\
  pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n\
  \            <span class=\"pl-kos\">}</span>\n\n            <span class=\"pl-k\"\
  >if</span> <span class=\"pl-kos\">(</span><span class=\"pl-s1\">Input</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">IsStartPressedOnce</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >)</span>\n            <span class=\"pl-kos\">{</span>\n                <span class=\"\
  pl-s1\">Runtime</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">Exit</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-kos\">}</span>\n\n            <span class=\"\
  pl-s1\">Graphics</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">Clear</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-s1\">Color</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-s1\">Black</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n            <span class=\"pl-s1\">Graphics</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">DrawText</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-c1\">8</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-c1\">8</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">App</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">GetName</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-s1\">Color</span><span class=\"pl-kos\">.</span><span class=\"pl-s1\">White</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n            <span class=\"\
  pl-s1\">Graphics</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">DrawText</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-c1\">8</span><span class=\"pl-kos\"\
  >,</span> <span class=\"pl-c1\">24</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-s\">\"FPS:\"</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">Color</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-s1\">Gray</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n            <span class=\"pl-s1\">Graphics</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">DrawText</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-c1\">56</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-c1\">24</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">Runtime</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">GetFps</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">.</span><span class=\"\
  pl-en\">ToString</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-s1\">Color</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-s1\">Green</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n\n            <span class=\"pl-s1\">Graphics</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">DrawLine</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-c1\">0</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-c1\">220</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\">319</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-c1\">220</span><span class=\"pl-kos\"\
  >,</span> <span class=\"pl-s1\">Color</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-s1\">Blue</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-s1\">Graphics</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">DrawCircle</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">x</span> <span class=\"pl-c1\">+</span> <span class=\"pl-c1\"\
  >6</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\">y</span> <span class=\"\
  pl-c1\">+</span> <span class=\"pl-c1\">6</span><span class=\"pl-kos\">,</span> <span\
  \ class=\"pl-c1\">12</span><span class=\"pl-kos\">,</span> <span class=\"pl-s1\"\
  >Color</span><span class=\"pl-kos\">.</span><span class=\"pl-s1\">Yellow</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n            <span class=\"\
  pl-s1\">Graphics</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">FillRect</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-s1\">x</span><span class=\"pl-kos\"\
  >,</span> <span class=\"pl-s1\">y</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-c1\">12</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\">12</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-s1\">Color</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-s1\">Green</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n\n            <span class=\"pl-k\">if</span> <span\
  \ class=\"pl-kos\">(</span><span class=\"pl-s1\">Time</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">Milliseconds</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-kos\">)</span> <span class=\"pl-c1\">-</span> <span class=\"pl-s1\"\
  >lastSaveTime</span> <span class=\"pl-c1\">&lt;</span> <span class=\"pl-c1\">1500</span><span\
  \ class=\"pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n     \
  \           <span class=\"pl-s1\">UI</span><span class=\"pl-kos\">.</span><span\
  \ class=\"pl-en\">DrawProgressBar</span><span class=\"pl-kos\">(</span><span class=\"\
  pl-c1\">8</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\">200</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-c1\">120</span><span class=\"pl-kos\"\
  >,</span> <span class=\"pl-c1\">10</span><span class=\"pl-kos\">,</span> <span class=\"\
  pl-c1\">100</span><span class=\"pl-kos\">,</span> <span class=\"pl-c1\">100</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n                <span\
  \ class=\"pl-s1\">Graphics</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >DrawText</span><span class=\"pl-kos\">(</span><span class=\"pl-c1\">8</span><span\
  \ class=\"pl-kos\">,</span> <span class=\"pl-c1\">184</span><span class=\"pl-kos\"\
  >,</span> <span class=\"pl-s\">\"Saved\"</span><span class=\"pl-kos\">,</span> <span\
  \ class=\"pl-s1\">Color</span><span class=\"pl-kos\">.</span><span class=\"pl-s1\"\
  >White</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n  \
  \          <span class=\"pl-kos\">}</span>\n\n            <span class=\"pl-s1\"\
  >Graphics</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">Present</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-s1\">Runtime</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">Yield</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n        <span class=\"\
  pl-kos\">}</span>\n    <span class=\"pl-kos\">}</span>\n<span class=\"pl-kos\">}</span></pre></div>"
updated: '2026-06-12T21:01:47Z'
version: v2.1.3
version_title: v2.1.3-beta.10
website: https://saysaa.github.io/ReSharp3DS/
wiki: https://saysaa.github.io/ReSharp3DS/
---
# Runtime & SDK for C#
## The project uses a C++ 3DS homebrew application to load C# assemblies compiled as .pe files, then executes them through nanoCLR.

### Links

<p align="center">
  <a href="https://saysaa.github.io/ReSharp3DS/">ReSharp3DS Documentation</a>
</p>

<p align="center">
  <a href="https://github.com/saysaa/ReSharp3DS/tree/main">Github repo</a>
</p>

<p align="center">
  <a href="https://discord.gg/ENBwURmUj8">Discord server</a>
</p>