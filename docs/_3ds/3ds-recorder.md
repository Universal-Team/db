---
author: Max Bolhar
avatar: https://avatars.githubusercontent.com/u/38209425?v=4
categories:
- utility
color: '#4f4c55'
color_bg: '#4f4c55'
created: '2026-11-08T07:44:38Z'
description: Record games, the HOME Menu and apps on your 3DS
download_page: https://github.com/BolgarMaxym97/3ds-recorder/releases
downloads:
  3ds-recorder.3dsx:
    size: 8619624
    size_str: 8 MiB
    url: https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/3ds-recorder.3dsx
  3ds-recorder.cia:
    size: 8397760
    size_str: 8 MiB
    url: https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/3ds-recorder.cia
  help-support-1.7.0.png:
    size: 42156
    size_str: 41 KiB
    url: https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/help-support-1.7.0.png
  qr-v1.7.0.png:
    size: 954
    size_str: 954 Bytes
    url: https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/qr-v1.7.0.png
  update-1.7.0.png:
    size: 34996
    size_str: 34 KiB
    url: https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/update-1.7.0.png
github: BolgarMaxym97/3ds-recorder
icon: https://raw.githubusercontent.com/BolgarMaxym97/3ds-recorder/main/app/assets/icon.png
image: https://raw.githubusercontent.com/BolgarMaxym97/3ds-recorder/main/app/assets/banner.png
image_length: 6289
layout: app
license: mit
license_name: MIT License
llm_generation: 'yes'
qr:
  3ds-recorder.cia: https://db.universal-team.net/assets/images/qr/3ds-recorder-cia.png
screenshots:
- description: Download to a phone
  url: https://db.universal-team.net/assets/images/screenshots/3ds-recorder/download-to-a-phone.png
- description: Gallery
  url: https://db.universal-team.net/assets/images/screenshots/3ds-recorder/gallery.png
- description: Main screen
  url: https://db.universal-team.net/assets/images/screenshots/3ds-recorder/main-screen.png
- description: Settings
  url: https://db.universal-team.net/assets/images/screenshots/3ds-recorder/settings.png
source: https://github.com/BolgarMaxym97/3ds-recorder
stars: 129
systems:
- 3DS
title: 3DS Recorder
unique_ids:
- '0xB3DA3'
update_notes: '<p dir="auto"><strong>3DS Recorder 1.7.0 updates itself: from now on
  a new version installs from Settings, no PC and no FBI needed. It also fixes a crash
  when the console is turned off during a recording, and New 3DS games restarting
  the console after the app.</strong></p>

  <p dir="auto">Tested on an Old 3DS with Luma3DS 13.5: the update from inside the
  app (CIA, the module swapped and restarted, a dropped Wi-Fi connection, Cancel),
  power-off during a recording, Mario Kart 7 with a CTRPF plugin. The New 3DS fixes
  come from the statistics and your reports. If something goes wrong, please <a href="https://github.com/BolgarMaxym97/3ds-recorder/issues/new">open
  an issue</a> and attach the log (phone page → <strong>Log for the developer</strong>,
  or <code class="notranslate">/3ds/recorder/app.log</code> and <code class="notranslate">recorder.log</code>
  from the SD card).</p>

  <h2 dir="auto">What''s new since 1.6.0</h2>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Updates from the app</strong> (Settings → App → <strong>Updates</strong>).
  When the app opens with Wi-Fi it checks for a newer version; a dot on <strong>Settings</strong>
  shows one, with what is new in your language. <strong>Update</strong> downloads
  and installs it, <strong>Restart</strong> opens the new version, and the recorder
  restarts with it (the <code class="notranslate">.3dsx</code>: close it and open
  it again). A dropped connection goes on from where it stopped. Every update is signed
  by the developer and each file is checked before anything is installed. The check
  sends nothing about you or the console; switch <strong>Check Automatically</strong>
  off to check only when you press <strong>Check Now</strong>. Not while a recording
  runs.</p>

  <p dir="auto"><strong>This one last time, install 1.7.0 by hand</strong> (FBI, or
  the QR code below). Every version after it comes through the app.</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/update-1.7.0.png"><img
  src="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/update-1.7.0.png"
  width="600" alt="The Updates screen: a new version with what is new, downloading,
  updated and Restart" style="max-width: 100%;"></a>

  </li>

  <li>

  <p dir="auto"><strong>Fixed: the console crashed when turned off during a recording
  with Record Buttons on.</strong> The recording is kept, nothing is written to the
  card after the power button, and the next start recovers the file.</p>

  </li>

  <li>

  <p dir="auto"><strong>New 3DS: Smash Bros and CTGP-7 no longer restart the console
  when started after 3DS Recorder.</strong> In 1.6.0 the app sometimes still left
  the next game with the smaller memory.</p>

  </li>

  <li>

  <p dir="auto"><strong>Fixed: Mario Kart 7 crashing with a CTRPF plugin menu while
  recording.</strong> Which picture the menu shows is now read from the screen itself.</p>

  </li>

  <li>

  <p dir="auto"><strong>Fixed: a rare console crash right after the app was updated</strong>
  (the new recorder started before the old one had quite gone).</p>

  </li>

  <li>

  <p dir="auto"><strong>A recording started from Replay keeps full quality:</strong>
  it waits up to 1 s for HOME Menu to give memory back instead of starting in the
  light profile.</p>

  </li>

  <li>

  <p dir="auto"><strong>Help → Support the project:</strong> QR codes for Ko-fi and
  the Monobank jar. The links come from the project''s page, so they stay current
  without an app update; without Wi-Fi the topic is not shown. The Help list now scrolls,
  and the half-shown last row says there is more below.</p>

  </li>

  <li>

  <p dir="auto"><strong>Downloading to a phone is private:</strong> the QR address
  now has a random key, so someone else on the same Wi-Fi cannot fetch your recordings
  by guessing it. Just scan the code as before.</p>

  </li>

  <li>

  <p dir="auto"><strong>Luma''s "external FIRMs and modules" option off:</strong>
  the app opens a screen that says how to turn it on, instead of the error "(luma,
  FFFFFFFD)" (<a class="issue-link js-issue-link" data-error-text="Failed to load
  title" data-id="6434347233" data-permission-text="Title is private" data-url="https://github.com/BolgarMaxym97/3ds-recorder/issues/4"
  data-hovercard-type="issue" data-hovercard-url="/BolgarMaxym97/3ds-recorder/issues/4/hovercard"
  href="https://github.com/BolgarMaxym97/3ds-recorder/issues/4">#4</a>).</p>

  </li>

  <li>

  <p dir="auto"><strong>The Replay tile says which keys save a clip</strong> while
  Replay is off.</p>

  </li>

  <li>

  <p dir="auto"><strong>Deleting a recording while its MP4 is being made</strong>
  waits for the converter (up to 30 s) instead of "could not delete".</p>

  </li>

  <li>

  <p dir="auto"><strong>The <a href="https://bolgarmaxym97.github.io/3ds-recorder/"
  rel="nofollow">converter page</a> makes MP4s over 2 GB</strong> in Firefox (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="6550256178" data-permission-text="Title
  is private" data-url="https://github.com/BolgarMaxym97/3ds-recorder/issues/35" data-hovercard-type="issue"
  data-hovercard-url="/BolgarMaxym97/3ds-recorder/issues/35/hovercard" href="https://github.com/BolgarMaxym97/3ds-recorder/issues/35">#35</a>).</p>

  </li>

  <li>

  <p dir="auto">More useful logs: HOME presses, applets, system events and a stuck
  screen are in <code class="notranslate">app.log</code>.</p>

  </li>

  </ul>

  <p dir="auto">Recordings, settings and the PC converters from 1.6.0 all keep working.</p>

  <p dir="auto"><strong>Install:</strong> <code class="notranslate">3ds-recorder.cia</code>
  with FBI (or <code class="notranslate">3ds-recorder.3dsx</code> in <code class="notranslate">/3ds/</code>
  for the Homebrew Launcher). In the Luma menu (hold SELECT at power-on), turn on
  <strong>Enable loading external FIRMs and modules</strong> (and <strong>Enable game
  patching</strong> for Launch On Startup). Open 3DS Recorder; <strong>R + SELECT</strong>
  starts and stops a recording. To update from 1.6.0 or older, install over the old
  version and open the app once. Details: <a href="https://github.com/BolgarMaxym97/3ds-recorder#readme">README</a>.</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/qr-v1.7.0.png"><img
  src="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/qr-v1.7.0.png"
  width="160" alt="QR code: 3ds-recorder.cia 1.7.0" style="max-width: 100%;"></a></p>

  <p dir="auto"><strong>Support:</strong> 3DS Recorder is free and stays free. If
  it is useful to you, there is <a href="https://ko-fi.com/maksymbolhar" rel="nofollow">Ko-fi</a>
  and a <a href="https://send.monobank.ua/jar/9jJDGho7H8" rel="nofollow">Monobank
  jar</a>, now in the app too (Help → Support the project). A star, a bug report or
  a video made with it helps just as much.</p>

  <hr>

  <p dir="auto"><strong>3DS Recorder 1.7.0 оновлюється сам: відтепер нова версія встановлюється
  з Налаштувань, без комп''ютера і без FBI. А ще виправлено збій, коли консоль вимикали
  під час запису, і перезапуск New 3DS в іграх після додатка.</strong></p>

  <p dir="auto">Перевірено на Old 3DS з Luma3DS 13.5: оновлення з додатка (CIA, заміна
  й перезапуск модуля, обрив Wi-Fi, «Скасувати»), вимкнення консолі під час запису,
  Mario Kart 7 з плагіном CTRPF. Виправлення для New 3DS зроблено за статистикою і
  вашими звітами. Якщо щось пішло не так, будь ласка, <a href="https://github.com/BolgarMaxym97/3ds-recorder/issues/new">створіть
  issue</a> і додайте журнал (сторінка в телефоні → <strong>Журнал для розробника</strong>,
  або <code class="notranslate">/3ds/recorder/app.log</code> і <code class="notranslate">recorder.log</code>
  з SD-картки).</p>

  <h2 dir="auto">Що нового після 1.6.0</h2>

  <ul dir="auto">

  <li>

  <p dir="auto"><strong>Оновлення з додатка</strong> (Налаштування → Додаток → <strong>Оновлення</strong>).
  Коли додаток відкривається з Wi-Fi, він перевіряє, чи є новіша версія; крапка на
  <strong>Налаштуваннях</strong> показує її разом зі списком змін вашою мовою. <strong>Оновити</strong>
  завантажує і встановлює її, <strong>Перезапустити</strong> відкриває нову версію,
  і рекордер перезапускається разом із нею (<code class="notranslate">.3dsx</code>:
  закрийте і відкрийте його знову). Обірване з''єднання продовжується з того самого
  місця. Кожне оновлення підписане розробником, і кожен файл перевіряється до встановлення.
  Перевірка не передає нічого про вас чи консоль; вимкніть <strong>Перевіряти самостійно</strong>,
  щоб перевіряти лише кнопкою <strong>Перевірити</strong>. Не під час запису.</p>

  <p dir="auto"><strong>Востаннє встановіть 1.7.0 вручну</strong> (FBI або QR-код
  нижче). Усі наступні версії прийдуть через додаток.</p>

  <a target="_blank" rel="noopener noreferrer" href="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/update-1.7.0.png"><img
  src="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/update-1.7.0.png"
  width="600" alt="Екран оновлень: нова версія зі списком змін, завантаження, оновлено
  і Перезапустити" style="max-width: 100%;"></a>

  </li>

  <li>

  <p dir="auto"><strong>Виправлено: консоль падала, якщо її вимкнути під час запису
  з увімкненим «Записувати кнопки».</strong> Запис зберігається, після кнопки живлення
  на картку нічого не пишеться, а наступний запуск відновлює файл.</p>

  </li>

  <li>

  <p dir="auto"><strong>New 3DS: Smash Bros і CTGP-7 більше не перезапускають консоль,
  якщо їх запустити після 3DS Recorder.</strong> У 1.6.0 додаток іноді все ще лишав
  наступній грі меншу пам''ять.</p>

  </li>

  <li>

  <p dir="auto"><strong>Виправлено: Mario Kart 7 падала з меню плагіна CTRPF під час
  запису.</strong> Яку картинку показує меню, тепер видно з самого екрана.</p>

  </li>

  <li>

  <p dir="auto"><strong>Виправлено рідкісний збій консолі одразу після оновлення додатка</strong>
  (новий рекордер стартував, поки старий ще не зовсім завершився).</p>

  </li>

  <li>

  <p dir="auto"><strong>Запис, розпочатий із Повтору, зберігає повну якість:</strong>
  він чекає до 1 с, поки меню HOME віддасть пам''ять, а не стартує в легкому профілі.</p>

  </li>

  <li>

  <p dir="auto"><strong>Допомога → Підтримати проєкт:</strong> QR-коди для Ko-fi і
  банки Monobank. Посилання беруться зі сторінки проєкту, тож лишаються актуальними
  без оновлення додатка; без Wi-Fi розділ не показується. Список Допомоги тепер гортається,
  а напівпоказаний останній рядок підказує, що нижче є ще.</p>

  </li>

  <li>

  <p dir="auto"><strong>Завантаження на телефон приватне:</strong> в адресі з QR-коду
  тепер випадковий ключ, тож хтось інший у тій самій Wi-Fi мережі не забере ваші записи,
  вгадавши адресу. Просто скануйте код, як і раніше.</p>

  </li>

  <li>

  <p dir="auto"><strong>Опцію Luma «external FIRMs and modules» вимкнено:</strong>
  додаток відкриває екран, де сказано, як її увімкнути, замість помилки «(luma, FFFFFFFD)»
  (<a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="6434347233"
  data-permission-text="Title is private" data-url="https://github.com/BolgarMaxym97/3ds-recorder/issues/4"
  data-hovercard-type="issue" data-hovercard-url="/BolgarMaxym97/3ds-recorder/issues/4/hovercard"
  href="https://github.com/BolgarMaxym97/3ds-recorder/issues/4">#4</a>).</p>

  </li>

  <li>

  <p dir="auto"><strong>Плитка Повтору підказує, якими кнопками зберегти кліп,</strong>
  коли Повтор вимкнено.</p>

  </li>

  <li>

  <p dir="auto"><strong>Видалення запису, поки з нього робиться MP4,</strong> чекає
  на конвертер (до 30 с), а не каже «не вдалося видалити».</p>

  </li>

  <li>

  <p dir="auto"><strong><a href="https://bolgarmaxym97.github.io/3ds-recorder/" rel="nofollow">Сторінка
  конвертера</a> робить MP4 понад 2 ГБ</strong> у Firefox (<a class="issue-link js-issue-link"
  data-error-text="Failed to load title" data-id="6550256178" data-permission-text="Title
  is private" data-url="https://github.com/BolgarMaxym97/3ds-recorder/issues/35" data-hovercard-type="issue"
  data-hovercard-url="/BolgarMaxym97/3ds-recorder/issues/35/hovercard" href="https://github.com/BolgarMaxym97/3ds-recorder/issues/35">#35</a>).</p>

  </li>

  <li>

  <p dir="auto">Корисніші журнали: натискання HOME, аплети, системні події і завислий
  екран тепер є в <code class="notranslate">app.log</code>.</p>

  </li>

  </ul>

  <p dir="auto">Записи, налаштування і конвертери для ПК з 1.6.0 і далі працюють.</p>

  <p dir="auto"><strong>Встановлення:</strong> <code class="notranslate">3ds-recorder.cia</code>
  через FBI (або <code class="notranslate">3ds-recorder.3dsx</code> у <code class="notranslate">/3ds/</code>
  для Homebrew Launcher). У меню Luma (затисніть SELECT під час увімкнення) увімкніть
  <strong>Enable loading external FIRMs and modules</strong> (і <strong>Enable game
  patching</strong> для «Запуску з консоллю»). Відкрийте 3DS Recorder; <strong>R +
  SELECT</strong> починає і зупиняє запис. Щоб оновитися з 1.6.0 чи старішої, встановіть
  поверх старої версії і відкрийте додаток один раз. Подробиці: <a href="https://github.com/BolgarMaxym97/3ds-recorder/blob/main/README.uk.md">README</a>.</p>

  <p dir="auto"><a target="_blank" rel="noopener noreferrer" href="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/qr-v1.7.0.png"><img
  src="https://github.com/BolgarMaxym97/3ds-recorder/releases/download/v1.7.0/qr-v1.7.0.png"
  width="160" alt="QR-код: 3ds-recorder.cia 1.7.0" style="max-width: 100%;"></a></p>

  <p dir="auto"><strong>Підтримка:</strong> 3DS Recorder безкоштовний і таким лишиться.
  Якщо він вам знадобився, є <a href="https://ko-fi.com/maksymbolhar" rel="nofollow">Ko-fi</a>
  і <a href="https://send.monobank.ua/jar/9jJDGho7H8" rel="nofollow">банка Monobank</a>,
  тепер і в самому додатку (Допомога → Підтримати проєкт). Зірка, звіт про помилку
  чи відео, записане ним, допомагають не менше.</p>'
updated: '2026-11-23T20:23:14Z'
version: v1.7.0
version_title: 3DS Recorder 1.7.0
website: https://github.com/BolgarMaxym97/3ds-recorder
---
Records the whole console: both screens with game sound, in any game, the HOME Menu or a system app. Press a button combination to start and again to stop, and the video is saved to the SD card. No PC or capture card needed.

The console turns each recording into an MP4 by itself, and you can send it to your phone over Wi-Fi by scanning a QR code. Works on Old and New 3DS, including games that use extended memory on Old 3DS.

Requires Luma3DS. Beta: please report problems on GitHub with the log attached.