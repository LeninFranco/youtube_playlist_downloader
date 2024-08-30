# YouTube Playlist Downloader and Converter

Este proyecto es una herramienta de consola en Python que permite descargar una playlist de YouTube en formato MP3. Utiliza `yt_dlp` para descargar los archivos de audio y `moviepy` para convertirlos de .webm a .mp3.

## Requisitos Previos

Antes de ejecutar el programa, asegúrate de tener instalados los siguientes paquetes de Python:

- `yt_dlp`
- `moviepy`

Puedes instalarlos utilizando `pip` con el archivo requeriments.txt

## Instrucciones
1. Abra su consola en la carpeta donde se encuentran los scripts.
2. Ejecuta el script Downloader.py donde te pedira el URL de la playlist (debe ser publico) y el nombre de la carpeta de destino.
3. Posterior a la descarga, debe ejecutar el segundo Script llamado Converter.py donde va a convertir los archivos descargados en .mp3. Le solicitará el nombre de la carpeta de destino.
4. Listo, disfrute su playlist en mp3 en una alta calidad sin necesidad de recurrir a sitios de descargar poco seguros.

## Casos especiales y excepciones
- URL Incorrecto: Asegúrate de que la URL de la playlist ingresada sea correcta. Si el video o playlist no se encuentra, el programa no descargará nada.
- Carpeta Incorrecta: Verifica que la carpeta de destino especificada para la conversión de archivos .webm exista. El script terminará con un mensaje de error si la carpeta no se encuentra.
- Formato de Archivos: El descargador guarda los archivos en formato .webm por defecto. Asegúrate de que los archivos en la carpeta de destino para la conversión tengan la extensión .webm.
- Playlist con videos ocultos: El script detecta todos los videos de la playlist junto a los videos ocultos y esto puede provocar un error en la descarga, asegurese de que la playlist no tenga videos ocultos.
- El script de descarga y el script de conversión deben ser ejecutados en la misma carpeta o especificar las rutas adecuadas.
- La conversión puede tardar algunos minutos dependiendo del número de archivos y su tamaño.
