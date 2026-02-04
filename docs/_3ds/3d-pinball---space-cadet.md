---
author: MaikelChan
avatar: https://avatars.githubusercontent.com/u/7031754?v=4
categories:
- game
color: '#77819a'
color_bg: '#636b80'
created: '2021-10-15T11:13:15Z'
description: Wii and 3DS ports of  3D Pinball - Space Cadet
download_page: https://github.com/MaikelChan/SpaceCadetPinball/releases
downloads:
  SpaceCadetPinball-3DS-v0.6.7z:
    size: 422160
    size_str: 412 KiB
    url: https://github.com/MaikelChan/SpaceCadetPinball/releases/download/v0.6-3ds/SpaceCadetPinball-3DS-v0.6.7z
github: MaikelChan/SpaceCadetPinball
icon: https://github.com/MaikelChan/SpaceCadetPinball/raw/3ds/ctr/icon.png
image: https://github.com/MaikelChan/SpaceCadetPinball/raw/3ds/ctr/banner.png
image_length: 17484
layout: app
license: mit
license_name: MIT License
screenshots:
- description: Awaiting deployment
  url: https://db.universal-team.net/assets/images/screenshots/3d-pinball---space-cadet/awaiting-deployment.png
script_message: 'Note: You will need the game data files from

  an actual copy of 3D pinball or "Full Tilt!".'
source: https://github.com/MaikelChan/SpaceCadetPinball/tree/3ds
stars: 112
systems:
- 3DS
title: 3D Pinball - Space Cadet
unique_ids:
- '0x21A39'
update_notes: '<h2 dir="auto">What''s Changed</h2>

  <ul dir="auto">

  <li>Replace PC Related text by <a class="user-mention notranslate" data-hovercard-type="user"
  data-hovercard-url="/users/korbosoft/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/korbosoft">@korbosoft</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1141628588"
  data-permission-text="Title is private" data-url="https://github.com/MaikelChan/SpaceCadetPinball/issues/12"
  data-hovercard-type="pull_request" data-hovercard-url="/MaikelChan/SpaceCadetPinball/pull/12/hovercard"
  href="https://github.com/MaikelChan/SpaceCadetPinball/pull/12">#12</a></li>

  <li>Add banner Sound Effect for the 3DS home menu by <a class="user-mention notranslate"
  data-hovercard-type="user" data-hovercard-url="/users/korbosoft/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/korbosoft">@korbosoft</a>
  in <a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="1241034277"
  data-permission-text="Title is private" data-url="https://github.com/MaikelChan/SpaceCadetPinball/issues/17"
  data-hovercard-type="pull_request" data-hovercard-url="/MaikelChan/SpaceCadetPinball/pull/17/hovercard"
  href="https://github.com/MaikelChan/SpaceCadetPinball/pull/17">#17</a></li>

  </ul>

  <p dir="auto"><strong>Full Changelog</strong>: <a class="commit-link" href="https://github.com/MaikelChan/SpaceCadetPinball/compare/v0.5-3ds...v0.6-3ds"><tt>v0.5-3ds...v0.6-3ds</tt></a></p>'
updated: '2024-02-08T04:33:50Z'
version: v0.6-3ds
version_title: v0.6 3DS
website: https://pacochan.net/software/3d-pinball-space-cadet/
---
# 3D Pinball - Space Cadet for 3DS

This is a port of 3D Pinball - Space Cadet for Nintendo 3DS. It's originally a game that came bundled with Windows from Windows 95 up to Windows XP. This is the current state of the project:

- No menus, options, or results screen.
- It plays sound effects and music (if the player supplies the music in OGG format).
- There are still some bugs here and there.
- It should be running fine on New 3DS, but on a regular 3DS it runs slow.

It is based on the PC decompilation made by [k4zmu2a](https://github.com/k4zmu2a): https://github.com/k4zmu2a/SpaceCadetPinball

The PC decompilation uses SDL2 to render the game. This 3DS port has been changed to use native GPU rendering with the Citro3D library.

## How to build

The main requirement is to have [devkitPro](https://devkitpro.org).

Follow the instructions to install devkitPro here: https://devkitpro.org/wiki/Getting_Started
You will also need the 3DS development package, and also the libraries 3ds-sdl and 3ds-sdl_mixer.

If you use Windows or Ubuntu, here are more detailed instructions.

### Windows

Even though devkitPro offers a Windows installer, I've had some issues setting it up. It's easier to use WSL. If you want to use the Windows installer anyway, check the link above for instructions.

1. Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install). By default it will install Ubuntu, which is fine.
2. Open a WSL terminal and just follow the Ubuntu instructions below. With the difference that, if you want to clone the project into, for example, the `C:\` folder, you will need move to that folder inside the terminal with the command `cd /mnt/c/`.

### Ubuntu and other Debian based linux distros

1. Open the terminal in the folder where you want to clone the project.
2. Clone it with the command `git clone --branch 3ds https://github.com/MaikelChan/SpaceCadetPinball`. A subfolder called `SpaceCadetPinball` will be created containing the project.
3. Move to that subfolder with `cd SpaceCadetPinball`.
4. Download the latest version of the [custom devkitPro pacman](https://github.com/devkitPro/pacman/releases/tag/v1.0.2), that will be used to download the compilers and libraries to build the project. Once downloaded, put it in the `SpaceCadetPinball` folder.
5. Install devkitPro pacman with this command: `sudo gdebi devkitpro-pacman.amd64.deb`. If gdebi is not found, install it with `sudo apt install gdebi-core`, and then try again installing pacman.
6. Use the following command to sync pacman databases: `sudo dkp-pacman -Sy`.
7. Now update packages with `sudo dkp-pacman -Syu`.
8. Install the 3DS development tools with `sudo dkp-pacman -S 3ds-dev`.
9. Install SDL with `sudo dkp-pacman -S 3ds-sdl`.
10. Install SDL_mixer with `sudo dkp-pacman -S 3ds-sdl_mixer`.
11. Set the DEVKITPRO environment variables so the system knows where the compilers and libraries are installed with these commands:
    - `export DEVKITPRO=/opt/devkitpro`.
    - `export DEVKITARM=/opt/devkitpro/devkitARM`.
12. To generate Build the project with the command `make -j4`.
13. Optionally, to generate a CIA file, you will need to have [bannertool](https://github.com/Steveice10/bannertool/releases/) and [makerom](https://github.com/3DSGuy/Project_CTR/releases) in the `$DEVKITPRO/tools/bin` folder. Then build the project with the command `make -j4 BUILD_CIA=1`.

After a successful build, you will get a file called `SpaceCadetPinball.3dsx`, which is the main executable.

## How to run

### 3DS with Homebrew Launcher

1. Go to your SD card and enter the `3ds` folder.
2. Copy `SpaceCadetPinbal.3dsx` into the `3ds` folder.
3. Make sure you have your `dspfirm.cdc` in the `3ds` folder, as you will need it to have sound in homebrew games. If you don't have it, [dump your DSP](https://github.com/zoogie/DSP1/releases/latest).
4. Inside the `3ds` folder, create a new folder named `SpaceCadetPinball`.
5. For legal reasons, you will need to get the original PC game on your own to obtain the assets like graphics and sound effects. Those are not contained in this repository.
6. Copy all files from the original PC version into the `SpaceCadetPinball` folder that was created earlier.
7. Optionally, since this port doesn't play MIDI files, you'll need to convert the music to ogg format, and call the file `PINBALL.ogg`, and put it along the other assets in the `SpaceCadetPinball` folder. Make sure that the music has a sample rate no higher than 44100Hz, or it won't play correctly.
8. If everything went fine, you should be able to run the game from the Homebrew Launcher.

### Citra

1. Get the [Citra emulator](https://citra-emu.org/download/) if you don't have it.
2. Open it and go to the menu `File/Open Citra Folder`. This will open the folder where Citra's configuration is stored.
3. Go to the `sdmc` folder and create a new folder there named `3ds` if it doesn't exist already.
4. Enter the `3ds` folder and create an empty file there named `dspfirm.cdc`. This will allow to have audio in homebrew apps.
5. Inside the `3ds` folder create another folder named `SpaceCadetPinball`.
6. For legal reasons, you will need to get the original PC game on your own to obtain the assets like graphics and sound effects. Those are not contained in this repository.
7. Copy all PC game's assets to the `SpaceCadetPinball` folder that was created earlier.
8. Optionally, since this port doesn't play MIDI files, you'll need to convert the music to ogg format, and call the file `PINBALL.ogg`, and put it along the other assets in the `SpaceCadetPinball` folder. Make sure that the music has a sample rate no higher than 44100Hz, or it won't play correctly.
9. If everything went fine, you should be able to run the game.

## How to play

| Button               | Action                                            |
|----------------------|---------------------------------------------------|
| A                    | Launch the ball                                   |
| L                    | Move the left paddle                              |
| R                    | Move the right paddle                             |
| DPad Left, Right, Up | Bump table                                        |
| X                    | Start a new game                                  |
| Y                    | Exit the game                                     |
| Start                | Pause                                             |
