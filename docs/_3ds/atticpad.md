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
    size: 324996
    size_str: 317 KiB
    url: https://github.com/atticpad/atticpad/releases/download/v0.5.0/atticpad-3ds.3dsx
  atticpad-3ds.cia:
    size: 400320
    size_str: 390 KiB
    url: https://github.com/atticpad/atticpad/releases/download/v0.5.0/atticpad-3ds.cia
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
stars: 2
systems:
- 3DS
title: AtticPad
unique_ids:
- '0xA771C'
update_notes: '<p dir="auto"><strong>First public release.</strong> AtticPad was built
  over several months before this<br>

  tag; everything is listed once here rather than backdated into releases that<br>

  were never published. A 0.4.0 was prepared and never finalised, so its work is<br>

  part of this release too.</p>

  <p dir="auto">Install instructions are in <a href="docs/INSTALL.md"><code class="notranslate">docs/INSTALL.md</code></a>
  — including a<br>

  QR code you can scan straight from FBI to install on a 3DS without touching an<br>

  SD card.</p>

  <h3 dir="auto">Highlights</h3>

  <ul dir="auto">

  <li><strong>The server now tells the client where its touch controls are.</strong>
  A new<br>

  message, <code class="notranslate">TOUCHMAP</code> (§6.12), carries the active profile''s
  touch regions —<br>

  their rectangles and the button each one presses. The 3DS draws them on the<br>

  touchscreen, so the bottom screen finally shows the controls you actually<br>

  have instead of a fixed block of text. The server sends the layout when a<br>

  client connects, when the profile is edited and saved, and when a connected<br>

  pad is switched to a different profile.</li>

  <li><strong>Protocol v1 is still frozen, and this did not unfreeze it.</strong>
  §4 requires a<br>

  client to silently discard message types it does not know, which is exactly<br>

  what a 0.4.0 client does with <code class="notranslate">TOUCHMAP</code>. Nothing
  that existed before changed<br>

  size, position or meaning. <code class="notranslate">docs/PROTOCOL.md</code> §6.14
  records what "frozen"<br>

  permits, so the next addition does not have to re-argue it.</li>

  <li><strong>The web UI''s test view draws a real Xbox 360 pad</strong> instead of
  numbered<br>

  boxes: sticks, triggers, bumpers and d-pad light up in place, so it is<br>

  obvious at a glance which physical control a client is actually sending.</li>

  </ul>

  <h3 dir="auto">Fixed</h3>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Analog sticks reached a diamond, not a circle.</strong> The
  server shaped each<br>

  stick axis independently, so with the default quadratic response curve a<br>

  round stick became the locus <code class="notranslate">|x| + |y| = 1</code> — full
  deflection on a diagonal<br>

  produced only <strong>0.66</strong> of the magnitude a cardinal push did, so every<br>

  diagonal was a third slower than it should have been. Shaping is now radial:<br>

  the magnitude is shaped once and re-projected along the input direction, so<br>

  direction is preserved exactly and the reachable set is a disc. The deadzone<br>

  becomes a dead <em>disc</em> rather than a dead <em>cross</em>, so a nearly-horizontal
  push<br>

  no longer has its small vertical component silently zeroed. This was<br>

  server-side, so it affected every client at once and is fixed for all of them<br>

  without updating anything on the device.</p>

  </li>

  <li>

  <p dir="auto"><strong>Bluetooth HID mode put the sticks and triggers on the wrong
  axes.</strong> The<br>

  HID report descriptor declared the right stick on <code class="notranslate">Z</code>/<code
  class="notranslate">Rz</code> and the triggers<br>

  on <code class="notranslate">Rx</code>/<code class="notranslate">Ry</code> — the
  DualShock arrangement — while Windows assigns axis slots<br>

  by usage and games expect the Xbox one. The result was a right stick that<br>

  drove a trigger and a trigger that drove a stick axis. The descriptor now<br>

  matches what an Xbox Bluetooth controller reports: left stick <code class="notranslate">X</code>/<code
  class="notranslate">Y</code>, left<br>

  trigger <code class="notranslate">Z</code>, right stick <code class="notranslate">Rx</code>/<code
  class="notranslate">Ry</code>, right trigger <code class="notranslate">Rz</code>,
  D-pad on the hat.<br>

  <strong>Re-pair the phone after updating</strong> — a host caches the report descriptor<br>

  from pairing, so it will keep using the old axis map until you remove the<br>

  device and pair again.</p>

  </li>

  <li>

  <p dir="auto"><strong>The web UI''s pad view mis-drew controllers the browser does
  not remap.</strong> It<br>

  assumed the Gamepad API''s <code class="notranslate">standard</code> layout for
  every pad. One the browser<br>

  does not recognise reports no mapping and exposes its axes in the device''s own<br>

  order, so the view drew the wrong controls and printed misleading axis<br>

  numbers. It now says so plainly and lists the raw axis and button values<br>

  instead of a picture that cannot be trusted.</p>

  </li>

  <li>

  <p dir="auto"><strong>The Windows server crashed on startup</strong> when it had
  no profiles directory,<br>

  because it freed uninitialised stack pointers on the built-in-profile<br>

  fallback path. Linux had the same bug and survived it by luck.</p>

  </li>

  <li>

  <p dir="auto"><strong>Duplicating a profile failed</strong> with "could not write
  the profile file" on a<br>

  machine that had never saved one. The profiles directory is now created on<br>

  demand.</p>

  </li>

  <li>

  <p dir="auto"><strong>A profile saved to disk hid the built-in profiles</strong>
  instead of taking<br>

  precedence over them, so editing one profile made the others disappear.<br>

  Startup and hot reload now assemble the list the same way, from one place.</p>

  </li>

  <li>

  <p dir="auto"><strong>Reloading profiles left already-connected pads on their old
  profile.</strong> A<br>

  live session now moves to a newly matching profile, unless it was pinned to<br>

  one by hand in the web UI.</p>

  </li>

  <li>

  <p dir="auto"><strong>The Android in-session dialogs had square corners showing
  through.</strong> The<br>

  platform draws its own opaque rectangular window behind a dialog, which showed<br>

  through the transparent corners of the app''s rounded card as four grey<br>

  notches — visible against the near-black session screen.</p>

  </li>

  <li>

  <p dir="auto"><strong>Debug and release Android builds can now coexist.</strong>
  They shared an<br>

  application ID, so installing either over the other failed on the signature<br>

  mismatch and the only way through was to uninstall first, taking the app''s<br>

  data with it. A debug build is now <code class="notranslate">net.atticpad.debug</code>,
  labelled "AtticPad<br>

  debug".</p>

  </li>

  </ul>

  <h3 dir="auto">Everything else that is in this release</h3>

  <ul dir="auto">

  <li><strong>Protocol v1</strong>, frozen: a byte-exact UDP wire format with a 12-byte
  header,<br>

  capability bits, three-tier discovery, a PIN/QR pairing handshake, and<br>

  wrap-safe sequence and tick arithmetic. <code class="notranslate">docs/PROTOCOL.md</code>
  is normative.</li>

  <li><strong><code class="notranslate">libapad</code></strong> — the shared protocol
  core in C99: codec, session state machine,<br>

  HMAC-SHA256, PBKDF2, and sequence helpers. No <code class="notranslate">malloc</code>
  after init, no<br>

  floating point, no stdio; it runs on a 67 MHz ARM9 with 4 MB RAM.</li>

  <li><strong>239 conformance vectors</strong>, generated from the specification alone
  by an<br>

  author who did not read the codec, and shipped in every client as an<br>

  on-device self-test — on consoles, by holding <strong>L+R+Start</strong> at launch.</li>

  <li><strong>Nintendo 3DS client</strong> — <code class="notranslate">.cia</code>
  and <code class="notranslate">.3dsx</code>. Buttons, circle pad, C-stick,<br>

  gyro, touchscreen, battery reporting, on-screen IP entry, and a QR scanner<br>

  for pairing.</li>

  <li><strong>Android client</strong> — a single APK with no third-party runtime dependencies.<br>

  On-screen touch controls, physical gamepad passthrough, gyro and<br>

  accelerometer, QR scanning, and a foreground service that survives the<br>

  screen going off. Android 8.0+, arm64-v8a / armeabi-v7a / x86_64.</li>

  <li><strong>Linux server</strong> — creates virtual gamepads through <code class="notranslate">uinput</code>,
  enumerating as<br>

  an Xbox 360 controller so games recognise them without configuration.</li>

  <li><strong>Windows server</strong> — creates XInput gamepads through ViGEmBus,
  with a tray<br>

  application and driver detection.</li>

  <li><strong>Mapping engine and profiles</strong> — JSONC profiles owning deadzone,
  response<br>

  curve, inversion, touch regions and gyro aim, so no client ever applies a<br>

  deadzone of its own.</li>

  <li><strong>Pairing</strong> — a 6-digit PIN valid for 120 seconds, five-attempt
  lockout,<br>

  PBKDF2-HMAC-SHA256 session key derivation, and QR-code pairing that carries<br>

  the same secret without typing.</li>

  <li><strong>Discovery</strong> — mDNS where available, LAN broadcast, and manual
  IP entry.<br>

  Manual entry is a first-class path, because client-isolating access points<br>

  and VPNs break the other two.</li>

  <li><strong>Local web UI</strong> — bound to <code class="notranslate">127.0.0.1</code>
  only, for pad status, round-trip<br>

  latency, and a profile editor with hot reload.</li>

  </ul>

  <h3 dir="auto">Known limitations</h3>

  <ul dir="auto">

  <li>The 3DS <code class="notranslate">.cia</code> is signed with the well-known
  test key, so it installs only on<br>

  a console running Luma3DS custom firmware.</li>

  <li>The 3DS client has been run on a <strong>New 3DS</strong> only. Old 3DS is untested.</li>

  <li>The Windows server requires <strong>ViGEmBus</strong>, whose upstream project
  is archived<br>

  and no longer updated. See <code class="notranslate">docs/INSTALL.md</code>.</li>

  <li><strong>The server accepts unauthenticated clients by default.</strong> Authentication<br>

  applies only while a pairing window is open, and pairing is not remembered<br>

  between sessions — there is no persistent trusted-device list yet. Run it<br>

  only on a network you trust. See <code class="notranslate">README.md</code>.</li>

  <li>Pairing is toy-grade even when open: a 6-digit PIN cannot resist offline<br>

  brute-force by an attacker already on your LAN.</li>

  <li>The server-sent touch layout is drawn by the <strong>3DS client only</strong>.
  Android<br>

  receives it through the same shared engine and ignores it; its on-screen<br>

  controls are still laid out by the app.</li>

  <li>PS Vita, PSP, DS/DSi, Switch and desktop clients are designed but not built.<br>

  The Vita toolchain is additionally blocked upstream.</li>

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

  It needs access to <code class="notranslate">/dev/uinput</code> — <a href="https://github.com/atticpad/atticpad/blob/v0.5.0/docs/INSTALL.md">INSTALL.md</a>
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

  <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/atticpad/atticpad/v0.5.0/docs/img/fbi-install-qr.png"><img
  src="https://raw.githubusercontent.com/atticpad/atticpad/v0.5.0/docs/img/fbi-install-qr.png"
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
updated: '2026-08-17T17:43:11Z'
version: v0.5.0
version_title: AtticPad v0.5.0
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