---
author: Universal-Team
avatar: https://avatars.githubusercontent.com/u/49733679?v=4
categories:
- utility
color: '#0b497b'
color_bg: '#0b497b'
created: '2019-10-31T02:19:37Z'
description: An easy to use app for installing and updating 3DS homebrew
download_page: https://github.com/Universal-Team/Universal-Updater/releases
downloads:
  Universal-Updater.3dsx:
    size: 3002452
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.4.1/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 2479040
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.4.1/Universal-Updater.cia
github: Universal-Team/Universal-Updater
icon: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/icon.png
image: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/resources/2d-banner.png
image_length: 24475
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'no'
nightly:
  download_page: https://github.com/Universal-Team/Universal-Updater/releases/tag/git
  downloads:
    Universal-Updater.3dsx:
      size: 3003700
      size_str: 2 MiB
      url: https://github.com/Universal-Team/Universal-Updater/releases/download/git/Universal-Updater.3dsx
    Universal-Updater.cia:
      size: 2479040
      size_str: 2 MiB
      url: https://github.com/Universal-Team/Universal-Updater/releases/download/git/Universal-Updater.cia
  qr:
    Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/git/universal-updater-cia.png
  update_notes: <p dir="auto">TWLBot - Automatic translation import</p>
  update_notes_md: TWLBot - Automatic translation import
  updated: '2026-07-01T03:00:43Z'
  version: git
  version_title: Continuous Build - 6998077
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
stars: 1253
systems:
- 3DS
title: Universal-Updater
unique_ids:
- '0x43917'
unistore_exclude: true
update_notes: '<p dir="auto">This release fixes an odd bug from v3.4.0 where the metadata
  file (containing marks and the update status of apps) stopped saving, thanks <a
  class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/syndenbock/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/syndenbock">@syndenbock</a>
  for the report! I also fixed a bug I''d noticed where Universal-Updater could crash
  if you exited while a thread was running. Italian and Russian translations have
  also been updated, thanks to everyone who''s helped with translations!</p>

  <p dir="auto">See <a href="https://github.com/Universal-Team/Universal-Updater/releases/tag/v3.4.0">v3.4.0''s
  Release notes</a> for full details on recent changes, the highlights were:</p>

  <ul dir="auto">

  <li>Universal-Updater now tracks installed apps (displayed by an SD card icon) and
  this can be used for filtering!</li>

  <li>Added a "NOT" filtering option to invert the filter, most useful for filtering
  to only apps not installed</li>

  <li>The search menu now includes all app names in the word completion dictionary!</li>

  <li>Proxies are now properly supported!</li>

  <li>The SSL CA certificate bundle is now be loaded from the SD card instead of RomFS</li>

  </ul>'
updated: '2026-06-20T17:08:42Z'
version: v3.4.1
version_title: Whoops
wiki: https://github.com/Universal-Team/Universal-Updater/wiki
---
Universal-Updater is a homebrew application for the Nintendo 3DS with the intention to make downloading other homebrew simple and easy. No need to manually copy files or go through installation processes, as it does that all for you.

### Features
- A store format with a concept similar to the Cydia Repositories
   - The default is [Universal-DB](https://db.universal-team.net)
   - Want to add more? Go to settings, choose "Select Unistore", click the + icon and select one from the list, enter a URL, or scan a QR code
- Customization in sorting and display
   - Several sorting keys: "Title", "Author", and "Last Updated"
   - Direction can be Ascending or Descending
   - App display can be shown in either a grid or rows
- Background installation so you can keep using the rest of the app while installing
- Searching and markings to make finding apps easy
- Viewing screenshots and release notes for apps
- Shortcuts for easily updating frequently updated apps when using the Homebrew Launcher
- Translations for users of many languages
   - To contribute to translations, join our [Crowdin project](https://crwd.in/universal-updater)
   - To request a new language, join our [Discord Server](https://universal-team.net/discord) or contact a project manager on Crowdin