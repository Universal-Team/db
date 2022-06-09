---
author: López Tutoriales
avatar: https://avatars.githubusercontent.com/u/5817696?v=4
categories:
- firm
- luma3ds
color: '#aea591'
color_bg: '#80796a'
created: '2021-05-15T18:53:42Z'
description: '"Firmware personalizado" (N)3DS a prueba de novatos'
download_page: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases
downloads:
  Luma3DSv11.0_ESP.zip:
    size: 390911
    size_str: 381 KiB
    url: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases/download/v11.0/Luma3DSv11.0_ESP.zip
github: LopezTutoriales/Luma3DS-Spanish
icon_index: 210
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

  <li>Migrar la configuración a formato INI (config.bin se convierte en config.ini)

  <ul dir="auto">

  <li>Esto significa que la configuración ahora es legible por humanos, y hace que
  situaciones como querer modificar el combo de Rosalina sin abrir su menú sean mucho
  más fáciles de resolver.</li>

  <li>Las siguientes opciones se han eliminado del menú de configuración y se han
  movido para que estén exclusivamente en el archivo INI:

  <ul dir="auto">

  <li>"Duración de pantalla de splash": esto se debe a que ahora se puede configurar
  para tomar cualquier valor de 32 bits (predeterminado: 3 segundos)</li>

  <li>"Establecer modo desarrollador UNITINFO",</li>

  <li>"Deshabilitar los controladores de excepciones Arm11"</li>

  <li>"Habilitar Rosalina en SAFE_FIRM"</li>

  </ul>

  </li>

  <li>"Mostrar NAND o texto personalizado en configuración del sistema" ahora está
  habilitado de forma predeterminada, cuando se genera automáticamente un archivo
  de configuración en blanco</li>

  </ul>

  </li>

  <li>Los archivos esenciales del sistema (bootROM, OTP, HWCAL, LCFS, SecureInfo)
  ahora se respaldan automáticamente en /luma/backups (al actualizar Luma3DS, si aún
  no están presentes en esa ubicación)</li>

  <li>Al actualizar Luma3DS, boot.firm ahora se copia automáticamente a la raíz de
  la partición CTRNAND</li>

  <li>Restaure el soporte remoto extendido (esto se rompió con versiones recientes
  de GDB). Cambio importante: use adjuntar &lt;PID+1&gt; (por ejemplo, 1 para fs)
  para adjuntar a un proceso, ya que GDB no admite PID 0.</li>

  <li>Agregar opción para alternar la ranura de la tarjeta (# 1202)</li>

  <li>Los filtros de pantalla ahora se pueden guardar en config.ini y restaurar en
  el arranque (debe ir a "Opciones Misceláneas &gt; Guardar configuración"). Ahora
  incluso puede editar manualmente config.ini para usar valores personalizados para
  esos (dentro del rango de 1000 a 25100K)</li>

  <li>La zona horaria NTP ahora también se puede guardar en config.ini; también corrige
  un error en el que algunas zonas horarias no serían accesibles</li>

  <li>Solucione un problema de larga data en el que algunas llamadas al sistema demoraron
  más de lo debido, lo que provocó retrasos en algunas situaciones (gracias <a class="user-mention
  notranslate" data-hovercard-type="user" data-hovercard-url="/users/PabloMK7/hovercard"
  data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/PabloMK7">@PabloMK7</a>)</li>

  <li>Arreglar el cálculo del voltaje de la batería que se muestra (gracias nocash)</li>

  <li>Traducido totalmente al español</li>

  </ul>'
updated: '2022-06-07T21:51:15Z'
version: v11.0
version_title: v11.0 en Español
---
Luma3DS es un programa para parchear el software del sistema de las (nuevas) consolas portátiles Nintendo (2) 3DS "sobre la marcha", agregando funciones como configuraciones de idioma por juego, capacidades de depuración para desarrolladores y eliminando restricciones impuestas por Nintendo como el bloqueo de la región.

También le permite ejecutar contenido no autorizado ("homebrew") eliminando los controles de firma. Para usarlo, necesitará una consola capaz de ejecutar software homebrew en el procesador Arm9.

Desde la versión 8.0, Luma3DS tiene su propio menú en el juego, que se puede activar con L + Abajo + Select.