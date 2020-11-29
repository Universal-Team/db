---
author: Steveice10
categories:
- utility
color: '#c0d0ff'
created: '2015-01-20T04:23:49Z'
description: Open source title manager for the 3DS.
download_page: https://github.com/Steveice10/FBI/releases/tag/2.6.0
downloads:
  FBI.3dsx:
    size: 1133148
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.3dsx
  FBI.cia:
    size: 1151936
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.cia
  FBI.zip:
    size: 4128978
    url: https://github.com/Steveice10/FBI/releases/download/2.6.0/FBI.zip
github: Steveice10/FBI
icon: https://raw.githubusercontent.com/Steveice10/FBI/master/meta/icon_3ds.png
image: https://raw.githubusercontent.com/Steveice10/FBI/master/romfs/logo.png
layout: app
license: mit
license_name: MIT License
qr:
  FBI.cia: https://db.universal-team.net/assets/images/qr/fbi.cia.png
source: https://github.com/Steveice10/FBI
systems:
- 3DS
title: FBI
update_notes: '<ul>

  <li>Remove TitleDB support.</li>

  <li>Add TLSv1.2 support.

  <ul>

  <li>In testing, speeds were ~70-80kbps, which should be good enough for homebrew
  downloads.

  <ul>

  <li>I hope to investigate the matter further and improve speeds in the future, but
  wanted to finally get something out for the time being.</li>

  </ul>

  </li>

  <li>Downloads from sources that support earlier TLS versions (i.e. not GitHub) will
  continue to use the 3DS''s built-in HTTP stack, and thus should progress at the
  same speeds as before.</li>

  </ul>

  </li>

  <li>Revert the built-in updater back to using GitHub.</li>

  </ul>

  <p>Make sure to report any new issues caused by these changes. The issue ticket
  for TLSv1.2 support can be found <a href="https://github.com/Steveice10/FBI/issues/450"
  data-hovercard-type="issue" data-hovercard-url="/Steveice10/FBI/issues/450/hovercard">here</a>.</p>

  <p>Also, this update cannot be installed using the built-in updater, as the TitleDB
  servers are no longer available for previous versions of FBI to pull from. (<strong>UPDATE</strong>:
  The author of TitleDB has <a href="https://www.reddit.com/r/3dshacks/comments/aboq3j/fbi_release_260_removes_titledb_support_adds/ed3k6v1/"
  rel="nofollow">stated</a> that the TitleDB servers are now set up to serve the new
  FBI release to the updater, so older versions should be able to update in-app now.)</p>'
updated: '2019-01-02T01:41:35Z'
version: 2.6.0
version_title: 2.6.0
---
