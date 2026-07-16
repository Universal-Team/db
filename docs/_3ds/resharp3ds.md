---
author: Saiitanaa
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
    size: 323952
    size_str: 316 KiB
    url: https://github.com/saiitanaa/ReSharp3DS/releases/download/v2.2.4/ReSharp3DS.3dsx
  ReSharp3DS.cia:
    size: 608192
    size_str: 593 KiB
    url: https://github.com/saiitanaa/ReSharp3DS/releases/download/v2.2.4/ReSharp3DS.cia
  TestApp.zip:
    size: 5016
    size_str: 4 KiB
    url: https://github.com/saiitanaa/ReSharp3DS/releases/download/v2.2.4/TestApp.zip
  mscorlib.pe:
    size: 31028
    size_str: 30 KiB
    url: https://github.com/saiitanaa/ReSharp3DS/releases/download/v2.2.4/mscorlib.pe
github: saysaa/ReSharp3DS
icon: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/icon.png
image: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/banner.png
image_length: 34706
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
preinstall_message: Remember to create a folder named “ReSharp3DS” at the root of
  your SD card
qr:
  ReSharp3DS.cia: https://db.universal-team.net/assets/images/qr/resharp3ds-cia.png
source: https://github.com/saiitanaa/ReSharp3DS
stars: 24
systems:
- 3DS
title: ReSharp3DS
unique_ids:
- '0x23400'
update_notes: "<p><a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/9168fcf4-9f7a-492c-9381-ef15543d499b\"\
  ><img width=\"600\" height=\"600\" alt=\"image\" src=\"https://github.com/user-attachments/assets/9168fcf4-9f7a-492c-9381-ef15543d499b\"\
  \ style=\"max-width: 100%; height: auto; max-height: 600px;; aspect-ratio: 600 /\
  \ 600; background-color: var(--bgColor-muted); border-radius: 6px\" class=\"js-gh-image-fallback\"\
  ></a></p>\n<h2>Fast CIA Installation</h2>\n<p><a target=\"_blank\" rel=\"noopener\
  \ noreferrer\" href=\"https://github.com/user-attachments/assets/49d7118a-319e-4760-b637-f55ce205a4a6\"\
  ><img width=\"250\" height=\"250\" alt=\"ReSharp3DS-QR_CODE\" src=\"https://github.com/user-attachments/assets/49d7118a-319e-4760-b637-f55ce205a4a6\"\
  \ style=\"max-width: 100%; height: auto; max-height: 250px;; aspect-ratio: 250 /\
  \ 250; background-color: var(--bgColor-muted); border-radius: 6px\" class=\"js-gh-image-fallback\"\
  ></a></p>\n<p align=\"center\">\n  <a href=\"https://discord.gg/RZPgeDpCNQ\" rel=\"\
  nofollow\">Discord server</a>\n</p>\n<h2>ReSharp3DS Runtime Update</h2>\n<h3>Added</h3>\n\
  <ul>\n<li>\n<p>Added <code class=\"notranslate\">manifest.json</code> support in\
  \ the launcher.</p>\n</li>\n<li>\n<p>Added support for manifest-based <code class=\"\
  notranslate\">.pe</code> display names.</p>\n<ul>\n<li>Example: <code class=\"notranslate\"\
  >app.pe</code> can now appear as <code class=\"notranslate\">TestApp</code>.</li>\n\
  </ul>\n</li>\n<li>\n<p>Added manifest metadata support:</p>\n<ul>\n<li><code class=\"\
  notranslate\">name</code></li>\n<li><code class=\"notranslate\">author</code></li>\n\
  <li><code class=\"notranslate\">version</code></li>\n<li><code class=\"notranslate\"\
  >entry</code></li>\n<li><code class=\"notranslate\">description</code></li>\n</ul>\n\
  </li>\n<li>\n<p>Added selected app metadata display in the launcher:</p>\n<ul>\n\
  <li><code class=\"notranslate\">Author: ...</code></li>\n<li><code class=\"notranslate\"\
  >Version: ...</code></li>\n</ul>\n</li>\n<li>\n<p>Added touchscreen support in the\
  \ launcher.</p>\n</li>\n<li>\n<p>Added better launcher file browser behavior.</p>\n\
  </li>\n<li>\n<p>Added app/folder sorting in the launcher.</p>\n</li>\n<li>\n<p>Added\
  \ <code class=\"notranslate\">runtime_net.cpp</code> and <code class=\"notranslate\"\
  >runtime_net.h</code>.</p>\n</li>\n<li>\n<p>Added runtime network/file helper functions:</p>\n\
  <ul>\n<li><code class=\"notranslate\">FileExists</code></li>\n<li><code class=\"\
  notranslate\">DirectoryExists</code></li>\n<li><code class=\"notranslate\">EnsureDirectory</code></li>\n\
  <li><code class=\"notranslate\">DownloadFile</code></li>\n</ul>\n</li>\n<li>\n<p>Added\
  \ basic crash log infrastructure.</p>\n</li>\n<li>\n<p>Added basic crash screen\
  \ infrastructure.</p>\n</li>\n<li>\n<p>Added future log paths:</p>\n<ul>\n<li><code\
  \ class=\"notranslate\">sdmc:/ReSharp3DS/logs/crash.txt</code></li>\n<li><code class=\"\
  notranslate\">sdmc:/ReSharp3DS/logs/clr-panic.txt</code></li>\n<li><code class=\"\
  notranslate\">sdmc:/ReSharp3DS/logs/&lt;AppName&gt;.log</code></li>\n</ul>\n</li>\n\
  <li>\n<p>Added centralized input snapshot logic.</p>\n</li>\n<li>\n<p>Added cached\
  \ runtime state for:</p>\n<ul>\n<li>held buttons</li>\n<li>pressed-once buttons</li>\n\
  <li>touch position</li>\n<li>circle pad position</li>\n</ul>\n</li>\n<li>\n<p>Added\
  \ graphics target support for top/bottom screen rendering.</p>\n</li>\n<li>\n<p>Added\
  \ transparent sprite drawing support.</p>\n</li>\n</ul>\n<h3>Changed</h3>\n<ul>\n\
  <li>Reworked launcher app naming.</li>\n<li>The launcher now uses <code class=\"\
  notranslate\">manifest.json</code> to rename the selected <code class=\"notranslate\"\
  >.pe</code> entry instead of only renaming the app folder.</li>\n<li>The launcher\
  \ now reads the manifest <code class=\"notranslate\">entry</code> field to know\
  \ which <code class=\"notranslate\">.pe</code> file should receive the display name.</li>\n\
  <li>Replaced the old update-oriented code with a smaller runtime network helper.</li>\n\
  <li>Improved input handling by avoiding multiple <code class=\"notranslate\">hidScanInput()</code>\
  \ calls per frame.</li>\n<li>Improved app browser organization and metadata rendering.</li>\n\
  </ul>\n<h3>Removed</h3>\n<ul>\n<li>Removed old updater-style API usage from the\
  \ launcher.</li>\n<li>Removed old <code class=\"notranslate\">UpdateInfo</code>\
  \ / <code class=\"notranslate\">CheckForUpdate</code> style update flow.</li>\n\
  <li>Removed runtime auto-update behavior from this part of the project.</li>\n</ul>\n\
  <h3>Fixed</h3>\n<ul>\n<li>\n<p>Fixed duplicated <code class=\"notranslate\">copy_json_string_value(...)</code>\
  \ definition in <code class=\"notranslate\">gui.cpp</code>.</p>\n</li>\n<li>\n<p>Fixed\
  \ generated C++ string literals where <code class=\"notranslate\">\\n</code> had\
  \ been converted into real line breaks.</p>\n</li>\n<li>\n<p>Fixed broken <code\
  \ class=\"notranslate\">printf(...)</code> statements in:</p>\n<ul>\n<li><code class=\"\
  notranslate\">gui.cpp</code></li>\n<li><code class=\"notranslate\">main.cpp</code></li>\n\
  <li><code class=\"notranslate\">runtime_net.cpp</code></li>\n</ul>\n</li>\n<li>\n\
  <p>Fixed invalid <code class=\"notranslate\">'\\0'</code> generation where real\
  \ null characters were inserted into source code.</p>\n</li>\n<li>\n<p>Fixed launcher\
  \ metadata display being inserted into the wrong function.</p>\n</li>\n<li>\n<p>Fixed\
  \ author/version metadata rendering placement.</p>\n</li>\n<li>\n<p>Fixed manifest\
  \ behavior so metadata can target a <code class=\"notranslate\">.pe</code> file\
  \ through the <code class=\"notranslate\">entry</code> field.</p>\n</li>\n</ul>\n\
  <hr>\n<h2>ReSharp3DS API Update</h2>\n<h3>Added</h3>\n<ul>\n<li>\n<p>Added native\
  \ runtime binding for returning to the launcher:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >RuntimeReturnToLauncher</code></li>\n</ul>\n</li>\n<li>\n<p>Added native debug\
  \ log binding:</p>\n<ul>\n<li><code class=\"notranslate\">DebugLogFile</code></li>\n\
  </ul>\n</li>\n<li>\n<p>Added native graphics target binding:</p>\n<ul>\n<li><code\
  \ class=\"notranslate\">GraphicsSetTarget</code></li>\n</ul>\n</li>\n<li>\n<p>Added\
  \ native transparent sprite binding:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >GraphicsDrawSpriteTransparent</code></li>\n</ul>\n</li>\n<li>\n<p>Added support\
  \ for native top/bottom screen drawing target selection.</p>\n</li>\n<li>\n<p>Added\
  \ native transparent sprite rendering.</p>\n</li>\n<li>\n<p>Added native debug file\
  \ logging path support.</p>\n</li>\n<li>\n<p>Added native system info improvements:</p>\n\
  <ul>\n<li>battery level</li>\n<li>free memory</li>\n<li>New 3DS detection</li>\n\
  </ul>\n</li>\n<li>\n<p>Added improved input native behavior using cached frame input\
  \ data.</p>\n</li>\n</ul>\n<h3>Changed</h3>\n<ul>\n<li>Native input calls now read\
  \ from a cached input snapshot instead of scanning input repeatedly.</li>\n<li>Native\
  \ graphics code can now target different screens.</li>\n<li>Native debug logging\
  \ is prepared to write logs into the ReSharp3DS logs folder.</li>\n<li>Native runtime\
  \ behavior is prepared for cleaner launcher return handling.</li>\n</ul>\n<h3>Fixed</h3>\n\
  <ul>\n<li>Fixed pressed-once input stability by preparing frame-based input state.</li>\n\
  <li>Fixed broken native C++ string literals generated during integration.</li>\n\
  <li>Fixed crash/debug helper code generation issues.</li>\n</ul>\n<hr>\n<h2>ReSharp3DS\
  \ SDK Update</h2>\n<h3>Added</h3>\n<ul>\n<li>\n<p>Added C# helper enum:</p>\n<ul>\n\
  <li><code class=\"notranslate\">Button</code></li>\n</ul>\n</li>\n<li>\n<p>Added\
  \ C# screen target enum:</p>\n<ul>\n<li><code class=\"notranslate\">ScreenTarget</code></li>\n\
  </ul>\n</li>\n<li>\n<p>Added C# helper structs:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >Vector2</code></li>\n<li><code class=\"notranslate\">Rect</code></li>\n</ul>\n\
  </li>\n<li>\n<p>Added C# utility class:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >Timer</code></li>\n</ul>\n</li>\n<li>\n<p>Added C# app base class:</p>\n<ul>\n\
  <li><code class=\"notranslate\">GameApp</code></li>\n</ul>\n</li>\n<li>\n<p>Added\
  \ input helpers:</p>\n<ul>\n<li><code class=\"notranslate\">Input.IsHeld(Button\
  \ button)</code></li>\n<li><code class=\"notranslate\">Input.IsPressed(Button button)</code></li>\n\
  <li><code class=\"notranslate\">Input.CirclePad()</code></li>\n</ul>\n</li>\n<li>\n\
  <p>Added touch helper:</p>\n<ul>\n<li><code class=\"notranslate\">Touch.Position()</code></li>\n\
  </ul>\n</li>\n<li>\n<p>Added runtime helper:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >Runtime.ReturnToLauncher()</code></li>\n</ul>\n</li>\n<li>\n<p>Added debug helpers:</p>\n\
  <ul>\n<li><code class=\"notranslate\">Debug.Log(...)</code></li>\n<li><code class=\"\
  notranslate\">Debug.Warn(...)</code></li>\n<li><code class=\"notranslate\">Debug.Error(...)</code></li>\n\
  <li><code class=\"notranslate\">Debug.LogInt(...)</code></li>\n</ul>\n</li>\n<li>\n\
  <p>Added graphics helpers:</p>\n<ul>\n<li><code class=\"notranslate\">Graphics.SetTarget(ScreenTarget.Top)</code></li>\n\
  <li><code class=\"notranslate\">Graphics.SetTarget(ScreenTarget.Bottom)</code></li>\n\
  <li><code class=\"notranslate\">Graphics.DrawSpriteTransparent(...)</code></li>\n\
  </ul>\n</li>\n<li>\n<p>Added save helpers:</p>\n<ul>\n<li><code class=\"notranslate\"\
  >Save.Exists(...)</code></li>\n<li><code class=\"notranslate\">Save.Delete(...)</code></li>\n\
  <li><code class=\"notranslate\">Save.SetBool(...)</code></li>\n<li><code class=\"\
  notranslate\">Save.GetBool(...)</code></li>\n</ul>\n</li>\n</ul>\n<h3>Changed</h3>\n\
  <ul>\n<li>Improved SDK usability for C# app developers.</li>\n<li>Made input code\
  \ cleaner by allowing button enums instead of many direct method calls.</li>\n<li>Made\
  \ touch handling cleaner by exposing a <code class=\"notranslate\">Vector2</code>\
  \ position helper.</li>\n<li>Made save data easier to use with boolean helpers.</li>\n\
  <li>Made graphics code more flexible with screen target support.</li>\n</ul>\n<h3>Fixed</h3>\n\
  <ul>\n<li>\n<p>Fixed <code class=\"notranslate\">UI.DrawProgressBar(...)</code>\
  \ so it avoids invalid/negative fill sizes.</p>\n</li>\n<li>\n<p>Fixed duplicate\
  \ SDK compile issue explanation:</p>\n<ul>\n<li>apps must not compile two copies\
  \ of <code class=\"notranslate\">ReSharp3DS.cs</code>.</li>\n</ul>\n</li>\n</ul>\n\
  <hr>\n<h2>Example manifest</h2>\n<div class=\"highlight highlight-source-json\"\
  ><pre class=\"notranslate\">{\n  <span class=\"pl-ent\">\"name\"</span>: <span class=\"\
  pl-s\"><span class=\"pl-pds\">\"</span>App de test<span class=\"pl-pds\">\"</span></span>,\n\
  \  <span class=\"pl-ent\">\"author\"</span>: <span class=\"pl-s\"><span class=\"\
  pl-pds\">\"</span>Saysaa<span class=\"pl-pds\">\"</span></span>,\n  <span class=\"\
  pl-ent\">\"version\"</span>: <span class=\"pl-s\"><span class=\"pl-pds\">\"</span>0.1.0<span\
  \ class=\"pl-pds\">\"</span></span>,\n  <span class=\"pl-ent\">\"entry\"</span>:\
  \ <span class=\"pl-s\"><span class=\"pl-pds\">\"</span>app.pe<span class=\"pl-pds\"\
  >\"</span></span>,\n  <span class=\"pl-ent\">\"description\"</span>: <span class=\"\
  pl-s\"><span class=\"pl-pds\">\"</span>Application de test pour ReSharp3DS<span\
  \ class=\"pl-pds\">\"</span></span>\n}</pre></div>\n<p>Expected SD structure:</p>\n\
  <div class=\"highlight highlight-text-adblock\"><pre class=\"notranslate\">sdmc:/ReSharp3DS/apps/TestApp/\n\
  \  manifest.json\n  app.pe</pre></div>\n<hr>\n<h2>Notes</h2>\n<ul>\n<li>This is\
  \ an integration update.</li>\n<li>Some features are implemented but still need\
  \ full real hardware validation.</li>\n<li>Crash screen and crash log functions\
  \ exist, but should still be fully wired into every runtime failure path.</li>\n\
  <li>Some non-blocking <code class=\"notranslate\">snprintf</code> path-length warnings\
  \ may remain.</li>\n</ul>"
updated: '2026-06-22T11:40:30Z'
version: v2.2.4
version_title: v2.2.4-release
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