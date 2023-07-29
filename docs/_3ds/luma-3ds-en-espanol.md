---
author: López Tutoriales
avatar: https://avatars.githubusercontent.com/u/5817696?v=4
categories:
- firm
- luma3ds
- translation
color: '#aea591'
color_bg: '#80796a'
created: '2021-05-15T18:53:42Z'
description: '"Firmware personalizado" para (N)3DS a prueba de novatos'
download_page: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases
downloads:
  Luma3DSv13.0.1_ESP.zip:
    size: 420641
    size_str: 410 KiB
    url: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases/download/v13.0.1/Luma3DSv13.0.1_ESP.zip
github: LopezTutoriales/Luma3DS-Spanish
image: https://avatars.githubusercontent.com/u/5817696?v=4&size=128
image_length: 26161
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LopezTutoriales/Luma3DS-Spanish
systems:
- 3DS
title: Luma 3DS En Español
update_notes: '<ul dir="auto">

  <li>Corregido error de la versión v13.0 donde se interrumpió la carga del modulo
  de FIRM externo (como TwlBg) que estaba roto</li>

  </ul>

  <p dir="auto"><strong>v13.0 registro de cambios:</strong></p>

  <ul dir="auto">

  <li>Se fusionó <a href="https://github.com/PabloMK7/Luma3DS_3GX">la bifurcación
  de @PabloMK7 y @Nanquitas</a>, agregando la compatibilidad con el uso de plugins.
  Esto permite reproducir mods como CTGP-7

  <ul dir="auto">

  <li>NOTA: Debido a los cambios planificados (como la reimplementación del kernel),
  los plugins más antiguos que ya no se actualizan o los de código cerrado pueden
  dejar de funcionar repentinamente en algún momento en el futuro. Recomendamos utilizar
  plugins de código abierto y/o actualizados activamente de fuentes confiables en
  su lugar.</li>

  </ul>

  </li>

  <li><strong>Se agregó soporte para reemplazar el filtro de escalado basado en convolución
  predeterminado en TWL_FIRM (es decir, software DS(i)) por el contenido de <code
  class="notranslate">/luma/twl_upscaling_filter.bin</code></strong>

  <ul dir="auto">

  <li>Puede encontrar ejemplos de matriz <a href="https://github.com/DullPointer/TWPatch_a/blob/master/soos/krnlist_all.h#L192">aquí</a>
  y el código Python para convertirlos al formato esperado <a href="https://github.com/LumaTeam/Luma3DS/blob/master/arm9/source/patches.c#L774">aquí</a>.</li>

  </ul>

  </li>

  <li>Se agregó soporte para permitir combinaciones de teclas Izquierda+Derecha y
  Arriba+Abajo en TWL_FIRM, aunque los juegos comerciales de DS(i) generalmente evitan
  estas combinaciones por sí solos.</li>

  <li>Se agregó soporte para TWL_FIRM y AGB_FIRM de tamaño arbitrario y sin comprimir,
  cuando se cargan externamente desde la carpeta <code class="notranslate">/luma</code>.</li>

  <li>Se simplifico la carga de CXI de sysmodule y la aplicación de parches IPS/BPS:
  el bit N3DS ahora se borra al considerar desde qué archivo CXI cargar desde <code
  class="notranslate">/luma/sysmodules</code>. La ruta de los parches IPS/BPS para
  sysmodules, y solo sysmodules, se ha movido a <code class="notranslate">/luma/sysmodules/&lt;IDTitulo
  sin bit N3DS&gt;</code> (resp. <code class="notranslate">.bps</code>). Este es un
  cambio radical.</li>

  <li>Se eliminó la opción "Usar FIRM EmuNAND si se inicia con R" y toda la lógica
  relacionada. Este fue un remanente de la era Gateway que no tiene cabida en 2023.</li>

  <li>Se corrigió un error raro en el que la consola arrancaba con 2 pantallas blancas.</li>

  <li>Otros cambios menores.</li>

  </ul>'
updated: '2023-07-29T12:15:11Z'
version: v13.0.1
version_title: v13.0.1 en Español
---
Luma3DS es un programa para parchear el software del sistema de las (nuevas) consolas portátiles Nintendo (2) 3DS "sobre la marcha", agregando funciones como configuraciones de idioma por juego, capacidades de depuración para desarrolladores y eliminando restricciones impuestas por Nintendo como el bloqueo de la región.

También le permite ejecutar contenido no autorizado ("homebrew") eliminando los controles de firma. Para usarlo, necesitará una consola capaz de ejecutar software homebrew en el procesador Arm9.

Desde la versión 8.0, Luma3DS tiene su propio menú en el juego, que se puede activar con L + Abajo + Select.