---
author: PainDe0Mie
avatar: https://avatars.githubusercontent.com/u/97704518?v=4
categories:
- utility
color: '#5f6983'
color_bg: '#5c6680'
created: '2026-04-18T02:45:15Z'
description: Gamestream client for old 2ds/3DS
download_page: https://github.com/PainDe0Mie/PotatoStream/releases
downloads:
  streampotato.3dsx:
    size: 7710000
    size_str: 7 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.3.5/streampotato.3dsx
  streampotato.cia:
    size: 4415936
    size_str: 4 MiB
    url: https://github.com/PainDe0Mie/PotatoStream/releases/download/v1.3.5/streampotato.cia
github: PainDe0Mie/PotatoStream
icon: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/ic_streampotato.png
image: https://raw.githubusercontent.com/PainDe0Mie/PotatoStream/n3ds-main/3ds/res/banner.png
image_length: 11016
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_generation: unknown
qr:
  streampotato.cia: https://db.universal-team.net/assets/images/qr/streampotato-cia.png
source: https://github.com/PainDe0Mie/PotatoStream
stars: 19
systems:
- 3DS
title: PotatoStream
unique_ids:
- '0x3700'
update_notes: '<h2 dir="auto">What''s New in v1.3.5</h2>

  <p dir="auto"><strong>Performance at a glance (Old 2DS)</strong></p>

  <ul dir="auto">

  <li>Video decoding is 1.4x faster: ~25 ms → 18 ms per frame on a high-motion 400x240
  stream, and up to ~2x with "Experimental video on 2nd core"</li>

  <li>Audio no longer uses the main CPU core (it took a third of it at 20 fps)</li>

  <li>20 fps now holds with 20-40 ms of delay, instead of 100 ms rising past 200 ms</li>

  </ul>

  <p dir="auto"><strong>Stability</strong></p>

  <ul dir="auto">

  <li>Fixed random freezes when starting or exiting a stream, caused by a missing
  header in the 3DS network code of ENet (inherited from upstream Moonlight)</li>

  <li>Fixed the text console writing into freed screen memory after the menu, which
  garbled the bottom screen and could hang the GPU</li>

  <li>The wait screen now shows each connection step (<code class="notranslate">RTSP
  handshake</code>, <code class="notranslate">control stream establishment</code>...)
  and the error code when a step fails (logs)</li>

  </ul>

  <p dir="auto"><strong>Performance (Old 3DS/2DS)</strong></p>

  <ul dir="auto">

  <li>Hand-written ARMv6 assembly for H.264 (IDCT, chroma motion compensation, block
  copy). FFmpeg only ships NEON versions, which the Old 3DS can''t run. This is the
  biggest decoding gain: -22% measured on an Old 2DS</li>

  <li>Rebuilt FFmpeg with ARMv5TE/ARMv6/VFP assembly instead of plain C</li>

  <li>Ported FFmpeg''s CABAC assembly to the 3DS CPU (helps streams that use CABAC,
  e.g. NVENC/AMF)</li>

  <li>New setting: "Experimental video on 2nd core" splits each frame between both
  CPU cores (about 30% faster decoding in tests, off by default)</li>

  <li>Rebuilt the Opus audio codec in fixed point with ARMv6 assembly. The previous
  floating-point build used about a third of the main CPU core</li>

  <li>Audio is now decoded on the 2nd CPU core: at 20 fps on an Old 2DS, latency drops
  to 20-40 ms instead of 100-200 ms and rising</li>

  <li>Audio packets are now 20 ms long with Sunshine, so there are half as many to
  receive</li>

  <li>Moved image conversion and display (Y2R, GPU, screen swap) to their own thread,
  so decoding no longer waits for the hardware</li>

  <li>Network polling now sleeps 1 ms between checks instead of 1 µs, wasting less
  CPU</li>

  <li>Raised the Old 3DS packet size from 896-1024 to 1392 bytes, about 26% fewer
  packets to receive</li>

  <li>Stream sizes are now aligned for the decoder: 320x192 instead of 320x180, 400x240,
  640x192 in Stereo</li>

  </ul>

  <p dir="auto"><strong>Settings &amp; Controls</strong></p>

  <ul dir="auto">

  <li>New "Stream profile" setting replaces the three experimental toggles: Default
  (320x192, 20 fps), Better screen (400x240, 15 fps), <strong>Smooth 30 fps</strong>
  (320x192, 30 fps, experimental), Stable (15 fps), Ultra potato (12 fps)</li>

  <li>New touch gamepad: ZL, L3, HOME, R3 and ZR buttons, and the rest of the bottom
  screen works as a right stick for the camera (double-tap and hold for R3)</li>

  <li>New settings: "Camera stick" (touch stick, touch swipe, or either one + gyro),
  "Camera sensitivity" and "Invert camera" (Right Stick)</li>

  <li>New setting: "Bottom screen auto-off" turns the bottom screen light off after
  10s without touch in Gamepad and Mouse modes, to save battery</li>

  <li><strong>Wake-on-LAN</strong>: after one connection, PotatoStream remembers your
  PC and offers "Wake PC" when it is off or asleep</li>

  <li>"Network on 2nd core" is no longer offered on Old 3DS/2DS: it was measured slower
  there</li>

  <li>Debug mode shows more stats (fps, decode time, queue wait, lag and audio CPU
  share)</li>

  <li>Decode benchmark: Settings → Record next stream, then Settings → Decode benchmark.
  Results are saved to <code class="notranslate">bench.txt</code></li>

  <li>The host list shows the real app version</li>

  </ul>

  <p dir="auto"><strong>Video &amp; Rendering</strong></p>

  <ul dir="auto">

  <li>Fixed colors with the software decoders: the 3DS now converts with the same
  <code class="notranslate">BT.601</code> coefficients the host encodes with (it used
  <code class="notranslate">BT.709</code>)</li>

  <li>Enabled Y2R spatial dithering for less banding in gradients (sky, dark areas)</li>

  <li>Fixed Magnify mode showing stripes and a stretched image in 800x480 (bottom
  screen texture too narrow)</li>

  </ul>

  <p dir="auto"><strong>New 3DS/2DS</strong></p>

  <ul dir="auto">

  <li>"Network on 2nd core": video reception runs on core 2 while the hardware decoder
  works (on by default)</li>

  <li>Lag recovery: when frames wait more than 150 ms to be decoded, the stream skips
  to the next keyframe instead of drifting behind</li>

  <li>Added an "Experimental 24-bit color" option for the hardware decoder</li>

  </ul>

  <p dir="auto"><strong>Build</strong></p>

  <ul dir="auto">

  <li>Added <code class="notranslate">3ds/build-opus.sh</code> (fixed-point Opus 1.4,
  installed in <code class="notranslate">extra_lib</code>)</li>

  <li><code class="notranslate">3ds/build-ffmpeg.sh</code> builds with ARMv6 assembly
  (H.264 and CABAC patches applied automatically) and no longer needs x264 or dav1d</li>

  <li>Submodule fixes (ENet freeze, network polling, 2nd core threads, 20 ms audio)</li>

  <li>Implicit function declarations are now build errors (that is how the freeze
  bug slipped through)</li>

  <li>App version set to <code class="notranslate">1.3.5</code>. It was <code class="notranslate">3.0.0</code>,
  inherited from <em>moonlight-N3DS</em>, so the update check never found newer releases</li>

  </ul>'
updated: '2026-11-05T03:04:24Z'
version: v1.3.5
version_title: PotatoStream v1.3.5
---
PotatoStream is a Moonlight game streaming client for all 3DS and 2DS models, with a focus on Old 3DS/2DS compatibility. Auto-detects hardware at startup and activates "Potato" mode on older models with smart frame skipping, Y2RU hardware pipeline and an optimized stream profile (400x240@24fps). (New 3DS keeps the standard MVD hardware decoder) Compatible with Sunshine and NVIDIA GameStream.