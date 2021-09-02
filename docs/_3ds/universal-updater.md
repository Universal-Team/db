---
author: Universal-Team
avatar: https://avatars.githubusercontent.com/u/49733679?v=4
categories:
- utility
color: '#0b497b'
created: '2019-10-31T02:19:37Z'
description: An easy to use app for installing and updating 3DS homebrew
download_page: https://github.com/Universal-Team/Universal-Updater/releases
downloads:
  Universal-Updater.3dsx:
    size: 2553036
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.2.3/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 2134976
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.2.3/Universal-Updater.cia
github: Universal-Team/Universal-Updater
icon: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/icon.png
icon_index: 0
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
    Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/nightly/universal-updater-cia.png
priority: true
qr:
  Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/universal-updater-cia.png
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
- description: Queue menu
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/queue-menu.png
- description: Recommended unistores
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/recommended-unistores.png
- description: Release notes
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/release-notes.png
- description: Screenshot
  url: https://db.universal-team.net/assets/images/screenshots/universal-updater/screenshot.png
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
update_notes: '<h3>Changes</h3>

  <ul>

  <li>Adds Danish and Turkish translations and updates to some existing translations</li>

  <li>Adds Makefile option to build a Citra compatible version (<code>make citra</code>)</li>

  </ul>

  <h3>Bug fixes</h3>

  <ul>

  <li>Fixes empty folders and 0 byte files not being extracted</li>

  </ul>

  <h3>Other notes</h3>

  <p>Pretty small update this time, it''s been a while since the last one though so
  we figured we should push out the couple changes we have at the moment.</p>

  <p>Find any bugs we missed, have suggestions, or need help? You can either make
  an issue or discussion here on GitHub or join our <a href="https://universal-team.net/discord"
  rel="nofollow">Discord server</a>.</p>

  <p>We hope you enjoy the new update!<br>

  ~ Universal-Team</p>

  <hr>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/128966211-6263b6b6-769b-4a54-b194-5f28b855903a.png"><img
  src="https://user-images.githubusercontent.com/41608708/128966211-6263b6b6-769b-4a54-b194-5f28b855903a.png"
  alt="QR code for universal-updater.cia" style="max-width:100%;"></a></p>'
updated: '2021-08-11T03:37:15Z'
version: v3.2.3
version_title: Translation updates and a bug fix
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