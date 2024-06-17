---
author: Alex Taber
avatar: https://avatars.githubusercontent.com/u/7305572?v=4
categories:
- utility
color: '#5a9cc8'
color_bg: '#396380'
created: '2017-07-10T21:48:13Z'
description: A theme and boot splash manager for the Nintendo 3DS console
download_page: https://github.com/astronautlevel2/Anemone3DS/releases
downloads:
  Anemone3DS.3dsx:
    size: 1721836
    size_str: 1 MiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v3.0.0/Anemone3DS.3dsx
  Anemone3DS.cia:
    size: 1733568
    size_str: 1 MiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v3.0.0/Anemone3DS.cia
github: astronautlevel2/Anemone3DS
icon: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/icon.png
image: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/banner.png
image_length: 152331
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  Anemone3DS.cia: https://db.universal-team.net/assets/images/qr/anemone3ds-cia.png
screenshots:
- description: Get themes mode
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/get-themes-mode.png
- description: Theme list
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/theme-list.png
source: https://github.com/astronautlevel2/Anemone3DS
systems:
- 3DS
title: Anemone3DS
unique_ids:
- '0xBAFE0'
update_notes: '<p dir="auto">About a month after the beta, we''re now releasing the
  full Anemone3DS v3.0.0 - the first major release of Anemone3DS in ~6 years! Without
  further ado, let''s get into the release notes. Things which are new from v3.0.0b
  will be bolded to indicate the new features.</p>

  <h2 dir="auto">Bugfixes</h2>

  <ul dir="auto">

  <li>Fixed various errors when downloading themes via the QR code reader

  <ul dir="auto">

  <li>Fix bug with files with * in their name (by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/Zemogiter/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Zemogiter">@Zemogiter</a>)</li>

  <li>Fix bugs with Unicode filenames</li>

  <li>Allow x-zip-compressed to be a valid Mime type</li>

  </ul>

  </li>

  <li>Disable home button after installing theme; this was deemed to be the root of
  a number of corruption issues</li>

  <li><strong>A failed search in the ThemePlaza browser now properly returns you to
  the previous page rather than locking the browser in a glitched state.</strong></li>

  <li><strong>Various scroll/jump bugs fixed</strong></li>

  </ul>

  <h2 dir="auto">New Features</h2>

  <ul dir="auto">

  <li><strong>Full badge support! Anemone3DS now supports installing badges, complete
  with custom sets and set icons. Additionally supports dumping badges, maintaining
  the set they''re from and also dumping the set icon. For more info, check out <a
  href="https://github.com/astronautlevel2/Anemone3DS/wiki/Badges">our wiki</a>.</strong></li>

  <li>Translation framework allowing for Anemone3DS to be displayed in your native
  language! Currently only Spanish, Portugese, and French are present, but we''re
  accepting PRs for more languages - feel free to message me or ping me on the ThemePlaza
  or Nintendo Homebrew discords if you want instructions!

  <ul dir="auto">

  <li>Added French translation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/cooolgamer/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a></li>

  <li>Added Portuguese translation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/iveurne/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/iveurne">@iveurne</a></li>

  <li><strong>Added Spanish translation by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Tristanabs/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Tristanabs">@Tristanabs</a>,
  Angelpro09_xd, and <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Gatokun/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Gatokun">@Gatokun</a></strong></li>

  </ul>

  </li>

  <li>Add libcurl fallback so that Anemone can scan QR Codes from anywhere - not just
  HTTP websites.</li>

  <li><strong>BCSTM Player added for theme previews, meaning that Anemone3DS should
  now more accurately represent what will be played on the Home Menu, and allowing
  for easier testing with tools like Kame Editor which don''t produce a preview ogg
  file.</strong></li>

  <li>Support for Korean region systems using the home menu patch (thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/cooolgamer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a>)</li>

  <li>Assemble a splash preview if none was found (thanks to <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/Jan200101/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Jan200101">@Jan200101</a>)</li>

  <li>Significant performance improvements, especially when scrolling between many
  themes</li>

  <li>New User Interface which should be both more intuitive (no more button combos!)
  and also more touch-screen friendly</li>

  <li>Respect Parental Controls which lock the user out of the browser and require
  a PIN on access if that restriction is enabled</li>

  <li>Warn the user on installing a theme with mono audio - this can cause many audio
  issues with the home menu</li>

  </ul>

  <h2 dir="auto">New Contributors</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Zemogiter/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Zemogiter">@Zemogiter</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2134172308" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/294"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/294/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/294">#294</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/cooolgamer/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1718116437" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/290"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/290/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/290">#290</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Jan200101/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Jan200101">@Jan200101</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="1393458348" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/277"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/277/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/277">#277</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/iveurne/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/iveurne">@iveurne</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2293607887" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/307"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/307/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/307">#307</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Tristanabs/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Tristanabs">@Tristanabs</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2328401594" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/312"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/312/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/312">#312</a></li>

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Gatokun/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Gatokun">@Gatokun</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="2341276117" data-permission-text="Title is private" data-url="https://github.com/astronautlevel2/Anemone3DS/issues/315"
  data-hovercard-type="pull_request" data-hovercard-url="/astronautlevel2/Anemone3DS/pull/315/hovercard"
  href="https://github.com/astronautlevel2/Anemone3DS/pull/315">#315</a></li>

  <li>An especially big thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/cooolgamer/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a>
  for all their testing; without them this release wouldn''t have been possible.</li>

  </ul>

  <h2 dir="auto">QR Download Code</h2>

  <p dir="auto"></p>

  <h2 dir="auto">A Personal Note</h2>

  <p dir="auto">When I initially created Anemone3DS I wasn''t in a great state of
  mind, and the project was something for me to pour myself into and forget about
  everything around me. I never expected it would end up becoming as widely used as
  it has; it''s genuinely incredible to look back on. Thank you all so, so much for
  all of your support and encouragement over the years, this community has genuinely
  changed my life.</p>'
updated: '2024-06-14T17:52:47Z'
version: v3.0.0
version_title: 'Anemone3DS: Beyond Journey''s End'
wiki: https://github.com/astronautlevel2/Anemone3DS/wiki
---
