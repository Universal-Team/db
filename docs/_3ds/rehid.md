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
    size: 750528
    size_str: 732 KiB
    url: https://github.com/hax0kartik/rehid/releases/download/v4.0/rehidhelper.cia
github: hax0kartik/rehid
image: https://avatars.githubusercontent.com/u/16360444?v=4&size=128
image_length: 21350
layout: app
qr:
  rehidhelper.cia: https://db.universal-team.net/assets/images/qr/rehidhelper-cia.png
screenshots:
- description: Helper
  url: https://db.universal-team.net/assets/images/screenshots/rehid/helper.png
source: https://github.com/hax0kartik/rehid
stars: 133
systems:
- 3DS
title: rehid
update_notes: '<p dir="auto">This is the fifth public release of rehid.<br>

  The following changes have been made:</p>

  <ul dir="auto">

  <li>Add debugpad support.</li>

  <li>Fix bugs in CPAD&gt;DPAD and DPAD&gt;CPAD remappings.</li>

  <li>Fix a bug where global remaps would <em>not</em> be applied on the home menu
  after you close a title.</li>

  <li>Rehidhelper has been rewritten and should be more stable.</li>

  <li>Rehidhelper is now available as a CIA and can be installed on the home screen
  directly.</li>

  <li>Add experimental support for turbofire/autofire. For further details, you can
  look at <a href="https://gbatemp.net/threads/wip-rehid-button-remapping-for-3ds.585387/post-10079729"
  rel="nofollow">this</a> post.</li>

  <li>Luma v13.0 support has been added by moving to CXI-based patching. <strong>This
  release will only work with luma v13.0 and above</strong></li>

  </ul>

  <p dir="auto"><strong>For newcomers, please download and install rehidhelper using
  FBI and then use rehidhelper to install rehid. You DO NOT need to download the 0004013000001D02.cxi
  file.</strong></p>

  <p dir="auto"><strong>If you''ve installed rehid previously, please delete the <code
  class="notranslate">/luma/titles/0004013000001D02</code> and <code class="notranslate">/luma/titles/0004013000003302</code>
  folder manually and then reinstall rehid using the new rehidhelper.</strong></p>

  <p dir="auto">You can ask for help either on <a href="https://discord.gg/hyuvmb9"
  rel="nofollow">my discord server</a> or on the gbatemp <a href="https://gbatemp.net/threads/wip-rehid-button-remapping-for-3ds.585387/"
  rel="nofollow">thread</a>.</p>

  <p dir="auto">Some premade configs can be found here:-  <a href="https://github.com/Nanashi13/Rehid-configs-files-3DS">https://github.com/Nanashi13/Rehid-configs-files-3DS</a></p>

  <p dir="auto">You can scan the following QR code to install rehidhelper using FBI.<br>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/762c824a-4f38-47de-bbce-fa35a94e2837"><img
  src="https://github.com/user-attachments/assets/762c824a-4f38-47de-bbce-fa35a94e2837"
  alt="image" style="max-width: 100%;"></a></p>'
updated: '2023-07-21T04:27:05Z'
version: v4.0
version_title: v4.0 Fifth Release
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