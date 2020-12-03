---
author: astronautlevel2
categories:
- utility
color: '#5a9cc8'
created: '2017-07-10T21:48:13Z'
description: A theme and boot splash manager for the Nintendo 3DS console
download_page: https://github.com/astronautlevel2/Anemone3DS/releases/tag/v2.1.0
downloads:
  Anemone3DS.3dsx:
    size: 621724
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.1.0/Anemone3DS.3dsx
  Anemone3DS.cia:
    size: 1020864
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.1.0/Anemone3DS.cia
  Anemone3DS.elf:
    size: 2815952
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.1.0/Anemone3DS.elf
  Anemone3DS.smdh:
    size: 14016
    url: https://github.com/astronautlevel2/Anemone3DS/releases/download/v2.1.0/Anemone3DS.smdh
github: astronautlevel2/Anemone3DS
icon: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/icon.png
image: https://raw.githubusercontent.com/astronautlevel2/Anemone3DS/master/meta/banner.png
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  Anemone3DS.cia: https://db.universal-team.net/assets/images/qr/anemone3ds.cia.png
screenshots:
- description: Get themes mode
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/get-themes-mode.png
- description: Theme list
  url: https://db.universal-team.net/assets/images/screenshots/anemone3ds/theme-list.png
source: https://github.com/astronautlevel2/Anemone3DS
systems:
- 3DS
title: Anemone3DS
update_notes: '<h1>NOTE: This release removes support for themes which don''t use
  an info.smdh file. Most themes use this file, including all themes from ThemePlaza,
  so I''m not expecting it to be an issue - if it is an issue, I can revert this change,
  but note that themes without an info.smdh are prone to cause crashes.</h1>

  <p>It''s been a while since the last update to Anemone3DS! We''re releasing a new
  edition to the software which should patch a number of outstanding bugs.</p>

  <p>As per usual, bugfixes:</p>

  <ul>

  <li>

  <p>Changed Title ID to not conflict with a game - this means you''ll <em>have to
  uninstall the old version of Anemone3DS after updating to v2.1.0</em>.</p>

  </li>

  <li>

  <p>Fixed various bugs caused by an outdated libarchive version.</p>

  </li>

  <li>

  <p>Fixed various bugs related to previous caused by lodepng by switching to libpng.</p>

  </li>

  <li>

  <p>Fixed race condition in icon scrolling.</p>

  </li>

  <li>

  <p>Fixed screen tearing in the QR reader.</p>

  </li>

  <li>

  <p>Fixed bug caused by playing music even when there was no theme preview.</p>

  </li>

  <li>

  <p>Fixed it being possible to try to preview themes/splashes even when there were
  no themes or splashes.</p>

  </li>

  <li>

  <p>Fixed bug caused by attempting to play audio when dspfirm wasn''t dumped.</p>

  </li>

  <li>

  <p>Fixed bug caused by attempting to install BGM for shuffle themes even when there
  was none.</p>

  </li>

  <li>

  <p>Fixed various bugs caused by not properly zeroing out files when creating them.</p>

  </li>

  <li>

  <p>Properly update the installed splash.</p>

  </li>

  </ul>

  <p>Bugs fixed since beta:</p>

  <ul>

  <li>

  <p>Fixed bug with QR initialization on o3ds/o2ds/n2dsxl. May still not be perfect,
  as I don''t have an o2ds test, but should be much improved based on reports from
  testers. Bug reports welcome.</p>

  </li>

  <li>

  <p>Updated to newest libctru version &amp; GCC version</p>

  </li>

  <li>

  <p>Patched memory leak in the preview code</p>

  </li>

  <li>

  <p>Updated to quirc v1.1, patching a segfault in the QR code reader</p>

  </li>

  <li>

  <p>Fix multiple race conditions involving the QR code reader which could potentially
  cause a crash when exiting camera mode</p>

  </li>

  <li>

  <p>Fix crash caused by quirc overflowing the 3DS stack when attempting to scan QR
  code like images that weren''t actually QR codes (such as mechanical keyboards)</p>

  </li>

  <li>

  <p>Fix double free which could potentially cause crashes when downloading from invalid
  zip files</p>

  </li>

  <li>

  <p>Fix QR download from sites other than ThemePlaza which used a different format
  for content disposition header</p>

  </li>

  <li>

  <p>Fix crashes caused by attempting to load invalid themes</p>

  </li>

  <li>

  <p>Fix memory leak in zip reading code</p>

  </li>

  <li>

  <p>Reset cursor when switching pages of the ThemePlaza browser to fix bug causing
  corruption.</p>

  </li>

  </ul>

  <p>Improvements:</p>

  <ul>

  <li>

  <p><strong>Huge improvements to the QR code reader''s speed.</strong> This is likely
  the fastest/smoothest it can possibly be (it''s now on-par with QRaken and FBI)
  thanks to a combination of improved multithreading and switching graphics libraries.</p>

  </li>

  <li>

  <p>Speaking of switching graphics libraries, we''ve completely switched from pp2d
  to citro2d! This allowed us to get the QR code reader substantially faster, as well
  as guarantees full support for the library in the future. Huge thanks to LiquidFenrir
  for doing most of the work of the change.</p>

  </li>

  <li>

  <p>Switch to using spritesheets to load the sprites rather than just loading them
  all into the romfs.</p>

  </li>

  <li>

  <p>Don''t wait for audio to finish loading before displaying the preview image,
  making previews display in the snappy fashion they used to before the audio player.</p>

  </li>

  <li>

  <p>Improved banner quality. Thanks to <a class="user-mention" data-hovercard-type="user"
  data-hovercard-url="/users/TurdPooCharger/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/TurdPooCharger">@TurdPooCharger</a>
  for this!</p>

  </li>

  </ul>

  <p>Additional credits:</p>

  <ul>

  <li>

  <p>Huge thanks to individuals on the Nintendo Homebrew server who helped test the
  new QR scanner on different consoles, especially Weeber#9048.</p>

  </li>

  <li>

  <p>Everyone who submitted bug reports through the beta program.</p>

  </li>

  </ul>

  <p>Final notes:</p>

  <p>It''s hard to believe that it''s already been almost three years since the initial
  release of Anemone3DS - it feels like it was just yesterday that I was pulling all
  nighters trying to get the app ready in time for my self-imposed deadline. So much
  has changed then, the support for the community has been incredible, and I''m incredibly
  grateful for all the help I''ve received from other developers. I''m hugely appreciative
  for everything everyone has done for me and for this application. I hope to continue
  to improve it in the future, adding more features and, importantly, squashing more
  bugs.</p>

  <p>This is probably the last release on this codebase! Hopefully, our next release
  will be using the rewrite codebase. This may still be a ways out, but we have nothing
  but time now, and will likely get started on it as soon as tomorrow.</p>

  <p>Finally, if there are any bugs, they can be reported on this issue tracker and
  one of us will be sure to get to them. If you''re not confident about posting an
  issue on the tracker, feel free to contact Asty#3336 on Discord - I''m on NH and
  ThemePlaza and will respond to your questions as soon as I see it.</p>

  <p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/2a22391a01beb1ad9178ac7543f7205be6ffee0ed2de3001d1bc6957184f5c60/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3637393930373030313031303039343135312f3732313934303232333534313337393037322f63616e7661732e706e67"><img
  src="https://camo.githubusercontent.com/2a22391a01beb1ad9178ac7543f7205be6ffee0ed2de3001d1bc6957184f5c60/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6174746163686d656e74732f3637393930373030313031303039343135312f3732313934303232333534313337393037322f63616e7661732e706e67"
  alt="canvas" data-canonical-src="https://cdn.discordapp.com/attachments/679907001010094151/721940223541379072/canvas.png"
  style="max-width:100%;"></a></p>'
updated: '2020-06-14T02:24:36Z'
version: v2.1.0
version_title: Revival Edition
wiki: https://github.com/astronautlevel2/Anemone3DS/wiki
---
