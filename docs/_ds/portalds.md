---
author: smealum
categories:
- game
color: '#675758'
created: '2014-02-21T21:33:14Z'
description: homebrew nintendo DS adaptation of Valve's Portal
download_page: https://github.com/smealum/portalDS/releases/tag/r1
downloads:
  ASDS_r1.zip:
    size: 1397420
    url: https://github.com/smealum/portalDS/releases/download/r1/ASDS_r1.zip
github: smealum/portalDS
icon: https://raw.githubusercontent.com/smealum/portalDS/master/logo.bmp
image: https://db.universal-team.net/assets/images/icons/portalds.png
layout: app
scripts:
  portalDS.nds:
  - file: ASDS.*\.zip
    message: Downloading ASDS.zip...
    output: /ASDS.zip
    repo: smealum/portalDS
    type: downloadRelease
  - file: /ASDS.zip
    input: portalDS.nds
    message: Extracting portalDS.nds...
    output: '%NDS%/portalDS.nds'
    type: extractFile
  - file: /ASDS.zip
    input: asds/
    message: Extracting asds...
    output: '%NDS%/asds/'
    type: extractFile
  - file: /ASDS.zip
    message: Deleting ASDS.zip...
    type: deleteFile
source: https://github.com/smealum/portalDS
systems:
- DS
title: portalDS
update_notes: <p>The first (and only) publicly released version of the Aperture Science
  DS.</p>
updated: '2019-11-23T23:14:24Z'
version: r1
version_title: Aperture Science DS r1
wiki: https://github.com/smealum/portalDS/wiki
---
