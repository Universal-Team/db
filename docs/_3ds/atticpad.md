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
prerelease:
  download_page: https://github.com/atticpad/atticpad/releases/tag/v0.6.0-rc2
  downloads:
    atticpad-3ds.3dsx:
      size: 366704
      size_str: 358 KiB
      url: https://github.com/atticpad/atticpad/releases/download/v0.6.0-rc2/atticpad-3ds.3dsx
    atticpad-3ds.cia:
      size: 420800
      size_str: 410 KiB
      url: https://github.com/atticpad/atticpad/releases/download/v0.6.0-rc2/atticpad-3ds.cia
  qr:
    atticpad-3ds.cia: https://db.universal-team.net/assets/images/qr/prerelease/atticpad-3ds-cia.png
  update_notes: '<h3 dir="auto">Added</h3>

    <ul dir="auto">

    <li>

    <p dir="auto"><strong>Keyboard, mouse and media remote control</strong>, on top
    of the gamepad. Four<br>

    new additive message types — <code class="notranslate">KEYBOARD</code> 0x21, <code
    class="notranslate">MOUSE</code> 0x22, <code class="notranslate">MEDIA</code>
    0x23,<br>

    <code class="notranslate">INPUTCAPS</code> 0x44 — allocated after the v1 freeze
    under the rule<br>

    <code class="notranslate">docs/PROTOCOL.md</code> §6.14 states and audits them
    against: nothing that<br>

    existed before changed size, position or meaning, and <code class="notranslate">caps</code>
    (§6.3) is<br>

    untouched on purpose. A server advertises which of the three it accepts via<br>

    <code class="notranslate">INPUTCAPS</code>; a client shows nothing until it hears
    that, and an old client<br>

    or an old server simply never speaks the new types at all. See<br>

    <a href="docs/KBM.md"><code class="notranslate">docs/KBM.md</code></a> for the
    full picture, including the Windows<br>

    <code class="notranslate">SendInput</code> limitations and the 10 of 24 §6.18
    media controls that backend<br>

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

    <a href="https://github.com/nefarius/ViGEmBus/releases">its releases page</a>.
    SmartScreen<br>

    will warn about AtticPad''s unsigned binary (<em>More info → Run anyway</em>).</p>

    </li>

    <li>

    <p dir="auto"><strong>Linux:</strong> download <code class="notranslate">atticpad-server-linux-x86_64</code>,
    <code class="notranslate">chmod +x</code> it, and run it.<br>

    It needs access to <code class="notranslate">/dev/uinput</code> — <a href="https://github.com/atticpad/atticpad/blob/v0.6.0-rc2/docs/INSTALL.md">INSTALL.md</a>
    has the<br>

    one-line udev rule.</p>

    </li>

    </ul>

    <p dir="auto">The server prints the address to type into a client, and serves
    a local page on<br>

    <a href="http://127.0.0.1:21150/" rel="nofollow">http://127.0.0.1:21150/</a> for
    pad status, round-trip latency and profile editing.</p>

    <p dir="auto"><strong>Client</strong> — on the device you want to hold:</p>

    <ul dir="auto">

    <li>

    <p dir="auto"><strong>Nintendo 3DS</strong> (needs Luma3DS custom firmware) —
    open <strong>FBI → Remote Install<br>

    → Scan QR Code</strong> and scan this. No SD card, no cable:</p>

    <a target="_blank" rel="noopener noreferrer nofollow" href="https://raw.githubusercontent.com/atticpad/atticpad/v0.6.0-rc2/docs/img/fbi-install-qr.png"><img
    src="https://raw.githubusercontent.com/atticpad/atticpad/v0.6.0-rc2/docs/img/fbi-install-qr.png"
    alt="QR code that installs the AtticPad .cia from the latest release" width="200"
    style="max-width: 100%;"></a>

    <p dir="auto">If that image does not load, the same code is attached to this release
    as<br>

    <code class="notranslate">atticpad-3ds-install-qr.png</code>, and FBI''s <em>Receive
    URLs over the network</em> will<br>

    take the URL it encodes directly:<br>

    <code class="notranslate">https://github.com/atticpad/atticpad/releases/latest/download/atticpad-3ds.cia</code></p>

    <p dir="auto">Or copy <code class="notranslate">atticpad-3ds.cia</code> to the
    SD card and install it with FBI from there.<br>

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

    memory stick and launch <strong>AtticPad</strong> from the XMB. Set up a saved
    Wi-Fi<br>

    connection first; the PSP speaks WEP and WPA over 802.11b, so a WPA2-only<br>

    router will refuse it.</p>

    </li>

    <li>

    <p dir="auto"><strong>Nintendo DS / DSi</strong> (flashcart or homebrew launcher)
    — copy<br>

    <code class="notranslate">atticpad-nds.nds</code> to the card and launch it. In
    DS mode the console can only<br>

    join an open or WEP network; <a href="https://github.com/atticpad/atticpad/blob/v0.6.0-rc2/docs/SETUP-DS.md">SETUP-DS.md</a>
    shows how to<br>

    run a small isolated one. In DSi mode it joins WPA2 and pairs by scanning<br>

    the QR with the camera.</p>

    </li>

    </ul>

    <p dir="auto">Then pair once. On the 3DS that means scanning the QR code the server
    shows —<br>

    the console has no PIN keypad, so the QR is the only way in. On Android you can<br>

    scan it or type the 6-digit PIN.</p>

    <p dir="auto"><strong>Before you use it on a network you do not control, read
    the security section<br>

    of the README.</strong> By default the server accepts any device on your LAN with
    no<br>

    PIN.</p>

    <p dir="auto">Verify what you downloaded:</p>

    <pre class="notranslate"><code class="notranslate">sha256sum -c SHA256SUMS

    </code></pre>

    <hr>

    <p dir="auto"><strong>This is a release candidate for 0.6.0, not a final release.</strong>
    Please report anything that behaves differently from the notes above.</p>'
  update_notes_md: "\n### Added\n\n- **Keyboard, mouse and media remote control**,\
    \ on top of the gamepad. Four\n  new additive message types — `KEYBOARD` 0x21,\
    \ `MOUSE` 0x22, `MEDIA` 0x23,\n  `INPUTCAPS` 0x44 — allocated after the v1 freeze\
    \ under the rule\n  `docs/PROTOCOL.md` §6.14 states and audits them against: nothing\
    \ that\n  existed before changed size, position or meaning, and `caps` (§6.3)\
    \ is\n  untouched on purpose. A server advertises which of the three it accepts\
    \ via\n  `INPUTCAPS`; a client shows nothing until it hears that, and an old client\n\
    \  or an old server simply never speaks the new types at all. See\n  [`docs/KBM.md`](docs/KBM.md)\
    \ for the full picture, including the Windows\n  `SendInput` limitations and the\
    \ 10 of 24 §6.18 media controls that backend\n  cannot drive.\n  - **Android**\
    \ — a mode bar (PAD/MOUSE/KEYBOARD/MEDIA): a trackpad view, a\n    real physical-style\
    \ key grid with genuine multi-finger chord support, a\n    curated text-entry\
    \ bar, and a media remote.\n  - **3DS** — the same four modes on the bottom screen,\
    \ adapted to a\n    resistive, single-contact touchscreen: a sticky SHIFT/CTRL\
    \ latch for\n    KEYS mode, plus physical L/R as always-live modifiers on top\
    \ of it.\n  - **Linux server** — three `uinput` nodes per session, created lazily\
    \ on\n    first use and torn down in spec order (release held state, then destroy\n\
    \    the device) before a session closes.\n  - **Windows server** — a `SendInput`-based\
    \ backend. Built and compiled in\n    CI on every push; **never run on real Windows\
    \ hardware as of this\n    writing** — see `docs/KBM.md` for the specific, permanent\
    \ limitations\n    (UIPI elevation, the secure desktop, anti-cheat rejection,\
    \ pointer\n    ballistics, and one shared system keyboard/mouse across sessions)\
    \ and\n    `docs/QA.md` §11 for the hardware checklist this still needs.\n  -\
    \ `docs/PROTOCOL.md` §6.22 reserves message type `0x24` for a future\n    `TEXT`\
    \ type, because today's `KEYBOARD` carries HID usage IDs (physical\n    key positions)\
    \ and text entry therefore assumes a US-QWERTY host layout\n    — see `docs/KBM.md`.\n\
    \n- **PlayStation Portable client** (`EBOOT.PBP`, in `atticpad-psp.zip`).\n  Analog\
    \ nub, every button, an on-screen keypad for the address and the\n  PIN, PIN pairing,\
    \ the server and network remembered, and the self-test.\n  Hardware-proven — see\
    \ `docs/SUPPORT-TIERS.md` and `docs/INSTALL.md`.\n- **Nintendo DS / DSi client**\
    \ (`atticpad-nds.nds`). The 3DS screens on a\n  DS: a network picker with WEP\
    \ keys typed on the touch keyboard, typed\n  address and PIN, the four PAD / MOUSE\
    \ / KEYS / MEDIA modes, the\n  self-test, and the last server and network remembered.\
    \ In DSi mode it\n  joins WPA2, reports the battery, and pairs by scanning the\
    \ server's QR\n  with the camera. The server ships a `ds-default` profile that\
    \ drives the\n  left stick from the touchscreen. Hardware-proven in both modes\
    \ — see\n  `docs/SUPPORT-TIERS.md`, `docs/INSTALL.md` and `docs/SETUP-DS.md` for\n\
    \  the open-or-WEP constraint of DS mode.\n\n### Changed\n\n- **Discovery on the\
    \ 3DS and DS prefers the server you last used.** When\n  more than one server\
    \ answers a LAN DISCOVER, the console now picks the one\n  whose address it saved\
    \ after its last session (or picked last time) rather\n  than whichever answered\
    \ first; the first responder only wins when the\n  remembered one stays silent\
    \ for the whole window. On a LAN with two\n  servers the faster machine used to\
    \ win every boot and look hardcoded.\n  Nothing is hardcoded: a fresh unit still\
    \ starts empty. The Android\n  address field's placeholder no longer looks like\
    \ a real address.\n\n\n---\n\n## Install\n\n**Server** — on the PC that needs\
    \ a controller. Pick one:\n\n- **Windows:** download `atticpad-server-windows-x86_64.exe`\
    \ and run it. It needs\n  the ViGEmBus driver, which is easiest to install with\
    \ winget:\n\n  ```\n  winget install ViGEm.ViGEmBus\n  ```\n\n  or grab the installer\
    \ from\n  [its releases page](https://github.com/nefarius/ViGEmBus/releases).\
    \ SmartScreen\n  will warn about AtticPad's unsigned binary (*More info → Run\
    \ anyway*).\n- **Linux:** download `atticpad-server-linux-x86_64`, `chmod +x`\
    \ it, and run it.\n  It needs access to `/dev/uinput` — [INSTALL.md](https://github.com/atticpad/atticpad/blob/v0.6.0-rc2/docs/INSTALL.md)\
    \ has the\n  one-line udev rule.\n\nThe server prints the address to type into\
    \ a client, and serves a local page on\n<http://127.0.0.1:21150/> for pad status,\
    \ round-trip latency and profile editing.\n\n**Client** — on the device you want\
    \ to hold:\n\n- **Nintendo 3DS** (needs Luma3DS custom firmware) — open **FBI\
    \ → Remote Install\n  → Scan QR Code** and scan this. No SD card, no cable:\n\n\
    \  <img src=\"https://raw.githubusercontent.com/atticpad/atticpad/v0.6.0-rc2/docs/img/fbi-install-qr.png\"\
    \ alt=\"QR code that installs the AtticPad .cia from the latest release\" width=\"\
    200\">\n\n  If that image does not load, the same code is attached to this release\
    \ as\n  `atticpad-3ds-install-qr.png`, and FBI's *Receive URLs over the network*\
    \ will\n  take the URL it encodes directly:\n  `https://github.com/atticpad/atticpad/releases/latest/download/atticpad-3ds.cia`\n\
    \n  Or copy `atticpad-3ds.cia` to the SD card and install it with FBI from there.\n\
    \  `atticpad-3ds.3dsx` runs from the Homebrew Launcher instead, without installing.\n\
    - **Android 8.0+** — sideload `atticpad-android.apk`. If you already have a debug\n\
    \  build installed, uninstall it first: the signatures differ.\n- **PSP** (custom\
    \ firmware) — unzip `atticpad-psp.zip` onto the root of the\n  memory stick and\
    \ launch **AtticPad** from the XMB. Set up a saved Wi-Fi\n  connection first;\
    \ the PSP speaks WEP and WPA over 802.11b, so a WPA2-only\n  router will refuse\
    \ it.\n- **Nintendo DS / DSi** (flashcart or homebrew launcher) — copy\n  `atticpad-nds.nds`\
    \ to the card and launch it. In DS mode the console can only\n  join an open or\
    \ WEP network; [SETUP-DS.md](https://github.com/atticpad/atticpad/blob/v0.6.0-rc2/docs/SETUP-DS.md)\
    \ shows how to\n  run a small isolated one. In DSi mode it joins WPA2 and pairs\
    \ by scanning\n  the QR with the camera.\n\nThen pair once. On the 3DS that means\
    \ scanning the QR code the server shows —\nthe console has no PIN keypad, so the\
    \ QR is the only way in. On Android you can\nscan it or type the 6-digit PIN.\n\
    \n**Before you use it on a network you do not control, read the security section\n\
    of the README.** By default the server accepts any device on your LAN with no\n\
    PIN.\n\nVerify what you downloaded:\n\n```\nsha256sum -c SHA256SUMS\n```\n\n---\n\
    \n**This is a release candidate for 0.6.0, not a final release.** Please report\
    \ anything that behaves differently from the notes above.\n"
  updated: '2026-09-12T11:22:21Z'
  version: v0.6.0-rc2
  version_title: AtticPad v0.6.0-rc2
qr:
  atticpad-3ds.cia: https://db.universal-team.net/assets/images/qr/atticpad-3ds-cia.png
source: https://github.com/atticpad/atticpad
stars: 4
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