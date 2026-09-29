---
author: quatric
avatar: https://avatars.githubusercontent.com/u/288748141?v=4
banner: https://raw.githubusercontent.com/quatric/3DS-DNS-Switcher/main/standalone/assets/banner-v3.png
categories:
- utility
color: '#357cc1'
color_bg: '#235280'
created: '2026-08-29T23:53:44Z'
description: A Nintendo 3DS application for quickly switching the DNS used by existing
  Wi-Fi connections.
download_page: https://github.com/quatric/3DS-DNS-Switcher/releases
downloads:
  3DS-DNS-Switcher.3dsx:
    size: 210800
    size_str: 205 KiB
    url: https://github.com/quatric/3DS-DNS-Switcher/releases/download/v1.1/3DS-DNS-Switcher.3dsx
  3DS-DNS-Switcher.cia:
    size: 330688
    size_str: 322 KiB
    url: https://github.com/quatric/3DS-DNS-Switcher/releases/download/v1.1/3DS-DNS-Switcher.cia
github: quatric/3DS-DNS-Switcher
icon: https://raw.githubusercontent.com/quatric/3DS-DNS-Switcher/main/standalone/assets/icon-v2.png
image: https://raw.githubusercontent.com/quatric/3DS-DNS-Switcher/main/standalone/assets/icon-v2.png
image_length: 3562
layout: app
llm_generation: 'yes'
qr:
  3DS-DNS-Switcher.cia: https://db.universal-team.net/assets/images/qr/3ds-dns-switcher-cia.png
source: https://github.com/quatric/3DS-DNS-Switcher
stars: 2
systems:
- 3DS
title: 3DS-DNS-Switcher
unique_ids:
- '0xBC8D4'
updated: '2026-09-28T18:15:31Z'
version: v1.1
version_title: v1.1
---
A Nintendo 3DS application for quickly switching the DNS used by existing Wi-Fi connections.

Features

- Saves named primary-DNS profiles on the SD card.
- Shows the profile list on every launch, including first setup.
- Press R to choose and remember the target: all configured Wi-Fi slots or connection slot 1, 2, or 3.
- Press A to apply the highlighted profile immediately.
- Always uses 1.1.1.1 as the secondary DNS.
- Exits automatically after a successful change.
- Preserves SSIDs, passwords, DHCP, proxy, and other connection settings.

Profiles are stored at sdmc:/3ds/dns-switcher/profiles.txt, and the target is stored at sdmc:/3ds/dns-switcher/settings.txt.