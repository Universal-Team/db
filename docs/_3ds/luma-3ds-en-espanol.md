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
description: '"Custom Firmware" para Nintendo 3DS'
download_page: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases
downloads:
  Luma3DSv13.1.1_ESP.zip:
    size: 538114
    size_str: 525 KiB
    url: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases/download/v13.1.1/Luma3DSv13.1.1_ESP.zip
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

  <li>Corregido error el cual la opción de conexión inalámbrica reemplazaba la anulación
  del botón físico de volumen</li>

  <li>Forzar conexión wifi: ahora se manejan correctamente las ranuras wifi no configuradas</li>

  <li>Pequeños cambios en el cargador de plugins</li>

  </ul>

  <hr>

  <p dir="auto"><strong>Registro de cambios de v13.1:</strong></p>

  <ul dir="auto">

  <li>Agregada funcion de activar/desactivar control de volumen fisico

  <ul dir="auto">

  <li>Actualmente, esta opción se encuentra en "Configuración del sistema" en el menú
  de Rosalina y se guarda automáticamente, mientras se encuentra en el apartado [misc]
  del archivo config.ini. Esto se debe a que esta opción solo es compatible con NATIVE_FIRM.
  Esto puede cambiar en el futuro.</li>

  </ul>

  </li>

  <li>Agregada la entrada "Iniciar cargador de payloads" encima de "Guardar y salir"
  en el menú de configuración de Luma</li>

  <li>Eliminada la opción no utilizada e inútil "Permitir combos Izq+Der / Arr+Aba
  para DSi"</li>

  <li>Ocultada la opción "Usar filtros de mejora personal para DSi"</li>

  <li>Solucionado un problema por el cual baremetal screeninit generaba dos pantallas
  blancas o colores incorrectos, generalmente al iniciar payloads de Arm9</li>

  <li>Rosalina: muestra el SSID en el menú de "Controlar conexión wifi"</li>

  <li>LayeredFS: mejora de detección del punto de montaje RomFS en la actualización
  del juego</li>

  <li>Se han realizado más mejoras en la estabilidad general del sistema y otros ajustes
  menores para mejorar la experiencia del usuario</li>

  </ul>

  <p dir="auto">Además, gracias a <a class="user-mention notranslate" data-hovercard-type="organization"
  data-hovercard-url="/orgs/devkitPro/hovercard" data-octo-click="hovercard-link-click"
  data-octo-dimensions="link_type:self" href="https://github.com/devkitPro">@devkitPro</a>,
  esta versión de Luma3DS incluye la versión 2.4.3 del Homebrew Launcher, que a su
  vez incluye el archivo config/ssl/cacert.pem para usarlo con libcurl.</p>'
updated: '2024-05-19T20:29:03Z'
version: v13.1.1
version_title: v13.1.1 en Español
---
Luma3DS es un programa para parchear el software del sistema de las (nuevas) consolas portátiles Nintendo (2) 3DS "sobre la marcha", agregando funciones como configuraciones de idioma por juego, capacidades de depuración para desarrolladores y eliminando restricciones impuestas por Nintendo como el bloqueo de la región.

También le permite ejecutar contenido no autorizado ("homebrew") eliminando los controles de firma. Para usarlo, necesitará una consola capaz de ejecutar software homebrew en el procesador Arm9.

Desde la versión 8.0, Luma3DS tiene su propio menú en el juego, que se puede activar con L + Abajo + Select.