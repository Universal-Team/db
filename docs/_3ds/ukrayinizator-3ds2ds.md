---
author: Max Bolhar
avatar: https://avatars.githubusercontent.com/u/38209425?v=4
categories:
- utility
color: '#828c8a'
color_bg: '#76807e'
created: '2026-07-30T15:37:14Z'
description: Українська мова для системного інтерфейсу Nintendo 3DS/2DS.
download_page: https://github.com/BolgarMaxym97/3ds-ua/releases
downloads:
  3ds-ua-from-en-2.0.0-new3ds.zip:
    size: 24122022
    size_str: 23 MiB
    url: https://github.com/BolgarMaxym97/3ds-ua/releases/download/v2.0.0/3ds-ua-from-en-2.0.0-new3ds.zip
  3ds-ua-from-en-2.0.0-old3ds.zip:
    size: 22274872
    size_str: 21 MiB
    url: https://github.com/BolgarMaxym97/3ds-ua/releases/download/v2.0.0/3ds-ua-from-en-2.0.0-old3ds.zip
  3ds-ua-from-ru-2.0.0-new3ds.zip:
    size: 24393156
    size_str: 23 MiB
    url: https://github.com/BolgarMaxym97/3ds-ua/releases/download/v2.0.0/3ds-ua-from-ru-2.0.0-new3ds.zip
  3ds-ua-from-ru-2.0.0-old3ds.zip:
    size: 22585332
    size_str: 21 MiB
    url: https://github.com/BolgarMaxym97/3ds-ua/releases/download/v2.0.0/3ds-ua-from-ru-2.0.0-old3ds.zip
  3ds-ua-installer-2.0.0.cia:
    size: 32752576
    size_str: 31 MiB
    url: https://github.com/BolgarMaxym97/3ds-ua/releases/download/v2.0.0/3ds-ua-installer-2.0.0.cia
github: BolgarMaxym97/3ds-ua
icon: https://raw.githubusercontent.com/BolgarMaxym97/3ds-ua/main/assets/unistore-icon.png
image: https://raw.githubusercontent.com/BolgarMaxym97/3ds-ua/main/assets/unistore-icon.png
image_length: 2095
layout: app
license: other
license_name: Other
llm_generation: 'yes'
preinstall_message: 'Потрібна Luma3DS з увімкненим Enable game patching.

  Після встановлення перемкніть мову консолі:

  Налаштування системи -> Iнші налаштування -> Мова,

  і перезапустіть консоль.


  Видалення перепитує про кожну папку - їх до 32.

  Universal-Updater інакше теки видаляти не вміє.'
qr:
  3ds-ua-installer-2.0.0.cia: https://db.universal-team.net/assets/images/qr/3ds-ua-installer-2-0-0-cia.png
source: https://github.com/BolgarMaxym97/3ds-ua
stars: 6
systems:
- 3DS
title: Українізатор 3DS/2DS
update_notes: '<h1 dir="auto">Українізатор 3DS/2DS 2.0.0 🇺🇦</h1>

  <p dir="auto"><strong>Українська мова для Nintendo 3DS.</strong> Українська стає
  на місце однієї з мов консолі, і система починає говорити українською. Решта мов
  лишається на місці.</p>

  <p dir="auto"><strong>Тепер це застосунок.</strong> «Українізатор 3DS» встановлюється
  на консоль, як звичайна програма, і робить усе сам: вибирає файли для вашої консолі,
  вмикає потрібне в Luma, додає в системний шрифт справжні літери <strong>і ї є ґ</strong>
  і перезавантажує консоль. Мову консолі міняти не треба. Оновлення, зміна мови й
  видалення — у тому ж застосунку, одним натиском.</p>

  <p dir="auto">Системні файли консолі не змінюються — усе живе на SD-карті, разом
  зі шрифтом.</p>

  <markdown-accessiblity-table><table role="table">

  <thead>

  <tr>

  <th>Файл</th>

  <th>Що це</th>

  </tr>

  </thead>

  <tbody>

  <tr>

  <td><code class="notranslate">3ds-ua-installer-2.0.0.cia</code></td>

  <td><strong>застосунок — беріть його.</strong> Один на всі консолі: 3DS, 3DS XL,
  2DS, New 3DS, New 3DS XL, New 2DS XL</td>

  </tr>

  <tr>

  <td><code class="notranslate">3ds-ua-from-ru-2.0.0-old3ds.zip</code></td>

  <td>ручне встановлення: замість російської, 3DS / 3DS XL / 2DS</td>

  </tr>

  <tr>

  <td><code class="notranslate">3ds-ua-from-ru-2.0.0-new3ds.zip</code></td>

  <td>ручне встановлення: замість російської, <strong>New</strong> 3DS / New 3DS XL
  / New 2DS XL</td>

  </tr>

  <tr>

  <td><code class="notranslate">3ds-ua-from-en-2.0.0-old3ds.zip</code></td>

  <td>ручне встановлення: замість англійської, 3DS / 3DS XL / 2DS</td>

  </tr>

  <tr>

  <td><code class="notranslate">3ds-ua-from-en-2.0.0-new3ds.zip</code></td>

  <td>ручне встановлення: замість англійської, <strong>New</strong> 3DS / New 3DS
  XL / New 2DS XL</td>

  </tr>

  </tbody>

  </table></markdown-accessiblity-table>

  <p dir="auto">Архіви — для тих, хто ставить файли на картку руками. Справжніх літер
  у них немає, а мову й Luma треба налаштовувати самому.</p>

  <hr>

  <h2 dir="auto">Що нового після 1.12.0</h2>

  <p dir="auto"><strong>Застосунок «Українізатор 3DS» замість скриптів Universal-Updater.</strong></p>

  <ul dir="auto">

  <li><strong>Справжні і ї є ґ і апостроф</strong> у всій системі й на клавіатурі.
  Застосунок будує шрифт на самій консолі з її власного, а консоль читає його з SD-карти
  — у NAND нічого не пишеться. Потрібна Luma3DS v13.0 або новіша; на старішій лишаються
  замінники.</li>

  <li><strong>Мову консолі більше міняти не треба.</strong> Українська вмикається
  лише для перекладених програм, ігри лишаються мовою системи.</li>

  <li><strong>Enable game patching застосунок вмикає сам.</strong></li>

  <li><strong>Встановлення переживає вимкнення живлення.</strong> Сіла батарея посеред
  роботи — після ввімкнення застосунок продовжить з того самого місця.</li>

  <li><strong>Стоїть українізатор від Universal-Updater чи з архіву?</strong> Ставте
  застосунок поверх і натисніть «Оновити»: він підхопить наявні файли, видаляти нічого
  не треба.</li>

  <li><strong>Анонімна статистика.</strong> Після встановлення, оновлення, видалення
  чи помилки застосунок надсилає короткий звіт без особистих даних — лише з Wi-Fi
  і лише з галочкою на екрані «Допомога», яку можна зняти. Що саме в ньому — <a href="https://github.com/BolgarMaxym97/3ds-ua#%D0%B0%D0%BD%D0%BE%D0%BD%D1%96%D0%BC%D0%BD%D0%B0-%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0">у
  README</a>.</li>

  <li>Налаштування системи: кнопка «Перенесення даних» переносилася на два рядки —
  тепер «Перенос даних».</li>

  </ul>

  <h2 dir="auto">Що вже українською</h2>

  <p dir="auto"><strong>32 частини системи:</strong> Меню HOME (разом з назвами додатків
  під іконками й банерами на верхньому екрані) · Налаштування системи (разом з назвами
  програм у <strong>Керуванні даними</strong>) · Mii Maker · Журнал дій · Електронний
  посібник · Гра по завантаженню · екранна клавіатура з українською розкладкою · Список
  друзів · Камера Nintendo 3DS · швидка камера на <code class="notranslate">L</code>+<code
  class="notranslate">R</code> · Звук Nintendo 3DS · Здоров''я і безпека · Площа StreetPass
  Mii · Вибір Mii · Сповіщення (разом з вбудованими підказками) · Ігрові записи ·
  екран помилки · Інтернет-браузер · Nintendo eShop · аплет покупок і оновлень eShop
  · Перенесення даних · Оглядач Nintendo Zone · Face Raiders · AR Games · Налаштування
  amiibo · 3DS Memo · аплет Circle Pad Pro · Miiverse · публікація в Miiverse · Дані
  Nintendo Network ID · тексти системних помилок — усі 259 повідомлень під «Код помилки:
  XXX-YYYY».</p>

  <p dir="auto"><strong>На New 3DS до цього додаються її власні версії</strong> Інтернет-браузера
  (інтерфейс, вбудована клавіатура, назва додатка, окремий довідник) і Здоров''я і
  безпеки (переглядач і сам документ).</p>

  <p dir="auto"><strong>Дванадцять електронних довідників</strong> — тих, що відкриваються
  кнопкою «Посібник» у меню HOME: Інтернет-браузера, Налаштувань системи, Журналу
  дій, Гри по завантаженню, Камери, Звуку, Mii Maker, Площі StreetPass Mii, Nintendo
  eShop, Face Raiders, AR Games та Інтернет-браузера New 3DS.</p>

  <p dir="auto"><strong>Країни й регіони.</strong> У налаштуваннях профілю та на Карті
  StreetPass перекладено всі 67 країн і всі 724 їхні області. України в списку немає:
  у таблиці кодів країн Nintendo її немає взагалі, а код <code class="notranslate">100</code>
  — це <code class="notranslate">росія (болота)</code>. Мова й країна в 3DS не пов''язані,
  тож інтерфейс лишиться українським з будь-якою країною в профілі.</p>

  <hr>

  <h2 dir="auto">Що потрібно</h2>

  <ul dir="auto">

  <li>Nintendo 3DS / 2DS / New 3DS <strong>європейського (EUR) регіону</strong></li>

  <li>встановлена <strong>Luma3DS v10.3 або новіша</strong>; для справжніх літер —
  <strong>v13.0 або новіша</strong> (краще найновіша)</li>

  <li>SD-карта з 40 МБ вільного місця</li>

  <li>заряджена батарея або зарядка — застосунок не почне на низькому заряді</li>

  </ul>

  <p dir="auto">Немає Luma3DS? Спершу пройдіть <a href="https://3ds.hacks.guide/"
  rel="nofollow">3ds.hacks.guide</a> — без неї мод не працює.</p>

  <p dir="auto">Консолі <strong>USA та JPN</strong> європейських мовних слотів не
  мають узагалі, тож для них потрібна окрема збірка. Напишіть в Issues, якщо вона
  вам потрібна.</p>

  <h2 dir="auto">Встановлення</h2>

  <p dir="auto"><strong>1. Поставте застосунок.</strong> Найпростіше — через Universal-Updater,
  він уже є в його основному магазині Universal-DB:</p>

  <ol dir="auto">

  <li>Відкрийте Universal-Updater і знайдіть <strong>Українізатор 3DS/2DS</strong>
  — лупою в лівій панелі, введіть «Українізатор».</li>

  <li>Відкрийте другу іконку згори — «Доступні для завантаження» — і виберіть <code
  class="notranslate">3ds-ua-installer-2.0.0.cia</code>.</li>

  <li>Дочекайтеся, поки запис зникне з черги (третя іконка).</li>

  </ol>

  <p dir="auto">Без Universal-Updater: скопіюйте <code class="notranslate">3ds-ua-installer-2.0.0.cia</code>
  на SD-карту й встановіть його через FBI.</p>

  <p dir="auto"><strong>2. Відкрийте «Українізатор 3DS»</strong> у меню HOME. Застосунок
  перевірить консоль: Luma, регіон, місце на картці й заряд.</p>

  <p dir="auto"><strong>3. Натисніть «Встановити»</strong> і виберіть, яку мову замінить
  українська: російську чи англійську. Змінити можна будь-коли потім, без перевстановлення.</p>

  <p dir="auto">Кілька хвилин консоль не вимикайте — кнопка HOME у цей час не працює.
  Потім консоль перезавантажиться сама й запуститься українською. Готово.</p>

  <p dir="auto"><strong>Оновлення.</strong> Коли вийде нова версія, на іконці <strong>Українізатор
  3DS/2DS</strong> в Universal-Updater з''явиться зелена стрілка. Встановіть новий
  CIA, відкрийте застосунок і натисніть «Оновити».</p>

  <p dir="auto"><strong>Додавали окремий магазин <code class="notranslate">3ds-ua.unistore</code>?</strong>
  Він теж ставить застосунок — пункт «Встановити застосунок».</p>

  <h3 dir="auto">Вручну, з архіву</h3>

  <p dir="auto">Виберіть архів: <code class="notranslate">from-ru</code>, якщо українська
  має стати на місце російської, або <code class="notranslate">from-en</code>, якщо
  на місце англійської; <code class="notranslate">-old3ds</code> для 3DS / 3DS XL
  / 2DS, <code class="notranslate">-new3ds</code> для New 3DS / New 3DS XL / New 2DS
  XL. Як відрізнити New: у неї є маленький сірий C-стик над кнопками A/B/X/Y і додаткові
  кнопки ZL/ZR згори.</p>

  <ol dir="auto">

  <li>Вимкніть консоль, вставте SD-карту в комп''ютер, розпакуйте архів і скопіюйте
  папку <code class="notranslate">luma</code> в корінь картки — туди, де вже є папка
  <code class="notranslate">luma</code>. Комп''ютер спитає, чи об''єднати папки —
  погодьтеся.</li>

  <li>Тримайте <strong>SELECT</strong> і увімкніть консоль. У синьому меню Luma позначте
  <strong><code class="notranslate">Enable game patching</code></strong> (кнопка <strong>A</strong>)
  і натисніть <strong>START</strong>.</li>

  <li><code class="notranslate">Налаштування системи</code> → <code class="notranslate">Інші
  налаштування</code> → <code class="notranslate">Мова</code> → <strong>Українська</strong>
  → <code class="notranslate">OK</code>. Це пункт, де раніше було «Русский» (у <code
  class="notranslate">from-en</code> — «English»).</li>

  </ol>

  <hr>

  <h2 dir="auto">Як повідомити про баг</h2>

  <p dir="auto">У репозиторії є два готові шаблони — <a href="https://github.com/BolgarMaxym97/3ds-ua/issues/new/choose">відкрийте
  Issue</a> і виберіть:</p>

  <ul dir="auto">

  <li><strong>Баг на консолі</strong> — щось крешить, не запускається, текст обрізаний
  чи накладений.</li>

  <li><strong>Кривий переклад</strong> — помилка в тексті, невдале формулювання, неузгоджений
  термін.</li>

  </ul>

  <p dir="auto">Шаблон сам спитає все потрібне, але коротко: <strong>застосунок чи
  архів (який саме), модель консолі, версія системи й Luma, який саме екран, і фото.</strong>
  Якщо ставили застосунком — додайте файл <code class="notranslate">3ds/3ds-ua-installer.log</code>
  з SD-карти.</p>

  <p dir="auto"><strong>Це не баг, репорт не потрібен:</strong></p>

  <ul dir="auto">

  <li><code class="notranslate">i ï ε г</code> замість <code class="notranslate">і
  ї є ґ</code> — встановлено з архіву, Luma старша за v13.0, або на картці вже є чужий
  патч модуля NS (тоді застосунок його не чіпає й лишає замінники).</li>

  <li>Технічні написи лишені як є: <code class="notranslate">OK</code>, <code class="notranslate">Miiverse</code>,
  <code class="notranslate">WPA2-PSK (AES)</code>, назви пошуковиків, формати дат,
  розкладки клавіш латиницею.</li>

  <li>Назви додатків у <strong>eShop, Перенесенні даних та Ігрових записах</strong>
  — лишаються мовою, місце якої зайняла українська.</li>

  <li><strong>Керування мікро-SD на New 3DS</strong> — не перекладено, цього титулу
  ще немає в дампах.</li>

  <li>Довідники решти додатків показують те саме, що й до мода.</li>

  </ul>

  <hr>

  <h2 dir="auto">Якщо щось пішло не так</h2>

  <p dir="auto"><strong>Консоль не запускається після встановлення.</strong> Вимкніть
  її, тримайте <strong>SELECT</strong> і увімкніть. У меню Luma зніміть галочку <strong><code
  class="notranslate">Enable loading external FIRMs and modules</code></strong> і
  натисніть <strong>START</strong>. Консоль запуститься з замінниками замість і ї
  є ґ; відкрийте застосунок — він сам усе виправить. Системні файли консолі не змінювалися.</p>

  <p dir="auto"><strong>Вимкнулося живлення посеред встановлення.</strong> Нічого
  не зламано: відкрийте застосунок, і він продовжить з того самого місця.</p>

  <p dir="auto"><strong>Застосунок пише, що Enable game patching вимкнено</strong>
  — ця галочка злітає після оновлення Luma. Натисніть «Увімкнути»; якщо такої кнопки
  немає (стара Luma) — застосунок покаже, як увімкнути її вручну.</p>

  <p dir="auto"><strong>Застосунок не починає: «Низький заряд»</strong> — підключіть
  зарядку, далі він піде сам.</p>

  <p dir="auto"><strong>Назви додатків українські, а кнопки Меню HOME («Помощь», «Запустить»)
  і статус-бар — ні</strong> — Luma старша за v10.3. Оновіть Luma за <a href="https://3ds.hacks.guide/updating-b9s"
  rel="nofollow">3ds.hacks.guide</a>.</p>

  <p dir="auto"><strong>Якийсь застосунок не відкривається, а на верхньому екрані
  текст помилки</strong> — у вас старіша версія цього застосунку. Видаліть із SD-карти
  його папку <code class="notranslate">luma/titles/&lt;номер&gt;</code> цілком і перезавантажте
  консоль; решта перекладу працюватиме далі. Номери папок — у <a href="https://github.com/BolgarMaxym97/3ds-ua/blob/main/docs/internals.md#%D1%89%D0%BE-%D0%B7%D0%B0-%D0%BF%D0%B0%D0%BF%D0%BA%D0%B8-%D0%B2-lumatitles">технічному
  описі</a>.</p>

  <p dir="auto"><strong>Порожні квадрати замість літер, обрізані чи накладені написи</strong>
  — це баг, надсилайте репорт із фото.</p>

  <hr>

  <h2 dir="auto">Як видалити</h2>

  <p dir="auto"><strong>Застосунком:</strong> відкрийте «Українізатор 3DS» → «Видалити».
  Застосунок прибере свої файли й шрифт, поверне файли інших модів, які довелося відкласти,
  вимкне завантаження зовнішніх модулів Luma, якщо вмикав його сам, і перезавантажить
  консоль. <code class="notranslate">Enable game patching</code> лишається: ним можуть
  користуватися інші моди. Сам застосунок лишиться в меню HOME; прибрати його можна
  в <code class="notranslate">Налаштування системи</code> → <code class="notranslate">Керування
  даними</code>.</p>

  <p dir="auto"><strong>Встановлено з архіву:</strong> видаліть папки мода з <code
  class="notranslate">luma/titles/</code> на SD-карті — усі вони перелічені в <a href="https://github.com/BolgarMaxym97/3ds-ua/blob/main/docs/internals.md#%D1%89%D0%BE-%D0%B7%D0%B0-%D0%BF%D0%B0%D0%BF%D0%BA%D0%B8-%D0%B2-lumatitles">таблиці</a>,
  — або поставте застосунок і натисніть «Видалити».</p>

  <p dir="auto"><strong>Один виняток — підказки у Сповіщеннях.</strong> Їх мод переписує
  в базі листів у NAND, бо іншого способу до них дістатися немає. Після видалення
  мода вони лишаться українськими — не зіпсованими, просто українськими. Нові листи
  мод не чіпає.</p>

  <hr>

  <p dir="auto">Повна документація, технічні подробиці й вихідний код: <a href="https://github.com/BolgarMaxym97/3ds-ua">https://github.com/BolgarMaxym97/3ds-ua</a></p>

  <p dir="auto">Ліцензія MIT. Файлів Nintendo в репозиторії немає. Проєкт неофіційний,
  з Nintendo не пов''язаний.</p>'
updated: '2026-10-23T10:04:23Z'
version: v2.0.0
version_title: v2.0.0
website: https://github.com/BolgarMaxym97/3ds-ua
---
Перекладає системний інтерфейс Nintendo 3DS, 3DS XL, 2DS, New 3DS, New 3DS XL і New 2DS XL українською: Меню HOME, Налаштування системи, Інтернет-браузер, eShop, Камеру, Звук, Mii Maker, Журнал дій, електронні довідники та решту системних застосунків.

Українська стає на місце російського або англійського мовного слота - який саме, питає під час установки. Потрібна Luma3DS з увімкненим Enable game patching і консоль європейського (EUR) регіону.

### Installation instructions

<div class="alert alert-info">These installation instructions have been automatically generated based on Universal-Updater's installation scripts</div>
<details class="alert alert-secondary"><summary>New 3DS / New 2DS XL - замість російської</summary>
<ol>
<li>Download <code>3ds-ua-from-ru-*-new3ds.zip</code></li>
<li>Extract the contents of <code>/luma/</code> from the zip to <code>/luma/</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>New 3DS / New 2DS XL - замість англійської</summary>
<ol>
<li>Download <code>3ds-ua-from-en-*-new3ds.zip</code></li>
<li>Extract the contents of <code>/luma/</code> from the zip to <code>/luma/</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>Old 3DS / Old 2DS - замість російської</summary>
<ol>
<li>Download <code>3ds-ua-from-ru-*-old3ds.zip</code></li>
<li>Extract the contents of <code>/luma/</code> from the zip to <code>/luma/</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>Old 3DS / Old 2DS - замість англійської</summary>
<ol>
<li>Download <code>3ds-ua-from-en-*-old3ds.zip</code></li>
<li>Extract the contents of <code>/luma/</code> from the zip to <code>/luma/</code> on your SD card</li>
</ol>
</details>

<details class="alert alert-secondary"><summary>Видалити українізатор</summary>
<ol>
</ol>
</details>

