---
author: Ewan Croft
avatar: https://avatars.githubusercontent.com/u/156911937?v=4
categories:
- app
color: '#c4dfce'
color_bg: '#708076'
created: '2026-10-02T22:29:06Z'
description: A native Bluesky client for the Nintendo 3DS.
download_filter: ^indigo\.3dsx$
download_page: https://github.com/ewanc26/indigo/releases
downloads:
  indigo.3dsx:
    size: 1740788
    size_str: 1 MiB
    url: https://github.com/ewanc26/indigo/releases/download/v0.21.0/indigo.3dsx
github: ewanc26/indigo
icon: https://raw.githubusercontent.com/ewanc26/indigo/main/assets/icon.png
image: https://raw.githubusercontent.com/ewanc26/indigo/main/assets/banner.png
image_length: 711
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
screenshots:
- description: A profile
  url: https://db.universal-team.net/assets/images/screenshots/indigo/a-profile.png
- description: A thread
  url: https://db.universal-team.net/assets/images/screenshots/indigo/a-thread.png
- description: Home timeline
  url: https://db.universal-team.net/assets/images/screenshots/indigo/home-timeline.png
- description: Notifications
  url: https://db.universal-team.net/assets/images/screenshots/indigo/notifications.png
- description: Settings
  url: https://db.universal-team.net/assets/images/screenshots/indigo/settings.png
- description: Writing a reply
  url: https://db.universal-team.net/assets/images/screenshots/indigo/writing-a-reply.png
source: https://github.com/ewanc26/indigo
stars: 0
systems:
- 3DS
title: Indigo
update_notes: '<h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>A profile''s avatar is covered when a label on the account asks for it, for
  example graphic media from a labeler you subscribe to. The image is not downloaded;
  a flat square is drawn in its place, and the status line says "Avatar hidden: ".
  Banners are not drawn by Indigo, so they are not covered. (<a href="https://github.com/ewanc26/indigo/issues/147"
  data-hovercard-type="issue" data-hovercard-url="/ewanc26/indigo/issues/147/hovercard">#147</a>)</li>

  </ul>'
updated: '2026-11-28T07:20:59Z'
version: v0.21.0
version_title: Indigo 0.21.0
---
Indigo exists because apparently making a Wii U post to Bluesky was not enough.

After forcing a PowerPC tri-core console to participate in the modern social web with [Cobalt](https://github.com/ewanc26/cobalt), I decided that the next reasonable target was a Nintendo 3DS: another machine with absolutely no business being a Bluesky client.

The goal is the same kind of hardware-first absurdity, but the implementation is deliberately different. Indigo is **not a port** of Cobalt. I am designing it around the 3DS's own hardware, input model and two-screen layout.

The project uses [Wolfram](https://github.com/ewanc26/wolfram), my C AT Protocol SDK, for protocol functionality. Indigo is scoped to the Bluesky app, not general AT Protocol use; accounts on custom PDSes are supported.

Indigo installs to `sdmc:/3ds/indigo.3dsx` and runs from the Homebrew Menu. It needs a Bluesky account; signing in takes an app password, or a hosted sign-in node for browser sign-in. Status, and what has and has not been run on a real 3DS: https://github.com/ewanc26/indigo#status