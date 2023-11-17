import pygame
from pygame.locals import *
from sys import exit
from random import randint, randrange

def salir():
    pygame.quit()
    exit()



def mostrar_texto(superficie, texto, fuente, coordenadas, color_fuente, color_fondo):
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenadas
    superficie.blit(sup_texto, rect_texto)



def dibujar_texto(surface, dir_fuente , text, color, size, x, y):
    font = pygame.font.Font(dir_fuente, size)
    text = font.render(text, True, color)
    rect_texto = text.get_rect(center = (x, y))
    surface.blit(text, rect_texto)



def dibujar_texto_en_rectangulo(surface, rect, dir_fuente, text, color, size):
    font = pygame.font.Font(dir_fuente, size)
    text = font.render(text, True, color)
    rect_texto = text.get_rect(center = rect.center)
    surface.blit(text, rect_texto)



def dibujar_texto_con_contorno(surface, estilo_titulo):
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] + estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] + estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] + estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] - estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] - estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] + estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_contorno"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"] - estilo_titulo["ancho_contorno"], estilo_titulo["rect_y"] - estilo_titulo["ancho_contorno"])
    dibujar_texto(surface, estilo_titulo["dir_fuente"], estilo_titulo["texto"], estilo_titulo["color_fuente"], estilo_titulo["tamanio_fuente"], estilo_titulo["rect_x"], estilo_titulo["rect_y"])
            


def invocar_menu_inicio(superficie, origen, estilo_interfaz, estilo_titulo, imagen_fondo, rect_botones, rect_ventana_opciones, centro_titulo_opciones, rect_ventana_salida, centro_titulo_ventana_salida, archivo_musica, volumen_musica):
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
                        invocar_ventana_opciones(superficie, estilo_interfaz, rect_ventana_opciones, centro_titulo_opciones, rect_botones["guardar"])
                    elif rect_botones["salir"].collidepoint(event.pos):
                        superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)
                        invocar_ventana_confirmar_salida(superficie, estilo_interfaz, rect_ventana_salida, centro_titulo_ventana_salida, rect_botones)

        superficie.blit(imagen_fondo, origen)

        dibujar_texto_con_contorno(superficie, estilo_titulo)

        crear_boton_con_contorno(estilo_interfaz, superficie, "Comenzar", rect_botones["comenzar"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "Opciones", rect_botones["opciones"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "Salir", rect_botones["salir"])

        pygame.display.flip()



def invocar_ventana_opciones(superficie, estilo_interfaz, rect_ventana, centro_texto, rect_guardar):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect_guardar.collidepoint(event.pos):
                        return
        
        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, "Opciones")
        
        crear_boton_con_contorno(estilo_interfaz, superficie, "Guardar", rect_guardar)

        pygame.display.flip()



def invocar_ventana_confirmar_salida(superficie, estilo_interfaz, rect_ventana, centro_texto, rect_botones):
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



def crear_slider(surface, color_slider, rect_slider, color_handle, default_value = 0):
    pygame.draw.rect(surface, color_slider, rect_slider, border_radius = 12)
    #value_rect_handle = default_value
    #relative_pos_rect_handle = rect_slider.width * value_rect_handle / 100
    center_handle_x = rect_slider.left
    pygame.draw.circle(surface, color_handle, (center_handle_x, rect_slider.centery), 10)
    #rect_handle = pygame.Rect(rect_slider.left - 5, rect_slider.top - 5)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect_slider.collidepoint(event.pos):
                    print("Hola mundo")
                    center_handle_x = pygame.mouse.get_pos()[0]
                    pygame.draw.circle(surface, color_handle, (center_handle_x, rect_slider.centery), 10)
    
    
                    



    
def crear_ventana(superficie, estilo_interfaz, rect_ventana, centro_texto, texto):
    pygame.draw.rect(superficie, estilo_interfaz["color_relleno_botones"], rect_ventana)
    dibujar_texto(superficie, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"], centro_texto[0], centro_texto[1])



def crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, texto):
    crear_ventana(superficie, estilo_interfaz, rect_ventana, centro_texto, texto)
    pygame.draw.rect(superficie, estilo_interfaz["color_contorno"], rect_ventana, estilo_interfaz["ancho_contorno"], estilo_interfaz["radio_borde"])



def crear_boton(estilo_interfaz, surface, texto, rect_boton):
    
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(surface, estilo_interfaz["color_relleno_hover_botones"], rect_boton, border_radius = 5)
        dibujar_texto_en_rectangulo(surface, rect_boton, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"])
    else:
        pygame.draw.rect(surface, estilo_interfaz["color_relleno_botones"], rect_boton, border_radius = 5)
        dibujar_texto_en_rectangulo(surface, rect_boton, estilo_interfaz["dir_fuente"], texto, estilo_interfaz["color_fuente"], estilo_interfaz["tamanio_fuente"])



def crear_boton_con_contorno(estilo_interfaz, surface, texto, rect_boton):
    crear_boton(estilo_interfaz, surface, texto, rect_boton)
    pygame.draw.rect(surface, estilo_interfaz["color_contorno"], rect_boton, estilo_interfaz["ancho_contorno"], 5)



def pausa(superficie, estilo_interfaz, rect_botones):
    in_pause = True
    while in_pause:
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
                    if rect_botones["opciones"].collidepoint(pygame.mouse.get_pos()):
                        invocar_ventana_opciones()
                    if rect_botones["volver_menu"].collidepoint(pygame.mouse.get_pos()):
                        return
        
        
        crear_boton_con_contorno(estilo_interfaz, superficie, "Opciones", rect_botones["opciones"])
        crear_boton_con_contorno(estilo_interfaz, superficie, "Volver al menu", rect_botones["volver_menu"])

        pygame.display.flip()



def fin_del_juego(superficie, origen, estilo_interfaz, rect_ventana, centro_texto, texto, rect_botones, diccionario_puntajes, archivo_musica, volumen_musica, flags_pantallas):
    superficie.blit(estilo_interfaz["oscurecer_pantalla"], origen)
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
                    if rect_botones["volver_menu"].collidepoint(event.pos):
                        flags_pantallas["fin"] = False
                        flags_pantallas["menu"] = True
                        return flags_pantallas
                    if rect_botones["estadisticas"].collidepoint(event.pos):
                        flags_pantallas["estadisticas"] = True
                        return flags_pantallas


        
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

        pygame.display.flip()



def estadisticas(superficie, estilo_interfaz, rect_ventana, diccionario_puntajes, centro_texto, texto, rect_botones, flags_pantallas):
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
                        flags_pantallas["estadisticas"] = False
                        return flags_pantallas
    
        crear_ventana_con_contorno(superficie, estilo_interfaz, rect_ventana, centro_texto, texto)

        crear_boton_con_contorno(estilo_interfaz, superficie, "Volver", rect_botones["volver_estadisticas"])

        pygame.display.flip()



def contar_puntaje(contador_enemigos_muertos, milisegundos):

    puntaje_veleros = contador_enemigos_muertos["velero"] * 10

    puntaje_barcos = contador_enemigos_muertos["barco"] * 20

    puntaje_fragatas = contador_enemigos_muertos["fragata"] * 30

    puntaje_lanchas = contador_enemigos_muertos["lancha"] * 50

    puntaje_portaaviones = contador_enemigos_muertos["portaaviones"] * 50

    puntaje_tiempo = 0

    minutos_completos = milisegundos // 60000

    puntos_por_segundo = 1



    for minuto in range(minutos_completos):
        puntaje_tiempo += minuto * puntos_por_segundo * 60
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
    
    diccionario_estadisticas = {}

    return diccionario_puntajes


def guardar_puntajes(diccionario_puntajes):
    print(diccionario_puntajes["puntaje_total"])
    estadisticas_txt = "estadisticas.txt"

    with open(estadisticas_txt, "a") as archivo:
        archivo.write(str(diccionario_puntajes["puntaje_total"]) + "\n")
