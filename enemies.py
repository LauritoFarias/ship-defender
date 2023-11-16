import pygame
from config import *
from random import randint



bala = pygame.image.load(r"assets\Imagenes\bala.png")
rect_bala = bala.get_rect()
mask_bala = pygame.mask.from_surface(bala)
diccionario_bala = {"mask": mask_bala, "imagen": bala, "rect": rect_bala}

cannonball = pygame.image.load(r"assets\Imagenes\cannonball.png")
rect_cannonball = cannonball.get_rect()
mask_cannonball = pygame.mask.from_surface(cannonball)
diccionario_cannonball = {"mask": mask_cannonball, "imagen": cannonball, "rect": rect_cannonball}



def invocar_velero():
    bala = pygame.image.load(r"assets\Imagenes\bala.png")
    rect_bala = bala.get_rect()
    mask_bala = pygame.mask.from_surface(bala)
    diccionario_bala = {"mask": mask_bala, "imagen": bala, "rect": rect_bala}

    imagen_velero = pygame.image.load(r"assets\Imagenes\velero.png")
    imagen_velero = pygame.transform.scale(imagen_velero, (15, 55))
    imagen_velero_rect = imagen_velero.get_rect()
    mask_velero = pygame.mask.from_surface(imagen_velero)

    diccionario_velero = {"tipo": "velero", "mask": mask_velero, "imagen": imagen_velero, "rect": imagen_velero_rect, "disparo": diccionario_bala, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 1, "vidas": 1, "arrollable": True}

    return diccionario_velero



def invocar_barco():
    cannonball = pygame.image.load(r"assets\Imagenes\cannonball.png")
    rect_cannonball = cannonball.get_rect()
    mask_cannonball = pygame.mask.from_surface(cannonball)
    diccionario_cannonball = {"mask": mask_cannonball, "imagen": cannonball, "rect": rect_cannonball}

    imagen_barco = pygame.image.load(r"assets\Imagenes\barco.png")
    imagen_barco = pygame.transform.scale(imagen_barco, (50, 75))
    imagen_barco_rect = imagen_barco.get_rect()
    mask_barco = pygame.mask.from_surface(imagen_barco)

    diccionario_barco = {"tipo": "barco", "mask": mask_barco, "imagen": imagen_barco, "rect": imagen_barco_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(),  "velocidad_movimiento": 2, "vidas": 1, "arrollable": False}

    return diccionario_barco



def invocar_fragata():
    cannonball = pygame.image.load(r"assets\Imagenes\cannonball.png")
    rect_cannonball = cannonball.get_rect()
    mask_cannonball = pygame.mask.from_surface(cannonball)
    diccionario_cannonball = {"mask": mask_cannonball, "imagen": cannonball, "rect": rect_cannonball}

    imagen_fragata = pygame.image.load(r"assets\Imagenes\fragata.png")
    imagen_fragata = pygame.transform.scale(imagen_fragata, (60, 100))
    imagen_fragata_rect = imagen_fragata.get_rect()
    mask_fragata = pygame.mask.from_surface(imagen_fragata)

    diccionario_fragata = {"tipo": "fragata", "mask": mask_fragata, "imagen": imagen_fragata, "rect": imagen_fragata_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 2, "vidas": 1, "arrollable": False}

    return diccionario_fragata



def invocar_lancha():
    bala = pygame.image.load(r"assets\Imagenes\bala.png")
    rect_bala = bala.get_rect()
    mask_bala = pygame.mask.from_surface(bala)
    diccionario_bala = {"mask": mask_bala, "imagen": bala, "rect": rect_bala}

    imagen_lancha = pygame.image.load(r"assets\Imagenes\lancha.png")
    imagen_lancha = pygame.transform.scale(imagen_lancha, (20, 50))
    imagen_lancha_rect = imagen_lancha.get_rect()
    mask_lancha = pygame.mask.from_surface(imagen_lancha)

    diccionario_lancha = {"tipo": "lancha", "mask": mask_lancha, "imagen": imagen_lancha, "rect": imagen_lancha_rect, "disparo": diccionario_bala,  "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 3, "vidas": 2, "arrollable": False}

    return diccionario_lancha



def invocar_portaaviones():
    cannonball = pygame.image.load(r"assets\Imagenes\bala.png")
    rect_cannonball = cannonball.get_rect()
    mask_cannonball = pygame.mask.from_surface(cannonball)
    diccionario_cannonball = {"mask": mask_cannonball, "imagen": cannonball, "rect": rect_cannonball}

    imagen_portaaviones = pygame.image.load(r"assets\Imagenes\portaaviones.png")
    imagen_portaaviones = pygame.transform.scale(imagen_portaaviones, (70, 120))
    imagen_portaaviones_rect = imagen_portaaviones.get_rect()
    mask_portaaviones = pygame.mask.from_surface(imagen_portaaviones)

    diccionario_portaaviones = {"tipo": "portaaviones", "mask": mask_portaaviones, "imagen": imagen_portaaviones, "rect": imagen_portaaviones_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 1, "vidas": 3, "arrollable": False}

    return diccionario_portaaviones