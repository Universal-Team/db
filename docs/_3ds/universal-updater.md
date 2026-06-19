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
    size: 3002740
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.4.0/Universal-Updater.3dsx
  Universal-Updater.cia:
    size: 2479040
    size_str: 2 MiB
    url: https://github.com/Universal-Team/Universal-Updater/releases/download/v3.4.0/Universal-Updater.cia
github: Universal-Team/Universal-Updater
icon: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/app/icon.png
image: https://raw.githubusercontent.com/Universal-Team/Universal-Updater/master/resources/2d-banner.png
image_length: 24475
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: none
nightly:
  download_page: https://github.com/Universal-Team/Universal-Updater/releases/tag/git
  downloads:
    Universal-Updater.3dsx:
      size: 3002856
      size_str: 2 MiB
      url: https://github.com/Universal-Team/Universal-Updater/releases/download/git/Universal-Updater.3dsx
    Universal-Updater.cia:
      size: 2479040
      size_str: 2 MiB
      url: https://github.com/Universal-Team/Universal-Updater/releases/download/git/Universal-Updater.cia
  qr:
    Universal-Updater.cia: https://db.universal-team.net/assets/images/qr/git/universal-updater-cia.png
  update_notes: '<p dir="auto">Pk11 - Fix crash on exiting while helper thread is
    running</p>

    <p dir="auto">This also merges both threaded activities onto the same thread state
    for simplicity, downside is that now you may be forced to wait out the other thread
    if you quickly switch between directory settings and UniStore settings... but
    that''s not too big a concern.</p>'
  update_notes_md: 'Pk11 - Fix crash on exiting while helper thread is running


    This also merges both threaded activities onto the same thread state for simplicity,
    downside is that now you may be forced to wait out the other thread if you quickly
    switch between directory settings and UniStore settings... but that''s not too
    big a concern.'
  updated: '2026-06-18T22:28:46Z'
  version: git
  version_title: Continuous Build - 85d397e
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
stars: 1238
systems:
- 3DS
title: Universal-Updater
unique_ids:
- '0x43917'
unistore_exclude: true
update_notes: '<p dir="auto">Proxy users rejoice! One of the oldest issues on the
  tracker that no one had had the motivation to test properly, proxies should now
  be fully supported. Universal-Updater also now checks for what you have installed
  on your system and shows it with a little icon by the app icon. This lets you filter
  to easily find apps you already have installed or if you''ve got a lot on your system
  you can now flip the filters and instead show only new apps!</p>

  <h3 dir="auto">Features</h3>

  <ul dir="auto">

  <li>Universal-Updater now tracks installed apps (displayed by an SD card icon) and
  this can be used for filtering! (Thanks <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/TrianguloY/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/TrianguloY">@TrianguloY</a>
  for the icon!)

  <ul dir="auto">

  <li>NOTE: The tracking is done by title ID and file path so conflicting apps will
  be displayed even if not installed (ex. HBL forks)</li>

  </ul>

  </li>

  <li>Added a "NOT" filtering option to invert the filter, most useful for filtering
  to only apps not installed</li>

  <li>The search menu now includes all app names in the word completion dictionary!</li>

  <li>Proxies are now properly supported! (Thanks <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/lxfly2000/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/lxfly2000">@lxfly2000</a>)

  <ul dir="auto">

  <li>By default the system proxy will be used as HTTP, but other types of proxies
  supported by curl can be set in settings</li>

  </ul>

  </li>

  </ul>

  <h3 dir="auto">Changes</h3>

  <ul dir="auto">

  <li>The SSL CA certificate bundle will now be loaded from the SD card instead of
  ROMFS

  <ul dir="auto">

  <li>Uses the location from Luma3DS (<code class="notranslate">sdmc:/config/ssl/cacert.pem</code>)</li>

  <li>Other homebrew desiring SSL peer verification are encouraged to use that location
  too, Universal-Updater will ensure it exists and is valid on load

  <ul dir="auto">

  <li>NOTE: Updating the CA certificate bundle on console in this way is technically
  a security hole as you''re downloading your source of trust from an unverified host...
  that said, its 3DS homebrew, its not that big a deal; but get the file manually
  from Luma3DS or curl if worried</li>

  </ul>

  </li>

  <li>Users are now presented with the option to disable peer verification if they
  really don''t want to fix their system date or update their certificate bundle</li>

  </ul>

  </li>

  <li>Universal-Updater now waits for a Wi-Fi connection on startup, previously it
  was possible to have the initial UniStore download fail if your 3DS was still trying
  to establish the connection</li>

  <li>The "select UniStore" menu now loads the UniStore list in a separate thread
  making for a more responsive menu</li>

  <li>A spinner is now shown when Universal-Updater is doing something in the background
  but user input is possible

  <ul dir="auto">

  <li>This is intended to draw attention to the fact that something can happen if
  you wait (or perform an outside action like syncing the time) and that skipping
  is not your only option</li>

  </ul>

  </li>

  <li>Updated for latest libctru</li>

  </ul>

  <h3 dir="auto">Bug fixes</h3>

  <ul dir="auto">

  <li>Fixed the list view cutting off one item when under 4 exist</li>

  <li>Universal-Updater now has the correct app title on the HOME Menu</li>

  <li>The update check (used for most internet sanity checks too) now pulls from Universal-DB
  instead of the GitHub API, hopefully reducing confusing errors</li>

  </ul>'
updated: '2026-06-15T20:19:18Z'
version: v3.4.0
version_title: Install checking, proxies, and more
website: https://universal-team.net/projects/universal-updater.html
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