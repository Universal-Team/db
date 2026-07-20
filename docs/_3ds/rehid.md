---
author: Kartik
autogen_scripts: true
avatar: https://avatars.githubusercontent.com/u/16360444?v=4
categories:
- utility
color: '#411c38'
color_bg: '#411c38'
created: '2020-11-07T12:39:47Z'
description: HID module rewrite(button remapping and more)
download_filter: cia
download_page: https://github.com/hax0kartik/rehid/releases
downloads:
  rehidhelper.cia:
    size: 803776
    size_str: 784 KiB
    url: https://github.com/hax0kartik/rehid/releases/download/v5.0/rehidhelper.cia
github: hax0kartik/rehid
image: https://avatars.githubusercontent.com/u/16360444?v=4&size=128
image_length: 21350
layout: app
llm_generation: unknown
qr:
  rehidhelper.cia: https://db.universal-team.net/assets/images/qr/rehidhelper-cia.png
screenshots:
- description: Helper
  url: https://db.universal-team.net/assets/images/screenshots/rehid/helper.png
source: https://github.com/hax0kartik/rehid
stars: 148
systems:
- 3DS
title: rehid
unique_ids:
- '0xDF10'
update_notes: '<p dir="auto">This is the sixth public release of rehid.</p>

  <p dir="auto"><strong>E: A hotfix has been made which fixes Zl/ZR behaviour on n3ds.
  Please update!</strong></p>

  <p dir="auto">The following changes have been made:</p>

  <ul dir="auto">

  <li>Fix a bug due to which ZL/ZR wouldn''t respond after sleep.</li>

  <li>Fix a bug in turbofire due to which remapping weren''t applied correctly.</li>

  <li>Fix bugs in title selection screen due to which mappings were generated for
  the wrong tid. (Sorry!)</li>

  <li>Other minor improvements.</li>

  </ul>

  <p dir="auto">One of the major features that have been worked for this release is
  <strong>Circle Pad Pro support on O3DS</strong>. <strong>This means you can now
  enjoy your Circle Pad Pro even with games which do not support it!</strong> However,
  this is <strong>highly experimental</strong>, and as such not included with the
  main release. <strong>Bugs and Crashes are to be expected</strong> and should be
  reported here on github or on my discord server: <a href="https://discord.gg/hyuvmb9"
  rel="nofollow">https://discord.gg/hyuvmb9</a>.</p>

  <p dir="auto">Folks interested in this feature can download <code class="notranslate">0004013000001D02_experimental.cxi</code>,
  rename it to <code class="notranslate">0004013000001D02.cxi</code>, and put it in
  <code class="notranslate">/luma/sysmodules</code> folder. Don''t forget to enable
  <code class="notranslate">Load external firms and modules</code> from luma config
  menu!</p>

  <p dir="auto">I would like to thank <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/rosaage/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/rosaage">@rosaage</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/EthanMac1915/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/EthanMac1915">@EthanMac1915</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Mayonaka-7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Mayonaka-7">@Mayonaka-7</a>
  and @tittilvero who have spent countless hours helping me test the cpp feature.</p>

  <p dir="auto"><strong>For newcomers, please download and install rehidhelper using
  FBI and then use rehidhelper to install rehid. You DO NOT need to download the 0004013000001D02.cxi
  file.</strong></p>

  <p dir="auto">Some premade configs can be found here:- <a href="https://github.com/Nanashi13/Rehid-configs-files-3DS">https://github.com/Nanashi13/Rehid-configs-files-3DS</a></p>

  <p dir="auto">As always, feel free to join the discord server mentioned above if
  you need help.</p>

  <p dir="auto">You can scan the following QR code to install rehidhelper using FBI.<br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/fb1ab101-127b-4a67-9d74-3d20ea6f4c0f"><img
  width="200" height="200" alt="qrcode (1)" src="https://github.com/user-attachments/assets/fb1ab101-127b-4a67-9d74-3d20ea6f4c0f"
  style="max-width: 100%; height: auto; max-height: 200px;; aspect-ratio: 200 / 200;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a></p>'
updated: '2026-04-05T15:10:32Z'
version: v5.0
version_title: v5.0 Sixth Release
---
# Rehid

HID module rewrite with the aim of easier button remapping and more.

## How To Use

You need to have the latest luma for this to work correctly.

* Download `rehidhelper.3dsx` from the latest release
* Open homebrew launcher and run the 3dsx
* Click `A` on the `Download Rehid` option
* Restart your 3ds
* Go to https://mikahjc.github.io/3dsRemapBuilder/config and generate your remappings.
* Run rehidhelper again and select the Scan QR code option
* Scan your QR.

## How To Remap Buttons

You first need to create a `rehid.json` file with the remappings you want. For eg:-
```Json
{
    "keys":[
        {"get":"R", "press":"ZR"},
        {"get":"L", "press":"ZL"}
    ]
}
```
With the above, everytime you press `ZR` key, `R` key would be triggered, 

and everytime you press `ZL` key, `L` key would be triggered.

It is also possible to do custom key combos, i.e.,
```Json
{
    "keys":[
        {"get":"R", "press":"X+Y"},
        {"get":"L+R", "press":"SELECT"}
    ]
}
```
Now everytime you press `X+Y`, `R` key would be triggered and on pressing `SELECT` button, both `L` and `R` would be triggered.

Possible Keys are:- 
`A`, `B`, `X`, `Y`, `SELECT`, `START`, `ZL`, `ZR`, `L`, `R`, `LEFT`, `RIGHT`, `UP`, `DOWN`, `CRIGHT`(CPAD), `CLEFT`(CPAD), `CUP`(CPAD), `CDOWN`(CPAD)

Copy your `rehid.json` file to the `rehid` folder.

### Per Title Button Remapping

It is possible to have different button remapings for different titles:-

Inside the `rehid` folder, create a folder with the titleid as the folder name.

You can use [this](https://hax0kartik.github.io/3dsdb/) to fidn the titleid for your game.

Copy the `rehid.json` file inside this folder.

## Compilation
Get devkitpro, ctrulib and makerom and then `make -j` to compile.

## Credits

@luigoalma Help, testing and listening to my rants.

Druivensap on my discord server for helping me test out.

Luma3ds devs and contributors

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>rehidhelper.cia</summary>
<ol>
<li>Download <code>rehidhelper.cia</code> to <code>/cias/rehidhelper.cia</code> on your SD card</li>
<li>Insert your SD card back into your 3DS and turn it on</li>
<li>Install and delete <code>/cias/rehidhelper.cia</code> using FBI or GodMode9</li>
</ol>
</details>

