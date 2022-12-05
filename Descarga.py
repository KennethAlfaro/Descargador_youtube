from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

folder = './musica_descargada'


# Cambiar la direccion de la playlist segun la deseada

playlist = Playlist(
    'https://www.youtube.com/playlist?list=PLxzN8WQX3_xPN8PgFRVekru4HPLCHdV2W')
playlist.video_urls

for url in playlist:
    YouTube(url).streams.first().download(folder)

#Busca los archivos en el formato asignado y los cambia por el deseado

formato_deseado = '.mp3'
Formato_actual = '3gpp'
for file in os.listdir(folder):
    if re.search(Formato_actual, file):
        mp4_path = os.path.join(folder, file)
        mp3_path = os.path.join(folder, os.path.splitext(file)[0]+formato_deseado)
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
