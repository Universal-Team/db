---
author: NateXS
avatar: https://avatars.githubusercontent.com/u/230057427?v=4
categories:
- emulator
- utility
color: '#c291a9'
color_bg: '#805f6f'
created: '2025-05-01T16:11:42Z'
description: Play Scratch games on your 3DS!
download_filter: (\.3dsx|\.cia|\.nds)
download_page: https://github.com/ScratchEverywhere/ScratchEverywhere/releases
downloads:
  scratch-3ds.3dsx:
    size: 10920548
    size_str: 10 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc3/scratch-3ds.3dsx
  scratch-3ds.cia:
    size: 9286592
    size_str: 8 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc3/scratch-3ds.cia
  scratch-ds.nds:
    size: 5643264
    size_str: 5 MiB
    url: https://github.com/ScratchEverywhere/ScratchEverywhere/releases/download/1.0-rc3/scratch-ds.nds
github: ScratchEverywhere/ScratchEverywhere
icon: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/icon.png
image: https://github.com/ScratchEverywhere/ScratchEverywhere/raw/refs/heads/main/gfx/3ds/banner.png
image_length: 30159
layout: app
license: lgpl-3.0
license_name: GNU Lesser General Public License v3.0
llm_generation: unknown
qr:
  scratch-3ds.cia: https://db.universal-team.net/assets/images/qr/scratch-3ds-cia.png
  scratch-ds.nds: https://db.universal-team.net/assets/images/qr/scratch-ds-nds.png
source: https://github.com/ScratchEverywhere/ScratchEverywhere
stars: 530
systems:
- 3DS
title: Scratch Everywhere!
unique_ids:
- '0x2143'
update_notes: '<h2 dir="auto">Runtime Changes</h2>

  <ul dir="auto">

  <li>Added support for custom extensions via Lua! (Via PR <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="4162634397" data-permission-text="Title
  is private" data-url="https://github.com/ScratchEverywhere/ScratchEverywhere/issues/594"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere/pull/594/hovercard"
  href="https://github.com/ScratchEverywhere/ScratchEverywhere/pull/594">#594</a>)

  <ul dir="auto">

  <li>This will make it way easier to port extensions from Scratch mods (e.g. TurboWarp)
  over to SE!</li>

  <li>We currently have TurboWarp''s <code class="notranslate">Gamepad</code>, <code
  class="notranslate">JSON</code> and <code class="notranslate">Utilities</code> extensions
  ported over, with more coming soon!</li>

  <li>Unlike native C++ extensions, Lua extensions support way more platforms!

  <ul dir="auto">

  <li>They are currently NOT supported on NDS, PSP, PS4, or Libretro. PSP and PS4
  may get support in a later release, but NDS will not due to RAM limits.</li>

  </ul>

  </li>

  <li>The extensions are compiled in a custom <code class="notranslate">.see</code>
  (<strong>S</strong>cratch <strong>E</strong>verywhere! <strong>E</strong>xtension)
  file format, for easy distribution!</li>

  <li>This release will have the above TurboWarp extensions packed in the executable,
  so all you need to do is run a project using one of those extensions and it should
  just work.

  <ul dir="auto">

  <li>Do note that future releases will NOT have the extensions included once we figure
  out a good way to distribute/download them separately.</li>

  </ul>

  </li>

  <li>You can also load extensions by putting the <code class="notranslate">.see</code>
  extension file inside of <code class="notranslate">(SE!-folder)/extensions/</code>.</li>

  <li>Lua extensions are located in the <a href="https://github.com/ScratchEverywhere/lua-extensions">lua-extensions
  repo</a>, with the <code class="notranslate">.see</code> compiler located in the
  <a href="https://github.com/ScratchEverywhere/seec">seec repo</a>.</li>

  <li>The Lua extensions API are <a href="https://github.com/ScratchEverywhere/ScratchEverywhere.github.io/pull/2"
  data-hovercard-type="pull_request" data-hovercard-url="/ScratchEverywhere/ScratchEverywhere.github.io/pull/2/hovercard">currently
  a W.I.P</a>. and not yet released at the time of writing :(</li>

  </ul>

  </li>

  <li>Fixed audio not playing in unzipped projects</li>

  </ul>

  <h2 dir="auto">Menu Changes</h2>

  <ul dir="auto">

  <li>Removed birthday theme</li>

  <li>Added French and Polish languages</li>

  </ul>

  <h2 dir="auto">3DS Changes</h2>

  <ul dir="auto">

  <li>Fixed crash when closing the app</li>

  <li>Fixed hang when trying to close the app when inside certain projects</li>

  </ul>

  <h2 dir="auto">Authors</h2>

  <p dir="auto">This release was brought to you by: <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Starlii10/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Starlii10">@Starlii10</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/ccawley2011/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ccawley2011">@ccawley2011</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Dogo6647/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Dogo6647">@Dogo6647</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/gradylink/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gradylink">@gradylink</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/NateXS/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NateXS">@NateXS</a><br>

  Translators: <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/matu6968/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/matu6968">@matu6968</a>
  (polish), <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SimsCrafterZ/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SimsCrafterZ">@SimsCrafterZ</a>
  (french)</p>'
updated: '2026-06-08T03:00:04Z'
version: 1.0-rc3
version_title: 1.0 Release Candidate 3
---
A custom Scratch runtime that allows you to run Scratch 3 projects on your 3DS!