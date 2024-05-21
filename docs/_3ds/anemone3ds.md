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
    size: 644612
    size_str: 629 KiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.3.1/Anemone3DS.3dsx
  Anemone3DS.cia:
    size: 1041344
    size_str: 1016 KiB
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.3.1/Anemone3DS.cia
github: astronautlevel2/Anemone3DS
icon: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/icon.png
image: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/banner.png
image_length: 152331
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
prerelease:
  download_page: https://github.com/astronautlevel2/Anemone3DS/releases/tag/v3.0.0b
  downloads:
    Anemone3DS.3dsx:
      size: 1623972
      size_str: 1 MiB
      url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v3.0.0b/Anemone3DS.3dsx
    Anemone3DS.cia:
      size: 1663936
      size_str: 1 MiB
      url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v3.0.0b/Anemone3DS.cia
  qr:
    Anemone3DS.cia: https://db.universal-team.net/assets/images/qr/prerelease/anemone3ds-cia.png
  update_notes: '<p dir="auto">I doubt many people were expecting a new Anemone3DS
    release - frankly I didn''t really expect to do more work on it, but life''s funny
    like that I guess. This is probably the biggest update we''ve done in a long while,
    and I haven''t had the time to test everything thoroughly, so we''re going to
    release it as a pre-release first and hope nothing breaks too bad 😄. I also want
    a few more languages supported (ideally Spanish and Japanese) before the full
    release, but more on that later!</p>

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

    <li>Disable home button after installing theme; this was deemed to be the root
    of a number of corruption issues</li>

    </ul>

    <h2 dir="auto">New Features</h2>

    <ul dir="auto">

    <li>Translation framework allowing for Anemone3DS to be displayed in your native
    language! Currently only Portugese and French are present, but we''re accepting
    PRs for more languages - feel free to message me or ping me on ThemePlaza or Nintendo
    Homebrew if you want instructions!

    <ul dir="auto">

    <li>Added French translation by <a class="user-mention notranslate" data-hovercard-type="user"
    data-hovercard-url="/users/cooolgamer/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a></li>

    <li>Added Portuguese translation by <a class="user-mention notranslate" data-hovercard-type="user"
    data-hovercard-url="/users/iveurne/hovercard" data-octo-click="hovercard-link-click"
    data-octo-dimensions="link_type:self" href="https://github.com/iveurne">@iveurne</a></li>

    </ul>

    </li>

    <li>Support for Korean region systems using the home menu patch (thanks to <a
    class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/cooolgamer/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/cooolgamer">@cooolgamer</a>)</li>

    <li>assemble a splash preview if none was found (thanks to <a class="user-mention
    notranslate" data-hovercard-type="user" data-hovercard-url="/users/Jan200101/hovercard"
    data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Jan200101">@Jan200101</a>)</li>

    <li>Significant performance improvements, especially when scrolling between many
    themes</li>

    <li>New User Interface which should be both more intuitive (no more button combos!)
    and also more touch-screen friendly</li>

    <li>Respect Parental Controls which lock the user out of the browser and require
    a PIN on access if that restriction is enabled</li>

    <li>Warn the user on installing a theme with mono audio - this can cause many
    audio issues with the home menu</li>

    <li>Add libcurl fallback so that Anemone can scan QR Codes from anywhere - not
    just HTTP websites.</li>

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

    </ul>

    <p dir="auto">Thanks to everyone who''s been along for the ride and made Anemone3DS
    the success it is, I truly appreciate all of you. Hopefully I''m able to get this
    out of beta soon.</p>

    <h2 dir="auto">QR Download</h2>

    '
  update_notes_md: "I doubt many people were expecting a new Anemone3DS release -\
    \ frankly I didn't really expect to do more work on it, but life's funny like\
    \ that I guess. This is probably the biggest update we've done in a long while,\
    \ and I haven't had the time to test everything thoroughly, so we're going to\
    \ release it as a pre-release first and hope nothing breaks too bad :smile:. I\
    \ also want a few more languages supported (ideally Spanish and Japanese) before\
    \ the full release, but more on that later!\n\n## Bugfixes\n* Fixed various errors\
    \ when downloading themes via the QR code reader\n  * Fix bug with files with\
    \ * in their name (by @Zemogiter)\n  * Fix bugs with Unicode filenames\n  * Allow\
    \ x-zip-compressed to be a valid Mime type\n* Disable home button after installing\
    \ theme; this was deemed to be the root of a number of corruption issues\n\n##\
    \ New Features\n* Translation framework allowing for Anemone3DS to be displayed\
    \ in your native language! Currently only Portugese and French are present, but\
    \ we're accepting PRs for more languages - feel free to message me or ping me\
    \ on ThemePlaza or Nintendo Homebrew if you want instructions!\n  * Added French\
    \ translation by @cooolgamer\n  * Added Portuguese translation by @iveurne\n*\
    \ Support for Korean region systems using the home menu patch (thanks to @cooolgamer)\n\
    * assemble a splash preview if none was found (thanks to @Jan200101)\n* Significant\
    \ performance improvements, especially when scrolling between many themes\n* New\
    \ User Interface which should be both more intuitive (no more button combos!)\
    \ and also more touch-screen friendly\n* Respect Parental Controls which lock\
    \ the user out of the browser and require a PIN on access if that restriction\
    \ is enabled\n* Warn the user on installing a theme with mono audio - this can\
    \ cause many audio issues with the home menu\n* Add libcurl fallback so that Anemone\
    \ can scan QR Codes from anywhere - not just HTTP websites.\n\n## New Contributors\n\
    * @Zemogiter made their first contribution in https://github.com/astronautlevel2/Anemone3DS/pull/294\n\
    * @cooolgamer made their first contribution in https://github.com/astronautlevel2/Anemone3DS/pull/290\n\
    * @Jan200101 made their first contribution in https://github.com/astronautlevel2/Anemone3DS/pull/277\n\
    * @iveurne made their first contribution in https://github.com/astronautlevel2/Anemone3DS/pull/307\n\
    \nThanks to everyone who's been along for the ride and made Anemone3DS the success\
    \ it is, I truly appreciate all of you. Hopefully I'm able to get this out of\
    \ beta soon. \n\n## QR Download\n<img src=\"https://github.com/astronautlevel2/Anemone3DS/assets/7305572/36d96105-40f4-49f6-a29f-9368a7b5de4a\"\
    \ data-canonical-src=\"https://github.com/astronautlevel2/Anemone3DS/assets/7305572/36d96105-40f4-49f6-a29f-9368a7b5de4a\"\
    \ width=\"300\" height=\"300\" />"
  updated: '2024-05-21T01:58:27Z'
  version: v3.0.0b
  version_title: 'Anemone3DS: Beyond Journey''s End Beta'
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
update_notes: '<p dir="auto">Sup gamers, just a patch release this time around. Of
  note this time around is that, if you have dumped official themes in the past, it
  didn''t actually work - so you may have to scramble around and dump them again.
  Sorry about that.</p>

  <h2 dir="auto">In this patch</h2>

  <ul dir="auto">

  <li>Dumping and then installing official themes caused a crash because the themes
  were never actually dumped; <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/LiquidFenrir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/LiquidFenrir">@LiquidFenrir</a>
  patched it.</li>

  <li>There were some problems with our audio thread, including not being joined back
  to the main thread on exit, causing bizarre crashes; that''s been patched, again
  by <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/LiquidFenrir/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/LiquidFenrir">@LiquidFenrir</a>.</li>

  <li>Some of you may have noticed that the error <code class="notranslate">FS Error:
  ...</code> would appear when downloading themes with certain special characters
  in them. That was my (<a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/Helloman892/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Helloman892">@Helloman892</a>''s)
  fault in v2.3.0, and you know what''s next: patched.</li>

  <li>Somewhat related to the above, searching for special characters in the TP browser
  has been broken for a while. Patched.</li>

  <li>There was another bug introduced in v2.3.0 as part of the networking overhaul;
  a useless-to-the-user 404 would be shown if a theme preview in the browser had no
  BGM. Patched.</li>

  <li>The Theme Plaza browser should crash less where previews are involved, thanks
  to yet another patch from <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/LiquidFenrir/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/LiquidFenrir">@LiquidFenrir</a>,
  without whom this patch release wouldn''t be happening.</li>

  </ul>

  <p dir="auto">That besides, sorry this took a while to come out, and especially
  sorry for so many of you thinking you needed to get a new SD card! I really should
  have made that error more descriptive...</p>

  <h2 dir="auto">And here''s a download QR to use with FBI</h2>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://user-images.githubusercontent.com/1565516/182042894-01d35270-5726-4d66-b940-77987fee7777.png"><img
  src="https://user-images.githubusercontent.com/1565516/182042894-01d35270-5726-4d66-b940-77987fee7777.png"
  alt="frame" style="max-width: 100%;"></a></p>'
updated: '2022-07-31T19:54:46Z'
version: v2.3.1
version_title: Anemone3DS Patchwork Update
wiki: https://github.com/astronautlevel2/Anemone3DS/wiki
---
