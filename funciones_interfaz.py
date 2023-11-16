import pygame
from pygame.locals import *
from sys import exit
from random import randint, randrange
from config import *

def salir():
    pygame.quit()
    exit()



def define_block(imagen = None, width:int = 800, height:int = 600, left:int = 0, top:int = 0, rect_width:int = 50, rect_height:int = 50, color:tuple = (255, 255, 255), dir:int = 9, borde:int = 0, radio:int = -1)->dict:

    rect = pygame.Rect(left, top, rect_width, rect_height)
    
    if color != None:
        block = ({"imagen": imagen, "rect": rect, "color": color, "dir": dir, "borde": borde, "radio": radio})
    else:
        block = ({"imagen": imagen, "rect": rect, "dir": dir, "borde": borde, "radio": radio})


    return block



def punto_en_rectangulo(punto, rect)->bool:
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom



def mostrar_texto(superficie, texto, fuente, coordenadas, color_fuente, color_fondo):
    sup_texto = fuente.render(texto, True, color_fuente, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = coordenadas
    superficie.blit(sup_texto, rect_texto)



def wait_user():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
                return
            


def invocar_menu_inicio(rect_comenzar, rect_opciones, rect_salir):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == PRIMARY_MOUSE_BUTTON:
                    if rect_comenzar.collidepoint(event.pos):
                        return
                    elif rect_opciones.collidepoint(event.pos):
                        screen.blit(transparent_screen, origin)
                        invocar_ventana_opciones()
                    elif rect_salir.collidepoint(event.pos):
                        screen.blit(transparent_screen, origin)
                        invocar_ventana_confirmar_salida(rect_confirmar_salida, rect_si, rect_no)

        screen.blit(background_menu, origin)

        dibujar_texto_con_contorno(screen, archivo_fuente, titulo, title_fill_color, size_titulo, rect_titulo_x, rect_titulo_y, ancho_contorno, title_outline_color)

        crear_boton_con_contorno(screen, "Comenzar", button_fill_color, green, rect_comenzar, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color, select_sound)
        crear_boton_con_contorno(screen, "Opciones", button_fill_color, green, rect_opciones, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color, select_sound)
        crear_boton_con_contorno(screen, "Salir", button_fill_color, green, rect_salir, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color, select_sound)

        pygame.display.flip()



def invocar_ventana_opciones():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == PRIMARY_MOUSE_BUTTON:
                    if rect_guardar.collidepoint(event.pos):
                        return
        
        crear_ventana_con_contorno(screen, "Opciones", button_fill_color, rect_confirmar_salida, color_fuente_botones, fuente_botones, rect_text_ventana_center, ancho_contorno, title_outline_color)
        
        crear_slider(screen, title_outline_color, rect_slider_musica, white)
        crear_slider(screen, title_outline_color, rect_slider_sonidos, white)

        crear_boton_con_contorno(screen, "Guardar", button_fill_color, green, rect_guardar, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color)

        pygame.display.flip()



def invocar_ventana_confirmar_salida(rect_confirmar_salida, rect_si, rect_no):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == PRIMARY_MOUSE_BUTTON:
                    if rect_si.collidepoint(pygame.mouse.get_pos()):
                        salir()
                    if rect_no.collidepoint(pygame.mouse.get_pos()):
                        if in_menu:
                            return
                        if in_pause:
                            pause()
        
        #pygame.draw.rect(screen, button_fill_color, rect_confirmar_salida, 5, 5)
        #render = fuente_botones.render(texto_ventana_confirmar_salida, True, color_fuente_botones)
        #rect_text = render.get_rect(center = rect_confirmar_salida.center)
        #screen.blit(render, rect_text)
        

        crear_ventana_con_contorno(screen, texto_ventana_confirmar_salida, button_fill_color, rect_confirmar_salida, color_fuente_botones, fuente_botones, rect_text_ventana_center, ancho_contorno, title_outline_color)

        crear_boton_con_contorno(screen, "Si", button_fill_color, green, rect_si, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color)
        crear_boton_con_contorno(screen, "No", button_fill_color, green, rect_no, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color)

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
            if event.button == PRIMARY_MOUSE_BUTTON:
                if rect_slider.collidepoint(event.pos):
                    print("Hola mundo")
                    center_handle_x = pygame.mouse.get_pos()[0]
                    pygame.draw.circle(surface, color_handle, (center_handle_x, rect_slider.centery), 10)
    
    
                    



    
def crear_ventana(surface, texto, bg_color, rect_ventana, font_color, fuente, rect_text_center):
    pygame.draw.rect(surface, bg_color, rect_ventana, border_radius = 5)
    render = fuente.render(texto, True, font_color)
    rect_text = render.get_rect(center = rect_text_center)
    surface.blit(render, rect_text)



def crear_ventana_con_contorno(surface, texto, bg_color, rect_ventana, font_color, fuente, rect_text_center, ancho_contorno, color_contorno):
    crear_ventana(surface, texto, bg_color, rect_ventana, font_color, fuente, rect_text_center)
    pygame.draw.rect(surface, color_contorno, rect_ventana, ancho_contorno, 5)



def crear_boton(surface, texto, bg_color, bg_color_hover, rect_boton, font_color, fuente, sonido = None):
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        #flag_collide = False
        pygame.draw.rect(surface, bg_color_hover, rect_boton, border_radius = 5)
        #if sonido and flag_collide == False:
            #sonido.play()
            #flag_collide = True
    else:
        pygame.draw.rect(surface, bg_color, rect_boton, border_radius = 5)
    render = fuente.render(texto, True, font_color)
    rect_text = render.get_rect(center = rect_boton.center)
    surface.blit(render, rect_text)



def crear_boton_con_contorno(surface, texto, bg_color, bg_color_hover, rect_boton, font_color, fuente, ancho_contorno, color_contorno, sonido = None):
    crear_boton(surface, texto, bg_color, bg_color_hover, rect_boton, font_color, fuente, select_sound)
    pygame.draw.rect(surface, color_contorno, rect_boton, ancho_contorno, 5)
    


def dibujar_texto(surface, font, text, color, size, x, y):
    font = pygame.font.Font(font, size)
    text = font.render(text, True, color)
    textbox = text.get_rect()
    textbox.center = (x, y)
    surface.blit(text, textbox)



def dibujar_texto_con_contorno(surface, font, text, color_relleno, size, x, y, ancho_contorno, color_contorno):
    dibujar_texto(surface, font, text, color_contorno, size, x + ancho_contorno, y + ancho_contorno)
    dibujar_texto(surface, font, text, color_contorno, size, x + ancho_contorno, y - ancho_contorno)
    dibujar_texto(surface, font, text, color_contorno, size, x - ancho_contorno, y + ancho_contorno)
    dibujar_texto(surface, font, text, color_contorno, size, x - ancho_contorno, y - ancho_contorno)
    dibujar_texto(surface, font, text, color_relleno, size, x, y)



def pause():
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
                if event.button == PRIMARY_MOUSE_BUTTON:
                    if rect_opciones.collidepoint(pygame.mouse.get_pos()):
                        invocar_ventana_opciones()
                    if rect_volver_menu.collidepoint(pygame.mouse.get_pos()):
                        return
        
        crear_boton_con_contorno(screen, "Opciones", button_fill_color, green, rect_opciones, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color)
        crear_boton_con_contorno(screen, "Volver al menu", button_fill_color, green, rect_volver_menu, color_fuente_botones, fuente_botones, ancho_contorno, title_outline_color)

        pygame.display.flip()



def fin_del_juego(surface, texto, bg_color, rect_ventana, font_color, fuente_textos, rect_text_center, rect_volver_menu, ancho_contorno, color_contorno):

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    salir()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == PRIMARY_MOUSE_BUTTON:
                    if rect_volver_menu.collidepoint(event.pos):
                        return
        
        crear_ventana_con_contorno(surface, texto, bg_color, rect_ventana, font_color, fuente_textos, rect_text_center, ancho_contorno, color_contorno)

        crear_boton_con_contorno(surface, "Volver al menu", button_fill_color, green, rect_volver_menu, font_color, fuente_textos, ancho_contorno, color_contorno)

        

        pygame.display.flip()