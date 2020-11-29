---
author: DomRe
categories:
- utility
color: '#905933'
created: '2016-05-02T12:42:03Z'
description: '[ARCHIVE] PoC 3DS eBook Reader.'
download_page: https://github.com/DomRe/3DS_eBook_Reader/releases/tag/1.2
downloads:
  release1.2.zip:
    size: 540204
    url: https://github.com/DomRe/3DS_eBook_Reader/releases/download/1.2/release1.2.zip
github: DomRe/3DS_eBook_Reader
icon: https://raw.githubusercontent.com/DomRe/3DS_eBook_Reader/master/meta/icon.png
image: https://raw.githubusercontent.com/DomRe/3DS_eBook_Reader/master/meta/banner.png
layout: app
license: mit
license_name: MIT License
scripts:
  eBook_Reader.cia:
  - file: release.*\.zip
    message: Downloading release zip...
    output: /release.zip
    repo: DomRe/3DS_eBook_Reader
    type: downloadRelease
  - file: /release.zip
    input: ''
    message: Extracting 3DS_eBook_Reader...
    output: /
    type: extractFile
  - file: /eBook_Reader.cia
    message: Installing eBook_Reader.cia...
    type: installCia
  - file: /eBook_Reader.cia
    message: Deleting eBook_Reader.cia...
    type: deleteFile
  - file: /release.zip
    message: Deleting release.zip...
    type: deleteFile
source: https://github.com/DomRe/3DS_eBook_Reader
systems:
- 3DS
title: 3DS_eBook_Reader
update_notes: '<p>Changes:</p>

  <ul>

  <li>Fixed about screen flickering.</li>

  </ul>

  <p>See <a href="https://www.reddit.com/r/3dshacks/comments/7su3f4/released_v10_of_my_ebook_reader/"
  rel="nofollow">reddit</a> or <a href="https://gbatemp.net/threads/release-ebook-reader-v1-0-read-ebooks-on-your-3ds.495129/"
  rel="nofollow">gbatemp</a>.</p>'
updated: '2018-01-29T06:38:15Z'
version: '1.2'
version_title: eBook Reader v1.2
---
