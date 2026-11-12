---
author: dwalker109
avatar: https://avatars.githubusercontent.com/u/4749645?v=4
categories:
- save-tool
- utility
color: '#e8b3fb'
color_bg: '#765b80'
created: '2025-11-28T10:52:26Z'
description: Bringing modern cloud save to 3DS.
download_page: https://github.com/dwalker109/cloudpoint/releases
downloads:
  cloudpoint.3dsx:
    size: 3156688
    size_str: 3 MiB
    url: https://github.com/dwalker109/cloudpoint/releases/download/0.9.1/cloudpoint.3dsx
  cloudpoint.cia:
    size: 2474944
    size_str: 2 MiB
    url: https://github.com/dwalker109/cloudpoint/releases/download/0.9.1/cloudpoint.cia
github: dwalker109/cloudpoint
icon: https://media.githubusercontent.com/media/dwalker109/cloudpoint/refs/heads/main/cloudpoint_app/cia/icon.png
image: https://media.githubusercontent.com/media/dwalker109/cloudpoint/refs/heads/main/cloudpoint_app/cia/banner.png
image_length: 7381
layout: app
license: mit
license_name: MIT License
llm_generation: minor
qr:
  cloudpoint.cia: https://db.universal-team.net/assets/images/qr/cloudpoint-cia.png
source: https://github.com/dwalker109/cloudpoint
stars: 91
systems:
- 3DS
title: Cloudpoint
unique_ids:
- '0xFF001'
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <p dir="auto">This is mainly a regression fix release to resolve problems with the
  refresh modals misbehaving on launch. They work OK but seem to hang a bit and it
  isn''t ideal on first run. They are now smooth and sensible again.</p>

  <p dir="auto">Also quits trying to reconnect to the server if a fatal error is encountered
  rather than just trying over and over again.</p>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Connect retries for ever even when connection is impossible by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwalker109/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwalker109">@dwalker109</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6174978159"
  data-permission-text="Title is private" data-url="https://github.com/dwalker109/cloudpoint/issues/180"
  data-hovercard-type="pull_request" data-hovercard-url="/dwalker109/cloudpoint/pull/180/hovercard"
  href="https://github.com/dwalker109/cloudpoint/pull/180">#180</a></li>

  <li>Better control of refresh modal trigger and close by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwalker109/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwalker109">@dwalker109</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6265774415"
  data-permission-text="Title is private" data-url="https://github.com/dwalker109/cloudpoint/issues/187"
  data-hovercard-type="pull_request" data-hovercard-url="/dwalker109/cloudpoint/pull/187/hovercard"
  href="https://github.com/dwalker109/cloudpoint/pull/187">#187</a></li>

  </ul>

  <h3 dir="auto">Improvements</h3>

  <ul dir="auto">

  <li>Switch to native libctru FSUSER_GetSdmcCtrRootPath by <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/dwalker109/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/dwalker109">@dwalker109</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6194465113"
  data-permission-text="Title is private" data-url="https://github.com/dwalker109/cloudpoint/issues/182"
  data-hovercard-type="pull_request" data-hovercard-url="/dwalker109/cloudpoint/pull/182/hovercard"
  href="https://github.com/dwalker109/cloudpoint/pull/182">#182</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/dwalker109/cloudpoint/compare/0.9.0...0.9.1"><tt>0.9.0...0.9.1</tt></a></p>'
updated: '2026-11-08T00:24:01Z'
version: 0.9.1
version_title: 0.9.1
---
Cloudpoint allows you to sync all of your saves (and extdata) between all of your 3DS & 2DS devices, 
via a central server. Transfer progress between consoles effortlessly, the way you're probably used 
to from more modern systems. Or PS Vita.