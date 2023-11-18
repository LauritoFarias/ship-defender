def fuera_de_pantalla(rect, screen_width, screen_height):
    """Determina si un objeto Rect está fuera de la pantalla

    Args:
        rect (Rect): rectángulo
        screen_width (_type_): ancho de la pantalla
        screen_height (_type_): alto_de_la_pantalla

    Returns:
        bool: "True" si está fuera de pantalla y "False" si se encuentra dentro de ésta.
    """
    if rect.right <= 0 or rect.left >= screen_width or rect.bottom <= 0 or rect.top >= screen_height:
        return True
    else:
        return False

def contar_nave_destruida(tipo_enemigo, diccionario_contadores):
    """Contar cada nave destruida por el jugador.

    Args:
        tipo_enemigo (str): tipo de enemigo
        diccionario_contadores (dict): diccionario de los contadores
    """
    tipo_enemigo = str(tipo_enemigo)
    diccionario_contadores[tipo_enemigo] += 1