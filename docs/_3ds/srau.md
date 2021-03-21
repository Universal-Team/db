---
author: noirscape
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/13433513?v=4
categories:
- utility
- save-tool
color: '#ddbca2'
created: '2018-04-08T18:03:47Z'
description: 'Samus Returns: Amiibo Unlocker'
download_page: https://github.com/noirscape/SRAU/releases
downloads:
  SRAU.7z:
    size: 556954
    size_str: 543 KiB
    url: https://github.com/noirscape/SRAU/releases/download/v1.1/SRAU.7z
  SRAU.cia:
    size: 582592
    size_str: 568 KiB
    url: https://github.com/noirscape/SRAU/releases/download/v1.1/SRAU.cia
github: noirscape/SRAU
icon: https://raw.githubusercontent.com/noirscape/SRAU/master/meta/icon.png
image: https://raw.githubusercontent.com/noirscape/SRAU/master/meta/banner.png
image_length: 13110
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  SRAU.cia: https://db.universal-team.net/assets/images/qr/srau.cia.png
source: https://github.com/noirscape/SRAU
systems:
- 3DS
title: SRAU
update_notes: '<p>This release mostly adds in a lot of missing error checks and adds
  in gamecard support + support for mismatched regions.</p>

  <p>This release would not have been possible without the help of <a class="user-mention"
  data-hovercard-type="user" data-hovercard-url="/users/Sonlen1414/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/Sonlen1414">@Sonlen1414</a>
  .</p>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/13433513/38756013-40d03e2e-3f68-11e8-96cb-83704530de74.gif"><img
  src="https://user-images.githubusercontent.com/13433513/38756013-40d03e2e-3f68-11e8-96cb-83704530de74.gif"
  alt="QR code" style="max-width:100%;"></a></p>

  <p>Changes:</p>

  <ul>

  <li>Closes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="312630837" data-permission-text="Title is private" data-url="https://github.com/noirscape/SRAU/issues/1"
  data-hovercard-type="issue" data-hovercard-url="/noirscape/SRAU/issues/1/hovercard"
  href="https://github.com/noirscape/SRAU/issues/1">#1</a> (no gamecard support).
  Thanks to astronautlevel for the bug report and Sonlen for testing my fixes. If
  a gamecard is found, it is chosen over any local installation.</li>

  <li>Closes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="312631121" data-permission-text="Title is private" data-url="https://github.com/noirscape/SRAU/issues/2"
  data-hovercard-type="issue" data-hovercard-url="/noirscape/SRAU/issues/2/hovercard"
  href="https://github.com/noirscape/SRAU/issues/2">#2</a> (no support for mismatched
  regions). Thanks to astronautlevel for this bug report. You are now prompted if
  the program detects multiple regions. If there is only one region, it is autodetected
  and you are not prompted.</li>

  <li>Closes <a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="313041232" data-permission-text="Title is private" data-url="https://github.com/noirscape/SRAU/issues/4"
  data-hovercard-type="issue" data-hovercard-url="/noirscape/SRAU/issues/4/hovercard"
  href="https://github.com/noirscape/SRAU/issues/4">#4</a> (no support for missing
  save files). The program only allows you to choose existing save files. If there
  is only one save file, it is autodetected and you are not prompted to select a save
  file.</li>

  <li>Restart functionality! You can at any point now press the L button to restart
  the entire process. Useful if you selected the wrong save file or region.</li>

  <li>Savedata readouts! After selecting a save file, the program now reads out the
  current state of the save file and shows it on the bottom left screen.</li>

  <li>Cleaner interface! The main text prompts by the program are now dedicated on
  the top screen. The bottom screen now contains a list of save data info on the left
  and a list of your choices made in the program on the right (this include autodetection).</li>

  </ul>

  <p>Under the hood changes (you probably don''t care about this but for my own memory
  it''s here):</p>

  <ul>

  <li>Loads and loads. Really, I''ve rewritten about 90% of the program logic except
  for the ctrulib function calls themselves.</li>

  <li>No more if blocks. The entirety of the state machine is now handled with a <code>switch</code>.</li>

  <li>Got rid of editprofile.c completely and split it up into various functions inside
  save.c with lowid selection getting moved to title.c.</li>

  <li>Dedicated failure state that is separate from SUCCES state.</li>

  </ul>'
updated: '2018-04-13T20:16:16Z'
version: v1.1
version_title: Release v1.1
website: https://discord.gg/Q6jmQcV
---
