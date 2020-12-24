---
author: Universal-Team
categories:
- utility
color: '#045190'
created: '2019-10-31T02:19:37Z'
description: An easy to use app for installing and updating 3DS homebrew
download_page: https://github.com/Universal-Team/Universal-Updater/releases/tag/untagged-f5b9aac21a7afd25a5ff
downloads: {}
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
update_notes: '<h3>What''s New?</h3>

  <ul>

  <li>Shortcuts: When using the homebrew launcher you can now create shortcuts for
  easily updating specific apps</li>

  <li>Screenshots: You can now see what apps look like before downloading!</li>

  <li>Sizes: Downloads can now have a size so you know how big they''ll be</li>

  <li>Songs: You can now use a WAV file up to 10 MiB as background music, place it
  at <code>sdmc:/3ds/Universal-Updater/music.wav</code></li>

  <li>Safety: Universal-Updater now has parental controls set, at the same level as
  the homebrew launcher and FBI, so you don''t have to worry about kids messing with
  it</li>

  <li>Stores: There''s now a list of of recommended UniStores accessible from the
  select UniStore menu so you don''t even need to find a QR code or enter a URL</li>

  <li>setoN: Okay fine, finally out of S words... but there''s still more! You can
  now view the release Notes for apps so you know what''s changed!</li>

  <li>Added Ukrainian</li>

  <li>Added custom font support

  <ul>

  <li>A default extended font will be downloaded on selecting Ukrainian as the default
  font is missing some letters</li>

  </ul>

  </li>

  <li>Toggle icons now have color when on to be more clear</li>

  <li>Portuguese (Portugal), Lithuanian, and Danish have been removed for now due
  to lack of translations, however if anyone helps translate they will be added back</li>

  </ul>

  <h3>Bug fixes:</h3>

  <ul>

  <li>Fixed an out of bounds access</li>

  <li>Fix grid scrolling sometimes going too far</li>

  <li>Fixed crashing when staring Universal-Updater without Wi-Fi</li>

  <li>Double new lines no longer break wrapped text (fixed by Citro2D v1.5.0)</li>

  </ul>

  <h3>Other notes:</h3>

  <p>Find any bugs we missed, have suggestions, or need help? Make an issue or discussion
  here on GitHub. Normally this is where we''d offer to join our <a href="https://universal-team.net/discord"
  rel="nofollow">Discord server</a>, but we''re not allowing new members as of the
  creation of this release unless you know someone on the server and ask them to let
  us know you should be let in.</p>

  <p>We hope you enjoy the new update and have a merry Christmas!<br>

  ~ Univeral-Team</p>'
updated: null
version: v3.1.0
version_title: Christmas Update - Shortcuts, Screenshots, Sizes, Songs, Safety, setoN
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