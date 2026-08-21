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
    url: https://github.com/tasken/cart-flasher/releases/download/v0.5.4-impidimp/cart_flasher.nds
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
stars: 2
systems:
- DS
title: cart-flasher
update_notes: '<p dir="auto"><strong>Fixed</strong><br>

  Acekard 2i HW-81 carts were treated as 16MB when the flash chip is really 2MB. That
  made backups eight times bigger than they should be, and restoring one often had
  to be repeated before it stuck, sometimes leaving the cart in a bad state. Backups
  are now the right size and restore in one go. Old 16MB backups should still work
  fine.</p>

  <p dir="auto">Thanks to <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/ApacheThunder/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/ApacheThunder">@ApacheThunder</a>
  for spotting it and testing the fix on real hardware.</p>

  <p dir="auto"><strong>Changed</strong><br>

  Updated DS banner and dev/nightly builds formatting.</p>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/tasken/cart-flasher/compare/v0.5.3-comfey...v0.5.4-impidimp"><tt>v0.5.3-comfey...v0.5.4-impidimp</tt></a></p>'
updated: '2026-08-19T04:07:51Z'
version: v0.5.4-impidimp
version_title: v0.5.4-impidimp
---
A DS/DSi homebrew application to backup and restore raw flash images to/from Slot-1 flashcarts.

Supports Ace3DS Plus, AK2i, DSTT, R4iSDHC family, and R4i Gold 3DS, in both DS and DSi mode.