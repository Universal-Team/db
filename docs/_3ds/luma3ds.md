---
author: LumaTeam
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/65085206?v=4
categories:
- utility
- firm
- luma3ds
color: '#82e5d9'
color_bg: '#488079'
created: '2016-02-08T02:26:12Z'
description: Noob-proof (N)3DS "Custom Firmware"
download_page: https://github.com/LumaTeam/Luma3DS/releases
downloads:
  Luma3DSv10.3.zip:
    size: 367144
    size_str: 358 KiB
    url: https://github.com/LumaTeam/Luma3DS/releases/download/v10.3/Luma3DSv10.3.zip
github: LumaTeam/Luma3DS
icon_index: 146
image: https://avatars.githubusercontent.com/u/65085206?v=4
image_length: 17885
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LumaTeam/Luma3DS
systems:
- 3DS
title: Luma3DS
update_notes: '<ul dir="auto">

  <li>Add more detailed battery percentage, plus battery voltage and temperature</li>

  <li>Add an option to dump the DSP firmware from Home Menu, effectively making programs
  like <code>DSP1</code> obsolete</li>

  <li>Split NTP and user time offset nullification. This means two things:

  <ul dir="auto">

  <li>Time changes are immmediately visible and you do not need to reboot your console
  after using the feature anymore (although Home Menu might not always immmediately
  display the new time -- just open and close an application in that case)</li>

  <li>Programs like <code>ctr-no-timeoffset</code> should not be needed anymore. Also,
  even if 3ds.hacks.guide recommends it and GodMode9 mandates it, time offset nullification
  should <em>not</em> be done</li>

  </ul>

  </li>

  <li>Also improve the precision of the NTP client implementation and fix a few bugs.
  It can be precise as +- 1ms (usually), although some of this precision is lost when
  rebooting</li>

  <li>Do not initialize the screens in the very common case the user has only one
  payload in the <code>/luma/payloads</code> folder, effectively working around a
  long-standing bug</li>

  <li>Fix reading emuNAND sector 0 for RedNAND and Gateway-style emuNAND (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1036563625" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1687" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1687/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1687">#1687</a>,
  <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

  <li>Fix a few bugs in the cheat system (<a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="855169992" data-permission-text="Title is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1623"
  data-hovercard-type="pull_request" data-hovercard-url="/LumaTeam/Luma3DS/pull/1623/hovercard"
  href="https://github.com/LumaTeam/Luma3DS/pull/1623">#1623</a>, <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/s5bug/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/s5bug">@s5bug</a>)</li>

  <li>Add ASCII View to Rosalina Process List (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1091294296" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1703" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1703/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1703">#1703</a>,
  <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/George-lewis/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/George-lewis">@George-lewis</a>)</li>

  <li>Allow using game-patching on Home Menu (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="911807068" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1634" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1634/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1634">#1634</a>,
  <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/gabe565/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gabe565">@gabe565</a>)</li>

  <li>Wait for the user to release the B key when exiting the Rosalina menu. This
  should prevent games to think the B key has been pressed (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="1087351954" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1701" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1701/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1701">#1701</a>,
  suggestion from <a class="user-mention" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)</li>

  <li>gdb: properly handle software breakpoints</li>

  <li>General system stability improvements to enhance the user''s experience</li>

  </ul>'
updated: '2022-03-16T22:37:49Z'
version: v10.3
version_title: v10.3
wiki: https://github.com/LumaTeam/Luma3DS/wiki
---
