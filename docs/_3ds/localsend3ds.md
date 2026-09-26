---
author: Val March
avatar: https://avatars.githubusercontent.com/u/246964079?v=4
categories:
- app
- utility
color: '#84c7c3'
color_bg: '#55807d'
created: '2026-08-27T12:25:45Z'
description: Unofficial LocalSend client for Nintendo 3DS.
download_filter: cia|3dsx
download_page: https://github.com/thevalmarch/localsend3ds/releases
downloads:
  LocalSend3DS-v1.0.0.3dsx:
    size: 669564
    size_str: 653 KiB
    url: https://github.com/thevalmarch/localsend3ds/releases/download/v1.0.0/LocalSend3DS-v1.0.0.3dsx
  LocalSend3DS-v1.0.0.cia:
    size: 575424
    size_str: 561 KiB
    url: https://github.com/thevalmarch/localsend3ds/releases/download/v1.0.0/LocalSend3DS-v1.0.0.cia
github: thevalmarch/localsend3ds
icon: https://raw.githubusercontent.com/thevalmarch/localsend3ds/main/icon.png
image: https://raw.githubusercontent.com/thevalmarch/localsend3ds/main/icon.png
image_length: 2731
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  LocalSend3DS-v1.0.0.cia: https://db.universal-team.net/assets/images/qr/localsend3ds-v1-0-0-cia.png
source: https://github.com/thevalmarch/localsend3ds
stars: 2
systems:
- 3DS
title: LocalSend3DS
unique_ids:
- '0xF5D53'
update_notes: '<p dir="auto">First public release of LocalSend3DS, an unofficial LocalSend-compatible
  client for the Nintendo 3DS family.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li>Native .3dsx and .cia builds</li>

  <li>Bidirectional LocalSend discovery</li>

  <li>One-file receive and send support</li>

  <li>Outgoing HTTP and fingerprint-pinned HTTPS with mutual TLS</li>

  <li>Verified on real New Nintendo 2DS XL hardware with official LocalSend peers
  on macOS, Linux, and Android</li>

  </ul>

  <h3 dir="auto">Current limitations</h3>

  <ul dir="auto">

  <li>Incoming transfers use HTTP</li>

  <li>PIN-protected recipients are not supported</li>

  <li>Multiple files, folders, text, and clipboard transfers are not supported</li>

  <li>Windows and iOS interoperability remain unverified</li>

  <li>Correct Nintendo 3DS system date and time are required for outgoing TLS certificate
  validation</li>

  </ul>

  <p dir="auto">See SHA256SUMS for release artifact checksums.</p>'
updated: '2026-08-27T12:32:37Z'
version: v1.0.0
version_title: LocalSend3DS v1.0.0
---
LocalSend3DS is an unofficial LocalSend-compatible client for the Nintendo 3DS family.

It supports bidirectional discovery and one-file transfers with official LocalSend clients. Incoming transfers use HTTP, while outgoing transfers support HTTP and fingerprint-pinned HTTPS with mutual TLS.

Real-hardware interoperability has been verified with macOS, Linux, and Android.

PIN-protected recipients, multiple files, folders, text, clipboard transfers, and incoming HTTPS are not currently supported.