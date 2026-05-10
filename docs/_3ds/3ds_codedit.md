---
author: David Cuevas
avatar: https://avatars.githubusercontent.com/u/98664178?v=4
categories:
- utility
- app
color: '#a2c4e4'
color_bg: '#5b6e80'
created: '2026-03-29T04:57:04Z'
description: 3DS CodEdit is a code-first editor and project workspace for Nintendo
  3DS. It combines a lightweight multi-tab text editor, project Git workflow, file
  manager tools, and a monochrome draw mode for quick PBM assets.
download_page: https://github.com/dcuevasa/3DS_CodEdit/releases
downloads:
  3DS_CodEdit.3dsx:
    size: 2656272
    size_str: 2 MiB
    url: https://github.com/dcuevasa/3DS_CodEdit/releases/download/v.1.0.0/3DS_CodEdit.3dsx
  3DS_CodEdit.cia:
    size: 2085824
    size_str: 1 MiB
    url: https://github.com/dcuevasa/3DS_CodEdit/releases/download/v.1.0.0/3DS_CodEdit.cia
github: dcuevasa/3DS_CodEdit
icon: https://raw.githubusercontent.com/dcuevasa/3DS_CodEdit/refs/heads/next/res/ic_launcher_filemanager.png
image: https://raw.githubusercontent.com/dcuevasa/3DS_CodEdit/refs/heads/next/res/banner.png
image_length: 37646
layout: app
qr:
  3DS_CodEdit.cia: https://db.universal-team.net/assets/images/qr/3ds_codedit-cia.png
source: https://github.com/dcuevasa/3DS_CodEdit
stars: 6
systems:
- 3DS
title: 3DS_CodEdit
unique_ids:
- '0x3DCE1'
update_notes: <p dir="auto">working</p>
updated: '2026-03-29T20:46:33Z'
version: v.1.0.0
version_title: 3DS_CodEdit
---
# 3DS CodEdit

3DS CodEdit is a code-first editor and project workspace for Nintendo 3DS.
It combines a lightweight multi-tab text editor, project Git workflow, file manager tools, and a monochrome draw mode for quick PBM assets.

## What It Focuses On

### 1. Code editing on-device
- Multi-tab text editor (up to 4 open documents).
- Create, open, edit, save, and save-as files directly on SD.
- Line-based editing with cursor movement, line numbers, and visible cursor position (Ln/Col).
- Fast editing actions from buttons and top menu:
	- edit current line with OSK,
	- insert newline,
	- close/switch tabs,
	- find next text match,
	- undo/redo support.
- Sidebar workflow for project files: open files/folders, create new file/folder, go to parent directory.

### 2. Integrated Git + GitHub workflow
- Local Git actions:
	- init repository,
	- add all,
	- commit staged changes,
	- staged file counter and branch display.
- GitHub actions:
	- probe remote,
	- clone to current path,
	- fetch,
	- pull (fast-forward),
	- push,
	- personal access token storage.
- `.gitignore` support in add-all and push file scanning.
- Multi-repository safety improvements:
	- repository-local remote/branch state is preferred,
	- `Root*` warning when operating from a subfolder,
	- double-confirm guard for root-scope actions.

### 3. Draw mode for pixel assets (`.pbm`)
- Built-in black/white canvas editor (stylus pen + eraser).
- Create new drawings from editor sidebar (`DRAW`).
- Open existing `.pbm` files from Explorer or editor sidebar.
- Save as PBM (`P4`) and return to Git workflow for commit/push.

## File and System Features

- Explorer with storage usage bar, icons, and multi-select.
- File operations: create, rename, delete, copy, move, and batch operations.
- Archive extraction support (`.zip`, `.rar`, `.7z`, `.lzma`).
- Image viewer with zoom/pan and image properties.
- Search and quick jump to a path.
- Optional CTRNAND browsing/copying in developer options.
- Sorting modes: alphabetical (asc/desc) and size (largest/smallest).
- Dark theme, updater, and persistent config (`last_dir`, sort mode, Git defaults, token).

## Quick Navigation Notes

- Home icon toggles between Explorer and editor.
- In Explorer, `SELECT` also returns to editor.
- In editor, `SELECT` opens/closes the top menu (`File`, `Edit`, `Search`, `View`, `Project`).
- `Project` opens the Git panel.