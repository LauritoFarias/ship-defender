import pygame

def reproducir_musica_de_fondo(archivo_musica,volumen):
    pygame.mixer.music.stop()

    pygame.mixer.music.load(archivo_musica)

    pygame.mixer.music.set_volume(volumen)

    pygame.mixer.music.play()