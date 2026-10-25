---
author: Tristán Álvarez
avatar: https://avatars.githubusercontent.com/u/76444200?v=4
categories:
- utility
color: '#701515'
color_bg: '#701515'
created: '2025-03-16T17:58:10Z'
description: Editor de texto para 3Ds. | Text Editor for 3DS
download_page: https://github.com/Tristanabs/bandolero3ds/releases
downloads:
  Bandolero3DS-next-2.3dsx:
    size: 1790984
    size_str: 1 MiB
    url: https://github.com/Tristanabs/bandolero3ds/releases/download/2.3.1_NX2/Bandolero3DS-next-2.3dsx
  Bandolero3DS-next-2.cia:
    size: 1799104
    size_str: 1 MiB
    url: https://github.com/Tristanabs/bandolero3ds/releases/download/2.3.1_NX2/Bandolero3DS-next-2.cia
github: Tristanabs/bandolero3ds
icon: https://raw.githubusercontent.com/Tristanabs/bandolero3ds/refs/heads/main/icon.png
image: https://raw.githubusercontent.com/Tristanabs/bandolero3ds/refs/heads/main/icon.png
image_length: 2256
layout: app
license: mit
license_name: MIT License
llm_generation: unknown
qr:
  Bandolero3DS-next-2.cia: https://db.universal-team.net/assets/images/qr/bandolero3ds-next-2-cia.png
source: https://github.com/Tristanabs/bandolero3ds
stars: 5
systems:
- 3DS
title: Bandolero 3DS
unique_ids:
- '0x20000'
update_notes: '<h1 dir="auto">Registro de cambios</h1>

  <h2 dir="auto">2.3.1 (Citro2D) — 2026-10-16</h2>

  <p dir="auto">Esta versión moderniza la edición anterior y cambia la presentación
  principal a Citro2D/Citro3D.</p>

  <h3 dir="auto">Interfaz</h3>

  <ul dir="auto">

  <li>Nueva interfaz para las dos pantallas de Nintendo 3DS.</li>

  <li>Editor adaptado a la resolución de la consola con 15 líneas visibles.</li>

  <li>Selección de línea, barra de estado y menú de controles renovados.</li>

  <li>Pantalla de carga y sección “Acerca de” rediseñadas.</li>

  <li>Inclusión del icono, QR y logo de Flagwave Open Code.</li>

  <li>Versión y build visibles en “Acerca de”.</li>

  </ul>

  <h3 dir="auto">Archivos y persistencia</h3>

  <ul dir="auto">

  <li>Guardado y apertura en <code class="notranslate">sdmc:/3ds/bandolero/files/</code>,
  incluyendo navegación<br>

  por subcarpetas.</li>

  <li>Creación automática de <code class="notranslate">files/</code>, <code class="notranslate">extensions/</code>
  y <code class="notranslate">config.ini</code>.</li>

  <li>Persistencia del idioma y del número de arranques.</li>

  <li>Conservación de extensiones de archivo personalizadas.</li>

  </ul>

  <h3 dir="auto">Idiomas y texto</h3>

  <ul dir="auto">

  <li>Español, inglés, portugués, francés, alemán y japonés.</li>

  <li>Cambio de idioma desde “Acerca de” mediante <code class="notranslate">R/L</code>.</li>

  <li>Fuente RomFS con glifos latinos, símbolos, tildes, <code class="notranslate">Ñ</code>
  y japonés.</li>

  <li>Mejoras en el manejo de texto UTF-8.</li>

  <li>Comprobación automática de secuencias UTF-8 inválidas antes de dibujar.</li>

  <li>Renderizado visual de <code class="notranslate">**negrita**</code> y encabezados
  Markdown.</li>

  <li>Dedicatoria oculta desbloqueable mediante el código Konami.</li>

  <li>La pantalla de “Acerca de” muestra <code class="notranslate">R/L: IDIOMA</code>
  y <code class="notranslate">X: AVISOS .BAN3</code>.</li>

  <li>El logo de Flagwave Open Code se coloca en la esquina inferior derecha del<br>

  panel superior.</li>

  </ul>

  <h3 dir="auto">Extensiones y temas</h3>

  <ul dir="auto">

  <li>Lectura de manifiestos <code class="notranslate">.ban3</code> desde <code class="notranslate">sdmc:/3ds/bandolero/extensions/</code>.</li>

  <li>Aplicación de colores de tema desde manifiestos de datos.</li>

  <li>Lista de extensiones cargadas en “Acerca de”.</li>

  <li>Nuevo <a href="./extension-generator.html">generador web</a>.</li>

  <li>Las extensiones no ejecutan código nativo externo.</li>

  <li><code class="notranslate">extensions_enabled=0</code> en <code class="notranslate">config.ini</code>
  desactiva manualmente la carga de<br>

  extensiones; no existe un control equivalente dentro de la app.</li>

  <li><code class="notranslate">config.ini</code> registra actividad con entradas
  <code class="notranslate">log=</code> y purga automáticamente<br>

  los eventos de más de 30 días, incluyendo aperturas, nuevas extensiones y<br>

  actualizaciones de versión.</li>

  </ul>

  <h3 dir="auto">CIA y banner</h3>

  <ul dir="auto">

  <li>Metadatos de aplicación actualizados:

  <ul dir="auto">

  <li>Nombre: Bandolero 3DS.</li>

  <li>Descripción: Un editor de texto para 3DS - Version 2.3.1.</li>

  <li>Editor: Tristanabs.</li>

  <li>ProductCode: <code class="notranslate">CTR-P-BNDR</code>.</li>

  <li>UniqueId solicitado en el RSF: <code class="notranslate">000400000FF3FF00</code>.</li>

  </ul>

  </li>

  <li>CIA empaquetado pasando explícitamente el SMDH y <code class="notranslate">banner.bnr</code>
  a <code class="notranslate">makerom</code>.</li>

  <li>El SMDH contiene el nombre, descripción, autor e icono de Bandolero 3DS.</li>

  <li><code class="notranslate">banner.bnr</code> conserva la imagen y el audio originales
  del menú HOME.</li>

  </ul>

  <h3 dir="auto">Próxima versión — base implementada</h3>

  <ul dir="auto">

  <li>Editor reducido a 15 líneas visibles con desplazamiento y aviso visual cuando
  hay más contenido.</li>

  <li>Explorador de archivos para abrir documentos de <code class="notranslate">files/</code>
  con cruceta, botones y pantalla táctil.</li>

  <li>El menú inferior reconoce las zonas táctiles de sus acciones principales.</li>

  <li>Apertura y guardado compatibles con formatos de texto y código, incluidos<br>

  <code class="notranslate">.txt</code>, <code class="notranslate">.md</code>, <code
  class="notranslate">.json</code>, <code class="notranslate">.xml</code>, <code class="notranslate">.html</code>,
  <code class="notranslate">.css</code>, <code class="notranslate">.js</code>, <code
  class="notranslate">.c</code>, <code class="notranslate">.cpp</code>, <code class="notranslate">.py</code>,<br>

  <code class="notranslate">.rs</code>, <code class="notranslate">.go</code> y <code
  class="notranslate">.sql</code>.</li>

  <li>Previsualización Markdown básica para encabezados, énfasis y listas.</li>

  <li>Las extensiones siguen siendo manifiestos de datos sin ejecución de código nativo
  y aceptan descripción.</li>

  <li>Avisos persistentes de nuevas extensiones, con opción para desactivarlos desde
  “Acerca de”.</li>

  <li>Catálogo web con cinco temas <code class="notranslate">.ban3</code> descargables
  y personalizados.</li>

  <li>Sección “Acerca de” reorganizada en bloques de identidad, enlaces y ajustes,
  con QR más grande y controles agrupados.</li>

  <li>Se conservan sin cambios el banner, el icono y el audio del menú HOME.</li>

  </ul>

  <h2 dir="auto">Versión anterior</h2>

  <p dir="auto">La versión anterior estaba basada en la interfaz original de Notepad
  3DS y no incluía la nueva pantalla Citro2D, la persistencia de configuración, el
  sistema <code class="notranslate">.ban3</code>, los seis idiomas ni el generador
  web.</p>'
updated: '2026-10-16T21:18:06Z'
version: 2.3.1_NX2
version_title: BANDOLERO 3DS 2.3.1. "NEXT 2"
---
Bandolero 3DS is a text editor application for the Nintendo 3DS, developed by Tristanabs. Based on Notepad 3DS, it currently allows users to view text files and plans to introduce enhancements over the original Notepad 3DS in the future. Installation is straightforward: simply install the provided .cia file. For support, users can visit the Homebrew Central server. The project is open-source and licensed under the MIT License.