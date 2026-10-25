---
author: cylin577
avatar: https://avatars.githubusercontent.com/u/78150792?v=4
categories:
- app
color: '#191919'
color_bg: '#191919'
created: '2025-08-19T21:40:47Z'
description: A universal 3DS screen capture and control software
download_page: https://github.com/cylin577/3DSC2/releases
downloads:
  uc2_calib.3dsx:
    size: 50368
    size_str: 49 KiB
    url: https://github.com/cylin577/UC2/releases/download/v2.0.0/uc2_calib.3dsx
  uc2_calib.cia:
    size: 290752
    size_str: 283 KiB
    url: https://github.com/cylin577/UC2/releases/download/v2.0.0/uc2_calib.cia
github: cylin577/3DSC2
icon: https://raw.githubusercontent.com/cylin577/3DSC2/main/resources/icon.png
image: https://raw.githubusercontent.com/cylin577/3DSC2/main/resources/banner.png
image_length: 4267
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  uc2_calib.cia: https://db.universal-team.net/assets/images/qr/uc2_calib-cia.png
source: https://github.com/cylin577/UC2
stars: 10
systems:
- 3DS
title: UC2
unique_ids:
- '0x1BF52'
update_notes: '<p><strong>First release under the UC2 name.</strong> The project was
  renamed from 3DSC2 (the GitHub repo is now <code class="notranslate">cylin577/UC2</code>),
  and behind that rename sits a big architectural change: devices are now data, and
  remote control is now pluggable. If you only read one line: <em>your 3DS setup keeps
  working exactly as before, and the app now supports a Nintendo Switch for capture
  and AI.</em></p>

  <hr>

  <h2>Highlights</h2>

  <h3>Nintendo Switch is now a supported device</h3>

  <p>Pick <strong>Nintendo Switch</strong> in the Device dropdown for capture, ROI
  selection, and the AI behavior-cloning model. Per request, <strong>no calibration
  client was built for the Switch</strong> — capture-only. The UI reflects this honestly:
  the IP field, TAS record/replay, controller remapping, and Auto Calibrate are disabled,
  the ROI selector locks after one quad instead of two, and the combined view renders
  a single 1280x720 screen. Control widgets are greyed out because the wire is off,
  not because of cosmetics — a no-control device structurally cannot emit input packets.</p>

  <h3>Devices are now data: <code class="notranslate">device.yaml</code></h3>

  <p>Supported devices live in <code class="notranslate">device.yaml</code> at the
  repo root: device id, friendly name, screen count, and per-screen properties (name,
  width, height, aspect ratio). The app reads this file on startup and derives all
  screen geometry from it. On every startup it fetches the file from GitHub, compares
  the SHA-256 of the remote against your local copy, and — when they differ — downloads
  and replaces it atomically. The replacement applies on the next start. Remote content
  is schema-validated before it is allowed to touch your disk, so a bad upstream push
  can never brick the app, and a bad or hand-broken local file falls back to the bundled
  copy instead of crashing.</p>

  <h3>Remote control is now modular</h3>

  <p>All input transport moved out of the main app into <code class="notranslate">remote_control.py</code>,
  behind a small per-device backend contract: <code class="notranslate">RemoteBackend</code>
  (base), <code class="notranslate">ThreeDSBackend</code> (the original UDP + InputRedirection
  HID path), <code class="notranslate">NullBackend</code> (no-op, used by no-control
  devices), and <code class="notranslate">make_backend(device, state)</code> to pick
  one. Packets on the wire are byte-for-byte identical to before — same UDP target
  and port, same <code class="notranslate">&lt;IIIII</code> layout, same 100 ms press-hold,
  same 20 Hz heartbeat pacing — the seam is just now real instead of hypothetical.
  Switching devices mid-session rebuilds the backend; switching to the Switch mid-calibration
  now routes presses to the no-op backend <em>and</em> trips the existing control
  gate.</p>

  <h3>A guide for building your own device support</h3>

  <p><code class="notranslate">docs/adding-devices.md</code> — the full contributor
  guide: the <code class="notranslate">device.yaml</code> schema reference, the <code
  class="notranslate">devices.py</code> load/validate/update flow, how the app consumes
  a device, how auto-calibration actually works (the AprilTag state machine, marker-to-screen
  quad extrapolation, the stability gate), and how to build your own calibration client
  (devkitARM setup, Makefile targets, the tag rendering contract, what the client
  must and must not do), plus the remote-control backend contract so the guide doubles
  as the spec.</p>

  <hr>

  <h2>Upgrading from 3DSC2</h2>

  <ul>

  <li><strong>Your saved settings migrate automatically.</strong> The settings namespace
  changed with the rename; on first launch the app copies your old 3DSC2 settings
  (IP, camera URL, invert flags, button mappings, touch coordinates) into the new
  one.</li>

  <li><strong>Re-select your IP.</strong> It migrates too — but calibration ROI quads
  are not persisted (unchanged from before), so run Auto Calibrate once.</li>

  <li><strong>Everything else is where you expect it.</strong> Camera sources, remote-cam
  server, ROI selection, TAS record/replay, AI record/predict, and the PyInstaller
  builds all behave as before for 3DS users.</li>

  </ul>

  <hr>

  <h2>Full changelog</h2>

  <h3>Added</h3>

  <ul>

  <li><code class="notranslate">device.yaml</code> device registry at the repo root
  — id, friendly name, screen count, per-screen name/width/height/aspect-ratio — with
  GitHub SHA-256 update check and atomic replace on change</li>

  <li>Nintendo Switch as a supported capture/AI device, with no control path and no
  calibration client (by design)</li>

  <li>Startup device update check: fetches <code class="notranslate">device.yaml</code>
  from GitHub, replaces the local copy when the checksum differs, applies on next
  start; offline failures are silent</li>

  <li><code class="notranslate">remote_control.py</code>: pluggable per-device remote-control
  backends (<code class="notranslate">ThreeDSBackend</code>, <code class="notranslate">NullBackend</code>,
  <code class="notranslate">make_backend</code>) with the UDP/HID transport extracted
  out of the main app</li>

  <li>One-time migration of settings from the old <code class="notranslate">3DSC2</code>
  namespace into <code class="notranslate">UC2</code></li>

  <li><code class="notranslate">docs/adding-devices.md</code> contributor guide (device
  authoring, auto-calibration internals, custom calibration client, backend contract)</li>

  <li>Device picker in the camera panel, with device-aware instruction text and per-device
  screen-count ROI locking</li>

  </ul>

  <h3>Changed</h3>

  <ul>

  <li>Project renamed <strong>3DSC2 → UC2</strong> everywhere: files (<code class="notranslate">uc2.py</code>,
  <code class="notranslate">uc2.spec</code>), the PyInstaller output name, window
  title, the calibration client homebrew (<code class="notranslate">uc2_calib</code>),
  CI artifact names, README, and the GitHub repository (<code class="notranslate">cylin577/3DSC2</code>
  → <code class="notranslate">cylin577/UC2</code>, which redirects)</li>

  <li>Screen geometry (targets, combined-view layout, touch clamping, offset) is now
  derived from <code class="notranslate">device.yaml</code> instead of module constants;
  the 3DS values are unchanged</li>

  <li>Remote-control sends are gated structurally: no-control devices cannot emit
  packets; calibration presses route through the active backend</li>

  <li><code class="notranslate">remote_build.sh</code> is now tracked in the repo
  so contributors can follow the remote-build instructions</li>

  <li>Version bumped to 2.0.0 for the rename</li>

  </ul>

  <h3>Fixed</h3>

  <ul>

  <li>Selecting a no-control device left the heartbeat thread firing 3DS packets at
  whatever IP was in settings — now impossible by construction</li>

  <li>Starting calibration on a 3DS and then switching to the Switch kept sending
  HID presses; calibration now bails out on a no-control device</li>

  <li>TAS playback state now resets when switching to a no-control device, instead
  of freezing with a stale button label</li>

  <li>A corrupt or invalid <code class="notranslate">device.yaml</code> (local or
  remote) can no longer break app startup; remote data is validated before it is written</li>

  <li>Switching devices before starting the camera no longer pops up orphaned view
  windows</li>

  </ul>

  <hr>

  <h2>Downloads</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Platform</th>

  <th>File</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td>Linux x64</td>

  <td><code class="notranslate">UC2-linux-x64</code></td>

  </tr>

  <tr>

  <td>Windows x64</td>

  <td><code class="notranslate">UC2-windows-x64.exe</code></td>

  </tr>

  <tr>

  <td>Linux aarch64</td>

  <td><code class="notranslate">UC2-linux-aarch64</code></td>

  </tr>

  <tr>

  <td>3DS homebrew (.3dsx)</td>

  <td><code class="notranslate">UC2-calibration-client.3dsx</code></td>

  </tr>

  <tr>

  <td>3DS installable (.cia)</td>

  <td><code class="notranslate">UC2-calibration-client.cia</code></td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p>Built automatically by CI when this release was published. The packaged desktop
  builds ship with <code class="notranslate">device.yaml</code> bundled, so the app
  runs even with no network; the GitHub update check refreshes it when you are online.</p>

  <h2>Verifying</h2>

  <p>CI does not generate checksums for the attached assets. Verify the download yourself,
  e.g. <code class="notranslate">shasum -a 256 UC2-linux-x64</code> and compare against
  a build you produce from the tagged source.</p>

  <h2>For contributors</h2>

  <p>Start with <strong><code class="notranslate">docs/adding-devices.md</code></strong>.
  To add a device you only touch two files: one entry in <code class="notranslate">device.yaml</code>,
  and — if the device has a control path — one small backend in <code class="notranslate">remote_control.py</code>.
  If your device needs a physical marker target for camera calibration, that is a
  separate homebrew per console; the doc walks through the existing 3DS client as
  the reference implementation.</p>'
updated: '2026-10-25T15:20:10Z'
version: v2.0.0
version_title: UC2 v2.0.0 — first release under the UC2 name
---
The calibration app for 3DSC2