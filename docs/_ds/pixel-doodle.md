---
author: Thomas Armstrong
avatar: https://avatars.githubusercontent.com/u/12937683?v=4
categories:
- app
color: '#87775c'
color_bg: '#807057'
created: '2026-10-15T04:59:26Z'
description: An offline pixel-art editor and animation tool for DS, DSi and 3DS.
download_filter: PixelDoodle\.(3dsx|cia|nds)$
download_page: https://github.com/ArmstrongThomas/PixelDoodle/releases
downloads:
  PixelDoodle.3dsx:
    size: 913896
    size_str: 892 KiB
    url: https://github.com/ArmstrongThomas/PixelDoodle/releases/download/v0.24.0/PixelDoodle.3dsx
  PixelDoodle.cia:
    size: 730048
    size_str: 712 KiB
    url: https://github.com/ArmstrongThomas/PixelDoodle/releases/download/v0.24.0/PixelDoodle.cia
  PixelDoodle.nds:
    size: 403968
    size_str: 394 KiB
    url: https://github.com/ArmstrongThomas/PixelDoodle/releases/download/v0.24.0/PixelDoodle.nds
github: ArmstrongThomas/PixelDoodle
icon: https://raw.githubusercontent.com/ArmstrongThomas/PixelDoodle/main/assets/icon-3ds.png
image: https://raw.githubusercontent.com/ArmstrongThomas/PixelDoodle/main/assets/pixel-doodle-logo.png
image_length: 1468
layout: app
llm_generation: 'yes'
qr:
  PixelDoodle.cia: https://db.universal-team.net/assets/images/qr/pixeldoodle-cia.png
  PixelDoodle.nds: https://db.universal-team.net/assets/images/qr/pixeldoodle-nds.png
screenshots:
- description: 01 canvas and frame strip
  url: https://db.universal-team.net/assets/images/screenshots/pixel-doodle/01-canvas-and-frame-strip.png
- description: 02 zoomed canvas
  url: https://db.universal-team.net/assets/images/screenshots/pixel-doodle/02-zoomed-canvas.png
- description: 03 timeline and frames
  url: https://db.universal-team.net/assets/images/screenshots/pixel-doodle/03-timeline-and-frames.png
- description: 04 colour picker
  url: https://db.universal-team.net/assets/images/screenshots/pixel-doodle/04-colour-picker.png
- description: 05 tools and brush options
  url: https://db.universal-team.net/assets/images/screenshots/pixel-doodle/05-tools-and-brush-options.png
source: https://github.com/ArmstrongThomas/PixelDoodle
stars: 1
systems:
- 3DS
- DS
title: Pixel Doodle
unique_ids:
- '0xCE678'
update_notes: '<h1 dir="auto">Pixel Doodle 0.24.0</h1>

  <p dir="auto">Pixel Doodle is an offline pixel-art editor for Nintendo DS, DSi and
  3DS.<br>

  This is the first public release, so it includes the complete editor and<br>

  animation toolset.</p>

  <h2 dir="auto">Canvas and drawing</h2>

  <ul dir="auto">

  <li>Canvases from 1 to 128 pixels per side on DS, and up to 512 pixels per side<br>

  on DSi and 3DS. New projects offer 16, 32, 64, 128, 256 and 512 pixel<br>

  presets on DSi and 3DS, plus custom width and height.</li>

  <li>Up to eight layers and up to 256 frames per project. The new-project screen<br>

  shows the layer capacity for the chosen canvas, and the timeline shows the<br>

  frame-memory budget in use.</li>

  <li>Pencil and eraser with 1-16 pixel size, square or round tips, four saved brush<br>

  presets, and a pixel-perfect mode for the one-pixel pencil.</li>

  <li>Pencil, fill and shape dithering at Solid, 25%, 50% or 75% coverage.</li>

  <li>Fill tool with contiguous-region or global colour replacement, active-layer<br>

  or visible-image matching, and 0-255 tolerance.</li>

  <li>Line, rectangle and ellipse tools with outline or filled interiors, shared<br>

  brush size, dithering, live preview and one undo step per shape.</li>

  <li>Colour sampling from the visible artwork.</li>

  <li>Undo and redo with 32 transactions in a 512 KiB history. Paint history is<br>

  frame-aware, so undo follows artwork across frames.</li>

  </ul>

  <h2 dir="auto">Selections and transforms</h2>

  <ul dir="auto">

  <li>Rectangle and freehand lasso selections.</li>

  <li>Replace, add and subtract selection modes.</li>

  <li>Move, cut, copy, paste and delete selected pixels, plus Select All and<br>

  Deselect.</li>

  <li>Flip horizontally, flip vertically and rotate 90 degrees clockwise.</li>

  <li>Duplicate the selection to a new layer.</li>

  <li>Scale the selection 2x, 3x or 4x, or to half size, preserving alpha and<br>

  selection holes.</li>

  </ul>

  <h2 dir="auto">Colour</h2>

  <ul dir="auto">

  <li>RGBA colour with separate foreground and background targets and one-tap swap.</li>

  <li>Square saturation/value picker, vertical hue rail and alpha control.</li>

  <li>RGB, hex and alpha numeric entry.</li>

  <li>Recent colours and a scrollable quick palette.</li>

  <li>Palettes from 1 to 256 colours with an adjustable swatch grid.</li>

  <li>Add, replace, remove and reorder swatches.</li>

  <li>Built-in default palette and a user-saved default palette.</li>

  <li>Import and export GPL, HEX and PNG-strip palettes.</li>

  <li>Project palettes are stored in native projects and Aseprite files.</li>

  </ul>

  <h2 dir="auto">Layers</h2>

  <ul dir="auto">

  <li>Add, delete, duplicate, rename and reorder layers.</li>

  <li>Per-layer visibility, lock, alpha lock and opacity.</li>

  <li>Normal, Multiply, Screen and Overlay blend modes.</li>

  <li>Merge down for normal-blend layers.</li>

  <li>Composite and active-layer previews on the upper screen, including a marker<br>

  when the active layer is hidden.</li>

  </ul>

  <h2 dir="auto">Animation</h2>

  <ul dir="auto">

  <li>Up to 256 frames with per-frame durations from 10 to 60,000 ms.</li>

  <li>Add, duplicate, delete and reorder frames.</li>

  <li>Layers and Timeline tabs with a frame grid, tag band, memory meter and<br>

  frame strip.</li>

  <li>Playback uses each frame''s own duration. It loops the innermost tag containing<br>

  the current frame, or the whole animation when no tag applies.</li>

  <li>Named tags with inclusive frame ranges, six colours and forward, reverse,<br>

  ping-pong or pong-ping playback.</li>

  <li>Linked cels: link a cel with the previous frame, unlink it, or add a new<br>

  linked frame. Editing any member of the group updates the whole group.</li>

  <li>Onion skin with 1-3 previous and next frames, 10-90% opacity and an optional<br>

  red/blue tint.</li>

  <li>Frame sheet with duration presets, fine adjustment, apply-to-one or<br>

  apply-to-all, move left/right, delete and tag editing.</li>

  <li>Timeline moves: hold L and tap frame numbers to mark whole frame columns, then<br>

  hold a marked number and drag the block to a new position. A single frame<br>

  moves the same way without marks. Hold a cel and drag it to another layer,<br>

  frame, or both.</li>

  <li>Canvas frame strip for scrubbing, stepping, play/pause and the onion toggle.</li>

  <li>Upper-screen animation view with the current frame, frame details and a<br>

  filmstrip.</li>

  </ul>

  <h2 dir="auto">Guides</h2>

  <ul dir="auto">

  <li>Pixel grid, shown from 4x zoom upward.</li>

  <li>Independent horizontal and vertical symmetry.</li>

  <li>Independent horizontal and vertical tiling, with repeated wrapped drawing and<br>

  fill support.</li>

  </ul>

  <h2 dir="auto">Files and storage</h2>

  <ul dir="auto">

  <li>Native <code class="notranslate">.pdd</code> projects preserving layers, frames,
  tags, linked cels and<br>

  palettes.</li>

  <li>Open, Save and Save As, with eight recent projects.</li>

  <li>File browser with folders, type filtering, previews, rename, duplicate and<br>

  confirmed deletion.</li>

  <li>Aseprite import and export for <code class="notranslate">.aseprite</code> and
  <code class="notranslate">.ase</code> files, including up to<br>

  256 frames, up to eight flat layers, raw or zlib cels, RGBA pixels, layer<br>

  order/visibility/opacity, Normal/Multiply/Screen/Overlay blending, per-frame<br>

  durations, tags with colours and linked cels.</li>

  <li>PNG artwork import as a single RGBA layer, including RGB, RGBA, grayscale,<br>

  grayscale-alpha and indexed PNGs with transparency.</li>

  <li>PNG export of the visible composite with alpha.</li>

  <li>Recovery snapshots, temporary-file verification and backup copies when<br>

  saving.</li>

  <li>On-screen lowercase, uppercase and symbol keyboard with cursor movement and<br>

  hold-to-delete.</li>

  </ul>

  <h2 dir="auto">Interface and settings</h2>

  <ul dir="auto">

  <li>Dual-screen layout with drawing and controls on the touch screen and<br>

  overview, layer or animation context on the upper screen.</li>

  <li>Tool rail with Pencil, Eraser, Sample, Fill, Select, Line, Rectangle, Ellipse<br>

  and Guides, each with a compact options panel.</li>

  <li>Touch panning, integer zoom from 1x to 32x, button shortcuts and 3DS Circle<br>

  Pad panning.</li>

  <li>Remappable Tools, Pan, Sample and Zoom bindings. L/R, START and SELECT remain<br>

  fixed.</li>

  <li>Adjustable toolbox and zoom-overlay side, drawing timing display, diagnostics<br>

  with memory and card-speed tests, and a built-in controls/help reference.</li>

  <li>Settings, palettes, brush presets and recent files persist between sessions.</li>

  </ul>

  <h2 dir="auto">Install</h2>

  <ul dir="auto">

  <li><strong>3DSX:</strong> copy <code class="notranslate">PixelDoodle.3dsx</code>
  to the SD card and launch it with the<br>

  Homebrew Launcher.</li>

  <li><strong>CIA:</strong> install <code class="notranslate">PixelDoodle.cia</code>
  with FBI or another title installer.</li>

  <li><strong>NDS/DSi:</strong> copy <code class="notranslate">PixelDoodle.nds</code>
  to the flashcart and launch it from the<br>

  loader.</li>

  </ul>

  <h2 dir="auto">Current limits</h2>

  <ul dir="auto">

  <li>DS mode supports canvases up to 128 pixels per side. DSi and 3DS support up<br>

  to 512.</li>

  <li>Up to eight layers and 256 frames, but the largest canvases reduce layer<br>

  capacity and all frames share a fixed memory budget.</li>

  <li>Selection scaling and clipboard transforms are limited to selections up to<br>

  128x128 pixels.</li>

  <li>Undo keeps 32 transactions within a 512 KiB budget.</li>

  </ul>

  <p dir="auto">30bd8aaafe7e0768273b7a497b8f48d6068adf48ee414ede1b22381fac433ea4  PixelDoodle.3dsx<br>

  a7ec6f5b90455ab5452c356c71a0d4bd5bb6d018208ba8b917534503e547abfc  PixelDoodle.cia<br>

  0894780e2f70dc54f827a9763c1d60535a589c6895029654cdba15f776b4e24a  PixelDoodle.nds</p>'
updated: '2026-10-26T23:20:03Z'
version: v0.24.0
version_title: v0.24.0 First public release
---
Pixel Doodle is an offline pixel-art editor and animation tool for the Nintendo DS, DSi and 3DS. It supports canvases up to 512 px, eight layers, 256 frames, tags, linked cels, onion skin, Aseprite import/export, PNG import/export and a full set of drawing, selection, colour and palette tools.