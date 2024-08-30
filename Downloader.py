import yt_dlp
import os

# URL de la playlist
playlist_url = input("Ingrese el URL de la playlist: ")

# Carpeta de destino
folder = input("Ingrese el nombre de la carpeta: ")
if not os.path.exists(folder):
    os.makedirs(folder)

# Opciones de descarga
ydl_opts = {
    'format': 'bestaudio/best',  # Descargar solo el mejor audio disponible
    'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),  # Guardar el archivo con el título del video
}

# Descargar la playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print(f"Proceso completado. Todos los archivos de audio se guardaron en la carpeta '{folder}'.")

