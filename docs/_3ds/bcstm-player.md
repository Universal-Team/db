---
author: NPI-D7
avatar: https://avatars.githubusercontent.com/u/71648010?v=4
categories:
- app
color: '#a1a0c9'
color_bg: '#666580'
created: '2021-02-04T09:53:45Z'
description: BCSTM-Player for 3ds
download_page: https://github.com/npid7/BCSTM-Player/releases
downloads:
  BCSTM-Player.3dsx:
    size: 1571892
    size_str: 1 MiB
    url: https://github.com/npid7/BCSTM-Player/releases/download/v2.0.0/BCSTM-Player.3dsx
  BCSTM-Player.cia:
    size: 1360832
    size_str: 1 MiB
    url: https://github.com/npid7/BCSTM-Player/releases/download/v2.0.0/BCSTM-Player.cia
github: npid7/BCSTM-Player
icon: https://raw.githubusercontent.com/npid7/BCSTM-Player/main/app/icon.png
image: https://raw.githubusercontent.com/npid7/BCSTM-Player/main/app/banner.png
image_length: 2829
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
qr:
  BCSTM-Player.cia: https://db.universal-team.net/assets/images/qr/bcstm-player-cia.png
screenshots:
- description: Credits
  url: https://db.universal-team.net/assets/images/screenshots/bcstm-player/credits.png
- description: Main menu
  url: https://db.universal-team.net/assets/images/screenshots/bcstm-player/main-menu.png
source: https://github.com/npid7/BCSTM-Player
stars: 1
systems:
- 3DS
title: BCSTM-Player
unique_ids:
- '0x78933'
update_notes: '<p dir="auto">After almost 3 years, it''s time for a new big update.</p>

  <p dir="auto">As all the Updates before only fixed Logical issues with the filebrowser
  and some visual bugs, it was time to focus on the file loading/decoding and playing
  code.</p>

  <h2 dir="auto">General Stuff</h2>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Type</th>

  <th>Before</th>

  <th>After</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td>Encoding</td>

  <td><strong>ADPCM</strong></td>

  <td><strong>ADPCM</strong>, <strong>PCM8</strong>, <strong>PCM16</strong></td>

  </tr>

  <tr>

  <td>Chennels</td>

  <td>1, 2</td>

  <td>1, 2, 4, 6, 8</td>

  </tr>

  <tr>

  <td>Play NonLoop to End</td>

  <td>No</td>

  <td>Yes</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <h2 dir="auto">Github Generated</h2>

  <ul dir="auto">

  <li>

  <p dir="auto">Dev 2.0.0 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tobid7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tobid7">@tobid7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3693589390"
  data-permission-text="Title is private" data-url="https://github.com/npid7/BCSTM-Player/issues/8"
  data-hovercard-type="pull_request" data-hovercard-url="/npid7/BCSTM-Player/pull/8/hovercard"
  href="https://github.com/npid7/BCSTM-Player/pull/8">#8</a></p>

  </li>

  <li>

  <p dir="auto">Dev 2.0.0 by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/tobid7/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/tobid7">@tobid7</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="3702276844"
  data-permission-text="Title is private" data-url="https://github.com/npid7/BCSTM-Player/issues/13"
  data-hovercard-type="pull_request" data-hovercard-url="/npid7/BCSTM-Player/pull/13/hovercard"
  href="https://github.com/npid7/BCSTM-Player/pull/13">#13</a></p>

  </li>

  <li>

  <p dir="auto"><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/tobid7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tobid7">@tobid7</a>
  made their first contribution in <a class="issue-link js-issue-link" data-error-text="Failed
  to load title" data-id="3693589390" data-permission-text="Title is private" data-url="https://github.com/npid7/BCSTM-Player/issues/8"
  data-hovercard-type="pull_request" data-hovercard-url="/npid7/BCSTM-Player/pull/8/hovercard"
  href="https://github.com/npid7/BCSTM-Player/pull/8">#8</a></p>

  </li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/npid7/BCSTM-Player/compare/v1.5.0...v2.0.0"><tt>v1.5.0...v2.0.0</tt></a></p>

  <h2 dir="auto">Fixes</h2>

  <ul dir="auto">

  <li>Fixed the glitched sound bug <a class="commit-link" data-hovercard-type="commit"
  data-hovercard-url="https://github.com/npid7/BCSTM-Player/commit/1085acb5b8bf507fb023650f83723edea3d265c4/hovercard"
  href="https://github.com/npid7/BCSTM-Player/commit/1085acb5b8bf507fb023650f83723edea3d265c4"><tt>1085acb</tt></a></li>

  <li>Fixed all the crashes of course by add c++ exceptions to catch issues</li>

  </ul>

  <h2 dir="auto">New Stuff</h2>

  <ul dir="auto">

  <li>Switched to <a href="https://github.com/tobid7/palladium/tree/development">palladium
  0.6.0 alpha</a> as backend library</li>

  <li>Added UI7 UI on the Bottom Screen</li>

  <li>Added <a href="https://github.com/tobid7/ctrff">ctrff</a> for fileinspector
  and ctrff-decoder</li>

  <li>Added Custom UI for FileInspector and Filebrowser on Top Screen</li>

  <li>Added Translations [en, de]</li>

  <li>Added partial theme support (Only for top Screen)</li>

  <li>Added support for opening bcwav in fileinspector (Not playable yet)</li>

  </ul>

  <h1 dir="auto">Other changes</h1>

  <ul dir="auto">

  <li>No more <a href="https://github.com/devkitpro/citro2d">citro2d</a> support</li>

  <li>No Systemfont support yet (cause it freezes)</li>

  </ul>

  <div class="markdown-alert markdown-alert-warning" dir="auto"><p class="markdown-alert-title"
  dir="auto"><svg class="octicon octicon-alert mr-2" viewBox="0 0 16 16" version="1.1"
  width="16" height="16" aria-hidden="true"><path d="M6.457 1.047c.659-1.234 2.427-1.234
  3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25
  0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53
  3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0
  1 2 0Z"></path></svg>Warning</p>

  <h2 dir="auto">Known Bugs</h2>

  <ul dir="auto">

  <li>License View shows text a bit out of the screen</li>

  <li>OLD3DS Only runs at 30FPS (WIP)</li>

  <li>It is possible to softlock in license menu</li>

  </ul>

  </div>

  <h2 dir="auto">Credits</h2>

  <ul dir="auto">

  <li><a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/tobid7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/tobid7">@tobid7</a>:
  Lead developer of the Project, German and Englisch Translation</li>

  <li><a class="user-mention notranslate" data-hovercard-type="organization" data-hovercard-url="/orgs/devkitPro/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/devkitPro">@devkitPro</a>:
  libctru, citro3d</li>

  </ul>

  <div class="markdown-alert markdown-alert-important" dir="auto"><p class="markdown-alert-title"
  dir="auto"><svg class="octicon octicon-report mr-2" viewBox="0 0 16 16" version="1.1"
  width="16" height="16" aria-hidden="true"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216
  0 16 .784 16 1.75v9.5A1.75 1.75 0 0 1 14.25 13H8.06l-2.573 2.573A1.458 1.458 0 0
  1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.5c0 .138.112.25.25.25h2a.75.75
  0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25
  0 0 0-.25-.25Zm7 2.25v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 9a1 1 0
  1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>Important</p><p dir="auto">And finally it is
  time to mention <strong><a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/cheuble/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/cheuble">@cheuble</a></strong>,
  the creator of the <a href="https://github.com/cheuble/BCSTM-Player">Original BCSTM-Player</a>
  which took advantage of <del>Freeshops</del> <strong>BCSTM Playing Code</strong>.
  This code is still kinda used in the <strong>BCSTMV2 decoder</strong> which i left
  in the codebase for <strong>historical reasons</strong>.</p>

  </div>

  <h2 dir="auto">Last words</h2>

  <p dir="auto">If you encounter any issues (including crashes or just bugs), report
  them in an issue please.</p>

  <p dir="auto">If you want to want to have your language supported as well, feel
  free to open a pullrequest with the json of your language. But keep in mind that
  i will remove some strings in some cleanup commit</p>

  <p dir="auto">I will get on them when I have time but for now i need to step back
  from coding. I always do too much projects and other stuff at once and it is finally
  time to take a break.</p>

  <p dir="auto">And finally:</p>

  <p dir="auto"><strong>Merry Christmas and happy holidays to everyone 🎄</strong></p>

  <p dir="auto"><em>-tobid7</em></p>'
updated: '2025-12-25T00:28:51Z'
version: v2.0.0
version_title: v2.0.0
wiki: https://github.com/npid7/BCSTM-Player/wiki
---
