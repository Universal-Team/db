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
  LocalSend3DS-v1.1.0.3dsx:
    size: 673392
    size_str: 657 KiB
    url: https://github.com/thevalmarch/localsend3ds/releases/download/v1.1.0/LocalSend3DS-v1.1.0.3dsx
  LocalSend3DS-v1.1.0.cia:
    size: 577984
    size_str: 564 KiB
    url: https://github.com/thevalmarch/localsend3ds/releases/download/v1.1.0/LocalSend3DS-v1.1.0.cia
github: thevalmarch/localsend3ds
icon: https://raw.githubusercontent.com/thevalmarch/localsend3ds/main/icon.png
image: https://raw.githubusercontent.com/thevalmarch/localsend3ds/main/icon.png
image_length: 2731
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  LocalSend3DS-v1.1.0.cia: https://db.universal-team.net/assets/images/qr/localsend3ds-v1-1-0-cia.png
source: https://github.com/thevalmarch/localsend3ds
stars: 9
systems:
- 3DS
title: LocalSend3DS
unique_ids:
- '0xF5D53'
update_notes: '<p dir="auto">LocalSend3DS v1.1.0 introduces five built-in themes,
  bringing more ways to customize the app while keeping its existing file transfer
  functionality unchanged.</p>

  <h3 dir="auto">What''s new</h3>

  <p dir="auto">Five built-in themes are now available:</p>

  <ul dir="auto">

  <li><strong>Light</strong> - The original LocalSend3DS appearance</li>

  <li><strong>Dark</strong> - A darker interface</li>

  <li><strong>OLED Black</strong> - A black-focused theme</li>

  <li><strong>Yaru Light</strong> - Inspired by Ubuntu''s Yaru color palette</li>

  <li><strong>Yaru Dark</strong> - A dark variant inspired by Yaru</li>

  </ul>

  <p dir="auto">Themes can be changed in <strong>Settings → Theme</strong> using touch
  or physical controls. Your selection is saved and restored when you restart the
  app.</p>

  <p dir="auto">The original Light theme remains the default for new installations
  and existing v1.0.0 configurations. Other settings are preserved when upgrading.</p>

  <p dir="auto">Custom user-made themes are not supported in this release.</p>

  <h3 dir="auto">Compatibility &amp; testing</h3>

  <ul dir="auto">

  <li>Both <code class="notranslate">.3dsx</code> and <code class="notranslate">.cia</code>
  builds tested on real <strong>New Nintendo 2DS XL</strong> hardware</li>

  <li>Upgrading the CIA from v1.0.0 preserves existing settings</li>

  <li>Theme switching and persistence verified</li>

  <li>File sending and receiving tested successfully</li>

  </ul>

  <p dir="auto">The existing LocalSend transfer functionality remains unchanged.</p>

  <h3 dir="auto">Current limitations</h3>

  <ul dir="auto">

  <li>PIN-protected recipients are not supported</li>

  <li>Multiple files, folders, text, and clipboard transfers are not supported</li>

  <li>Incoming transfers use HTTP; incoming HTTPS is not supported</li>

  <li>Correct Nintendo 3DS system date and time are required for outgoing TLS certificate
  validation</li>

  </ul>

  <h3 dir="auto">Downloads</h3>

  <p dir="auto">Download the <code class="notranslate">.cia</code> or <code class="notranslate">.3dsx</code>
  file below, depending on your preferred installation method.</p>

  <p dir="auto">See <code class="notranslate">SHA256SUMS</code> for release file checksums.</p>

  <h3 dir="auto">Thank you!</h3>

  <p dir="auto">LocalSend3DS has surpassed <strong>1,000 GitHub release binary downloads</strong>
  since its first public release!</p>

  <p dir="auto">Thank you to everyone who downloaded the app, tried it on their 3DS,
  shared feedback, or suggested improvements.</p>

  <p dir="auto">It''s been great to see this little homebrew project reach this milestone.
  I really appreciate your support!</p>'
updated: '2026-11-11T21:41:47Z'
version: v1.1.0
version_title: LocalSend3DS v1.1.0
---
LocalSend3DS is an unofficial LocalSend-compatible client for the Nintendo 3DS family.

It supports bidirectional discovery and one-file transfers with official LocalSend clients. Incoming transfers use HTTP, while outgoing transfers support HTTP and fingerprint-pinned HTTPS with mutual TLS.

Real-hardware interoperability has been verified with macOS, Linux, and Android.

PIN-protected recipients, multiple files, folders, text, clipboard transfers, and incoming HTTPS are not currently supported.