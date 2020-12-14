---
author: hax0kartik
categories:
- utility
color: '#411d38'
created: '2020-08-20T12:36:12Z'
description: Amiibo Emulation for 3ds
download_page: https://github.com/hax0kartik/wumiibo/releases/tag/v2.0
downloads:
  0004013000004002.zip:
    size: 42617
    url: https://github.com/hax0kartik/wumiibo/releases/download/v2.0/0004013000004002.zip
github: hax0kartik/wumiibo
image: https://avatars0.githubusercontent.com/u/16360444?v=4
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
scripts:
  wumiibo:
  - file: 0004013000004002.zip
    message: Downloading 0004013000004002.zip...
    output: /0004013000004002.zip
    repo: hax0kartik/wumiibo
    type: downloadRelease
  - file: /0004013000004002.zip
    input: 0004013000004002/
    message: Extracting 0004013000004002...
    output: /luma/titles/0004013000004002/
    type: extractFile
  - file: /0004013000004002.zip
    message: Deleting 0004013000004002.zip...
    type: deleteFile
source: https://github.com/hax0kartik/wumiibo
systems:
- 3DS
title: wumiibo
update_notes: '<p>This is the third public release for wumiibo.<br>

  Following list of changes has been made.</p>

  <ul>

  <li>

  <p>Proper UID assignment and UID Randomization has been added.</p>

  <ul>

  <li>Wumiibo no longer uses a hardcoded UID for every amiibo. It automatically assigns
  a new UID to every amiibo.</li>

  <li>Some games limit users to only one scan of a specific amiibo per 24 hours. By
  randomizing an amiibo''s UID you can overcome this limit.<br>

  <strong>NOTE</strong>:- This depends on the game''s logic, and may not work with
  every title.</li>

  </ul>

  </li>

  <li>

  <p>Default wumiibo menu button can now be overridden.</p>

  <ul>

  <li>This can be done by creating a <code>wumiibo.ini</code> file on the root of
  your sd card. A sample of this file is <a href="https://github.com/hax0kartik/wumiibo/blob/master/wumiibo.ini">here</a>.</li>

  </ul>

  </li>

  <li>

  <p>DirectoryLister code has been improved.</p>

  <ul>

  <li>You can now have upto <code>49</code> folders within the <code>wumiibo</code>
  folder. Inside every folder you can have even more subfolders or amiibos. So if
  you create your folders properly, there is virtually no limit on how many amiibos
  you can have at a time.</li>

  <li>As a bonus feature, if you want to have a dedicated folder for a game, you can
  give a folder the game''s TitleID and put all relevant amiibos in there. For example,
  for Super Smash Bros EUR, you can create a folder <code>sd:/wumiibo/00040000000EE000</code>
  and put the amiibos in there. Wumiibo will automatically open this folder in-game.</li>

  </ul>

  </li>

  <li>

  <p>Various bugs have been fixed and minor improvements have been made.</p>

  </li>

  </ul>

  <p>If this the first time you''re installing wumiibo, you can follow the instruction
  in the readme <a href="https://github.com/hax0kartik/wumiibo/blob/master/Readme.md">here</a>.</p>

  <p>As of writing 42 out of 47 know games that have amiibo capabalities are known
  to work. You can check the compatibility list <a href="https://github.com/hax0kartik/wumiibo/wiki/Compatibility-List">here</a>.</p>

  <p>Massive thanks to Marcus7777, druivensap, Love Leiz and Graymar on my discord
  server for helping me test out the games, wouldn''t been possible without you guys!</p>

  <p>If you like my work, you can support me by buying me a coffee on <a href="https://ko-fi.com/hax0kartik"
  rel="nofollow">ko-fi</a> or you can <a href="https://www.paypal.com/paypalme/preetiagarwala?locale.x=en_GB"
  rel="nofollow">paypal</a> me!</p>'
updated: '2020-09-24T18:30:26Z'
version: v2.0
version_title: v2.0 Third Release
wiki: https://github.com/hax0kartik/wumiibo/wiki
---
