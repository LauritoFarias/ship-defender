import pygame
from enemies import *
from random import randint, randrange



def invocar_velero():
    bala = pygame.image.load(r"assets\Imagenes\bala.png")
    rect_bala = bala.get_rect()
    mask_bala = pygame.mask.from_surface(bala)
    diccionario_bala = {"mask": mask_bala, "imagen": bala, "rect": rect_bala}

    imagen_velero = pygame.image.load(r"assets\Imagenes\velero.png")
    imagen_velero = pygame.transform.scale(imagen_velero, (15, 55))
    imagen_velero_rect = imagen_velero.get_rect()
    mask_velero = pygame.mask.from_surface(imagen_velero)

    diccionario_velero = {"tipo": "velero", "mask": mask_velero, "imagen": imagen_velero, "rect": imagen_velero_rect, "disparo": diccionario_bala, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 1, "velocidad_disparo": 4, "vidas": 1, "arrollable": True, "hit": False}

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

    diccionario_barco = {"tipo": "barco", "mask": mask_barco, "imagen": imagen_barco, "rect": imagen_barco_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(),  "velocidad_movimiento": 2, "velocidad_disparo": 6, "vidas": 1, "arrollable": False, "hit": False}

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

    diccionario_fragata = {"tipo": "fragata", "mask": mask_fragata, "imagen": imagen_fragata, "rect": imagen_fragata_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 1, "velocidad_disparo": 8, "vidas": 2, "arrollable": False, "hit": False}

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

    diccionario_lancha = {"tipo": "lancha", "mask": mask_lancha, "imagen": imagen_lancha, "rect": imagen_lancha_rect, "disparo": diccionario_bala,  "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 3, "velocidad_disparo": 20, "vidas": 1, "arrollable": False, "hit": False}

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

    diccionario_portaaviones = {"tipo": "portaaviones", "mask": mask_portaaviones, "imagen": imagen_portaaviones, "rect": imagen_portaaviones_rect, "disparo": diccionario_cannonball, "milisegundos": pygame.time.get_ticks(), "velocidad_movimiento": 1, "velocidad_disparo": 10, "vidas": 3, "arrollable": False, "hit": False}

    return diccionario_portaaviones



def invocar_enemigo(tipo_enemigo, x_invocacion):
    try:

        if tipo_enemigo == "velero":
            diccionario_enemigo = invocar_velero()
        if tipo_enemigo == "barco":
            diccionario_enemigo = invocar_barco()
        if tipo_enemigo == "fragata":
            diccionario_enemigo = invocar_fragata()
        if tipo_enemigo == "lancha":
            diccionario_enemigo = invocar_lancha()
        if tipo_enemigo == "portaaviones":
            diccionario_enemigo = invocar_portaaviones()
    
    except:
        print("No se ha detectado ningún tipo de enemigo")
    
    diccionario_enemigo["rect"].centerx = x_invocacion
    diccionario_enemigo["rect"].bottom = 0

    return diccionario_enemigo



def disparo_velero(player, enemigo):
    if player["rect"].centerx >= enemigo["rect"].centerx:
        enemigo["disparo"]["rect"].midleft = enemigo["rect"].midright
        direccion = 6
    elif player["rect"].centerx <= enemigo["rect"].centerx:
        enemigo["disparo"]["rect"].midright = enemigo["rect"].midleft
        direccion = 4
    else:
        enemigo["disparo"]["rect"].midtop = enemigo["rect"].midbottom
        direccion = 2
        
    diccionario_disparo_enemigo = {"mask": enemigo["disparo"]["mask"], "imagen": enemigo["disparo"]["imagen"], "rect": enemigo["disparo"]["rect"], "direccion": direccion}
    return diccionario_disparo_enemigo

    



def disparo_barco(player, enemigo, milisegundos):
    if (milisegundos - enemigo["milisegundos"]) % 3000 == 0:
        if player["rect"].centerx >= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midleft = enemigo["rect"].midright
            direccion = 6
        elif player["rect"].centerx <= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midright = enemigo["rect"].midleft
            direccion = 4
        else:
            enemigo["disparo"]["rect"].midtop = enemigo["rect"].midbottom
            direccion = 2
        
        diccionario_disparo_enemigo = {"mask": enemigo["disparo"]["mask"], "imagen": enemigo["disparo"]["imagen"], "rect": enemigo["disparo"]["rect"], "direccion": direccion}
        return diccionario_disparo_enemigo



def disparo_fragata(player, enemigo, milisegundos):
    if (milisegundos - enemigo["milisegundos"]) % 2000 == 0:
        if player["rect"].centerx >= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midleft = enemigo["rect"].midright
            direccion = 6
        elif player["rect"].centerx <= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midright = enemigo["rect"].midleft
            direccion = 4
        else:
            enemigo["disparo"]["rect"].midtop = enemigo["rect"].midbottom
            direccion = 2
        
        diccionario_disparo_enemigo = {"mask": enemigo["disparo"]["mask"], "imagen": enemigo["disparo"]["imagen"], "rect": enemigo["disparo"]["rect"], "direccion": direccion}
        return diccionario_disparo_enemigo



def disparo_lancha(player, enemigo, milisegundos):
    if (milisegundos - enemigo["milisegundos"]) % 1000 == 0:
        if player["rect"].centerx >= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midleft = enemigo["rect"].midright
            direccion = 6
        elif player["rect"].centerx <= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midright = enemigo["rect"].midleft
            direccion = 4
        else:
            enemigo["disparo"]["rect"].midtop = enemigo["rect"].midbottom
            direccion = 2
        
        diccionario_disparo_enemigo = {"mask": enemigo["disparo"]["mask"], "imagen": enemigo["disparo"]["imagen"], "rect": enemigo["disparo"]["rect"], "direccion": direccion}
        return diccionario_disparo_enemigo



def disparo_portaaviones(player, enemigo, milisegundos):
    if (milisegundos - enemigo["milisegundos"]) % 1000 == 0:
        if player["rect"].centerx >= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midleft = enemigo["rect"].midright
            direccion = 6
        elif player["rect"].centerx <= enemigo["rect"].centerx:
            enemigo["disparo"]["rect"].midright = enemigo["rect"].midleft
            direccion = 4
        else:
            enemigo["disparo"]["rect"].midtop = enemigo["rect"].midbottom
            direccion = 2
        
        diccionario_disparo_enemigo = {"mask": enemigo["disparo"]["mask"], "imagen": enemigo["disparo"]["imagen"], "rect": enemigo["disparo"]["rect"], "direccion": direccion}
        return diccionario_disparo_enemigo
    


def crear_disparo_al_jugador(enemigo_disparo:dict, imagen_disparo, posicion, direccion:int, velocidad_disparo:int):
    if enemigo_disparo == "bala":
        tipo = "bala"
        if direccion == 6:
            imagen_disparo = pygame.transform.rotate(imagen_disparo, 180)
            rect_disparo = pygame.Rect(posicion[0], posicion[1] - 5, 6, 10)
        elif direccion == 4:
            rect_disparo = pygame.Rect(posicion[0], posicion[1] - 10, 6, 10)
        elif direccion == 2:
            rect_disparo = pygame.Rect(posicion[0], posicion[1] + 50, 6, 10)
    else:
        tipo = "cannonball"
        if direccion == 6:
            imagen_disparo = pygame.transform.rotate(imagen_disparo, 180)
            rect_disparo = pygame.Rect(posicion[0], posicion[1] - 8, 15, 15)
        elif direccion == 4:
            rect_disparo = pygame.Rect(posicion[0], posicion[1] - 15, 15, 15)
        elif direccion == 2:
            rect_disparo = pygame.Rect(posicion[0], posicion[1] + 50, 15, 15)

    mask_disparo = pygame.mask.from_surface(imagen_disparo)
    diccionario_disparo = {"tipo": tipo, "imagen": imagen_disparo, "mask": mask_disparo, "rect": rect_disparo, "direccion": direccion, "velocidad_disparo": velocidad_disparo}
    return diccionario_disparo



def disparar_al_jugador(player, enemigo, milisegundos, disparos_enemigos, sonido_bala, sonido_cannon_shot):
    tipo_enemigo = enemigo["tipo"]

    if tipo_enemigo == "velero":
        temporizador = 3000
    elif tipo_enemigo == "lancha":
        temporizador = 1000
    else:
        temporizador = 2000

    if (milisegundos - enemigo["milisegundos"]) >= temporizador:
        if player["rect"].centerx >= enemigo["rect"].centerx:
            posicion_salida_disparo = enemigo["rect"].midright
            direccion = 6
        elif player["rect"].centerx <= enemigo["rect"].centerx:
            posicion_salida_disparo = enemigo["rect"].midleft
            direccion = 4
        else:
            posicion_salida_disparo = enemigo["rect"].midbottom
            direccion = 2

        if tipo_enemigo == "barco" or tipo_enemigo == "fragata":
            tipo_disparo = "cannonball"
        else:
            tipo_disparo = "bala"

        disparo_enemigo = crear_disparo_al_jugador(tipo_disparo, enemigo["disparo"]["imagen"], posicion_salida_disparo, direccion, enemigo["velocidad_disparo"])

        disparos_enemigos.append(disparo_enemigo)

        if tipo_disparo == "bala":
            sonido_bala.play()
        else:
            sonido_cannon_shot.play()

        enemigo["milisegundos"] = milisegundos
    