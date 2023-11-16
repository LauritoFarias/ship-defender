def out_of_screen(rect, screen_width, screen_height):
    if rect.right <= 0 or rect.left >= screen_width or rect.bottom <= 0 or rect.top >= screen_height:
        return True
    else:
        return False

def contar_nave_destruida(tipo_enemigo, diccionario_contadores):
        tipo_enemigo = str(tipo_enemigo)
        diccionario_contadores[tipo_enemigo] += 1