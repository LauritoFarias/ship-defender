import pygame
from math import cos, sin, radians

def disparar(imagen_disparo, centro, angulo_jugador, direccion, velocidad):
    """Invoca un disparo del jugador en dirección hacia adelante, derecha o izquierda.

    Args:
        imagen_disparo (Surface): imagen del disparo
        centro (tuple): centro del rectángulo jugador
        angulo_jugador (int): ángulo del jugador
        direccion (str): dirección relativa del disparo del jugador
        velocidad (int): velocidad del disparo

    Returns:
        dict: diccionario con las propiedades del disparo
    """

    angulo_jugador_radianes = radians(angulo_jugador - 90)

    offset_y = 20 * sin(angulo_jugador_radianes)
    
    if direccion == "forward":
        rect_disparo = pygame.Rect(centro[0] - 4, centro[1] + offset_y, 8, 8)
        angulo_disparo = mover_segun_angulo(angulo_jugador, velocidad)
    if direccion == "right":
        rect_disparo = pygame.Rect(centro[0] - 4, centro[1]- 4, 8, 8)
        angulo_disparo = mover_segun_angulo(angulo_jugador - 90, velocidad)
    if direccion == "left":    
        rect_disparo = pygame.Rect(centro[0] - 4, centro[1], 8, 8)
        angulo_disparo = mover_segun_angulo(angulo_jugador + 90, velocidad)

    mask_disparo = pygame.mask.from_surface(imagen_disparo)
    diccionario_disparo = {"imagen": imagen_disparo, "mask": mask_disparo, "rect": rect_disparo, "direccion": direccion, "angulo": angulo_disparo, "velocidad": velocidad}
    return diccionario_disparo



def mover_segun_angulo(angulo, velocidad):
    """Determina el vector de movimiento (x, y) del jugador según su ángulo.

    Args:
        angulo (int): ángulo del jugador
        velocidad (int): velocidad del jugador

    Returns:
        tuple: vector de movimiento
    """
    angulo_radianes = radians(angulo - 90)
    move_x = velocidad * cos(angulo_radianes)
    move_y = velocidad * sin(angulo_radianes)
    return -move_x, move_y
