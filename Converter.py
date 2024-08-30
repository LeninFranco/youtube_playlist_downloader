from moviepy.editor import AudioFileClip
import os

# Carpeta de destino con archivos .webm
folder = input("Ingrese el nombre de la carpeta con archivos .webm: ")

# Verifica que la carpeta existe
if not os.path.exists(folder):
    print(f"La carpeta '{folder}' no existe.")
    exit()

# Convierte todos los archivos .webm a .mp3
for filename in os.listdir(folder):
    if filename.endswith(".webm"):
        webm_path = os.path.join(folder, filename)
        mp3_path = os.path.join(folder, filename.rsplit(".", 1)[0] + ".mp3")

        print(f"Convirtiendo {filename} a MP3...")

        # Cargar el archivo de audio y convertirlo
        audio_clip = AudioFileClip(webm_path)
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()

        os.remove(webm_path)
        print(f"{filename} convertido a {mp3_path}.")

print("Conversión completada para todos los archivos .webm.")
