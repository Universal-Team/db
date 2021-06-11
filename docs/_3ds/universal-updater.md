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
    size: 2545148
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.2.2/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 2126784
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.2.2/Universal-Updater.cia
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
priority: true
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
update_notes: '<h3>What''s New?</h3>

  <ul>

  <li>Adds Korean and most other translations have been fully completed</li>

  <li>Uninstalling an app now makes it not show an icon for updates</li>

  <li>Changed to a new icon with better shading</li>

  </ul>

  <h3>Bug fixes</h3>

  <ul>

  <li>Fixes fonts being too large on Chinese, Taiwanese, and Korean consoles</li>

  <li>Blocks going to the HOME menu and quitting the app while the queue is running,
  which could cause buggy behavior</li>

  <li>Adds safety checks for low SD card space</li>

  </ul>

  <h3>Other notes</h3>

  <p>A fairly minor update this time, but we''ve got enough bug fixes and new little
  things that we figured it was a good time.</p>

  <p>Find any bugs we missed, have suggestions, or need help? You can either make
  an issue or discussion here on GitHub or join our <a href="https://universal-team.net/discord"
  rel="nofollow">Discord server</a>. That''s right, we''re letting people in again
  now!</p>

  <p>We hope you enjoy the new update!<br>

  ~ Universal-Team</p>

  <hr>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/119982867-00ce2e80-bf85-11eb-967f-d0b8c66b73e8.png"><img
  src="https://user-images.githubusercontent.com/41608708/119982867-00ce2e80-bf85-11eb-967f-d0b8c66b73e8.png"
  alt="QR code for universal-updater.cia" style="max-width:100%;"></a></p>'
updated: '2021-05-28T12:14:25Z'
version: v3.2.2
version_title: New icon, Korean, and bug fixes
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