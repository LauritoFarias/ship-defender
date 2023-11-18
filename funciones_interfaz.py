import pygame
from pygame.locals import *
from sys import exit
from random import randint, randrange

def salir():
    """Termina la ejecución del luego.
    """
    pygame.quit()
    exit()



def dibujar_texto(surface, dir_fuente , text, color, size, x, y):
    """Dibuja un texto en la superficie y coordenadas deseadas.

    Args:
        surface (Surface): superficie a dibujar
        dir_fuente (str): directorio de la fuente
        text (str): texto a dibujar
        color (tuple): color de la fuente del texto
        size (tuple): tamaño de la fuente del texto
        x (int): coordenada x del texto
        y (int): coordenada y del texto
    
    Returns:
        None
    """
    font = pygame.font.Font(dir_fuente, size)
    text = font.render(text, True, color)
    rect_texto = text.get_rect(center = (x, y))
    surface.blit(text, rect_texto)



def dibujar_texto_en_rectangulo(surface, rect, dir_fuente, text, color, size):
    """Dibuja un texto respecto de un rectángulo.

    Args:
        surface (Surface): superficie a dibujar
        rect (Rect): rectángulo en el cual dibujar el texto
        dir_fuente (str): directorio de la fuente
        text (str): texto a dibujar
        color (tuple): color de la fuente
        size (tuple): tamaño de la fuente

    Returns:
        None
    """
    font = pygame.font.Font(dir_fuente, size)
    text = font.render(text, True, color)
    rect_texto = text.get_rect(center = rect.center)
    surface.blit(text, rect_texto)



def dibujar_texto_con_contorno(surface, estilo_titulo):
    """Dibuja un texto con un contorno.

    Args:
        surface (Surface): superficie a dibujar
        estilo_titulo (dict): diccionario con el estilo del texto
    
    Returns:
        None
    """
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] + estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] + estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] + estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] - estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] - estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] + estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] - estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] - estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_fuente"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"], estilo_titulo["rect_y"])
            


def invocar_menu_inicio(superficie, origen, estilo_interfaz, estilo_titulo, imagen_fondo, rect_botones, rect_ventana_opciones, centro_titulo_opciones, rect_ventana_salida, centro_titulo_ventana_salida, archivo_musica, volumen_musica, flags):
    """Invoca el menú de inicio.

    Args:
        superficie (Surface): superficie en la cual dibujar objetos
        origen (tuple): origen de la superficie
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        estilo_titulo (dict): diccionario con el estilo del título
        imagen_fondo (Surface): imagen de fondo del menú
        rect_botones (dict): diccionario con los rectángulos de cada botón
        rect_ventana_opciones (Rect): rectángulo de la ventana
        centro_titulo_opciones (tuple): centro del título
        rect_ventana_salida (Rect): rectángulo de la ventana de la confirmación de salida
        centro_titulo_ventana_salida (tuple): centro del título de la ventana de confirmación de salida
        archivo_musica (str): directorio de la música del menú
        volumen_musica (float): volumen de la música del menú
        flags (dict): diccionario de flags
    
    Returns:
        None
    """
    pygame.mixer.music.load(archivo_musica)

    pygame.mixer.music.set_volume(volumen_musica)

    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["comenzar"].collidepoint(event.pos):
                        return
                    elif rect_botones["opciones"].collidepoint(event.pos):
                        superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)
                        invocar_ventana_opciones(superficie, estilo_interfaz, rect_ventana_opciones, centro_titulo_opciones, rect_botones, flags, volumen_musica)
                    elif rect_botones["salir"].collidepoint(event.pos):
                        superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)
                        invocar_ventana_confirmar_salida(superficie, estilo_interfaz, rect_ventana_salida, centro_titulo_ventana_salida, rect_botones)

        superficie.blit(imagen_fondo, origen)

        dibujar_texto_con_contorno(superficie, estilo_titulo)

        crear_boton_con_contorno(estilo_interfaz, superficie, "Comenzar", rect_botones["comenzar"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "Opciones", rect_botones["opciones"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "Salir", rect_botones["salir"])

        pygame.display.flip()



def invocar_ventana_opciones(superficie, estilo_interfaz, rect_ventana, centro_texto, rect_botones, flags, volumen_musica):
    """Invoca la ventana de opciones.

    Args:
        superficie (Surface): superficie en la cual dibujar los objetos
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        centro_texto (tuple): centro del título
        rect_botones (dict): diccionario de los rectángulos de los botones
        flags (dict): diccionario de flags
        volumen_musica (float): volumen de la música
    
    Returns:
        None
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["silenciar_musica"].collidepoint(event.pos):
                        if flags["musica_on"]:
                            pygame.mixer.music.set_volume(0)
                            flags["musica_on"] = False
                            flags["musica_off"] = True
                        else:
                            pygame.mixer.music.set_volume(volumen_musica)
                            flags["musica_on"] = True
                            flags["musica_off"] = False
                    
                    if rect_botones["guardar"].collidepoint(event.pos):
                        return
        
        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, "Opciones")

        crear_boton_con_contorno(estilo_interfaz, superficie, "Silenciar música", rect_botones["silenciar_musica"])
        
        crear_boton_con_contorno(estilo_interfaz, superficie, "Guardar", rect_botones["guardar"])

        pygame.display.flip()



def invocar_ventana_confirmar_salida(superficie, estilo_interfaz, rect_ventana, centro_texto, rect_botones):
    """Invocar la ventana de confirmación de salida

    Args:
        superficie (Surface): superficie en la cual dibujar los objetos
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        centro_texto (tuple): centro del título
        rect_botones (dict): diccionario de los rectángulos de los botones
    
        Returns:
            None
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["si"].collidepoint(pygame.mouse.get_pos()):
                        salir()
                    if rect_botones["no"].collidepoint(pygame.mouse.get_pos()):
                        return

        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, "¿Estás seguro de que deseas salir?")

        crear_boton_con_contorno(estilo_interfaz, superficie, "Sí", rect_botones["si"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "No", rect_botones["no"])

        pygame.display.flip()


    
def crear_ventana(superficie, estilo_interfaz, rect_ventana, centro_texto, texto):
    """Invoca una ventana.

    Args:
        superficie (Surface): superficie en la cual invocar ventana
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        centro_texto (tuple): centro del título de la ventana
        texto (str): título de la ventana
    """
    pygame.draw.rect(superficie, estilo_interfaz["color_relleno_botones"], rect_ventana, border_radius = estilo_interfaz["radio_borde"])
    dibujar_texto(superficie, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"], centro_texto[0], centro_texto[1])



def crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, texto):
    """Crea una ventana con un contorno.

    Args:
        superficie (Surface): superficie en la cual invocar ventana
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        centro_texto (tuple): centro del título de la ventana
        texto (str): título de la ventana
    """
    crear_ventana(superficie, estilo_interfaz, rect_ventana, centro_texto, texto)
    pygame.draw.rect(superficie, estilo_interfaz["color_contorno"], rect_ventana, estilo_interfaz["ancho_contorno"], estilo_interfaz["radio_borde"])



def crear_boton(estilo_interfaz, surface, texto, rect_boton):
    """Crea un botón.

    Args:
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        surface (Surface): superficie en la cual dibujar el botón
        texto (str): texto del botón
        rect_boton (_type_): rectángulo del botón
    
    Return:
        None
    """
    
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface, estilo_interfaz["color_relleno_hover_botones"], rect_boton, border_radius = 5)
        dibujar_texto_en_rectangulo(surface, rect_boton, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"])
    else:
        pygame.draw.rect(surface, estilo_interfaz["color_relleno_botones"], rect_boton, border_radius = 5)
        dibujar_texto_en_rectangulo(surface, rect_boton, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"])



def crear_boton_con_contorno(estilo_interfaz, surface, texto, rect_boton):
    """Crea un botón con un contorno.

    Args:
        estilo_interfaz (dict): diccionario con el estilo de la interfaz
        surface (Surface): superficie en la cual dibujar el botón
        texto (str): texto del botón
        rect_boton (_type_): rectángulo del botón
    """
    crear_boton(estilo_interfaz, surface, texto, rect_boton)
    pygame.draw.rect(surface, estilo_interfaz["color_contorno"], rect_boton, estilo_interfaz["ancho_contorno"], 5)



def pausa(superficie, origen, estilo_interfaz, rect_botones, volumen_musica):
    """Pausa el juego.

    Args:
        superficie (Surface): superficie en la cual invocar el menú de pausa
        origen (tuple): origen del menú
        estilo_interfaz (dict): diccionario del estilo de la interfaz
        rect_botones (dict): diccionario de los rectángulos de los botones
        volumen_musica (float): volumen de la música durante el menú de pausa
    """
    superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)

    pygame.mixer.music.set_volume(0.1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
                if event.type == K_p:
                    return
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["comenzar"].collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.set_volume(volumen_musica)
                        return
        
        crear_boton_con_contorno(estilo_interfaz, superficie, "Continuar", rect_botones["comenzar"])

        pygame.display.flip()



def fin_del_juego(superficie, origen, estilo_interfaz, rect_ventana, centro_texto, texto, rect_botones, contador_enemigos_muertos, milisegundos, archivo_musica, volumen_musica, flags):
    """Termina el juego. Registra los puntajes de la partida e históricos e invoca el menú del final del juego.

    Args:
        superficie (Surface): superficie en la cual invocar el menú del final del juego
        origen (tuple): origen del menú
        estilo_interfaz (dict): diccionario del estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        centro_texto (tuple): centro del título de la ventana
        texto (str): título de la ventana
        rect_botones (dict): diccionario de los rectángulos de los botones
        contador_enemigos_muertos (dict): diccionario de contadores de enemigos destruidos
        milisegundos (int): milisegundos de duración de la partida
        archivo_musica (str): directorio de la música del menú
        volumen_musica (float): volumen de la música del menú
        flags (dict): diccionario con los flag para manejar las ocasiones de entrar o evitar las invocaciones de menúes

    Returns:
        dict: diccionario de flags actualizado
    """

    try:

        superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)

        pygame.mixer.music.load(archivo_musica)

        pygame.mixer.music.set_volume(volumen_musica)

        pygame.mixer.music.play(-1)

        diccionario_puntajes = contar_puntaje(contador_enemigos_muertos, milisegundos)

        archivo_estadisticas = "estadisticas.txt"
                
        guardar_puntajes(diccionario_puntajes, archivo_estadisticas)

        diccionario_estadisticas = cargar_estadisticas(archivo_estadisticas)
    
    except:

        print("No se pudo obtener las estadísticas del juego")
    
    
    while flags["fin"]:

        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["volver_menu"].collidepoint(event.pos):
                        flags["fin"] = False
                        flags["menu"] = True
                        return flags
                    if rect_botones["estadisticas"].collidepoint(event.pos):
                        flags["estadisticas"] = True
        
        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, texto)

        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por veleros: {diccionario_puntajes['puntaje_veleros']}", estilo_interfaz["color_fuente"], 24, 400, 180)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por barcos: {diccionario_puntajes['puntaje_barcos']}", estilo_interfaz["color_fuente"], 24, 400, 220)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por fragatas: {diccionario_puntajes['puntaje_fragatas']}", estilo_interfaz["color_fuente"], 24, 400, 260)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por lanchas: {diccionario_puntajes['puntaje_lanchas']}", estilo_interfaz["color_fuente"], 24, 400, 300)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por portaaviones: {diccionario_puntajes['puntaje_portaaviones']}", estilo_interfaz["color_fuente"], 24, 400, 340)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje por tiempo: {diccionario_puntajes['puntaje_tiempo']}", estilo_interfaz["color_fuente"], 24, 400, 380)
        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje total: {diccionario_puntajes['puntaje_total']}", estilo_interfaz["color_fuente"], 24, 400, 420)

        crear_boton_con_contorno(estilo_interfaz, superficie, "Volver al menu", rect_botones["volver_menu"])

        crear_boton_con_contorno(estilo_interfaz, superficie, "Estadisticas", rect_botones["estadisticas"])

        if flags["estadisticas"]:
            flags = estadisticas(superficie, estilo_interfaz, rect_ventana, diccionario_estadisticas, centro_texto, "Estadisticas", rect_botones, flags)

        pygame.display.flip()



def contar_puntaje(contador_enemigos_muertos, milisegundos):
    """Cuenta el puntaje de la partida.

    Args:
        contador_enemigos_muertos (dict): diccionario de contadores de enemigos destruidos
        milisegundos (int): milisegundos de duración de la partida

    Returns:
        dict: diccionario de los puntajes por ítem
    """

    puntaje_veleros = contador_enemigos_muertos["velero"] * 10

    puntaje_barcos = contador_enemigos_muertos["barco"] * 20

    puntaje_fragatas = contador_enemigos_muertos["fragata"] * 30

    puntaje_lanchas = contador_enemigos_muertos["lancha"] * 50

    puntaje_portaaviones = contador_enemigos_muertos["portaaviones"] * 50

    puntaje_tiempo = 0

    minutos_completos = milisegundos // 60000

    puntos_por_segundo = 1



    for _ in range(minutos_completos):
        puntaje_tiempo += puntos_por_segundo * 60
        puntos_por_segundo *= 2
        
    milisegundos_restantes = milisegundos % 60000

    segundos_restantes = milisegundos_restantes // 1000

    for segundo in range(segundos_restantes):
        puntaje_tiempo += segundo * puntos_por_segundo
        
    puntaje_total = puntaje_veleros + puntaje_barcos + puntaje_fragatas + puntaje_lanchas + puntaje_portaaviones + puntaje_tiempo



    diccionario_puntajes = {"puntaje_veleros": puntaje_veleros,
                                "puntaje_barcos": puntaje_barcos,
                                "puntaje_fragatas": puntaje_fragatas,
                                "puntaje_lanchas": puntaje_lanchas,
                                "puntaje_portaaviones": puntaje_portaaviones,
                                "puntaje_tiempo": puntaje_tiempo,
                                "puntaje_total": puntaje_total}

    return diccionario_puntajes



def guardar_puntajes(diccionario_puntajes, archivo_estadisticas):
    """Guarda los puntajes de la partida

    Args:
        diccionario_puntajes (dict): diccionario de los puntajes por ítem
        archivo_estadisticas (str): directorio del archivo de las estadísticas
    """
    try:

        with open(archivo_estadisticas, "a") as archivo:
            archivo.write(str(diccionario_puntajes["puntaje_total"]) + "\n")
    
    except:
        print("No se pudo guardar las puntaciones del archivo")




def cargar_estadisticas(archivo_estadisticas):
    """Carga las estadísticas de las puntuaciones

    Args:
        archivo_estadisticas (str): directorio del archivo de estadísticas

    Returns:
       dict: diccionario de estadísticas a mostrar
    """

    puntajes = []

    try:
        
        with open(archivo_estadisticas, "r") as file:
            for linea in file:
                puntaje = int(linea.strip())
                puntajes.append(puntaje)
    
    except:
        print("No se pudo leer las puntaciones del archivo")
        
    puntaje_maximo = None
        
    for puntaje in puntajes:
        if puntaje_maximo == None or puntaje >= puntaje_maximo:
            puntaje_maximo = puntaje
    
    diccionario_estadisticas = {"puntaje_maximo": puntaje_maximo}
    
    return diccionario_estadisticas



def estadisticas(superficie, estilo_interfaz, rect_ventana, diccionario_estadisticas, centro_texto, texto, rect_botones, flags):
    """Invoca la ventana de las estadísticas.

    Args:
        superficie (Surface): superficie en la cual invocar la ventana
        estilo_interfaz (dict): diccionario del estilo de la interfaz
        rect_ventana (Rect): rectángulo de la ventana
        diccionario_estadisticas (dict): diccionario de las estadísticas a mostrar
        centro_texto (tuple): centro del título de la ventana
        texto (str): título de la ventana
        rect_botones (dict): diccionario de los rectángulos de los botones
        flags (dict): diccionario con los flags para manejar las ocasiones de entrar o evitar las invocaciones de menúes

    Returns:
        dict: diccionario con los flags para manejar las ocasiones de entrar o evitar las invocaciones de menúes
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_botones["volver_estadisticas"].collidepoint(event.pos):
                        flags["estadisticas"] = False
                        return flags
    
        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, texto)

        dibujar_texto(superficie, estilo_interfaz["dir_fuente"], f"Puntaje maximo: {diccionario_estadisticas['puntaje_maximo']}", estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"], 400, 180)

        crear_boton_con_contorno(estilo_interfaz, superficie, "Volver", rect_botones["volver_estadisticas"])

        pygame.display.flip()