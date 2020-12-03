---
author: Universal-Team
categories:
- utility
color: '#045190'
created: '2019-10-31T02:19:37Z'
description: An easy to use app for installing and updating 3DS homebrew
download_page: https://github.com/Universal-Team/Universal-Updater/releases/tag/v3.0.0
downloads:
  Universal-Updater.3dsx:
    size: 2210344
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.0.0/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 1868736
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.0.0/Universal-Updater.cia
github: Universal-Team/Universal-Updater
icon: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/icon.png
image: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/banner.png
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
update_notes: '<p>Universal-Updater v3.0.0 is here with a complete overhaul to the
  app! Everything has been thought through and redesigned with the goal of making
  using Universal-Updater a much simpler and more intuitive experience.</p>

  <p>Now when loading Universal-Updater it immediately opens the last used UniStore,
  by default <a href="https://db.universal-team.net" rel="nofollow">Universal-DB</a>,
  and from there you can see all the apps on the top screen and the bottom now has
  separate tabs for information, downloads, search, sort, and settings while still
  keeping the app list active on the top screen. The graphics have also been redone
  to give a cleaner and more modern feel.</p>

  <details><summary>Screenshot</summary>

  <p><a target="_blank" rel="noopener noreferrer" href="https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/screenshots/EntryInfo.png"><img
  src="https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/screenshots/EntryInfo.png"
  alt="A screenshot showing the info of an app" style="max-width:100%;"></a></p>

  </details>

  <p>Searching and filtering have also been improved, you can now mark apps and filter
  to just show apps with specific marks and/or only apps that have updates available.
  Searching is now case-insensitive and you can edit the filters and the search without
  having to dig through menus.</p>

  <p>The old "scripts" have been dropped completely in favor of just UniStores, but
  no functionality is lost here as all of the apps that could be downloaded with the
  official scripts are now on Universal-DB and even ones with complex installation
  processes like TWiLight Menu++ still work correctly, plus update tracking and more
  information.</p>

  <p>We hope you enjoy the new changes!<br>

  ~ Universal-Team</p>

  <hr>

  <p>A couple notes:</p>

  <ul>

  <li>To UniStore creators: All existing UniStores will needed to be updated to version
  3, check out the wiki for more information.</li>

  <li>If updating from a previous version and you get an error that the UniStore is
  invalid:

  <ol>

  <li>Go to <code>Settings</code></li>

  <li>Go to <code>Select UniStore</code></li>

  <li>Press the update icon at the bottom on the UniStore</li>

  <li>Press <kbd>A</kbd> on the UniStore</li>

  </ol>

  </li>

  </ul>

  <hr>

  <p><a target="_blank" rel="noopener noreferrer" href="https://user-images.githubusercontent.com/41608708/98047935-6e9ce800-1df2-11eb-8ff4-8146a71c90c8.png"><img
  src="https://user-images.githubusercontent.com/41608708/98047935-6e9ce800-1df2-11eb-8ff4-8146a71c90c8.png"
  alt="universal-updater cia" style="max-width:100%;"></a></p>'
updated: '2020-11-03T16:59:59Z'
version: v3.0.0
version_title: Universal Updater 3.0.0 - Happy 1st Anniversary
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