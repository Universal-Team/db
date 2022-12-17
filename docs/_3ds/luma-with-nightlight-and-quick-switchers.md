---
author: Nutez
avatar: https://gbatemp.net/data/avatars/l/439/439371.jpg
categories:
- utility
- firm
- luma3ds
color: '#957d64'
color_bg: '#806b56'
created: '2019-02-24T20:26:40Z'
description: On-boot, customisable screen filters & other QoL improvements
download_page: https://gbatemp.net/download/35619/
downloads:
  luma1030_QuickSwitchers - NightLight .zip:
    url: https://gbatemp.net/download/35619/download
gbatemp: '35619'
github: DullPointer/Luma3DS
image: https://gbatemp.net/data/avatars/l/439/439371.jpg
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/DullPointer/Luma3DS
systems:
- 3DS
title: Luma with Night/Light and Quick-Switchers
update_notes: 'Official Luma version number bump<br/>

  <ul>

  <li data-xf-list-type="ul">Recent official Luma changes e.g. improved system time
  setting and "Wait for B release before exiting rosalina menu".</li>

  <li data-xf-list-type="ul"><a class="link link--external" href="https://github.com/Pixel-Pop/Luma3DS/commit/d225d9fa507dcccce3a6c86d0a38f7998f39b7a2"
  rel="nofollow ugc noopener" target="_blank">Pixel-Pop''s</a> feature to load custom
  logo.bin from "/luma/logo.bin" (example: rename <a class="link link--external" href="https://github.com/badda71/vice3ds/blob/master/meta/logo-padded.lz11"
  rel="nofollow ugc noopener" target="_blank">this file</a> to "logo.bin" or <a class="link
  link--internal" href="https://gbatemp.net/threads/tutorial-create-your-own-app-logo-logo-bin.433006/">create
  your own</a>).</li>

  </ul>'
updated: '2022-03-24T20:27:22Z'
version: 10.3 2022-03-24
version_title: Luma 10.3 with Night/Light and Quick-Switchers
---
<a class="link link--internal" href="https://gbatemp.net/threads/unofficial-luma-build-discussion.573617/">Discussion/question thread</a><br/>
<a class="link link--external" href="https://github.com/DullPointer/Luma3DS" rel="nofollow ugc noopener" target="_blank">Source</a><br/>
<br/>
Features:<br/>
<span style="color: rgb(0, 102, 0)"><b>Luma 10.3</b></span><br/>
<ul>
<li data-xf-list-type="ul">Thank you to the Luma developers <a class="link link--external" href="https://github.com/LumaTeam/Luma3DS/wiki" rel="nofollow ugc noopener" target="_blank">official github</a></li>
</ul><span style="color: rgb(0, 102, 0)"><a class="link link--internal" href="https://gbatemp.net/threads/ctr_redshift-hardware-based-blue-light-filter-for-old3ds-and-2ds.493736/page-5">Redshift</a><b> custom screen filter (thanks to Sono):</b></span><br/>
<ul>
<li data-xf-list-type="ul">Tweak screens individually (not possible for o2DS due to single screen hardware)</li>
<li data-xf-list-type="ul">Dimming effect for additional brightness reduction</li>
<li data-xf-list-type="ul">Much greater range of filter customisation</li>
<li data-xf-list-type="ul">Reapplies saved filter on awaken from sleep</li>
<li data-xf-list-type="ul">Automatic LED suppression when filter applied</li>
</ul><span style="color: rgb(0, 102, 0)"><b>Night/Light on-boot screen filters (Sono discovery):</b></span><br/>
<ul>
<li data-xf-list-type="ul">Apply custom screen filter and adjust brightness on-boot/awaken depending on time of day!</li>
<li data-xf-list-type="ul">Access Night/Light Config and Edit Filters via Screen filters menu. Config saved in "/luma/" as "configBootshift.bin", "lightshift.bin" and "nightshift.bin".</li>
<li data-xf-list-type="ul">Temporarily disable Night/Light time check via X button in menus. Manual application of screen filters also disables Night/Light.</li>
</ul><span style="color: rgb(0, 102, 0)"><b>Extra Config sub menu to manage optional features:</b></span><br/>
<ul>
<li data-xf-list-type="ul">Automatically suppress LEDs on boot</li>
<li data-xf-list-type="ul">Automatic cut to slot power when booted with DS/TWL game cartridge inserted. This stops DS flashcarts from <a class="link link--external" href="https://github.com/LumaTeam/Luma3DS/issues/1202#issuecomment-449624237" rel="nofollow ugc noopener" target="_blank">leeching power</a> when not in use. You will need to force boot into DS game cartridge by using the CIA from <a class="link link--internal" href="https://gbatemp.net/threads/twl-slot-1-launcher-first-custom-dsiware-app.414501/">here</a>, with <a class="link link--external" href="https://github.com/DS-Homebrew/TWiLightMenu/releases" rel="nofollow ugc noopener" target="_blank">TWiLightMenu</a> or reinsert the cartridge</li>
<li data-xf-list-type="ul">Automatic cut 3DS WiFi in sleep mode</li>
<li data-xf-list-type="ul">Open Rosalina menu with Home Button</li>
<li data-xf-list-type="ul">Toggle bottom LCD backlight from menus with Y button (also exits menu)</li>
</ul><b><span style="color: rgb(0, 102, 0)">Quick-Switchers sub menu:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Quick-Switch between your preferred filters/config for DS/i games (<a class="link link--internal" href="https://gbatemp.net/threads/twpatcher-ds-i-mode-screen-filters-and-patches.542694/">TwlBg</a>) and GBA games (<a class="link link--internal" href="https://gbatemp.net/threads/twpatcher-ds-i-mode-screen-filters-and-patches.542694/page-71#post-9143128">AgbBg</a>, <a class="link link--external" href="https://github.com/profi200/open_agb_firm" rel="nofollow ugc noopener" target="_blank">open_agb_firm</a>, <a class="link link--internal" href="https://gbatemp.net/download/open-agb-launcher.36828/">Open AGB Launcher</a>)</li>
<li data-xf-list-type="ul">TwlBg option displays ".cxi" files from "/luma/sysmodules/TwlBg" and persists selected file name to "/luma/sysmodules/twlbgName.txt"</li>
<li data-xf-list-type="ul"><a class="link link--external" href="https://wiki.ds-homebrew.com/twilightmenu/playing-in-widescreen.html" rel="nofollow ugc noopener" target="_blank">Widescreen</a> option displays ".cxi" files from "/luma/sysmodules/Widescreen" and persists selected file name to "/luma/sysmodules/widescreenName.txt"</li>
<li data-xf-list-type="ul">AgbBg option displays ".cxi" files from "/luma/sysmodules/AgbBg" and persists selected file name to "/luma/sysmodules/agbbgName.txt"</li>
<li data-xf-list-type="ul">Open_AGB option displays ".ini" files from "/3ds/open_agb_firm" and persists selected file name to "/3ds/open_agb_firm/configName.txt"</li>
<li data-xf-list-type="ul">Works best with meaningful file names e.g. "redshiftWideMode.cxi", "pixelPerfect.cxi", "lowBrightness.ini"</li>
<li data-xf-list-type="ul">Delete the .txt file when creating new TwlBg/AgbBg patches to avoid the persisted name being incorrect</li>
<li data-xf-list-type="ul">Option to force revert TWiLightMenu widescreen patch</li>
</ul><b><span style="color: rgb(0, 102, 0)">Plugin loader:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Not CTGP-7 compatible</li>
<li data-xf-list-type="ul">All credit to Nanquitas and PabloMK7 and anyone else involved in the CTRPF project!</li>
<li data-xf-list-type="ul">Supports new CTRPF v0.6.0 and v0.7.0 .3GX format (header 3GX$0002) plugin</li>
<li data-xf-list-type="ul">Not backwards compatible with .plg or old .3gx</li>
<li data-xf-list-type="ul">Default plugin available from <a class="link link--internal" href="https://gbatemp.net/threads/ctrpluginframework-blank-plugin-now-with-action-replay.487729/page-68#post-9343144">CTRPF thread</a> or <a class="link link--external" href="https://discord.com/invite/z4ZMh27" rel="nofollow ugc noopener" target="_blank">Nanquitas' Playground</a> announcements channel</li>
<li data-xf-list-type="ul">"default.3gx" goes in "/luma/plugins" directory</li>
</ul><b><span style="color: rgb(0, 102, 0)">Enhanced brightness adjustment interface:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Adjust brightness of top and bottom screens independently (not possible for o2DS due to single screen hardware)</li>
<li data-xf-list-type="ul">Option to use hidden true maximum brightness (at your own risk?)</li>
<li data-xf-list-type="ul">Option to use hidden true minimum brightness</li>
<li data-xf-list-type="ul">Option to switch off bottom screen backlight entirely</li>
</ul><b><span style="color: rgb(0, 102, 0)">Software volume control interface (thanks again to <a class="link link--internal" href="https://gbatemp.net/threads/is-there-an-volume-management-homebrew.474817/#post-8699169">Sono</a>):</span></b><br/>
<ul>
<li data-xf-list-type="ul">Accessible from System Configuration sub menu</li>
<li data-xf-list-type="ul">Change volume in 1/64 steps without using physical volume slider</li>
<li data-xf-list-type="ul">Volume percentage now displayed in sub menus</li>
</ul><b><span style="color: rgb(0, 102, 0)">Permanent brightness recalibration:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Recalibration is applied for 3DS, DS/i and GBA modes</li>
<li data-xf-list-type="ul">Accessible from System Configuration sub menu</li>
<li data-xf-list-type="ul">Edit the values behind the 5 selectable brightness levels</li>
<li data-xf-list-type="ul">Changes are saved to NAND so use sparingly to avoid wearing out the memory</li>
<li data-xf-list-type="ul">Upper limit of 172 is found in code so it is presumed to be safe but may reduce LCD lifespan</li>
</ul><b><span style="color: rgb(0, 102, 0)">Title specific N3DS settings:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Automatically launch chosen titles with N3DS 804MHz cpu &amp; L2 cache enabled - option available in N3DS menu when title is running (config file saved to "/luma/n3ds" folder).</li>
</ul><b><span style="color: rgb(0, 102, 0)">Misc/QoL:</span></b><br/>
<ul>
<li data-xf-list-type="ul">Quick toggle LEDs from menus by pressing SELECT</li>
<li data-xf-list-type="ul">Quick toggle WiFi from menus by pressing START</li>
<li data-xf-list-type="ul">New3DS clock/cache status visible on main menu</li>
<li data-xf-list-type="ul"><a class="link link--external" href="https://github.com/LumaTeam/Luma3DS/pull/1634" rel="nofollow ugc noopener" target="_blank">Allow Patches in the Home Menu</a> e.g. place files from <a class="link link--internal" href="https://gbatemp.net/threads/release-betterbatterycolors-for-homemenu.523138/">BetterBatteryColors</a> or another <a class="link link--internal" href="https://gbatemp.net/threads/unofficial-luma-build-discussion.573617/page-5#post-9540802">example</a> in /luma/titles/*YourRegionHomeMenuTitleId*/romfs - thank you <a class="link link--external" href="https://github.com/gabe565" rel="nofollow ugc noopener" target="_blank"><span style="font-size: 12px">gabe565</span></a></li>
<li data-xf-list-type="ul">Merged in <a class="link link--external" href="https://github.com/LumaTeam/Luma3DS/pull/1623" rel="nofollow ugc noopener" target="_blank">enhancements</a> to Luma <a class="gbaKw" data-xf-init="tooltip" href="https://gbatemp.net/forums/cheat-codes-add-and-request.412/" style="font-weight: inherit; text-decoration: underline; text-decoration-style: dotted;" target="_blank" title="Cheat Codes Add and Request">cheats</a> system - thank you <a class="link link--external" href="https://github.com/s5bug" rel="nofollow ugc noopener" target="_blank"><span style="font-size: 12px">s5bug</span></a></li>
<li data-xf-list-type="ul">Option to toggle <a class="link link--external" href="https://github.com/hax0kartik/rehid" rel="nofollow ugc noopener" target="_blank">rehid</a> folder System configuration sub menu (folder must be disabled before loading game to not have rehid apply)</li>
<li data-xf-list-type="ul">Thanks to <a class="link link--external" href="https://github.com/Pixel-Pop/Luma3DS/commit/d225d9fa507dcccce3a6c86d0a38f7998f39b7a2" rel="nofollow ugc noopener" target="_blank">Pixel-Pop</a>: load custom logo.bin from "/luma/logo.bin" (example: rename <a class="link link--external" href="https://github.com/badda71/vice3ds/blob/master/meta/logo-padded.lz11" rel="nofollow ugc noopener" target="_blank">this file</a> to "logo.bin" or <a class="link link--internal" href="https://gbatemp.net/threads/tutorial-create-your-own-app-logo-logo-bin.433006/">create your own</a>).</li>
</ul>