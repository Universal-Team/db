---
author: PabloMK7
avatar: https://avatars.githubusercontent.com/u/10946643?v=4
categories:
- utility
color: '#8a959b'
color_bg: '#727b80'
created: '2022-05-23T21:53:52Z'
description: Easy Boot9Strap Updater for the 3DS
github: PabloMK7/EzB9SUpdater
icon: https://raw.githubusercontent.com/PabloMK7/EzB9SUpdater/main/resources/icon.png
image: https://raw.githubusercontent.com/PabloMK7/EzB9SUpdater/main/resources/banner.png
image_length: 27384
layout: app
license: other
license_name: Other
screenshots:
- description: Main menu
  url: https://db.universal-team.net/assets/images/screenshots/ezb9supdater/main-menu.png
source: https://github.com/PabloMK7/EzB9SUpdater
stars: 25
systems:
- 3DS
title: EzB9SUpdater
unique_ids:
- '0xECB95'
updated: '---'
---
EzB9SUpdater is an utility that allows updating to the latest Boot9Strap version directly on the 3DS without the need of a computer or SD card reader. This tool downloads the latest Boot9Strap and SafeB9SInstaller to the SD card and starts the B9S update process. Since the app fetches the latest version and configuration from its github repo, it can be adjusted or disabled remotely if a new version of B9S is released again or compatibility is lost. As the app does exactly the same steps as the 3DS hacking guide, it's perfectly safe to use.

## Usage

1. Install the EzB9SUpdater cia or scan the QR code above.
1. Launch the EzB9SUpdater app from the Home Menu.
1. Follow the instructions in the app. At some point, you will be asked to press and hold the START button to reboot into SafeB9SInstaller. It is important that you keep holding the button until you see the SafeB9SInstaller screen. Otherwise, the console will just reboot into EzB9SUpdater and no update will be performed.
1. Once you finish the B9S update, you can exit the app and uninstall it from FBI.
1. In order to check if you updated B9S from 1.3 to 1.4 do the following steps:
   1. Power off your console.
   1. Press and hold the following button combination: `X + START + SELECT`.
   1. Without releasing those buttons, power on your device.
   1. Your notification LED should lit up for a second ([status codes](https://github.com/PabloMK7/boot9strap/tree/patch-1#led-status-codes)). If it didn't, the update wasn't installed properly.