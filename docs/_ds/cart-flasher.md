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
    size: 255488
    size_str: 249 KiB
    url: https://github.com/tasken/cart-flasher/releases/download/v0.8-tinkatuff/cart_flasher.nds
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
stars: 5
systems:
- DS
title: cart-flasher
update_notes: '<h3 dir="auto">Ace3DS+ support</h3>

  <ul dir="auto">

  <li>Added support for the 2 MiB Tsingteng TH25Q16 Ace3DS+ variant.</li>

  <li><code class="notranslate">Back up DS banner</code> and <code class="notranslate">Write
  DS banner</code> now work with its verified Deep Labyrinth <code class="notranslate">ADLE</code>
  layout.</li>

  <li>Cart information now names the known Tsingteng and Macronix 2 MiB variants.</li>

  </ul>

  <h3 dir="auto">Cart detection</h3>

  <ul dir="auto">

  <li>A nonresponsive cart no longer leaves Cart-Flasher stuck during detection or
  reset. It returns to the detection-failure screen instead.</li>

  <li>Press <code class="notranslate">&lt;SELECT&gt;</code> on the cart list to open
  Hardware probe.</li>

  </ul>

  <h3 dir="auto">Ease of use</h3>

  <ul dir="auto">

  <li>Overall verbiage clearer and more consistent.</li>

  <li>A wrong key combo immediately shows a new sequence.</li>

  <li>Improved the layout of flash-backup and destructive confirmation screens.</li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/tasken/cart-flasher/compare/v0.7-kirlia...v0.8-tinkatuff"><tt>v0.7-kirlia...v0.8-tinkatuff</tt></a></p>'
updated: '2026-09-12T01:55:03Z'
version: v0.8-tinkatuff
version_title: v0.8-tinkatuff
---
A DS/DSi homebrew application to backup and restore raw flash images to/from Slot-1 flashcarts.

Supports Ace3DS Plus, AK2i, DSTT, R4iSDHC family, and R4i Gold 3DS, in both DS and DSi mode.