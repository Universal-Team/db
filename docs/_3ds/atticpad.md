---
author: ProPaint
avatar: https://avatars.githubusercontent.com/u/316614385?v=4
categories:
- app
color: '#605039'
color_bg: '#605039'
created: '2026-08-13T14:33:00Z'
description: Use your 3DS as a gamepad for a Windows or Linux PC over Wi-Fi.
download_filter: 3dsx|cia
download_page: https://github.com/atticpad/atticpad/releases
downloads:
  atticpad-3ds.3dsx:
    size: 366880
    size_str: 358 KiB
    url: https://github.com/atticpad/atticpad/releases/download/v0.6.0/atticpad-3ds.3dsx
  atticpad-3ds.cia:
    size: 420800
    size_str: 410 KiB
    url: https://github.com/atticpad/atticpad/releases/download/v0.6.0/atticpad-3ds.cia
github: atticpad/atticpad
icon: https://raw.githubusercontent.com/atticpad/atticpad/main/clients/3ds/meta/icon.png
image: https://raw.githubusercontent.com/atticpad/atticpad/main/clients/3ds/meta/banner3d/preview.png
image_length: 62032
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
preinstall_message: Install AtticPad server on your PC first, this app is a controller
  for it. github.com/atticpad/atticpad
qr:
  atticpad-3ds.cia: https://db.universal-team.net/assets/images/qr/atticpad-3ds-cia.png
source: https://github.com/atticpad/atticpad
stars: 4
systems:
- 3DS
title: AtticPad
unique_ids:
- '0xA771C'
update_notes: '<h3 dir="auto">Added</h3>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Keyboard, mouse and media remote control</strong>, on top
  of the gamepad. Four<br>

  new additive message types — <code class="notranslate">KEYBOARD</code> 0x21, <code
  class="notranslate">MOUSE</code> 0x22, <code class="notranslate">MEDIA</code> 0x23,<br>

  <code class="notranslate">INPUTCAPS</code> 0x44 — allocated after the v1 freeze
  under the rule<br>

  <code class="notranslate">docs/PROTOCOL.md</code> §6.14 states and audits them against:
  nothing that<br>

  existed before changed size, position or meaning, and <code class="notranslate">caps</code>
  (§6.3) is<br>

  untouched on purpose. A server advertises which of the three it accepts via<br>

  <code class="notranslate">INPUTCAPS</code>; a client shows nothing until it hears
  that, and an old client<br>

  or an old server simply never speaks the new types at all. See<br>

  <a href="docs/KBM.md"><code class="notranslate">docs/KBM.md</code></a> for the full
  picture, including the Windows<br>

  <code class="notranslate">SendInput</code> limitations and the 10 of 24 §6.18 media
  controls that backend<br>

  cannot drive.</p>

  <ul dir="auto">

  <li><strong>Android</strong> — a mode bar (PAD/MOUSE/KEYBOARD/MEDIA): a trackpad
  view, a<br>

  real physical-style key grid with genuine multi-finger chord support, a<br>

  curated text-entry bar, and a media remote.</li>

  <li><strong>3DS</strong> — the same four modes on the bottom screen, adapted to
  a<br>

  resistive, single-contact touchscreen: a sticky SHIFT/CTRL latch for<br>

  KEYS mode, plus physical L/R as always-live modifiers on top of it.</li>

  <li><strong>Linux server</strong> — three <code class="notranslate">uinput</code>
  nodes per session, created lazily on<br>

  first use and torn down in spec order (release held state, then destroy<br>

  the device) before a session closes.</li>

  <li><strong>Windows server</strong> — a <code class="notranslate">SendInput</code>-based
  backend. Built and compiled in<br>

  CI on every push; <strong>never run on real Windows hardware as of this<br>

  writing</strong> — see <code class="notranslate">docs/KBM.md</code> for the specific,
  permanent limitations<br>

  (UIPI elevation, the secure desktop, anti-cheat rejection, pointer<br>

  ballistics, and one shared system keyboard/mouse across sessions) and<br>

  <code class="notranslate">docs/QA.md</code> §11 for the hardware checklist this
  still needs.</li>

  <li><code class="notranslate">docs/PROTOCOL.md</code> §6.22 reserves message type
  <code class="notranslate">0x24</code> for a future<br>

  <code class="notranslate">TEXT</code> type, because today''s <code class="notranslate">KEYBOARD</code>
  carries HID usage IDs (physical<br>

  key positions) and text entry therefore assumes a US-QWERTY host layout<br>

  — see <code class="notranslate">docs/KBM.md</code>.</li>

  </ul>

  </li>

  <li>

  <p dir="auto"><strong>PlayStation Portable client</strong> (<code class="notranslate">EBOOT.PBP</code>,
  in <code class="notranslate">atticpad-psp.zip</code>).<br>

  Analog nub, every button, an on-screen keypad for the address and the<br>

  PIN, PIN pairing, the server and network remembered, and the self-test.<br>

  Hardware-proven — see <code class="notranslate">docs/SUPPORT-TIERS.md</code> and
  <code class="notranslate">docs/INSTALL.md</code>.</p>

  </li>

  <li>

  <p dir="auto"><strong>Nintendo DS / DSi client</strong> (<code class="notranslate">atticpad-nds.nds</code>).
  The 3DS screens on a<br>

  DS: a network picker with WEP keys typed on the touch keyboard, typed<br>

  address and PIN, the four PAD / MOUSE / KEYS / MEDIA modes, the<br>

  self-test, and the last server and network remembered. In DSi mode it<br>

  joins WPA2, reports the battery, and pairs by scanning the server''s QR<br>

  with the camera. The server ships a <code class="notranslate">ds-default</code>
  profile that drives the<br>

  left stick from the touchscreen. Hardware-proven in both modes — see<br>

  <code class="notranslate">docs/SUPPORT-TIERS.md</code>, <code class="notranslate">docs/INSTALL.md</code>
  and <code class="notranslate">docs/SETUP-DS.md</code> for<br>

  the open-or-WEP constraint of DS mode.</p>

  </li>

  <li>

  <p dir="auto"><strong>A profile can map a button to a trigger.</strong> <code class="notranslate">"L":
  "LT"</code> in a profile''s<br>

  buttons map gives a device with no analog triggers, such as the PSP, a<br>

  full-pull LT while the button is held; the web editor offers LT and RT<br>

  in the button dropdown.</p>

  </li>

  </ul>

  <h3 dir="auto">Changed</h3>

  <ul dir="auto">

  <li><strong>Discovery on the 3DS and DS prefers the server you last used.</strong>
  When<br>

  more than one server answers a LAN DISCOVER, the console now picks the one<br>

  whose address it saved after its last session (or picked last time) rather<br>

  than whichever answered first; the first responder only wins when the<br>

  remembered one stays silent for the whole window. On a LAN with two<br>

  servers the faster machine used to win every boot and look hardcoded.<br>

  Nothing is hardcoded: a fresh unit still starts empty. The Android<br>

  address field''s placeholder no longer looks like a real address.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li><strong>A sticky Shift on the 3DS typed a lowercase letter.</strong> The server
  applied<br>

  a report''s keys in usage order, so a letter arriving in the same report as<br>

  Shift was pressed before it. Modifiers now go first, as a host treats a<br>

  real HID keyboard report.</li>

  <li><strong>The 3DS never updated its remembered server after the first save.</strong>
  The<br>

  console''s filesystem refuses a rename onto an existing file; the old file<br>

  is removed first now.</li>

  <li><strong>The PSP rejoins the network after a suspend.</strong> A power callback
  re-runs<br>

  the network bring-up on resume.</li>

  </ul>

  <hr>

  <h2 dir="auto">Install</h2>

  <p dir="auto"><strong>Server</strong> — on the PC that needs a controller. Pick
  one:</p>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Windows:</strong> download <code class="notranslate">atticpad-server-windows-x86_64.exe</code>
  and run it. It needs<br>

  the ViGEmBus driver, which is easiest to install with winget:</p>

  <pre class="notranslate"><code class="notranslate">winget install ViGEm.ViGEmBus

  </code></pre>

  <p dir="auto">or grab the installer from<br>

  <a href="https://github.com/nefarius/ViGEmBus/releases">its releases page</a>. SmartScreen<br>

  will warn about AtticPad''s unsigned binary (<em>More info → Run anyway</em>).</p>

  </li>

  <li>

  <p dir="auto"><strong>Linux:</strong> download <code class="notranslate">atticpad-server-linux-x86_64</code>,
  <code class="notranslate">chmod +x</code> it, and run it.<br>

  It needs access to <code class="notranslate">/dev/uinput</code> — <a href="https://github.com/atticpad/atticpad/blob/v0.6.0/docs/INSTALL.md">INSTALL.md</a>
  has the<br>

  one-line udev rule.</p>

  </li>

  </ul>

  <p dir="auto">The server prints the address to type into a client, and serves a
  local page on<br>

  <a href="http://127.0.0.1:21150/" rel="nofollow">http://127.0.0.1:21150/</a> for
  pad status, round-trip latency and profile editing.</p>

  <p dir="auto"><strong>Client</strong> — on the device you want to hold:</p>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Nintendo 3DS</strong> (needs Luma3DS custom firmware) — open
  <strong>FBI → Remote Install<br>

  → Scan QR Code</strong> and scan this. No SD card, no cable:</p>

  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/atticpad/atticpad/v0.6.0/docs/img/fbi-install-qr.png"><img
  src="https://raw.githubusercontent.com/atticpad/atticpad/v0.6.0/docs/img/fbi-install-qr.png"
  alt="QR code that installs the AtticPad .cia from the latest release" width="200"
  style="max-width: 100%;"></a>

  <p dir="auto">If that image does not load, the same code is attached to this release
  as<br>

  <code class="notranslate">atticpad-3ds-install-qr.png</code>, and FBI''s <em>Receive
  URLs over the network</em> will<br>

  take the URL it encodes directly:<br>

  <code class="notranslate">https://github.com/atticpad/atticpad/releases/latest/download/atticpad-3ds.cia</code></p>

  <p dir="auto">Or copy <code class="notranslate">atticpad-3ds.cia</code> to the SD
  card and install it with FBI from there.<br>

  <code class="notranslate">atticpad-3ds.3dsx</code> runs from the Homebrew Launcher
  instead, without installing.</p>

  </li>

  <li>

  <p dir="auto"><strong>Android 8.0+</strong> — sideload <code class="notranslate">atticpad-android.apk</code>.
  If you already have a debug<br>

  build installed, uninstall it first: the signatures differ.</p>

  </li>

  <li>

  <p dir="auto"><strong>PSP</strong> (custom firmware) — unzip <code class="notranslate">atticpad-psp.zip</code>
  onto the root of the<br>

  memory stick and launch <strong>AtticPad</strong> from the XMB. Set up a saved Wi-Fi<br>

  connection first; the PSP speaks WEP and WPA over 802.11b, so a WPA2-only<br>

  router will refuse it.</p>

  </li>

  <li>

  <p dir="auto"><strong>Nintendo DS / DSi</strong> (flashcart or homebrew launcher)
  — copy<br>

  <code class="notranslate">atticpad-nds.nds</code> to the card and launch it. In
  DS mode the console can only<br>

  join an open or WEP network; <a href="https://github.com/atticpad/atticpad/blob/v0.6.0/docs/SETUP-DS.md">SETUP-DS.md</a>
  shows how to<br>

  run a small isolated one. In DSi mode it joins WPA2 and pairs by scanning<br>

  the QR with the camera.</p>

  </li>

  </ul>

  <p dir="auto">Then pair once. On the 3DS that means scanning the QR code the server
  shows —<br>

  the console has no PIN keypad, so the QR is the only way in. On Android you can<br>

  scan it or type the 6-digit PIN.</p>

  <p dir="auto"><strong>Before you use it on a network you do not control, read the
  security section<br>

  of the README.</strong> By default the server accepts any device on your LAN with
  no<br>

  PIN.</p>

  <p dir="auto">Verify what you downloaded:</p>

  <pre class="notranslate"><code class="notranslate">sha256sum -c SHA256SUMS

  </code></pre>'
updated: '2026-09-15T12:20:54Z'
version: v0.6.0
version_title: AtticPad v0.6.0
---
Use your 3DS as a gamepad for your PC, over Wi-Fi.

**You need the server too.** It runs on the PC you want to play on, and it is
what creates the virtual controller:
https://github.com/atticpad/atticpad/releases

Windows and Linux. One file, no installer.

## What the 3DS sends

- All buttons, Circle Pad, and C-Stick on a New 3DS
- Gyro, for motion aiming
- The touch screen, configurable via profiles on the server.
- Its battery level, shown on the PC.

## Setting it up

1. Run the server on your PC. It shows you an address.
2. Open AtticPad on the 3DS and scan the QR code the
   server shows on screen. (or type the IP)
3. Play.

## Good to know

Everything stays on your own network. No account, no internet, no cloud.

Pairing is a QR code. By default the server accepts any device
on your LAN without one, so run it on a network you trust.

Tested on a New 3DS. The Old 3DS should work but has never been tried.

MIT licensed. Source, docs and issues:
https://github.com/atticpad/atticpad