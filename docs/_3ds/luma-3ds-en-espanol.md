---
author: López Tutoriales
avatar: https://avatars.githubusercontent.com/u/5817696?v=4
categories:
- firm
- luma3ds
color: '#ada491'
color_bg: '#80796b'
created: '2021-05-15T18:53:42Z'
description: '"Firmware personalizado" (N)3DS a prueba de novatos'
download_page: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases
downloads:
  Luma3DSv10.3ESP.rar:
    size: 343836
    size_str: 335 KiB
    url: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases/download/v10.3/Luma3DSv10.3ESP.rar
  boot.firm:
    size: 226816
    url: https://www.dropbox.com/s/wr4hpebjz215avm/boot.firm?dl=1
github: LopezTutoriales/Luma3DS-Spanish
icon_index: 209
image: https://avatars.githubusercontent.com/u/5817696?v=4
image_length: 151760
layout: app
license: gpl-3.0
license_name: GNU General Public License v3.0
source: https://github.com/LopezTutoriales/Luma3DS-Spanish
systems:
- 3DS
title: Luma 3DS En Español
update_notes: '<ul dir="auto">

  <li>Agregue un porcentaje de batería más detallado, además del voltaje y la temperatura
  de la batería</li>

  <li>Agregue una opción para volcar el firmware DSP desde el menú de inicio, lo que
  hace que programas como DSP1 queden obsoletos.</li>

  <li>NTP dividido y anulación de compensación de tiempo de usuario. Esto significa
  dos cosas:

  <ul dir="auto">

  <li>Los cambios de hora son inmediatamente visibles y no necesita reiniciar su consola
  después de usar la función (aunque es posible que el menú de inicio no siempre muestre
  inmediatamente la nueva hora, solo abra y cierre una aplicación en ese caso)</li>

  <li>Programas como ctr-no-timeoffset ya no deberían ser necesarios. Además, incluso
  si 3ds.hacks.guide lo recomienda y GodMode9 lo ordena, no se debe realizar la anulación
  de compensación de tiempo.</li>

  </ul>

  </li>

  <li>También mejore la precisión de la implementación del cliente NTP y corrija algunos
  errores. Puede tener una precisión de +- 1 ms (generalmente), aunque parte de esta
  precisión se pierde al reiniciar</li>

  <li>No inicialice las pantallas en el caso muy común de que el usuario tenga solo
  una carga útil en la carpeta /luma/payloads, solucionando un error de larga data.</li>

  <li>Se corrigió la lectura del sector 0 de emuNAND para RedNAND y emuNAND estilo
  Gateway (<a class="issue-link js-issue-link" data-error-text="Failed to load title"
  data-id="1036563625" data-permission-text="Title is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1687"
  data-hovercard-type="pull_request" data-hovercard-url="/LumaTeam/Luma3DS/pull/1687/hovercard"
  href="https://github.com/LumaTeam/Luma3DS/pull/1687">LumaTeam#1687</a>, <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/aspargas2/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aspargas2">@aspargas2</a>)</li>

  <li>Solucione algunos errores en el sistema de trucos (# 1623, @ s5bug)</li>

  <li>Agregar Vista ASCII a la Lista de Procesos de Rosalina (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1091294296" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1703" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1703/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1703">LumaTeam#1703</a>,
  <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/George-lewis/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/George-lewis">@George-lewis</a>)</li>

  <li>Permitir el uso de parches de juegos en el menú de inicio (n.º 1634, <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/gabe565/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/gabe565">@gabe565</a>)</li>

  <li>Espere a que el usuario suelte la tecla B al salir del menú de Rosalina. Esto
  debería evitar que los juegos piensen que se presionó la tecla B (<a class="issue-link
  js-issue-link" data-error-text="Failed to load title" data-id="1087351954" data-permission-text="Title
  is private" data-url="https://github.com/LumaTeam/Luma3DS/issues/1701" data-hovercard-type="pull_request"
  data-hovercard-url="/LumaTeam/Luma3DS/pull/1701/hovercard" href="https://github.com/LumaTeam/Luma3DS/pull/1701">LumaTeam#1701</a>,
  sugerencia de <a class="user-mention notranslate" data-hovercard-type="user" data-hovercard-url="/users/Epicpkmn11/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/Epicpkmn11">@Epicpkmn11</a>)</li>

  <li>gdb: manejar correctamente los puntos de interrupción del software</li>

  <li>Mejoras generales en la estabilidad del sistema para mejorar la experiencia
  del usuario</li>

  <li>Traducido totalmente a español por López Tutoriales</li>

  </ul>'
updated: '2022-04-29T20:01:47Z'
version: v10.3
version_title: v10.3 en Español
---
Luma3DS es un programa para parchear el software del sistema de las (nuevas) consolas portátiles Nintendo (2) 3DS "sobre la marcha", agregando funciones como configuraciones de idioma por juego, capacidades de depuración para desarrolladores y eliminando restricciones impuestas por Nintendo como el bloqueo de la región.

También le permite ejecutar contenido no autorizado ("homebrew") eliminando los controles de firma. Para usarlo, necesitará una consola capaz de ejecutar software homebrew en el procesador Arm9.

Desde la versión 8.0, Luma3DS tiene su propio menú en el juego, que se puede activar con L + Abajo + Select.