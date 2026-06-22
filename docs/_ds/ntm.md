---
author: Pk11
avatar: https://avatars.githubusercontent.com/u/41608708?v=4
categories:
- utility
color: '#81de8e'
color_bg: '#4a8052'
created: '2022-01-09T06:28:39Z'
description: NAND Title Manager for DSi
download_page: https://github.com/Epicpkmn11/NTM/releases
downloads:
  NTM.dsi:
    size: 161280
    size_str: 157 KiB
    url: https://github.com/Epicpkmn11/NTM/releases/download/v0.5.0/NTM.dsi
github: Epicpkmn11/NTM
icon: https://raw.githubusercontent.com/Epicpkmn11/NTM/master/icon.png
image: https://raw.githubusercontent.com/Epicpkmn11/NTM/master/icon.png
image_length: 497
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
qr:
  NTM.dsi: https://db.universal-team.net/assets/images/qr/ntm-dsi.png
source: https://github.com/Epicpkmn11/NTM
stars: 86
systems:
- DS
title: NTM
unistore_exclude: true
update_notes: '<p dir="auto">So my Calico update was a bit hasty in dropping the custom
  ARM7 and turns out I completely broke ticket generation... 😅</p>

  <p dir="auto">This release fixes that and also save files being created with garbage
  data instead of zero filled! Thank you to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Nadeflore/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Nadeflore">@Nadeflore</a>
  for the bug reports and <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Riven-Spell/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Riven-Spell">@Riven-Spell</a>
  for the save file fix!</p>

  <p dir="auto">To make that easier and just generally cause I wanted to, I switched
  from devkitPro''s Calico to BlocksDS. This is a behind the scenes change that shouldn''t
  really affect the end user, though it did shove in my face a whole bunch of minor
  issues (mostly use after frees) that didn''t obviously break anything on devkitPro''s
  tooling but on BlocksDS outright crashed... well, good that they''re fixed now.</p>

  <p dir="auto">I also added support for the DS Pico! When you load NTM from DSi SD
  it''ll behave as before, but when you load from a DS Pico it''ll default to the
  Pico''s SD card and if you have an internal SD too it''ll give you the option to
  switch between them. Note that I did not currently do anything special for SDNAND
  mode so if you install a ROM on the Pico to SDNAND it will install it to hiya style
  SDNAND on the Pico''s SD... I don''t think that''s particularly useful so I may
  change that later.</p>'
updated: '2026-06-08T06:53:56Z'
version: v0.5.0
version_title: Bug fixes and BlocksDS
wiki: https://github.com/Epicpkmn11/NTM/wiki
---
NAND Title Manager, NTM for short, is an application for the Nintendo DSi that allows you to manage titles on your NAND. It can manage titles on both [hiyaCFW](https://wiki.ds-homebrew.com/hiyacfw/)'s SDNAND and your actual internal memory, typically called SysNAND. **When using in SysNAND mode please use with caution**.

Please see the [guide on the wiki](https://github.com/Epicpkmn11/NTM/wiki/How-to-Install-DSiWare) for how to properly and safely use NTM.