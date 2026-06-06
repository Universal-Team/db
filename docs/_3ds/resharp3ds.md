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
    size: 301264
    size_str: 294 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v1.7.3/ReSharp3DS.3dsx
  ReSharp3DS.cia:
    size: 1111488
    size_str: 1 MiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v1.7.3/ReSharp3DS.cia
  sample-app.zip:
    size: 247255
    size_str: 241 KiB
    url: https://github.com/saysaa/ReSharp3DS/releases/download/v1.7.3/sample-app.zip
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
stars: 3
systems:
- 3DS
title: ReSharp3DS
unique_ids:
- '0x23400'
update_notes: "<a target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/user-attachments/assets/2576cb17-503a-45a3-bf79-e4c602d59722\"\
  ><img width=\"600\" height=\"600\" alt=\"image\" src=\"https://github.com/user-attachments/assets/2576cb17-503a-45a3-bf79-e4c602d59722\"\
  \ style=\"max-width: 100%; height: auto; max-height: 600px;; aspect-ratio: 600 /\
  \ 600; background-color: var(--bgColor-muted); border-radius: 6px\" class=\"js-gh-image-fallback\"\
  ></a>\n<h3 dir=\"auto\">Fast CIA Installation</h3>\n<a target=\"_blank\" rel=\"\
  noopener noreferrer\" href=\"https://github.com/user-attachments/assets/cda0017e-5547-4b19-b9c9-ec969598434f\"\
  ><img width=\"250\" height=\"250\" alt=\"ReSharp3DS-QR_CODE\" src=\"https://github.com/user-attachments/assets/cda0017e-5547-4b19-b9c9-ec969598434f\"\
  \ style=\"max-width: 100%; height: auto; max-height: 250px;; aspect-ratio: 250 /\
  \ 250; background-color: var(--bgColor-muted); border-radius: 6px\" class=\"js-gh-image-fallback\"\
  ></a>\n<h2 dir=\"auto\">ReSharp3DS Runtime Update</h2>\n<ul dir=\"auto\">\n<li>Add\
  \ <strong>app</strong> file explorer</li>\n<li>New Makefile</li>\n</ul>\n<h2 dir=\"\
  auto\">ReSharp3DS SDK Update</h2>\n<ul dir=\"auto\">\n<li>Add Audio Support</li>\n\
  </ul>\n<h3 dir=\"auto\">Available methods:</h3>\n<p dir=\"auto\">Audio.Init();<br>\n\
  Audio.Beep(int frequency, int durationMs);<br>\nAudio.PlayWav(string path);<br>\n\
  Audio.SetVolume(int volume);<br>\nAudio.Loop(string path);<br>\nAudio.StopMusic();<br>\n\
  Audio.Stop();<br>\nBeep / frequency audio<br>\nAudio.Beep(440, 200);<br>\nAudio.Beep(880,\
  \ 150);<br>\nCustom WAV playback<br>\nAudio.PlayWav(\"audio.wav\");<br>\nAudio.PlayWav(\"\
  sfx/jump.wav\");</p>\n<p dir=\"auto\"><strong>Paths can be relative to the launched\
  \ .pe file or absolute:</strong></p>\n<p dir=\"auto\"><code class=\"notranslate\"\
  >Audio.PlayWav(\"sdmc:/MyGame/sounds/select.wav\"); </code></p>\n<h3 dir=\"auto\"\
  >Recommended WAV format:</h3>\n<p dir=\"auto\">PCM 16-bit<br>\nMono or stereo<br>\n\
  44100 Hz or 22050 Hz<br>\nMusic looping<br>\nAudio.SetVolume(80);<br>\nAudio.Loop(\"\
  music.wav\");<br>\nAudio.StopMusic();</p>\n<h2 dir=\"auto\">Exemple</h2>\n<div class=\"\
  highlight highlight-source-cs\" dir=\"auto\"><pre class=\"notranslate\"><span class=\"\
  pl-k\">namespace</span> <span class=\"pl-v\">ReSharp3DS</span>\n<span class=\"pl-kos\"\
  >{</span>\n    <span class=\"pl-k\">public</span> <span class=\"pl-k\">class</span>\
  \ <span class=\"pl-smi\">Program</span>\n    <span class=\"pl-kos\">{</span>\n \
  \       <span class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"\
  pl-smi\">bool</span> <span class=\"pl-s1\">initialized</span> <span class=\"pl-c1\"\
  >=</span> <span class=\"pl-c1\">false</span><span class=\"pl-kos\">;</span>\n  \
  \      <span class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"\
  pl-smi\">bool</span> <span class=\"pl-s1\">oldA</span> <span class=\"pl-c1\">=</span>\
  \ <span class=\"pl-c1\">false</span><span class=\"pl-kos\">;</span>\n        <span\
  \ class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"pl-smi\"\
  >bool</span> <span class=\"pl-s1\">oldX</span> <span class=\"pl-c1\">=</span> <span\
  \ class=\"pl-c1\">false</span><span class=\"pl-kos\">;</span>\n        <span class=\"\
  pl-k\"><span class=\"pl-k\">static</span></span> <span class=\"pl-smi\">bool</span>\
  \ <span class=\"pl-s1\">oldY</span> <span class=\"pl-c1\">=</span> <span class=\"\
  pl-c1\">false</span><span class=\"pl-kos\">;</span>\n\n        <span class=\"pl-k\"\
  >public</span> <span class=\"pl-k\"><span class=\"pl-k\">static</span></span> <span\
  \ class=\"pl-smi\">void</span> <span class=\"pl-en\">Main</span><span class=\"pl-kos\"\
  >(</span><span class=\"pl-kos\">)</span>\n        <span class=\"pl-kos\">{</span>\n\
  \            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-c1\">!</span><span class=\"pl-s1\">initialized</span><span class=\"\
  pl-kos\">)</span>\n            <span class=\"pl-kos\">{</span>\n               \
  \ <span class=\"pl-s1\">initialized</span> <span class=\"pl-c1\">=</span> <span\
  \ class=\"pl-c1\">true</span><span class=\"pl-kos\">;</span>\n\n               \
  \ <span class=\"pl-s1\">Console</span><span class=\"pl-kos\">.</span><span class=\"\
  pl-en\">Clear</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n                <span class=\"pl-s1\">Console</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">WriteLine</span><span class=\"\
  pl-kos\">(</span><span class=\"pl-s\">\"Audio test\"</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n\n                <span class=\"pl-s1\"\
  >Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">Init</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n                <span class=\"pl-s1\">Audio</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">SetVolume</span><span class=\"pl-kos\">(</span><span\
  \ class=\"pl-c1\">80</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n                <span class=\"pl-s1\">Audio</span><span class=\"pl-kos\"\
  >.</span><span class=\"pl-en\">Loop</span><span class=\"pl-kos\">(</span><span class=\"\
  pl-s\">\"music.wav\"</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-kos\">}</span>\n\n            <span class=\"\
  pl-smi\">bool</span> <span class=\"pl-s1\">a</span> <span class=\"pl-c1\">=</span>\
  \ <span class=\"pl-s1\">Input</span><span class=\"pl-kos\">.</span><span class=\"\
  pl-en\">IsAPressed</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n            <span class=\"pl-smi\">bool</span> <span\
  \ class=\"pl-s1\">x</span> <span class=\"pl-c1\">=</span> <span class=\"pl-s1\"\
  >Input</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">IsXPressed</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-smi\">bool</span> <span class=\"pl-s1\"\
  >y</span> <span class=\"pl-c1\">=</span> <span class=\"pl-s1\">Input</span><span\
  \ class=\"pl-kos\">.</span><span class=\"pl-en\">IsYPressed</span><span class=\"\
  pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\">;</span>\n\
  \n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">a</span> <span class=\"pl-c1\">&amp;&amp;</span> <span class=\"\
  pl-c1\">!</span><span class=\"pl-s1\">oldA</span><span class=\"pl-kos\">)</span>\n\
  \            <span class=\"pl-kos\">{</span>\n                <span class=\"pl-s1\"\
  >Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">PlayWav</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-s\">\"audio.wav\"</span><span class=\"\
  pl-kos\">)</span><span class=\"pl-kos\">;</span>\n            <span class=\"pl-kos\"\
  >}</span>\n\n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">x</span> <span class=\"pl-c1\">&amp;&amp;</span> <span class=\"\
  pl-c1\">!</span><span class=\"pl-s1\">oldX</span><span class=\"pl-kos\">)</span>\n\
  \            <span class=\"pl-kos\">{</span>\n                <span class=\"pl-s1\"\
  >Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">SetVolume</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-c1\">40</span><span class=\"pl-kos\"\
  >)</span><span class=\"pl-kos\">;</span>\n            <span class=\"pl-kos\">}</span>\n\
  \n            <span class=\"pl-k\">if</span> <span class=\"pl-kos\">(</span><span\
  \ class=\"pl-s1\">y</span> <span class=\"pl-c1\">&amp;&amp;</span> <span class=\"\
  pl-c1\">!</span><span class=\"pl-s1\">oldY</span><span class=\"pl-kos\">)</span>\n\
  \            <span class=\"pl-kos\">{</span>\n                <span class=\"pl-s1\"\
  >Audio</span><span class=\"pl-kos\">.</span><span class=\"pl-en\">StopMusic</span><span\
  \ class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-kos\">}</span>\n\n            <span class=\"\
  pl-s1\">oldA</span> <span class=\"pl-c1\">=</span> <span class=\"pl-s1\">a</span><span\
  \ class=\"pl-kos\">;</span>\n            <span class=\"pl-s1\">oldX</span> <span\
  \ class=\"pl-c1\">=</span> <span class=\"pl-s1\">x</span><span class=\"pl-kos\"\
  >;</span>\n            <span class=\"pl-s1\">oldY</span> <span class=\"pl-c1\">=</span>\
  \ <span class=\"pl-s1\">y</span><span class=\"pl-kos\">;</span>\n\n            <span\
  \ class=\"pl-s1\">Runtime</span><span class=\"pl-kos\">.</span><span class=\"pl-en\"\
  >Yield</span><span class=\"pl-kos\">(</span><span class=\"pl-kos\">)</span><span\
  \ class=\"pl-kos\">;</span>\n        <span class=\"pl-kos\">}</span>\n    <span\
  \ class=\"pl-kos\">}</span>\n<span class=\"pl-kos\">}</span></pre></div>"
updated: '2026-06-06T07:32:37Z'
version: v1.7.3
version_title: ReSharp3DS Runtime & SDK - v1.7.3-beta.6
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

