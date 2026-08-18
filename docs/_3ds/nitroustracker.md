---
author: NitrousTracker contributors - original by Tobias Weyand
avatar: https://codeberg.org/avatars/dfbeab2ccbd74b48c2eded683b6fc5fe8c64ad01d4a41725cc263d2522c26b4e
categories:
- app
color: '#876f18'
color_bg: '#806917'
created: '2026-07-24T13:42:31Z'
description: Unofficial fork of 0xtob's NitroTracker, a Fasttracker II-style tracker
  for the DS.
download_filter: -(n3ds|nds)\.zip
download_page: https://codeberg.org/NitrousTracker/NitrousTracker/releases
downloads:
  NitrousTracker-0.6.6-nds.zip:
    size: 2497359
    size_str: 2 MiB
    url: https://codeberg.org/NitrousTracker/nitroustracker/releases/download/release%2F0.6.6/NitrousTracker-0.6.6-nds.zip
forgejo: NitrousTracker/NitrousTracker
forgejo_host: codeberg.org
icon: https://codeberg.org/NitrousTracker/nitroustracker/raw/branch/develop/assets/icon48.png
image: https://codeberg.org/NitrousTracker/nitroustracker/raw/branch/develop/assets/icon48.png
image_length: 1291
layout: app
llm_generation: unknown
prerelease:
  download_page: https://codeberg.org/NitrousTracker/nitroustracker/releases/tag/release/0.7.0b3
  downloads:
    NitrousTracker-0.7.0b3-n3ds.zip:
      size: 1891646
      size_str: 1 MiB
      url: https://codeberg.org/NitrousTracker/nitroustracker/releases/download/release%2F0.7.0b3/NitrousTracker-0.7.0b3-n3ds.zip
    NitrousTracker-0.7.0b3-nds.zip:
      size: 2556205
      size_str: 2 MiB
      url: https://codeberg.org/NitrousTracker/nitroustracker/releases/download/release%2F0.7.0b3/NitrousTracker-0.7.0b3-nds.zip
  update_notes: '<p><strong>This is a beta release!</strong> Report any issues found
    via the Codeberg repository.</p>

    <p>New features:</p>

    <ul>

    <li>native 3DS port!

    <ul>

    <li>pros: bigger screens, more channels supported (16 -&gt; 32), more sample RAM</li>

    <li>cons: slightly higher audio latency</li>

    </ul>

    </li>

    <li>playback engine migrated to a port of the FastTracker 2 play routine!

    <ul>

    <li>much better playback accuracy and near-complete effect support</li>

    <li>note: this may require tweaks to old songs which depended on NitroTracker
    play routine quirks. some

    quirks are adjusted for on load - resaving such songs should make them play more
    accurately in

    FT2-compatible players as well.</li>

    </ul>

    </li>

    <li>added support for inputting most effects</li>

    <li>[#35] added support for loading and saving instruments (.xi files)</li>

    <li>added support for configuring instrument panning envelopes</li>

    <li>added support for configuring instrument envelope loops</li>

    <li>[#106] added support for configuring instrument vibrato</li>

    <li>added support for editing note components with buttons only - use A / A +
    D-Pad</li>

    <li>[#273] added support for previewing samples while the song is playing</li>

    <li>[#65] added support for importing .mod files</li>

    <li>3DS: open the NitrousTracker manual directly from the program</li>

    <li>NDS: updated BlocksDS to 1.22.2</li>

    </ul>

    <p>Improvements:</p>

    <ul>

    <li>24/32-bit wav samples now load faster</li>

    <li>browsing themes no longer pauses playback</li>

    <li>fx keyboard now supports pen sliding (prayerie)</li>

    <li>greatly improved bpm/timing accuracy</li>

    <li>[#230] loop points are now retained when disabling and re-enabling sample
    loop</li>

    <li>NDS: debug build now shows wifi debug messages</li>

    <li>numerous minor ui/ux tweaks (prayerie)</li>

    <li>sample snapping to zero crossing now respects zoom level</li>

    <li>themes are now bundled within the .nds/.3dsx file</li>

    </ul>

    <p>Fixes:</p>

    <ul>

    <li>[#152] fixed inconsistent sample preview looping behaviour</li>

    <li>[#148] fixed sustain envelope not working in certain situations</li>

    <li>fixed DSi mode frequency setting not being applied on load</li>

    <li>fixed default sample/instrument filenames containing prohibited characters</li>

    <li>fixed file corruption when out of memory and trying to save .xm files with
    8-bit samples</li>

    </ul>

    '
  update_notes_md: "**This is a beta release!** Report any issues found via the Codeberg\
    \ repository.\n\nNew features:\n\n- native 3DS port!\n  - pros: bigger screens,\
    \ more channels supported (16 -> 32), more sample RAM\n  - cons: slightly higher\
    \ audio latency\n- playback engine migrated to a port of the FastTracker 2 play\
    \ routine!\n  - much better playback accuracy and near-complete effect support\n\
    \  - note: this may require tweaks to old songs which depended on NitroTracker\
    \ play routine quirks. some\n    quirks are adjusted for on load - resaving such\
    \ songs should make them play more accurately in\n    FT2-compatible players as\
    \ well.\n- added support for inputting most effects\n- [#35] added support for\
    \ loading and saving instruments (.xi files)\n- added support for configuring\
    \ instrument panning envelopes\n- added support for configuring instrument envelope\
    \ loops\n- [#106] added support for configuring instrument vibrato\n- added support\
    \ for editing note components with buttons only - use A / A + D-Pad\n- [#273]\
    \ added support for previewing samples while the song is playing\n- [#65] added\
    \ support for importing .mod files\n- 3DS: open the NitrousTracker manual directly\
    \ from the program\n- NDS: updated BlocksDS to 1.22.2\n\nImprovements:\n\n- 24/32-bit\
    \ wav samples now load faster\n- browsing themes no longer pauses playback\n-\
    \ fx keyboard now supports pen sliding (prayerie)\n- greatly improved bpm/timing\
    \ accuracy\n- [#230] loop points are now retained when disabling and re-enabling\
    \ sample loop\n- NDS: debug build now shows wifi debug messages\n- numerous minor\
    \ ui/ux tweaks (prayerie)\n- sample snapping to zero crossing now respects zoom\
    \ level\n- themes are now bundled within the .nds/.3dsx file\n\nFixes:\n\n- [#152]\
    \ fixed inconsistent sample preview looping behaviour\n- [#148] fixed sustain\
    \ envelope not working in certain situations\n- fixed DSi mode frequency setting\
    \ not being applied on load\n- fixed default sample/instrument filenames containing\
    \ prohibited characters\n- fixed file corruption when out of memory and trying\
    \ to save .xm files with 8-bit samples"
  updated: '2026-08-08T12:51:07Z'
  version: release/0.7.0b3
  version_title: NitrousTracker v0.7.0 beta 3
source: https://codeberg.org/NitrousTracker/nitroustracker
stars: 8
systems:
- DS
- 3DS
title: NitrousTracker
update_notes: '<p>Fixes:</p>

  <ul>

  <li>fix rare .xm corruption edge case when free memory is very low</li>

  <li>fix rare potential record box crash on really short recordings</li>

  </ul>

  '
updated: '2026-08-08T12:50:08Z'
version: release/0.6.6
version_title: NitrousTracker v0.6.6
website: http://docs.asie.pl/nitroustracker/
---
NitrousTracker is a fork of NitroTracker, a FastTracker II style tracker for the Nintendo DS originally created by 0xtob.

A tracker is a type of music sequencer built around patterns which contain arrangements of notes and effects. NitrousTracker is built around the popular XM file format that is supported by many PC trackers.

With NitrousTracker, you can carry your XMs around in your DS and compose whenever and wherever you feel like it. You might be thinking something along the lines of “Tracking on a handheld console? Sounds like a pain”. However, thanks to the stylus-operated touch display of the DS, it’s quite easy. You can compose your melodies using an on-screen keyboard, directly edit your patterns by making selections, copying and pasting - all using the stylus. And that’s not where it ends: If you don’t have any samples on hand, make your own with the DS’s microphone. You can even replace the samples in existing songs with your own recorded ones! There are many possibilities already and there will be even more.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>nitroustracker.nds</summary>
<ol>
<li>Download <code>NitrousTracker-0.6.6-nds.zip</code></li>
<li>Extract <code>/nitroustracker.nds</code> from the zip to where you keep NDS files on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>nitroustracker.midi.nds</summary>
<ol>
<li>Download <code>NitrousTracker-0.6.6-nds.zip</code></li>
<li>Extract <code>/nitroustracker.midi.nds</code> from the zip to where you keep NDS files on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[prerelease] nitroustracker.3dsx</summary>
<ol>
<li>Download <code>NitrousTracker-0.7.0b3-n3ds.zip</code></li>
<li>Extract <code>/nitroustracker.3dsx</code> from the zip to <code>/3ds/nitroustracker.3dsx</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[prerelease] nitroustracker.nds</summary>
<ol>
<li>Download <code>NitrousTracker-0.7.0b3-nds.zip</code></li>
<li>Extract <code>/nitroustracker.nds</code> from the zip to where you keep NDS files on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>[prerelease] nitroustracker.midi.nds</summary>
<ol>
<li>Download <code>NitrousTracker-0.7.0b3-nds.zip</code></li>
<li>Extract <code>/nitroustracker.midi.nds</code> from the zip to where you keep NDS files on your SD card</li>
</ol>
</details>

