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
    size: 10398652
    size_str: 9 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.2/TJAP_3DS.3dsx
  TJAP_3DS.cia:
    size: 10568640
    size_str: 10 MiB
    url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.2/TJAP_3DS.cia
github: LuMariGames/TJAP_3DS
icon: https://raw.githubusercontent.com/LuMariGames/TJAP_3DS/main/resource/icon.png
image: https://raw.githubusercontent.com/togetg/TJAPlayer_for_3DS/master/resource/banner.png
image_length: 17026
layout: app
llm_generation: unknown
prerelease:
  download_page: https://github.com/LuMariGames/TJAP_3DS/releases/tag/v2.3.3
  downloads:
    TJAP_3DS.3dsx:
      size: 9873792
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.3/TJAP_3DS.3dsx
    TJAP_3DS.cia:
      size: 10040256
      size_str: 9 MiB
      url: https://github.com/LuMariGames/TJAP_3DS/releases/download/v2.3.3/TJAP_3DS.cia
  qr:
    TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/tjap_3ds-cia.png
  update_notes: '<h2 dir="auto">チェンジログ</h2>

    <ul dir="auto">

    <li>譜面をまとめて読み込む際のロード時間を短縮</li>

    <li>特定の条件下で読み込み開始時にクラッシュする不具合の修正</li>

    <li>譜面分岐時に違うコースの挙動が起きる可能性のあった不具合の修正</li>

    <li><code class="notranslate">#SUDDEN</code>命令が正しく機能していなかったのを修正</li>

    </ul>

    <h2 dir="auto">Changelog</h2>

    <ul dir="auto">

    <li>Reduced loading time when loading multiple scores at once.</li>

    <li>Fixed a bug that caused a crash at the start of loading under certain conditions.</li>

    <li>Fixed a bug that could cause the game to behave differently depending on the
    song''s branching point.</li>

    <li>Fixed an issue where the <code class="notranslate">#SUDDEN</code> command
    was not working correctly.</li>

    </ul>'
  update_notes_md: '## チェンジログ

    - 譜面をまとめて読み込む際のロード時間を短縮

    - 特定の条件下で読み込み開始時にクラッシュする不具合の修正

    - 譜面分岐時に違うコースの挙動が起きる可能性のあった不具合の修正

    - `#SUDDEN`命令が正しく機能していなかったのを修正


    ## Changelog

    - Reduced loading time when loading multiple scores at once.

    - Fixed a bug that caused a crash at the start of loading under certain conditions.

    - Fixed a bug that could cause the game to behave differently depending on the
    song''s branching point.

    - Fixed an issue where the `#SUDDEN` command was not working correctly.'
  updated: '2026-08-12T06:43:30Z'
  version: v2.3.3
  version_title: TJAPlayer for 3DS v2.3.3
qr:
  TJAP_3DS.cia: https://db.universal-team.net/assets/images/qr/tjap_3ds-cia.png
screenshots:
- description: Gameplay 1
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-1.png
- description: Gameplay 2
  url: https://db.universal-team.net/assets/images/screenshots/tjap_3ds/gameplay-2.png
source: https://github.com/LuMariGames/TJAP_3DS
stars: 13
systems:
- 3DS
title: TJAP_3DS
unique_ids:
- '0xB7655'
update_notes: '<h2 dir="auto">チェンジログ</h2>

  <ul dir="auto">

  <li><code class="notranslate">#SUDDEN (spawntime) (movetime)</code>の実装</li>

  <li><code class="notranslate">#NEXTSONG</code>命令によって譜面がプレイ中一時的に破損する不具合の修正</li>

  <li><code class="notranslate">TITLEJA:</code> <code class="notranslate">SUBTITLEJA:</code>
  <code class="notranslate">TITLEES:</code> <code class="notranslate">SUBTITLEES:</code>タグの対応</li>

  <li>特定の条件下でフリーズする不具合の修正</li>

  <li>曲名が長い場合、文字を縮小表示する様に仕様変更</li>

  </ul>

  <h2 dir="auto">Changelog</h2>

  <ul dir="auto">

  <li>Implemented <code class="notranslate">#SUDDEN (spawntime) (movetime)</code></li>

  <li>Fixed a bug where the <code class="notranslate">#NEXTSONG</code> command would
  temporarily corrupt the score during gameplay.</li>

  <li>Support for <code class="notranslate">TITLEJA:</code> <code class="notranslate">SUBTITLEJA:</code>
  <code class="notranslate">TITLEES:</code> <code class="notranslate">SUBTITLEES:</code>
  tags.</li>

  <li>Fix for a bug that caused the game to freeze under certain conditions.</li>

  <li>The specifications have been changed to display long song titles in a smaller
  font size.</li>

  </ul>'
updated: '2026-08-05T04:14:53Z'
version: v2.3.2
version_title: TJAPlayer for 3DS v2.3.2
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