---
author: TogeToge & MarioGames
avatar: https://avatars.githubusercontent.com/u/176740851?v=4
categories:
- game
color: '#9e4d4d'
color_bg: '#803e3e'
created: '2024-07-27T07:58:35Z'
description: TJAPlayer for 3DS - Music game of the TJA file.
download_page: https://github.com/LuMariGames/TJAP_3DS/releases
downloads:
  TJAP_3DS.3dsx:
    size: 709860
    size_str: 693 KiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.5/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 1024960
    size_str: 1000 KiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.5/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v1.4.6
  downloads:
    TJAP_3DS.3dsx:
      size: 685800
      size_str: 669 KiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.6/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 1004480
      size_str: 980 KiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v1.4.6/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>tjaファイル内に「SONGVOL:」を記述する事で楽曲の音量調整が可能に</li>

    <li>譜面と楽曲がズレる際の幅が減少しました(完全に無くすのは難しい...)</li>

    </ul>

    <h2 dir="auto">Change log</h2>

    <ul dir="auto">

    <li>It is possible to adjust the volume of the song by writing "SONGVOL:" in the
    tja file</li>

    <li>The width when the score and the song shift have decreased (it is difficult
    to get rid of it completely...)</li>

    </ul>'
  update_notes_md: "## チェンジログ\n - tjaファイル内に「SONGVOL:」を記述する事で楽曲の音量調整が可能に\n - 譜面と楽曲がズレる際の幅が減少しました(完全に無くすのは難しい...)\n\
    \n## Change log\n- It is possible to adjust the volume of the song by writing\
    \ \"SONGVOL:\" in the tja file\n- The width when the score and the song shift\
    \ have decreased (it is difficult to get rid of it completely...)"
  updated: '2025-01-25T01:09:40Z'
  version: v1.4.6
  version_title: TJAPlayer for 3DS v1.4.6
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 2
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li>音声部分に関する大幅な軽量化</li>

  <li>曲全体のBPMを倍率で変更できる様に</li>

  <li>双打譜面の試験的対応</li>

  <li>譜面分岐の条件に「大音符を叩いた数」を追加しました。(ドン(大)とカッ(大)が対象です)</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">#BRANCHSTART d, X, Y

  </code></pre>

  <h2 dir="auto">Change log</h2>

  <ul dir="auto">

  <li>Significant weight reduction in the audio part</li>

  <li>So that the BPM of the entire song can be changed by magnification</li>

  <li>Experimental response to the double sheet music</li>

  <li>Added "number of times big notes were hit" to the conditions for music score
  branching. (This applies to DON and KA)</li>

  </ul>

  <pre class="notranslate"><code class="notranslate">#BRANCHSTART d, X, Y

  </code></pre>'
updated: '2024-12-17T08:32:50Z'
version: v1.4.5
version_title: TJAPlayer for 3DS v1.4.5
wiki: https://github.com/LuMariGames/TJAP_3DS/wiki
---
TJAPlayer for 3DSを約2年ぶりにTogeToge公認の上、更新しました。
This software is produced under the official authorization of TogeToge.

・太鼓タワーと段位道場の実装
・一部オプションの追加
・その他一部の不具合修正

・Implementation of Taiko Tower and Rank Dojo
・Addition of some options
・FIXES OF OTHER FAILURE