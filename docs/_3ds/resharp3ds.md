---
author: Saysaa
avatar: https://avatars.githubusercontent.com/u/112180175?v=4
categories:
- app
color: '#3c4037'
color_bg: '#3c4037'
created: '2026-06-01T16:33:12Z'
description: C# runtime and SDK for Nintendo 3DS
download_page: https://github.com/saysaa/ReSharp3DS/releases
downloads:
  ReSharp3DS.3dsx:
    size: 344804
    size_str: 336 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v1.5.3/ReSharp3DS.3dsx
  ReSharp3DS.cia:
    size: 1103808
    size_str: 1 MiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v1.5.3/ReSharp3DS.cia
github: saysaa/ReSharp3DS
icon: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/icon.png
image: https://raw.githubusercontent.com/saysaa/ReSharp3DS/refs/heads/docs/banner.png
image_length: 34706
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
llm_usage: undisclosed
qr:
  ReSharp3DS.cia: https://db.universal-team.net/assets/images/qr/resharp3ds-cia.png
script_message: Remember to create a folder named “ReSharp3DS” at the root of your
  SD card
source: https://github.com/saysaa/ReSharp3DS
stars: 2
systems:
- 3DS
title: ReSharp3DS
unique_ids:
- '0x23400'
update_notes: '<a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/43ffdbc3-789c-451c-a992-18b4fd937105"><img
  width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/43ffdbc3-789c-451c-a992-18b4fd937105"
  style="max-width: 100%; height: auto; max-height: 600px;; aspect-ratio: 600 / 600;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <h3 dir="auto">Fast CIA Installation</h3>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/user-attachments/assets/18f0b938-001c-49f3-a157-07cf714e56ba"><img
  width="250" height="250" alt="ReSharp3DS-QR_CODE" src="https://github.com/user-attachments/assets/18f0b938-001c-49f3-a157-07cf714e56ba"
  style="max-width: 100%; height: auto; max-height: 250px;; aspect-ratio: 250 / 250;
  background-color: var(--bgColor-muted); border-radius: 6px" class="js-gh-image-fallback"></a>

  <h2 dir="auto">ReSharp3DS Runtime Update</h2>

  <ul dir="auto">

  <li>Change the banner, sound, and icon for the .cia file</li>

  <li>Converting <code class="notranslate">gui.c</code> to <code class="notranslate">gui.cpp</code></li>

  <li>Added a graphical user interface to <code class="notranslate">gui.cpp</code>
  (finally!)</li>

  <li>Change in version number: Before: v1.3.2, After: v1.3.2-beta.X (This is an example)</li>

  <li>Bugs Fixes</li>

  <li>Available on Universal-Updater!</li>

  </ul>'
updated: '2026-06-05T10:02:43Z'
version: v1.5.3
version_title: ReSharp3DS Runtime & API - v1.5.3-beta.4
website: https://saysaa.github.io/ReSharp3DS/
wiki: https://saysaa.github.io/ReSharp3DS/
---
<img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=ReSharp3DS&section=header&reversal=false&textBg=false&descAlign=64" />

<p align="center">
  <a href="https://github.com/saysaa/ReSharp3DS/tree/docs">ReSharp3DS Documentation</a>
</p>

ReSharp3DS is an experimental project that runs C# code on the Nintendo 3DS using nanoCLR / nanoFramework.

The project uses a C++ 3DS homebrew application to load C# assemblies compiled as `.pe` files, then executes them through nanoCLR.

### Screenshots 
<img width="400" height="300" alt="IMG_0694" src="https://github.com/user-attachments/assets/8ad88d4e-ba59-45e4-a533-e22ee33996cb" />
<img width="400" height="300" alt="IMG_0703" src="https://github.com/user-attachments/assets/08046418-f449-4dc3-8240-dbe1549b0781" />


## Progress & Roadmap

<details>
<summary><b>Done (Click to expand)</b></summary>

* [x] Initialize nanoCLR on Nintendo 3DS
* [x] Load `mscorlib.pe` and `app.pe` from SD card
* [x] Execute C# `Program.Main()`
* [x] Call native C++ functions from C# using `InternalCall`
* [x] Basic Console API (`Clear`, `Write`, `WriteLine`)
* [x] Input support (`Start`, `Select`)
* [x] Full Button Mapping (A, B, X, Y, D-Pad, L, R)
* [x] Runtime management (`Runtime.Yield()`, static state preservation)
* [x] Validate on Citra & Real Hardware
* [x] Fix screen flickering by avoiding full redraw every tick
</details>

<details>
<summary><b>To be implemented (Click to expand)</b></summary>

* [ ] Expanded Console API (bool, float, better formatting)
* [ ] Automatic native method binding instead of index-based mapping
* [ ] Graphics & Audio APIs
* [ ] Filesystem support
* [ ] Better error reporting for C# exceptions
* [ ] Proper SDK structure & templates
* [ ] Stabilize HOME Menu suspend/resume behavior
</details>

---

## File Structure

For the runtime to function correctly, your SD card must be organized as follows:

```
SD:/
├── 3ds/
│   └── ReSharp3DS.3dsx          # Runtime Homebrew
└── ReSharp3DS/                  # Data folder
    ├── mscorlib.pe              # nanoFramework base library
    └── app.pe                   # C# program (user app)
```

> **Note:** The runtime specifically looks for the assemblies in `sdmc:/ReSharp3DS/`.

---

### What is it for?

ReSharp3DS is meant for experimenting with managed C# code execution on the Nintendo 3DS. It can be used as a base to build 3DS homebrew logic in C#, test nanoCLR on non-standard platforms, and call native C++ code from C#.

**Example:**

```csharp
namespace ReSharp3DS
{
    public class Program
    {
        public static void Main()
        {
            Console.Clear();
            Console.WriteLine("Hello from C# on 3DS!");
            Console.WriteLine("Press START to quit.");

            while (!Input.IsStartPressed())
            {
                Runtime.Yield();
            }

            Console.WriteLine("Bye.");
        }
    }
}
```

---

### Requirements

* **C++ Side:** devkitPro (devkitARM, libctru, make).
* **C# Side:** nanoFramework-compatible compiler (e.g., nanoFramework.CoreLibrary).
* **Hardware:** A Nintendo 3DS with Luma3DS and Homebrew Launcher.

---

### Installation & Build

#### 1. Building the Homebrew (C++)
From the project folder, run:
```bash
make clean
make
```
This generates `ReSharp3DS.3dsx`.

#### 2. Building the C# application
Compile your C# code into a `.pe` assembly using the nanoFramework toolchain. Rename the output file to `app.pe`.

#### 3. Deployment
1. Copy `ReSharp3DS.3dsx` to `SD:/3ds/`.
2. Copy `mscorlib.pe` and your `app.pe` to `SD:/ReSharp3DS/` (create the folder at the root of the SD if it doesn't exist).
3. Launch the app from the **Homebrew Launcher**.

---

### Troubleshooting

If a file is missing or incorrectly placed, the program will display an error:
`[FATAL] app load failed`

Make sure the `ReSharp3DS` folder is at the **root** of the SD card, not inside the `/3ds/` folder.

