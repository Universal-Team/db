---
author: cmdada
avatar: https://avatars.githubusercontent.com/u/79297197?v=4
categories:
- emulator
color: '#433943'
color_bg: '#433943'
created: '2026-05-10T04:52:37Z'
description: Run full RISCV Linux on (almost) every single Nintendo console
download_page: https://github.com/cmdada/3DS-CLI/releases
downloads:
  3ds_cli.zip:
    size: 57500649
    size_str: 54 MiB
    url: https://github.com/cmdada/3DS-CLI/releases/download/4.0/3ds_cli.zip
github: cmdada/3DS-CLI
icon: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image: https://raw.githubusercontent.com/cmdada/3DS-CLI/main/icon.png
image_length: 3509
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
source: https://github.com/cmdada/3DS-CLI
stars: 38
systems:
- 3DS
title: 3DS-CLI
unique_ids:
- '0x1111'
update_notes: '<h2 dir="auto">Setup</h2>

  <p dir="auto">One <code class="notranslate">Image</code> serves every console -
  the guest is identical, only the<br>

  host binary differs. Copy <code class="notranslate">Image</code> to the root of
  your SD card, then<br>

  the binary for your console:</p>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Console</th>

  <th>Binary</th>

  <th>Goes to</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td>3DS</td>

  <td><code class="notranslate">3ds/3ds-cli.3dsx</code></td>

  <td><code class="notranslate">sdmc:/3ds/3ds-cli/</code></td>

  </tr>

  <tr>

  <td>Wii U</td>

  <td><code class="notranslate">wiiu/3ds-cli.wuhb</code></td>

  <td><code class="notranslate">sd:/wiiu/apps/</code></td>

  </tr>

  <tr>

  <td>Switch</td>

  <td><code class="notranslate">switch/3ds-cli.nro</code></td>

  <td><code class="notranslate">sdmc:/switch/</code></td>

  </tr>

  <tr>

  <td>Wii</td>

  <td><code class="notranslate">wii/3ds-cli.dol</code></td>

  <td><code class="notranslate">sd:/apps/3ds-cli/boot.dol</code></td>

  </tr>

  <tr>

  <td>GameCube</td>

  <td><code class="notranslate">gamecube/3ds-cli.dol</code></td>

  <td>SD Gecko / SD2SP2</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">The Image has the root filesystem bundled in: on first boot the app<br>

  unpacks it to <code class="notranslate">rootfs.ext2</code> on the card, which stays
  as the writable<br>

  disk from then on - changes persist across sessions.<br>

  Includes: bash, htop, neofetch, nano, vim, tree, wget, dropbear,<br>

  procps, util-linux.</p>'
updated: '2026-08-21T19:15:34Z'
version: '4.0'
version_title: V4.0 - Wii U, Switch, Wii and GameCube
---

A Nintendo 3DS homebrew application that embeds a full RISC-V CPU emulator (`mini-rv32ima` by cnlohr) to boot a real Linux environment inside the 3DS Horizon OS.

Features a custom ANSI/xterm terminal emulator on the top screen with full 16/256/24-bit colour support, zoom, and viewport panning, plus a custom bottom-screen touch keyboard. Comes with a prebuilt image including BusyBox tools, a JavaScript runtime, and some other goodies.

## Controls
- **L / Y**: Zoom out
- **R / X**: Zoom in
- **ZL**: Toggle auto-follow cursor
- **ZR**: Toggle font (8x8 ↔ 5x7 compact)
- **Circle Pad**: Pan viewport
- **D-Pad**: Send arrow keys to Linux
- **START**: Quit and return to Homebrew Launcher

## Keyboard
- **SHF**: Shift (uppercase)
- **?#1 / #+=**: Symbol layers
- **ABC**: Return to alphabetic layer
- **CTL**: Ctrl modifier
- **TAB / ESC / ENT / DEL**: As labelled

## Credits
- Built using libctru and minirv32-ima

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>3ds-cli.3dsx</summary>
<ol>
<li>Download <code>3ds_cli.zip</code></li>
<li>Extract <code>/3ds-cli.3dsx</code> from the zip to <code>/3ds/3ds-cli.3dsx</code> on your SD card</li>
<li>Extract <code>/Image</code> from the zip to <code>/Image</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>3ds-cli.cia</summary>
<ol>
<li>Download <code>3ds_cli.zip</code></li>
<li>Extract <code>/3ds-cli.cia</code> from the zip to <code>/cias/3ds-cli.cia</code> on your SD card</li>
<li>Extract <code>/Image</code> from the zip to <code>/Image</code> on your SD card</li>
<li>Insert your SD card back into your 3DS and turn it on</li>
<li>Install and delete <code>/cias/3ds-cli.cia</code> using FBI or GodMode9</li>
</ol>
</details>

