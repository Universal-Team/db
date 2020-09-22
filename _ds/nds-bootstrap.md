---
author: DS-Homebrew
categories:
- emulator
created: '2016-09-11T19:50:26Z'
description: Boot an nds file
download_page: https://github.com/DS-Homebrew/nds-bootstrap/releases/tag/v0.35.1
downloads:
  nds-bootstrap.7z: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.35.1/nds-bootstrap.7z
  nds-bootstrap.zip: https://github.com/DS-Homebrew/nds-bootstrap/releases/download/v0.35.1/nds-bootstrap.zip
github: DS-Homebrew/nds-bootstrap
icon: https://raw.githubusercontent.com/DS-Homebrew/nds-bootstrap/master/retail/assets/icon.bmp
image: https://i.imgur.com/BFIu7xX.png
layout: app
scripts:
  nds-bootstrap Nightly:
  - file: https://github.com/TWLBot/Builds/raw/master/nds-bootstrap.7z
    message: Downloading nds-bootstrap Nightly...
    output: /nds-bootstrap.7z
    type: downloadFile
  - file: /nds-bootstrap.7z
    input: nds-bootstrap/
    message: Extracting nds-bootstrap...
    output: /_nds/
    type: extractFile
  - file: /nds-bootstrap.7z
    type: deleteFile
  nds-bootstrap Release:
  - file: nds-bootstrap.7z
    message: Downloading nds-bootstrap...
    output: /nds-bootstrap.7z
    repo: ahezard/nds-bootstrap
    type: downloadRelease
  - file: /nds-bootstrap.7z
    input: ''
    message: Extracting nds-bootstrap...
    output: /_nds/
    type: extractFile
  - file: /nds-bootstrap.7z
    type: deleteFile
source: https://github.com/DS-Homebrew/nds-bootstrap
systems:
- DS
title: nds-bootstrap
updated: '2020-05-09T19:31:50Z'
version: v0.35.1
version_title: v0.35.1
wiki: https://github.com/DS-Homebrew/nds-bootstrap/wiki
---
nds-bootstrap is an open-source application that allows Nintendo DS/DSi ROMs and homebrew to be natively utilised rather than using an emulator. nds-bootstrap works on Nintendo DSi/3DS SD cards through CFW and on Nintendo DS through flashcarts.