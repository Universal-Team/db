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
description: '"Firmware personalizado" (N)3DS a prueba de novatos'
download_page: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases
downloads:
  Luma3DSv12.0_ESP.zip:
    size: 405997
    size_str: 396 KiB
    url: https://github.com/LopezTutoriales/Luma3DS-Spanish/releases/download/v12.0/Luma3DSv12.0_ESP.zip
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

  <li>Se agregó un nuevo submenú de "configuración avanzada" para los filtros de pantalla,
  lo que permite una personalización mucho mayor (en particular, el aumento de gama).
  Permite configurar diferentes filtros para la pantalla superior e inferior por separado,
  y todas las configuraciones se pueden guardar en el archivo de configuración .ini</li>

  <li>Se implementó el arranque automático en el menú Homebrew, tanto en el modo 3DS
  como en el modo DSi:

  <ul dir="auto">

  <li>El modo DSi usa el TID de <a href="https://github.com/devkitPro/nds-hb-menu/releases/latest">bootstrap
  de nds-hb-menu</a> de forma predeterminada, y es un poco lento para comenzar, ya
  que primero debe pasar por el sistema operativo 3DS nativo</li>

  <li>Homebrew debe compilarse con libctru v2.0.0 como mínimo, y se recomienda encarecidamente
  libctru v2.1.2 para corregir errores</li>

  </ul>

  </li>

  <li>Se ha movido "Guardar configuración" al menú principal de Rosalina</li>

  <li>Se agregó la capacidad de forzar el enrutamiento de audio a los auriculares.
  Esto está dirigido a usuarios de mod de hardware Bluetooth

  <ul dir="auto">

  <li>Una limitación es que esta opción se deshace si inserta y luego quita los auriculares
  en el puerto de auriculares, cerrando y volviendo a abrir la tapa se soluciona este
  problema.</li>

  </ul>

  </li>

  <li>Se agregó la capacidad de redirigir los subprocesos de la aplicación core1 al
  core2, en N3DS:

  <ul dir="auto">

  <li>Solo es útil en juegos muy exigentes como Pokémon (Ultra) Sol/Luna, donde se
  obtiene aprox. una ganancia del 10%, debido a cómo funciona el sistema operativo
  3DS</li>

  <li>Podría romper algunos juegos y aplicaciones homebrew</li>

  </ul>

  </li>

  <li>Se agregó la carga de módulo de sistema externo *.cxi no-KIP (desde /luma/sysmodules),
  cuando la opción "Habilitar carga de FIRM y módulos externos" está habilitada

  <ul dir="auto">

  <li>El formato esperado es {IDTitulo}.cxi (no el nombre, a diferencia de los KIP),
  donde {IDTitulo} es una cadena de 16 dígitos hexadecimales y se tiene en cuenta
  el bit N3DS.</li>

  <li>La carga de code.bin para sysmodules todavía se mantiene como una función, pero
  ahora debe habilitar tanto esta opción como "Habilitar parcheo de juegos" (para
  módulos que no sean sys, con solo "Habilitar parcheo de juegos" es suficiente)</li>

  </ul>

  </li>

  <li>Se habilitaron las funciones de "parcheo de juegos" para todos los applets (no
  probados exhaustivamente), no solo para juegos o aplicaciones. Dicho esto, es posible
  que LayeredFs no funcione en cosas como el teclado del software, pero se espera
  que en la "emulación local" funcione siempre.</li>

  <li>Se eliminó la verificación del kernel para crear subprocesos en core2/core3.
  Esto no influye en que homebrew pueda acceder a core2, ya que siempre ha tenido
  los bits de acceso adecuados. Además, no debe crear subprocesos en core3, ya que
  el seguimiento del header consume la mayor parte del tiempo de la CPU y el controlador
  de gráficos depende del seguimiento del header.</li>

  <li>Se otorgó acceso completo a la RAM DSP a todos los homebrew 3dsx</li>

  <li>Se movió hb:ldr de Rosalina a la reimplementación del cargador</li>

  <li>Se agregó soporte PASLR deshabilitado por defecto en nuestra reimplementación
  de cargador personalizado; esto debería coincidir con lo que hace el sysmodule oficial
  1:1</li>

  <li>Se solucionó un error en el que un error que indicaba que la versión de firmware
  de MCU era demasiado baja, incluso si esto siempre era incorrecto</li>

  <li>Se solucionó un error de larga data en el que los módulos del sistema podrían
  eliminarse incorrectamente al usar la función "Cambiar Homebrew Launcher por esta
  app" seguida de cerrar la aplicación actual. Esto podría haber causado problemas
  con esta función y la aplicación Salud y Seguridad de New 3DS en el pasado</li>

  <li>Se muestran los mensajes de error correctos al quitar el cartucho o la tarjeta
  SD mientras juegas en cualquier medio, en lugar de un código de error crítico. También
  se agregó la información de fecha y hora a las entradas de errdisp.txt</li>

  <li>Mejoras generales en la estabilidad del sistema para mejorar la experiencia
  del usuario</li>

  </ul>'
updated: '2023-02-18T20:04:53Z'
version: v12.0
version_title: v12.0 en Español
---
Luma3DS es un programa para parchear el software del sistema de las (nuevas) consolas portátiles Nintendo (2) 3DS "sobre la marcha", agregando funciones como configuraciones de idioma por juego, capacidades de depuración para desarrolladores y eliminando restricciones impuestas por Nintendo como el bloqueo de la región.

También le permite ejecutar contenido no autorizado ("homebrew") eliminando los controles de firma. Para usarlo, necesitará una consola capaz de ejecutar software homebrew en el procesador Arm9.

Desde la versión 8.0, Luma3DS tiene su propio menú en el juego, que se puede activar con L + Abajo + Select.