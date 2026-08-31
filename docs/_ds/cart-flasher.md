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
    size: 252416
    size_str: 246 KiB
    url: https://github.com/tasken/cart-flasher/releases/download/v0.7-kirlia/cart_flasher.nds
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
stars: 4
systems:
- DS
title: cart-flasher
update_notes: '<h3 dir="auto">DS banner tools</h3>

  <ul dir="auto">

  <li>Added <strong>Back up DS banner</strong> and <strong>Write DS banner</strong>
  for supported Ace3DS+ and R4iSDHC carts.</li>

  <li>Banner backups are validated and saved in <code class="notranslate">cart-backups/banners</code>
  without replacing older backups.</li>

  <li>Banner writes validate the selected Regular DS v1 banner and the cart''s known
  layout before changing anything, update only the banner blocks, and verify the result
  afterward.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/tasken/cart-flasher/compare/v0.6-shiinotic...v0.7-kirlia"><tt>v0.6-shiinotic...v0.7-kirlia</tt></a></p>'
updated: '2026-08-26T05:02:27Z'
version: v0.7-kirlia
version_title: v0.7-kirlia
---
A DS/DSi homebrew application to backup and restore raw flash images to/from Slot-1 flashcarts.

Supports Ace3DS Plus, AK2i, DSTT, R4iSDHC family, and R4i Gold 3DS, in both DS and DSi mode.