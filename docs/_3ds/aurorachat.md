---
author: Unitendo
avatar: https://avatars.githubusercontent.com/u/241876109?v=4
categories:
- app
color: '#2d8d97'
color_bg: '#267780'
created: '2026-03-14T01:11:35Z'
description: ' Real Time Chatting for the 3DS, Wii, Wii U, and Web'
download_page: https://github.com/Unitendo/aurorachat/releases
downloads:
  aurorachat.3dsx:
    size: 180920
    size_str: 176 KiB
    url: https://github.com/Unitendo/aurorachat/releases/download/v7.0.0/aurorachat.3dsx
  aurorachat.cia:
    size: 522688
    size_str: 510 KiB
    url: https://github.com/Unitendo/aurorachat/releases/download/v7.0.0/aurorachat.cia
github: Unitendo/aurorachat
icon: https://raw.githubusercontent.com/Unitendo/aurorachat-3ds/main/meta/icon.png
image: https://raw.githubusercontent.com/Unitendo/aurorachat-3ds/main/meta/banner.png
image_length: 28629
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
prerelease:
  download_page: https://github.com/Unitendo/aurorachat/releases/tag/pre2-v7.0
  downloads:
    aurorachat.3dsx:
      size: 180756
      size_str: 176 KiB
      url: https://github.com/Unitendo/aurorachat/releases/download/pre2-v7.0/aurorachat.3dsx
    aurorachat.cia:
      size: 522688
      size_str: 510 KiB
      url: https://github.com/Unitendo/aurorachat/releases/download/pre2-v7.0/aurorachat.cia
  qr:
    aurorachat.cia: https://db.universal-team.net/assets/images/qr/prerelease/aurorachat-cia.png
  update_notes: '<h1 dir="auto">Changelog</h1>

    <ul dir="auto">

    <li><em><strong>Changed GUI</strong></em></li>

    <li>Resentfully added a form of socket buffering</li>

    <li>Changed the way data is received</li>

    <li><em><strong>Added message history</strong></em></li>

    <li><em><strong>Added themes</strong></em></li>

    <li>and more! (probably)</li>

    </ul>'
  update_notes_md: '# Changelog

    - _**Changed GUI**_

    - Resentfully added a form of socket buffering

    - Changed the way data is received

    - _**Added message history**_

    - _**Added themes**_

    - and more! (probably)'
  updated: '2026-08-21T21:13:56Z'
  version: pre2-v7.0
  version_title: 'v7 Pre-release 2: Glow-up'
qr:
  aurorachat.cia: https://db.universal-team.net/assets/images/qr/aurorachat-cia.png
source: https://github.com/Unitendo/aurorachat
stars: 21
systems:
- 3DS
title: aurorachat
unique_ids:
- '0xBAFD2'
update_notes: '<p dir="auto">Introducing the full, proper release of v7 for Nintendo
  3DS.</p>

  <p dir="auto">v7: The Better One does not introduce too much more from its pre-releases,
  mostly because the pre-releases were so good that there was practically nothing
  to add without wasting time!</p>

  <p dir="auto">Aurorachat v7 will be taking over COMPLETELY from v6. v6 will receive
  no new support and will be shut down in due time.</p>

  <h1 dir="auto">v7 Overall Changelog</h1>

  <p dir="auto"><a href="https://github.com/Unitendo/aurorachat-server-v7">The changes
  listed can be found at this repository.</a></p>

  <ul dir="auto">

  <li>Switch back entirely to sockets, it is purely pointless to still be receiving
  from them while using HTTP for requests, especially considering HTTP is basically
  just sockets with some fancy formatting added.</li>

  <li>Add VPN detection, this is to stop people from easily bypassing IP bans, we
  apologize if you want to use a VPN but cannot due to this security measure, it has
  been taken only because of issues with spammers on the platform.</li>

  <li>Rewrite server codebase, make it much more modular.</li>

  <li>Plugin support.</li>

  <li>and a lot more, why don''t you play around to find out?</li>

  </ul>

  <h1 dir="auto">v7 3DS Changelog</h1>

  <p dir="auto"><a href="https://github.com/Unitendo/aurorachat-3ds/tree/v7">The changes
  listed can be found at this repository.</a></p>

  <ul dir="auto">

  <li>Rewrite codebase, optimize stability and usability</li>

  <li>Reduce executable size (removes large audio files that were not in use...)</li>

  <li>Rewrite GUI</li>

  <li>Re-introduce themes in a brand new, modular system.</li>

  <li>Switch to v7 server protocol (including switching to sockets)</li>

  <li>and probably more!</li>

  </ul>

  <h1 dir="auto">Contributors</h1>

  <p dir="auto">These are people who have helped develop this update:</p>

  <ul dir="auto">

  <li><a href="https://github.com/VirtuallyExisting">Virtualle</a> wrote the 3DS client</li>

  <li><a href="https://github.com/JakubKwantowy">KwTheDsGuy/jakubkwantowy</a> wrote
  the v7 server</li>

  <li><a href="https://github.com/3pm-on-github">3pm</a> contributed some code and/or
  files to the 3DS v7 repository, v7 server work</li>

  </ul>'
updated: '2026-08-25T22:23:39Z'
version: v7.0.0
version_title: 'v7: The Better One'
---
A safer chatting app for the Nintendo 3DS line of systems.