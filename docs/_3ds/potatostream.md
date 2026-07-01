---
author: PainDe0Mie
avatar: https://avatars.githubusercontent.com/u/97704518?v=4
categories:
- utility
color: '#5f6983'
color_bg: '#5c6680'
created: '2026-04-18T02:45:15Z'
description: Gamestream client for old 2ds/3DS
download_page: https://github.com/PainDe0Mie/PotatoStream/releases
downloads:
  streampotato.3dsx:
    size: 7624708
    size_str: 7 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.1.0/streampotato.3dsx
  streampotato.cia:
    size: 4373440
    size_str: 4 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.1.0/streampotato.cia
github: PainDe0Mie/PotatoStream
icon: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/ic_streampotato.png
image: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/banner.png
image_length: 11016
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  streampotato.cia: https://db.universal-team.net/assets/images/qr/streampotato-cia.png
source: https://github.com/PainDe0Mie/PotatoStream
stars: 7
systems:
- 3DS
title: PotatoStream
unique_ids:
- '0x3700'
update_notes: '<h1 dir="auto">PotatoStream</h1>

  <p dir="auto"><strong>PotatoStream</strong> is a game streaming client for <strong>Old
  3DS, Old 3DS XL and 2DS</strong>, forked from <a href="https://github.com/zoeyjodon/moonlight-N3DS">moonlight-N3DS</a>
  by zoeyjodon.</p>

  <p dir="auto">Compatible with <a href="https://github.com/LizardByte/Sunshine">Sunshine</a>
  (open-source, recommended) and NVIDIA GameStream.</p>

  <blockquote>

  <p dir="auto">The original project targets the <em>New</em> 3DS and its hardware
  MVD decoder. PotatoStream shifts the focus to older models: ARM11 compiler optimizations,
  smart frame skipping, auto-configured stream profile, and native Y2RU video pipeline.</p>

  </blockquote>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/a810c0b0-3cf6-4a24-bcb4-12221882a18e"><img
  width="512" height="256" alt="banner" src="https://github.com/user-attachments/assets/a810c0b0-3cf6-4a24-bcb4-12221882a18e"
  style="max-width: 100%; height: auto; max-height: 256px;; aspect-ratio: 512 / 256;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/145308d6-a33a-4d8a-93e4-1c8276015f4f"><img
  width="272" height="270" alt="qrcode" src="https://github.com/user-attachments/assets/145308d6-a33a-4d8a-93e4-1c8276015f4f"
  style="max-width: 100%; height: auto; max-height: 270px;; aspect-ratio: 272 / 270;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <h2 dir="auto">What''s new in v1.1.0?</h2>

  <ul dir="auto">

  <li>Improved Sunshine pairing and HTTP stability.</li>

  <li>Persisted confirmed pairs to avoid repairing the same host every time.</li>

  <li>Added v1.1 stream profiles and experimental stereoscopic 3D.</li>

  <li>Reduced framebuffer glitches and gated 3D rendering behind the experimental
  option.</li>

  <li>Improved host flow, stream options, and menu UX.</li>

  </ul>'
updated: '2026-05-09T04:09:14Z'
version: v1.1.0
version_title: PotatoStream v1.1.0
---
PotatoStream is a Moonlight game streaming client for all 3DS and 2DS models, with a focus on Old 3DS/2DS compatibility. Auto-detects hardware at startup and activates "Potato" mode on older models with smart frame skipping, Y2RU hardware pipeline and an optimized stream profile (400x240@24fps). (New 3DS keeps the standard MVD hardware decoder) Compatible with Sunshine and NVIDIA GameStream.