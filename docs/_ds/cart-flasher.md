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
    size: 236032
    size_str: 230 KiB
    url: https://github.com/tasken/cart-flasher/releases/download/v0.6-shiinotic/cart_flasher.nds
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
update_notes: '<h3 dir="auto">Recovery</h3>

  <ul dir="auto">

  <li>Added recovery for 2 MiB Ace3DS+/R4iLS carts using the SpongeBob <code class="notranslate">AL3E</code>
  boot profile.</li>

  <li>Recovery now tries the validated Deep Labyrinth <code class="notranslate">ADLE</code>
  and SpongeBob <code class="notranslate">AL3E</code> profiles.</li>

  <li>Both profiles verify the expected flash capacity before enabling backup or write,
  and keep ntrboot injection disabled during recovery.</li>

  </ul>

  <h3 dir="auto">Reliability</h3>

  <ul dir="auto">

  <li>Cart command failures now stop the affected operation instead of continuing
  with stale results.</li>

  </ul>

  <h3 dir="auto">Interface</h3>

  <ul dir="auto">

  <li>Improved recovery, backup, write, progress, and error-screen layout.</li>

  <li>Improved cart driver-credit display.</li>

  </ul>'
updated: '2026-08-22T05:53:26Z'
version: v0.6-shiinotic
version_title: v0.6-shiinotic
---
A DS/DSi homebrew application to backup and restore raw flash images to/from Slot-1 flashcarts.

Supports Ace3DS Plus, AK2i, DSTT, R4iSDHC family, and R4i Gold 3DS, in both DS and DSi mode.