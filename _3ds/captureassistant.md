---
author: ItsDeidara
categories:
- utility
color: '#71524e'
created: '2016-08-26T15:57:26Z'
description: A capture alignment assistant for 3ds capture cards and NTRviewer
download_page: https://github.com/ItsDeidara/CaptureAssistant/releases/tag/1.3
downloads:
  CaptureAssistant.cia:
    size: 1606592
    url: https://github.com/ItsDeidara/CaptureAssistant/releases/download/1.3/CaptureAssistant.cia
  CaptureAssistantv1.3.zip:
    size: 1285025
    url: https://github.com/ItsDeidara/CaptureAssistant/releases/download/1.3/CaptureAssistantv1.3.zip
github: ItsDeidara/CaptureAssistant
icon: https://raw.githubusercontent.com/ItsDeidara/CaptureAssistant/master/assets/icon.png
image: https://raw.githubusercontent.com/ItsDeidara/CaptureAssistant/master/assets/banner.png
layout: app
license: mit
license_name: MIT License
qr:
  CaptureAssistant.cia: https://db.universal-team.net/assets/images/qr/captureassistant.cia.png
scripts:
  CaptureAssistant.cia:
  - file: CaptureAssistant.*\.zip
    message: Downloading CaptureAssistant zip...
    output: /CaptureAssistant.zip
    repo: ItsDeidara/CaptureAssistant
    type: downloadRelease
  - file: /CaptureAssistant.zip
    input: CaptureAssistant.cia
    message: Extracting CaptureAssistant.cia...
    output: /CaptureAssistant.cia
    type: extractFile
  - count: 3
    message: Use alternate calibration images?
    type: promptMessage
  - file: /CaptureAssistant.zip
    input: calibrationalt.png
    message: Extracting calibration.png...
    output: /calibration.png
    type: extractFile
  - file: /CaptureAssistant.zip
    input: calibrationalt2.png
    message: Extracting calibration2.png...
    output: /calibration2.png
    type: extractFile
  - count: 2
    type: skip
  - file: /CaptureAssistant.zip
    input: calibration.png
    message: Extracting calibration.png...
    output: /calibration.png
    type: extractFile
  - file: /CaptureAssistant.zip
    input: calibration2.png
    message: Extracting calibration2.png...
    output: /calibration2.png
    type: extractFile
  - file: /CaptureAssistant.cia
    message: Installing CaptureAssistant.cia...
    type: installCia
  - file: /CaptureAssistant.cia
    message: Deleting CaptureAssistant.cia...
    type: deleteFile
  - file: /CaptureAssistant.zip
    message: Deleting CaptureAssistant.zip...
    type: deleteFile
source: https://github.com/ItsDeidara/CaptureAssistant
systems:
- 3DS
title: CaptureAssistant
updated: '2016-08-26T23:13:12Z'
version: '1.3'
wiki: https://github.com/ItsDeidara/CaptureAssistant/wiki
---
