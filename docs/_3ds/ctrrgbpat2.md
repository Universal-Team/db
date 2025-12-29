---
author: CPunch & Golem64
avatar: https://avatars.githubusercontent.com/u/65229557?v=4
categories:
- utility
color: '#4887af'
color_bg: '#346280'
created: '2023-05-11T08:48:45Z'
description: LED color and pattern modifier for 3DS. Customize your notifications
  however you want !
download_page: https://github.com/Golem642/CtrRGBPAT2/releases
downloads:
  CtrRGBPAT2.3dsx:
    size: 628880
    size_str: 614 KiB
    url: https://github.com/Golem642/CtrRGBPAT2/releases/download/v2.5/CtrRGBPAT2.3dsx
  CtrRGBPAT2.cia:
    size: 1014208
    size_str: 990 KiB
    url: https://github.com/Golem642/CtrRGBPAT2/releases/download/v2.5/CtrRGBPAT2.cia
github: Golem642/CtrRGBPAT2
icon: https://raw.githubusercontent.com/Golem642/CtrRGBPAT2/master/resources/icon.png
image: https://raw.githubusercontent.com/Golem642/CtrRGBPAT2/master/resources/banner.png
image_length: 12658
layout: app
license: mit
license_name: MIT License
qr:
  CtrRGBPAT2.cia: https://db.universal-team.net/assets/images/qr/ctrrgbpat2-cia.png
screenshots:
- description: Custom pattern editor
  url: https://db.universal-team.net/assets/images/screenshots/ctrrgbpat2/custom-pattern-editor.png
- description: Install menu
  url: https://db.universal-team.net/assets/images/screenshots/ctrrgbpat2/install-menu.png
- description: Notification color
  url: https://db.universal-team.net/assets/images/screenshots/ctrrgbpat2/notification-color.png
- description: Pattern modifier
  url: https://db.universal-team.net/assets/images/screenshots/ctrrgbpat2/pattern-modifier.png
- description: Testing functionnality
  url: https://db.universal-team.net/assets/images/screenshots/ctrrgbpat2/testing-functionnality.png
script_message: 'You will need to have "Game Patching" and "Loading external FIRMs
  and modules"

  enabled in LumaCFW settings (hold select on boot)'
source: https://github.com/Golem642/CtrRGBPAT2
stars: 11
systems:
- 3DS
title: CtrRGBPAT2
unique_ids:
- '0xD37BB'
update_notes: '<p dir="auto">Hello again</p>

  <p dir="auto">I''m back for another release with quite the exciting changes. Most
  notably...</p>

  <h2 dir="auto">Low battery pattern editing</h2>

  <p dir="auto">That''s right, you can now make this annoying blinking light less
  of a pain with this new release. I know some of you had been waiting for it for
  a long time so here it finally is. Do note that there is currently no way to change
  the color of the LED as it does not function the same way as a classic animation.</p>

  <p dir="auto">For the rest, here''s a full list of the changes :</p>

  <ul dir="auto">

  <li>Reworked the menus a bit (again)</li>

  <li>Pattern editor now also shows separate R G and B values that you can edit</li>

  <li>Added loading menus for default animations and currently installed animations</li>

  <li>Added previews in a few places (pattern editor, low battery, and some loading
  menus)</li>

  <li>Added joystick/CPAD support</li>

  <li>Added direction holding support (you can now move faster in the menus)</li>

  <li>Added better B key handling (go back one menu at a time instead of directly
  to the main menu)</li>

  <li>Fixed the colors not showing on the display (pull request have been sent to
  <a href="https://github.com/devkitPro/libctru/pull/570" data-hovercard-type="pull_request"
  data-hovercard-url="/devkitPro/libctru/pull/570/hovercard">devkitPro/libctru</a>)</li>

  <li>Fixed the preview holding a color if the last one was set (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="2069165368" data-permission-text="Title
  is private" data-url="https://github.com/Golem642/CtrRGBPAT2/issues/1" data-hovercard-type="issue"
  data-hovercard-url="/Golem642/CtrRGBPAT2/issues/1/hovercard" href="https://github.com/Golem642/CtrRGBPAT2/issues/1">#1</a>,
  do any action to stop the preview)</li>

  <li>Fixed the building process a bit. No more errors</li>

  </ul>

  <p dir="auto">Note that if you try to build the file manually, the result might
  be different as i have used my own version of libctru which includes the lastest
  version with <a href="https://github.com/devkitPro/libctru/pull/570" data-hovercard-type="pull_request"
  data-hovercard-url="/devkitPro/libctru/pull/570/hovercard">devkitPro/libctru#570</a>
  and <a href="https://github.com/devkitPro/libctru/pull/561" data-hovercard-type="pull_request"
  data-hovercard-url="/devkitPro/libctru/pull/561/hovercard">devkitPro/libctru#561</a>
  applied.</p>

  <p dir="auto">I hope you enjoy this release, the next one will probably add pattern
  loading from a file.</p>

  <p dir="auto">Have fun ! :)</p>

  <p dir="auto">QR code download :<br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/8fdb95f3-dcbc-4d34-af05-c4018373587b"><img
  src="https://github.com/user-attachments/assets/8fdb95f3-dcbc-4d34-af05-c4018373587b"
  alt="image" style="max-width: 100%;"></a></p>'
updated: '2025-04-27T15:28:52Z'
version: v2.5
version_title: V2.5
website: https://db.universal-team.net/3ds/ctrrgbpat2
---
# CtrRGBPAT2
This 3DS application allows the LED color to be changed. In order for this to work, Luma CFW (custom firmware) needs to be installed.
Thanks to [CPunch](https://github.com/CPunch/CtrRGBPATTY/) for the original project !

## Features
Customize the LED color and pattern for when you receive notifications ! Whether SpotPass, StreetPass, online Friends, or more (Yes, there's more) ! Why keep the default blue when you can have a cool-looking purple for example 😎

Everything is simple and made so you cannot possibly screw something up (or else you really wanted to)

## Upcoming
- Save and restore feature
- Proper UI ?

Hope you enjoy ! :)