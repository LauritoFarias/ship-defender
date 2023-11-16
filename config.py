import pygame



pygame.init()

pygame.font.init()

SPEED = 8

#screen
width = 800
height = 600
origin = (0, 0)
center_screen_x = width // 2
center_screen_y = height // 2
size_screen = (width, height)
center_screen = (center_screen_x, center_screen_y)



screen = pygame.display.set_mode((size_screen))



background_menu = pygame.image.load(r"assets\Imagenes\undersea.png")
background_menu = pygame.transform.scale(background_menu, size_screen)

background_game = pygame.image.load(r"assets\Imagenes\mar.png")
background_game = pygame.transform.scale(background_game, size_screen)



FPS = 60

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
turqoise = (64, 192, 192)
black = (0, 0, 0)
white = (255, 255, 255)

title_fill_color = (150, 200, 250)
title_outline_color = (80, 40, 20)
button_fill_color = (255, 205, 10)

colors = [red, green, blue, yellow, black, white]



#Fuentes
#Titulo
archivo_fuente = r"assets\Pirate Ship.ttf"
titulo = "Ship Defender"
color = title_outline_color
size_titulo = 100
rect_titulo_x = center_screen_x
rect_titulo_y = 120
ancho_contorno = 3

fuente_textos = r"assets\MorrisRomanBlack.ttf"
fuente_botones = pygame.font.Font(fuente_textos, 40)
color_fuente_botones = black

rect_text_ventana_center = (400, 140)


#Reloj
clock = pygame.time.Clock()



# Teclas
PRIMARY_MOUSE_BUTTON = 1
SECONDARY_MOUSE_BUTTON = 3
SCROLL_MOUSE_BUTTON = 2
SCROLL_UP_MOUSE = 4
SCROLL_DOWN_MOUSE = 5



# Sonidos
select_sound = pygame.mixer.Sound(r"assets\select.mp3")



#Botones
size_button = (250, 60)
left_button = screen.get_width() // 2 - size_button[0] // 2

rect_comenzar = pygame.Rect(left_button, 240, *size_button)
rect_opciones = pygame.Rect(left_button, 320, *size_button)
rect_salir = pygame.Rect(left_button, 400, *size_button)



rect_volver_menu = pygame.Rect(left_button, 410, *size_button)



#Salir
size_ventana_confirmar_salida = (600, 400)
left_ventana_confirmar_salida = screen.get_width() // 2 - size_ventana_confirmar_salida[0] // 2

size_botones_confirmar_salida = (80, 50)
left_boton_si_confirmar_salida = screen.get_width() // 2 - (size_ventana_confirmar_salida[0] // 4 + size_botones_confirmar_salida[0] // 2)
left_boton_no_confirmar_salida = screen.get_width() // 2 + (size_ventana_confirmar_salida[0] // 4 - size_botones_confirmar_salida[0] // 2)
texto_ventana_confirmar_salida = "¿Estás seguro de que deseas salir?"

rect_confirmar_salida = pygame.Rect(left_ventana_confirmar_salida, 100, *size_ventana_confirmar_salida)
rect_si = pygame.Rect(left_boton_si_confirmar_salida, 360, *size_botones_confirmar_salida)
rect_no = pygame.Rect(left_boton_no_confirmar_salida, 360, *size_botones_confirmar_salida)

lista_botones = [rect_comenzar, rect_opciones, rect_salir]



# Opciones
size_ventana_opciones = (600, 400)
left_ventana_opciones = screen.get_width() // 2 - size_ventana_opciones[0] // 2

size_slider = (500, 10)
left_top_musica = (150, 180)
left_top_sonidos = (150, 270)
size_handle = (20, 20)



# Pantalla de fin del juego
SIZE_VENTANA_FIN = (690, 430)
LEFT_VENTANA_FIN = screen.get_width() // 2 - SIZE_VENTANA_FIN[0] // 2
RECT_VENTANA_FIN = pygame.Rect(LEFT_VENTANA_FIN, 55, *SIZE_VENTANA_FIN)

CENTER_RECT_TITULO_VENTANA_FIN = (400, 85)

SIZE_BOTON_VOLVER_MENU = (200, 50)
LEFT_BOTON_VOLVER_MENU = screen.get_width() // 2 - (SIZE_VENTANA_FIN[0] // 4 + SIZE_BOTON_VOLVER_MENU[0] // 2)
TEXTO_BOTON_VOLVER_MENU = "Volver al menu"
RECT_BOTON_VOLVER_MENU_DESDE_FIN = pygame.Rect(LEFT_BOTON_VOLVER_MENU, 500, *SIZE_BOTON_VOLVER_MENU)








texto_opcion_musica = "Musica"
rect_slider_musica = pygame.Rect(*left_top_musica, *size_slider)



texto_opcion_sonidos = "Sonidos"
rect_slider_sonidos = pygame.Rect(*left_top_sonidos, *size_slider)



rect_guardar = pygame.Rect(screen.get_width() // 2 - 80, 400, 160, 60)


transparent_screen = pygame.Surface(size_screen)
transparent_screen.fill(black)
transparent_screen.set_alpha(192)



#Flags
diccionario_flags = {"running":True, "menu":True, "pause":False}
is_running = True
in_menu = True
in_pause = False
timers_cargados = False



velocidad_disparo_jugador = 4
velocidad_disparo_enemigos = 4