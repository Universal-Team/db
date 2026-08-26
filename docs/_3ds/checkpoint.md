---
author: Bernardo Giordano
avatar: https://avatars.githubusercontent.com/u/17624378?v=4
categories:
- utility
color: '#40576f'
color_bg: '#40576f'
created: '2017-09-06T17:20:55Z'
description: Fast and simple homebrew save management framework for 3DS and Switch.
download_page: https://github.com/BernardoGiordano/Checkpoint/releases
downloads:
  Checkpoint.3dsx:
    size: 3569484
    size_str: 3 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.2.0/Checkpoint.3dsx
  Checkpoint.cia:
    size: 2593728
    size_str: 2 MiB
    url: https://github.com/BernardoGiordano/Checkpoint/releases/download/v5.2.0/Checkpoint.cia
github: BernardoGiordano/Checkpoint
icon: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/icon.png
image: https://raw.githubusercontent.com/BernardoGiordano/Checkpoint/master/3ds/assets/banner.png
image_length: 5618
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  Checkpoint.cia: https://db.universal-team.net/assets/images/qr/checkpoint-cia.png
source: https://github.com/BernardoGiordano/Checkpoint
stars: 3056
systems:
- 3DS
title: Checkpoint
unique_ids:
- '0xBCFFF'
update_notes: '<h3 dir="auto">Updates: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>autoupdater</strong> (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="332533639" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/106"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/106/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/106">#106</a>).

  <ul dir="auto">

  <li>The check runs in the background, so the title list still loads while it happens.
  Nothing is ever installed without you agreeing to it first.</li>

  <li>Automatic updates are on by default and can be turned off in Settings.</li>

  <li>Fun fact: this was the oldest open feature request on the repository. It was
  filed in June 2018. Eight years is a long time to wait, but here it is.</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Switch: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>MTP USB transfers</strong>. Plug the console into your PC with
  the charging cable and Checkpoint shows up as a portable device, exactly like a
  phone or a camera does.

  <ul dir="auto">

  <li>Turn it on in Settings &gt; Connectivity, under <strong>USB (MTP)</strong>.
  It''s off by default, and the line underneath tells you its status: waiting for
  a PC, connected, or USB unavailable.</li>

  <li>USB unavailable usually means the console is docked or something else has already
  claimed the port. Checkpoint keeps trying in the background, so undocking is enough:
  no restart needed.</li>

  </ul>

  </li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <h3 dir="auto">3DS: What''s new</h3>

  <ul dir="auto">

  <li>Added: <strong>the Internet Browser is back in the title list</strong> (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5131929318" data-permission-text="Title
  is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/579"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/579/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/579">#579</a>), so its
  save data can be backed up and restored like any other title''s. It used to be hidden
  away with the manuals and the update titles.</li>

  <li>Added: an empty title list now says so, and tells you how to load it again,
  instead of showing you a blank screen with no explanation (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="5165128832" data-permission-text="Title
  is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/580"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/580/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/580">#580</a>).</li>

  <li>Fixed: <strong>Backup and Restore now fill the row properly when wireless transfer
  is turned off</strong>. The Send button''s slot used to stay behind as an empty
  gap. The two buttons now split the space between them, which also leaves room for
  the full "Backup" and "Restore" wording instead of the shortened labels.</li>

  <li>Added: <strong>notifications</strong>, a script that backs up and restores everything
  behind the Notifications applet (3DS, <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="5131929318" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/579"
  data-hovercard-type="issue" data-hovercard-url="/BernardoGiordano/Checkpoint/issues/579/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/issues/579">#579</a>).

  <ul dir="auto">

  <li>The SpotPass content and the notification list don''t belong to a title, so
  nothing in Checkpoint could reach it before.</li>

  </ul>

  </li>

  <li>Added: <strong>citrahold</strong>, a script that syncs your save and extdata
  backups with a 3rd party service called <a href="https://www.citrahold.com" rel="nofollow">Citrahold</a>
  (3DS, <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="5231403028" data-permission-text="Title is private" data-url="https://github.com/BernardoGiordano/Checkpoint/issues/585"
  data-hovercard-type="pull_request" data-hovercard-url="/BernardoGiordano/Checkpoint/pull/585/hovercard"
  href="https://github.com/BernardoGiordano/Checkpoint/pull/585">#585</a>, thanks
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/solitonmedic/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/solitonmedic">@solitonmedic</a>),
  which we are not affiliated with.

  <ul dir="auto">

  <li>Setup is in <a href="https://github.com/FlagBrew/Checkpoint/blob/master/scripts/citrahold.md"><code
  class="notranslate">scripts/citrahold.md</code></a>.</li>

  </ul>

  </li>

  <li>Added: <code class="notranslate">sav_open_system</code>, a new API call that
  lets a script reach the console''s own system save data (3DS).</li>

  <li>Removed: holding B to reload the title list. <strong>Refresh title list</strong>
  is a normal entry in the SELECT menu now.</li>

  <li>General system stability improvements to enhance the user''s experience.</li>

  </ul>

  <hr>

  <p dir="auto">If you wish to contribute, pull requests are highly appreciated.</p>

  <hr>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/090a15f2-c434-4ecd-92e2-59f44778f99a"><img
  width="178" height="176" alt="immagine" src="https://github.com/user-attachments/assets/090a15f2-c434-4ecd-92e2-59f44778f99a"
  style="max-width: 100%; height: auto; max-height: 176px;; aspect-ratio: 178 / 176;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <hr>

  <p dir="auto"><a href="https://discord.gg/bGKEyfY" rel="nofollow"><img src="https://camo.githubusercontent.com/4072fe46d2eb0f8f41a49c5795b2b971f9402f61fe2438cf9f2cded9d2af6915/68747470733a2f2f646973636f72646170702e636f6d2f6170692f6775696c64732f3237383232323833343633333830313732382f7769646765742e706e673f7374796c653d62616e6e6572332674696d652d"
  alt="Discord" data-canonical-src="https://discordapp.com/api/guilds/278222834633801728/widget.png?style=banner3&amp;time-"
  style="max-width: 100%;"></a></p>'
updated: '2026-08-26T13:30:35Z'
version: v5.2.0
version_title: Checkpoint 5.2.0
---
