---
author: RocketRobz
categories:
- utility
color: '#5f5f5f'
created: '2017-08-04T22:17:54Z'
description: A demonstration of the 800px mode on 3DS consoles.
download_page: https://github.com/RocketRobz/HoriHD-Gallery/releases/tag/v1.0.2
downloads:
  HoriHD-Gallery.7z:
    size: 36652357
    url: https://github.com/RocketRobz/HoriHD-Gallery/releases/download/v1.0.2/HoriHD-Gallery.7z
github: RocketRobz/HoriHD-Gallery
icon: https://raw.githubusercontent.com/RocketRobz/HoriHD-Gallery/master/app/icon.png
image: https://raw.githubusercontent.com/RocketRobz/HoriHD-Gallery/master/app/banner.png
layout: app
scripts:
  HoriHD-Gallery.3dsx:
  - file: HoriHD-Gallery.7z
    message: Downloading HoriHD-Gallery.7z...
    output: /HoriHD-Gallery.7z
    repo: RocketRobz/HoriHD-Gallery
    type: downloadRelease
  - file: /HoriHD-Gallery.7z
    input: HoriHD-Gallery.cia
    message: Extracting HoriHD-Gallery.3dsx...
    output: '%3DSX%/HoriHD-Gallery.3dsx'
    type: extractFile
  - file: /HoriHD-Gallery.7z
    message: Deleting HoriHD-Gallery.7z...
    type: deleteFile
  HoriHD-Gallery.cia:
  - file: HoriHD-Gallery.7z
    message: Downloading HoriHD-Gallery.7z...
    output: /HoriHD-Gallery.7z
    repo: RocketRobz/HoriHD-Gallery
    type: downloadRelease
  - file: /HoriHD-Gallery.7z
    input: HoriHD-Gallery.cia
    message: Extracting HoriHD-Gallery.cia...
    output: /HoriHD-Gallery.cia
    type: extractFile
  - file: /HoriHD-Gallery.cia
    message: Installing HoriHD-Gallery.cia...
    type: installCia
  - file: /HoriHD-Gallery.cia
    message: Deleting HoriHD-Gallery.cia...
    type: deleteFile
  - file: /HoriHD-Gallery.7z
    message: Deleting HoriHD-Gallery.7z...
    type: deleteFile
source: https://github.com/RocketRobz/HoriHD-Gallery
systems:
- 3DS
title: HoriHD-Gallery
update_notes: '<p><strong>What''s new?</strong></p>

  <ul>

  <li>Added toggling between 400px and 800px modes, by pressing SELECT.</li>

  </ul>

  <p><strong>Improvement</strong></p>

  <ul>

  <li>Added linear filtering in 400px mode (and O2DS consoles), so images don''t look
  jagged.</li>

  </ul>'
updated: '2020-06-21T01:28:09Z'
version: v1.0.2
version_title: 400/800px release
wiki: https://github.com/RocketRobz/HoriHD-Gallery/wiki
---
A demonstration of the 800px mode on 3DS consoles. Will not work on O2DS consoles.