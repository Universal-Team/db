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
    size: 8174516
    size_str: 7 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.2/PKSM.3dsx
  PKSM.cia:
    size: 6841280
    size_str: 6 MiB
    url: https://github.com/FlagBrew/PKSM/releases/download/10.4.2/PKSM.cia
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
stars: 2275
systems:
- 3DS
title: PKSM
unique_ids:
- '0xEC100'
update_notes: '<h2 dir="auto">What''s new</h2>

  <ul dir="auto">

  <li>Fixed: <strong>PKSM failing to start with error <code class="notranslate">0xC8804464</code>
  or <code class="notranslate">std::bad_alloc</code>, even after a clean reinstall</strong>
  (fix <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="5433181894" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1581"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1581/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1581">#1581</a>, fix <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5973122826" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1597" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1597/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1597">#1597</a>)

  <ul dir="auto">

  <li>Both were caused by a corrupted PKSM extdata, which is not removed when PKSM
  is uninstalled or reinstalled</li>

  <li>PKSM now detects it on boot and asks whether to reset it. Storage banks kept
  in the extdata will be lost, as they were already unreadable</li>

  </ul>

  </li>

  <li>Fixed: <strong>the additional assets download failing with error <code class="notranslate">0xFFFFFE6D</code>
  on some consoles</strong> (fix <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5624575241" data-permission-text="Title is private" data-url="https://github.com/FlagBrew/PKSM/issues/1586"
  data-hovercard-type="issue" data-hovercard-url="/FlagBrew/PKSM/issues/1586/hovercard"
  href="https://github.com/FlagBrew/PKSM/issues/1586">#1586</a>)

  <ul dir="auto">

  <li>When the main CDN turns your console away, PKSM now falls back to a mirror on
  GitHub. Downloaded assets are still verified before being used</li>

  </ul>

  </li>

  <li>Fixed: extra saves added or removed not being remembered after restarting PKSM,
  unless an unrelated setting was changed as well (fix <a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="5840995969" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/1594" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/1594/hovercard" href="https://github.com/FlagBrew/PKSM/issues/1594">#1594</a>)</li>

  <li>Fixed: Gen 1/2/3 items turning into a different item or disappearing when edited
  in the bag, Gen 3 HMs included</li>

  <li>Fixed: Gen 1 bags showing leftover items that had already been tossed</li>

  <li>Fixed: items losing their marks, such as new and favourite, when the bag is
  edited in Gen 7</li>

  <li>Fixed: editing the bag leaving stale data behind in the slots of Sword/Shield</li>

  <li>Fixed: item lists drifting from what the games actually accept

  <ul dir="auto">

  <li>Sword/Shield now include the Crown Tundra key items (Reins of Unity, Legendary
  Clues, Crown Pass and more), Galarica Wreath, Dynite Ore and Ability Patch, and
  no longer list duplicates</li>

  <li>Emerald, FireRed/LeafGreen and Omega Ruby/Alpha Sapphire no longer list key
  items from other games, and X/Y now include the Poké Flute</li>

  </ul>

  </li>

  <li>Fixed: the <code class="notranslate">swarms</code> script now shows the right
  swarms for HeartGold or SoulSilver, instead of listing both games'' at once</li>

  <li>Fixed: the <code class="notranslate">inject-bank-to-dex</code> script always
  failing with "Impossible Ball" on Gen 3 saves (fix PKSM-Scripts <a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="192586456" data-permission-text="Title
  is private" data-url="https://github.com/FlagBrew/PKSM/issues/65" data-hovercard-type="issue"
  data-hovercard-url="/FlagBrew/PKSM/issues/65/hovercard" href="https://github.com/FlagBrew/PKSM/issues/65">#65</a>)</li>

  <li>All submodules and build dependencies updated to latest release</li>

  <li>General system stability improvements to enhance the user''s experience</li>

  </ul>

  <p dir="auto">Thanking <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Omar-Kay/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Omar-Kay">@Omar-Kay</a>
  for the contributions to <a href="https://github.com/FlagBrew/PKSM-Core">PKSM-Core</a>
  and <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/SpiredMoth/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SpiredMoth">@SpiredMoth</a>
  for the contributions to <a href="https://github.com/FlagBrew/PKSM-Scripts">PKSM-Scripts</a>.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/5a71f1c9-b620-4732-8acb-ac0851f7e44f"><img
  width="200" height="200" alt="qr" src="https://github.com/user-attachments/assets/5a71f1c9-b620-4732-8acb-ac0851f7e44f"
  style="max-width: 100%; height: auto; max-height: 200px;; aspect-ratio: 200 / 200;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-10-25T14:51:51Z'
version: 10.4.2
version_title: PKSM 10.4.2
wiki: https://github.com/FlagBrew/PKSM/wiki
---
