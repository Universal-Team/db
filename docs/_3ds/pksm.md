---
author: FlagBrew
avatar: https://avatars.githubusercontent.com/u/42673825?v=4
categories:
- utility
color: '#749285'
color_bg: '#658074'
created: '2016-05-15T08:26:47Z'
description: Gen I to GenVIII save manager.
download_page: https://github.com/FlagBrew/PKSM/releases
downloads:
  PKSM.3dsx:
    size: 8162004
    size_str: 7 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.1/PKSM.3dsx
  PKSM.cia:
    size: 6828992
    size_str: 6 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.1/PKSM.cia
github: FlagBrew/PKSM
icon: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/icon.png
image: https://raw.githubusercontent.com/FlagBrew/PKSM/master/assets/banner.png
image_length: 8070
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  PKSM.cia: https://db.universal-team.net/assets/images/qr/pksm-cia.png
source: https://github.com/FlagBrew/PKSM
stars: 2236
systems:
- 3DS
title: PKSM
unique_ids:
- '0xEC100'
update_notes: '<h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li>Added: Sword/Shield wonder cards now actually hand out the BP and the clothing
  they promise when injected</li>

  <li>Added: Gen 7 to Gen 8 transfers now carry handling trainer data, form duration
  and totem forms across correctly</li>

  <li>Added: every save format now reports whether its checksums are valid, so broken
  files are caught before they are loaded instead of half-loading</li>

  <li>Fixed: <strong>the camera not opening and freezing the app when scanning a QR
  code</strong> (fix <a class="issue-link js-issue-link" data-error-text="Failed to
  load title" data-id="5332685304" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1579"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1579/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1579">#1579</a>)

  <ul dir="auto">

  <li>The faster scanner introduced in 10.4.0 has been temporarily reverted while
  a proper fix is worked on</li>

  </ul>

  </li>

  <li>Fixed: Sword/Shield saves with an invalid hash being loaded instead of rejected</li>

  <li>Fixed: money, badges and BP being read from the wrong offsets in Sword/Shield
  saves</li>

  <li>Fixed: Pokémon being written to boxes unencrypted in Gen 4/5/6/7 saves, which
  the games read back as corrupted data</li>

  <li>Fixed: Pokédex seen and caught counts being computed incorrectly in Sword/Shield</li>

  <li>Fixed: Crown Tundra Pokémon looking up the wrong personal data entry</li>

  <li>Fixed: Gen 8 trades assigning the original trainer and the handling trainer
  the wrong way round</li>

  <li>Fixed: Gen 3 saves being loaded from the slot with an incomplete sector table</li>

  <li>Fixed: Gen 3 box writes going past the size of the stored entry</li>

  <li>Fixed: Korean Gen 2 strings being written at the wrong offset</li>

  <li>Fixed: Gen 2 list validation ignoring the capacity it was given</li>

  <li>Fixed: Sword/Shield block lookups reading past the end of the block table</li>

  <li>Removed: the fake handling trainer memory that was forged on every Gen 7 to
  Gen 8 transfer</li>

  <li>All submodules and build dependencies updated to latest release</li>

  <li>General system stability improvements to enhance the user''s experience</li>

  </ul>

  <p dir="auto">Thanking <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Omar-Kay/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Omar-Kay">@Omar-Kay</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Insektaure/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Insektaure">@Insektaure</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/nicooo-dev/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/nicooo-dev">@nicooo-dev</a>
  for the contributions to <a href="https://github.com/FlagBrew/PKSM-Core">PKSM-Core</a>.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/84a2aef0-70e2-4b45-b116-a2104b8157bd"><img
  width="182" height="181" alt="qr" src="https://github.com/user-attachments/assets/84a2aef0-70e2-4b45-b116-a2104b8157bd"
  style="max-width: 100%; height: auto; max-height: 181px;; aspect-ratio: 182 / 181;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-09-07T18:59:01Z'
version: 10.4.1
version_title: PKSM 10.4.1
wiki: https://github.com/FlagBrew/PKSM/wiki
---
