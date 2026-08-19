---
author: Tasken/Nimbo
avatar: https://avatars.githubusercontent.com/u/12686734?v=4
categories:
- app
- utility
color: '#536152'
color_bg: '#536152'
created: '2026-07-13T12:10:39Z'
description: A DS/DSi homebrew application to backup and restore raw flash images
  to/from Slot-1 flashcarts
download_page: https://github.com/tasken/Cart-Flasher/releases
downloads:
  cart_flasher.nds:
    size: 216576
    size_str: 211 KiB
    url: https://github.com/tasken/cart-flasher/releases/download/v0.5.3-comfey/cart_flasher.nds
github: tasken/Cart-Flasher
icon: https://raw.githubusercontent.com/tasken/Cart-Flasher/refs/heads/main/resources/icon.png
image: https://raw.githubusercontent.com/tasken/Cart-Flasher/main/resources/logo.png
image_length: 317497
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: 'yes'
qr:
  cart_flasher.nds: https://db.universal-team.net/assets/images/qr/cart_flasher-nds.png
source: https://github.com/tasken/cart-flasher
stars: 1
systems:
- DS
title: cart-flasher
update_notes: '<ul dir="auto">

  <li>Fixed firmware writes to use safe 64 KiB chunks, preventing partial-page corruption
  on Acekard 2i, DSTT, R4i Gold 3DS, and R4 SDHC Dual-Core carts.</li>

  <li>Removed two vendor build warnings: an incompatible libncgc reset-callback cast
  and an unused R4 SDHC Dual-Core local.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/tasken/cart-flasher/compare/v0.5.2-comfey...v0.5.3-comfey"><tt>v0.5.2-comfey...v0.5.3-comfey</tt></a></p>'
updated: '2026-08-01T20:04:29Z'
version: v0.5.3-comfey
version_title: v0.5.3-comfey
---
A DS/DSi homebrew application to backup and restore raw flash images to/from Slot-1 flashcarts.

Supports Ace3DS Plus, AK2i, DSTT, R4iSDHC family, and R4i Gold 3DS, in both DS and DSi mode.