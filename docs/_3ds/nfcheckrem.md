---
author: Golem64
avatar: https://avatars.githubusercontent.com/u/65229557?v=4
categories:
- utility
color: '#3f3428'
color_bg: '#3f3428'
created: '2024-03-29T19:18:41Z'
description: Patch for Nintendo consoles to remove the read-only check on amiibos
  and allow for rewritable Ntag215 NFC tags
download_page: https://github.com/Golem642/NFCheckRem/releases
downloads:
  New_3DS_and_New_2DS.zip:
    size: 615
    size_str: 615 Bytes
    url: https://github.com/Golem642/NFCheckRem/releases/download/3ds/New_3DS_and_New_2DS.zip
  Old_3DS_and_Old_2DS.zip:
    size: 616
    size_str: 616 Bytes
    url: https://github.com/Golem642/NFCheckRem/releases/download/3ds/Old_3DS_and_Old_2DS.zip
github: Golem642/NFCheckRem
icon: https://raw.githubusercontent.com/Golem642/NFCheckRem/main/NFCheckRem.png
image: https://raw.githubusercontent.com/Golem642/NFCheckRem/main/NFCheckRem.png
image_length: 13600
layout: app
script_message: 'You will need to have "Game Patching" and "Loading external FIRMs
  and modules"

  enabled in LumaCFW settings (hold select on boot)'
source: https://github.com/Golem642/NFCheckRem
stars: 12
systems:
- 3DS
title: NFCheckRem
update_notes: '<p dir="auto">Here''s the first fully working version of the patch.
  As of now, it''s only for the 3DS/2DS family. Everything is working : You can scan
  any amiibo you want with your DS, whether normal (locked) or unlocked and it will
  recognize it</p>

  <p dir="auto">Alongside it is a modified build of TagMo which essentially disable
  writing the lock bits onto your NFC tags. (You will have to uninstall the actual
  TagMo beforehand if you have it, otherwise Android will not let you update as I
  signed the APK with my own keys since i don''t know the ones used for TagMo)<br>

  So you can rewrite over an unlocked tag as many times as you want, and change it''s
  figurine anytime.<br>

  But keep in mind as of now the save data inside the tag is deleted too if you rewrite
  it (although only a few games uses save data onto amiibos)</p>

  <p dir="auto">Before making an issue saying it''s not working, please make sure
  you :</p>

  <ul dir="auto">

  <li>Installed the correct patch</li>

  <li>Activated "Enable game patching" And "Allow custom firmware" in Luma3DS settings
  (hold SELECT on console startup)</li>

  <li>Used the modified TagMo to flash either : a blank NFC tag, or an already rewritable
  amiibo nfc Tag. Classic amiibos you flashed with the official TagMo will not be
  able to be rewritten</li>

  </ul>

  <p dir="auto">If you have any other problem, then create an issue so i can help
  you fix it.</p>

  <p dir="auto">Have fun !</p>'
updated: '2024-06-06T23:17:35Z'
version: 3ds
version_title: Fully working patch for the 3DS/2DS family
---
Patch for Nintendo consoles to remove the read-only check on amiibos and allow for rewritable Ntag215 NFC tags
# Installation
- Nintendo 3DS : Ensure you have the latest [Luma3DS](https://github.com/LumaTeam/Luma3DS/) version, then go into the folder corresponding to your console and download the .ips file. 
Put this file into your SD card in the following folder : `/luma/sysmodules/` then ensure you have "Enable loading external FIRMs and modules" and "Enable game patching" enabled in the Luma3DS settings (hold SELECT on boot)
- Wii U : (not yet implemented)
- Switch : (not yet implemented)
### Note for 3DS users
The patch will do nothing if wumiibo is enabled, ensure wumiibo is disabled before attempting to scan any Amiibo or NFC tag
# Why ?
When writing an Amiibo to a blank Ntag215 NFC tag with an app such as [TagMo](https://github.com/HiddenRamblings/TagMo), the tag will become read-only on some parts of the data.

This data includes the Amiibo game character id, variant, figure type, model number and series.

This means that if it's read-only, you cannot change the figure stored on the NFC tag, which therefore mean having to buy multiple tags for every Amiibo you want.
# Can't I just use Wumiibo/re_nfpii ?
Well yes but sometimes games won't like when you open their menu and give you intense lag until you restart it, making those amiibo emulation apps unusable on those games.

Moreover, this solution will give you the possibility to have physical tags, so you get the original experience with a few more features + you can easily share it with others as long as they have the patch too
# What does this do ?
This modifies the NFC system module to disable the checks that are made on those areas, yes the console checks if the tag is read-only.

By disabling these checks, this means you can have write-enabled tags and they would still work on consoles with the patch installed

And thus, you can reuse your tag forever without being constrained to have it as one specific Amiibo (you still have to rewrite it every time you want to change it)
# Technical details
See the [GitHub repository](https://github.com/Golem642/NFCheckRem)