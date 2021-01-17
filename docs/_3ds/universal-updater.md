---
author: Universal-Team
categories:
- utility
color: '#045190'
created: '2019-10-31T02:19:37Z'
description: An easy to use app for installing and updating 3DS homebrew
download_page: https://github.com/Universal-Team/Universal-Updater/releases/tag/v3.1.1
downloads:
  Universal-Updater.3dsx:
    size: 2431136
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.1.1/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 2032576
    size_str: 1 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.1.1/Universal-Updater.cia
github: Universal-Team/Universal-Updater
icon: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/icon.png
image: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/banner.png
image_length: 24475
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
nightly:
  download_page: https://github.com/Universal-Team/extras/tree/master/builds/Universal-Updater
  downloads:
    Universal-Updater.3dsx:
      url: https://github.com/Universal-Team/extras/raw/master/builds/Universal-Updater/Universal-Updater.3dsx
    Universal-Updater.cia:
      url: https://github.com/Universal-Team/extras/raw/master/builds/Universal-Updater/Universal-Updater.cia
  qr:
    Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/nightly/universal-updater.cia.png
qr:
  Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/universal-updater.cia.png
screenshots:
- description: Auto update settings
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/auto-update-settings.png
- description: Credits
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/credits.png
- description: Directory selection
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/directory-selection.png
- description: Directory settings
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/directory-settings.png
- description: Download list
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/download-list.png
- description: Entry info
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/entry-info.png
- description: Gui settings
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/gui-settings.png
- description: Language selection
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/language-selection.png
- description: List style
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/list-style.png
- description: Mark menu
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/mark-menu.png
- description: Search menu
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/search-menu.png
- description: Settings menu
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/settings-menu.png
- description: Sort menu
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/sort-menu.png
- description: Store selection
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/store-selection.png
source: https://github.com/Universal-Team/Universal-Updater
systems:
- 3DS
title: Universal-Updater
unistore_exclude: true
update_notes: '<p>See <a href="https://github.com/Universal-Team/Universal-Updater/releases/tag/v3.1.0">v3.1.0</a>''s
  changelog for full notes if updating from v3.0.0</p>

  <p>This is just a little update with a single bug fix, but it''s a pretty important
  bug fix. For a while 7z extraction has just been randomly failing sometimes and
  we figured out it was due to the 2013 version of libarchive devkitPro provides,
  but we weren''t exactly sure how to get the latest version working, we finally did
  so here''s a little update.</p>

  <p>The updated pkgbuild patches are at <a href="https://github.com/Epicpkmn11/pacman-packages">Epicpkmn11/pacman-packages</a>,
  I would PR them to devkitPro''s, but we''re all banned so I can''t. If anyone at
  devkitPro wants to upstream those changes please do. I will note though I have basically
  no idea what I''m doing when it comes to porting libraries, so please report any
  extraction problems and if upstreaming you may want to check if I did anything really
  dumb ;P</p>

  <p>Apps that were known to be broken before but work now are:</p>

  <ul>

  <li>open_agb_firm</li>

  <li>OpenTitus (New 3DS versions)</li>

  </ul>'
updated: '2020-12-29T00:40:07Z'
version: v3.1.1
version_title: 'Bug fix update: Update to latest libarchive version'
website: https://universal-team.net/projects/universal-updater.html
wiki: https://github.com/Universal-Team/Universal-Updater/wiki
---
Universal-Updater is a homebrew application for the Nintendo 3DS with the intention to make downloading other homebrew simple and easy. No need to manually copy files or go through installation processes, as we do that for you.

Its features include:
- A store format with a concept similar to the Cydia Repositories
   - The default is [Universal-DB](https://db.universal-team.net)
   - Want to add your own? Go to settings, find "Select Unistore", hit the + icon and type the URL or hit the QR button and scan the QR code (if they have one)
- Customization in sorting and display
   - Sort by Title, Author, or Last Updated
   - Direction can be Ascending or Descending
   - App display can be shown in either a Grid or Rows
- Translations for users of many languages
   - To contribute to translations, join our [Crowdin](https://crwd.in/universal-updater)
   - Request a new language on our [Discord Server](https://universal-team.net/discord)