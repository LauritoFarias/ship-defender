import pygame

pygame.init()

pygame.font.init()



##########     PANTALLA     ##########

# Coordenadas
ANCHO = 800
ALTO = 600
ORIGEN = (0, 0)
PANTALLA_CENTRO_X  = ANCHO // 2
PANTALLA_CENTRO_Y = ALTO // 2
TAMANIO_PANTALLA = (ANCHO, ALTO)
CENTRO_PANTALLA = (PANTALLA_CENTRO_X , PANTALLA_CENTRO_Y)

# Imagenes de fondo
FONDO_MENU = pygame.image.load(r"assets\Imagenes\undersea.png")
FONDO_MENU = pygame.transform.scale(FONDO_MENU, TAMANIO_PANTALLA)

FONDO_PARTIDA = pygame.image.load(r"assets\Imagenes\mar.png")
FONDO_PARTIDA = pygame.transform.scale(FONDO_PARTIDA, TAMANIO_PANTALLA)

# Configuracion
FPS = 60

##########     COLORES     ##########

# Definicion de colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MAGENTA = (255, 0, 255)
CIAN = (0, 255, 255)
TURQUESA = (64, 192, 192)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Designacion de colores a objetos del juego
COLOR_RELLENO_TITULO = (150, 200, 250)
COLOR_CONTORNOS = (80, 40, 20)
COLOR_RELLENO_BOTONES = (255, 205, 10)
COLOR_FLOTANTE_RELLENO_BOTONES = VERDE



# Fuentes

transparent_screen = pygame.Surface(TAMANIO_PANTALLA)
transparent_screen.fill(NEGRO)
transparent_screen.set_alpha(192)

fuente_textos_archivo = r"assets\MorrisRomanBlack.ttf"
fuente_textos = pygame.font.Font(fuente_textos_archivo, 40)
COLOR_FUENTE_TEXTOS = NEGRO

ANCHO_CONTORNO = 3



#Titulo
dir_fuente_titulo = r"assets\Pirate Ship.ttf"
tamanio_fuente_titulo = 100
fuente_titulo = pygame.font.Font(dir_fuente_titulo, tamanio_fuente_titulo)
color_fuente_titulo = BLANCO
texto_titulo = "Ship Defender"
color = COLOR_CONTORNOS
rect_titulo_x = PANTALLA_CENTRO_X
rect_titulo_y = 120

ESTILO_INTERFAZ = {"oscurecer_pantalla": transparent_screen,
                   "dir_fuente": fuente_textos_archivo,
                   "fuente": fuente_textos,
                   "tamanio_fuente": 40,
                   "color_fuente": COLOR_FUENTE_TEXTOS,
                   "color_relleno_botones": COLOR_RELLENO_BOTONES,
                   "color_relleno_hover_botones": COLOR_FLOTANTE_RELLENO_BOTONES,
                   "ancho_contorno": ANCHO_CONTORNO,
                   "color_contorno": COLOR_CONTORNOS,
                   "radio_borde": 5}

ESTILO_TITULO = {"dir_fuente": dir_fuente_titulo,
                 "fuente": fuente_titulo,
                 "tamanio_fuente": tamanio_fuente_titulo,
                 "color_fuente": color_fuente_titulo,
                 "ancho_contorno": ANCHO_CONTORNO,
                 "color_contorno": COLOR_CONTORNOS,
                 "texto": texto_titulo,
                 "rect_x": rect_titulo_x,
                 "rect_y": rect_titulo_y}









#Reloj
clock = pygame.time.Clock()



# Teclas
PRIMARY_MOUSE_BUTTON = 1
SECONDARY_MOUSE_BUTTON = 3
SCROLL_MOUSE_BUTTON = 2
SCROLL_UP_MOUSE = 4
SCROLL_DOWN_MOUSE = 5



# Musica y sonidos
VOLUMEN_MUSICA = 0.5
ARCHIVO_MUSICA_MENU = r"assets\menu.mp3"
ARCHIVO_MUSICA_BATALLA = r"assets\battleship.mp3"
ARCHIVO_MUSICA_FIN = r"assets\after-the-battle.mp3"



VOLUMEN_SONIDOS = 0.5
SONIDO_SELECCION = pygame.mixer.Sound(r"assets\select.mp3")
SONIDO_BALA = pygame.mixer.Sound(r"assets\bullet-shot.mp3")
SONIDO_DISPARO_CANION = pygame.mixer.Sound(r"assets\cannon-shot.mp3")
SONIDO_EXPLOSION_1 = pygame.mixer.Sound(r"assets\explosion-1.mp3")
SONIDO_EXPLOSION_2 = pygame.mixer.Sound(r"assets\explosion-2.mp3")
SONIDO_IMPACTO_MUNICION = pygame.mixer.Sound(r"assets\impacto-municion.mp3")
SONIDOS = [SONIDO_SELECCION, SONIDO_BALA, SONIDO_DISPARO_CANION, SONIDO_EXPLOSION_1, SONIDO_EXPLOSION_2, SONIDO_IMPACTO_MUNICION]



##########      BOTONES     ##########

# Menu de inicio
TAMANIO_BOTONES = (250, 60)
IZQUIERDA_BOTONES = ANCHO // 2 - TAMANIO_BOTONES[0] // 2
CENTRO_TEXTO_VENTANA = (ANCHO // 2, 200)

# Opciones
TAMANIO_VENTANA_OPCIONES = (600, 520)
IZQUIERDA_VENTANA_OPCIONES = ANCHO // 2 - TAMANIO_VENTANA_OPCIONES[0] // 2
RECT_VENTANA_OPCIONES = pygame.Rect(IZQUIERDA_VENTANA_OPCIONES, 40, *TAMANIO_VENTANA_OPCIONES)
TAMANIO_BOTON_GUARDAR = ANCHO // 2 - 80
CENTRO_TITULO_OPCIONES = (ANCHO // 2, 100)
#size_slider = (500, 10)
#left_top_musica = (150, 180)
#left_top_SONIDOs = (150, 270)
#size_handle = (20, 20)

#texto_opcion_musica = "Musica"
#rect_slider_musica = pygame.Rect(*left_top_musica, *size_slider)

#texto_opcion_sonidos = "Sonidos"
#rect_slider_sonidos = pygame.Rect(*left_top_sonidos, *size_slider)

# Confirmar salida
TAMANIO_VENTANA_CONFIRMAR_SALIDA = (600, 380)
IZQUIERDA_VENTANA_CONFIRMAR_SALIDA = ANCHO // 2 - TAMANIO_VENTANA_CONFIRMAR_SALIDA[0] // 2
RECT_VENTANA_CONFIRMAR_SALIDA = pygame.Rect(IZQUIERDA_VENTANA_CONFIRMAR_SALIDA, 110, *TAMANIO_VENTANA_CONFIRMAR_SALIDA)
CENTRO_TITULO_VENTANA_CONFIRMAR_SALIDA = (ANCHO // 2, 200)

TAMANIO_BOTONES_CONFIRMAR_SALIDA = (80, 50)
IZQUIERDA_BOTON_SI = ANCHO // 2 - (TAMANIO_VENTANA_CONFIRMAR_SALIDA[0] // 4 + TAMANIO_BOTONES_CONFIRMAR_SALIDA[0] // 2)
IZQUIERDA_BOTON_NO = ANCHO // 2 + (TAMANIO_VENTANA_CONFIRMAR_SALIDA[0] // 4 - TAMANIO_BOTONES_CONFIRMAR_SALIDA[0] // 2)
TITULO_VENTANA_CONFIRMAR_SALIDA = "¿Estás seguro de que deseas salir?"

# Final del juego
TAMANIO_VENTANA_FIN = (680, 520)
IZQUIERDA_VENTANA_FIN = ANCHO // 2 - TAMANIO_VENTANA_FIN[0] // 2
RECT_VENTANA_FIN = pygame.Rect(IZQUIERDA_VENTANA_FIN, 40, *TAMANIO_VENTANA_FIN)
CENTRO_RECT_TITULO_VENTANA_FIN = (ANCHO // 2, 100)

TAMANIO_BOTON_VOLVER_MENU = (250, 50)
IZQUIERDA_BOTON_VOLVER_MENU = ANCHO // 2 - 125
TEXTO_BOTON_VOLVER_MENU = "Volver al menu"
#RECT_BOTON_VOLVER_MENU_DESDE_FIN = pygame.Rect(IZQUIERDA_BOTON_VOLVER_MENU, 480, *TAMANIO_BOTON_VOLVER_MENU)

RECT_BOTON_COMENZAR = pygame.Rect(IZQUIERDA_BOTONES, 240, *TAMANIO_BOTONES)
RECT_BOTON_OPCIONES = pygame.Rect(IZQUIERDA_BOTONES, 320, *TAMANIO_BOTONES)
RECT_BOTON_SALIR = pygame.Rect(IZQUIERDA_BOTONES, 400, *TAMANIO_BOTONES)
RECT_BOTON_GUARDAR = pygame.Rect(ANCHO // 2 - 80, 480, 160, 60)
RECT_BOTON_CONFIRMAR_SALIDA = pygame.Rect(IZQUIERDA_VENTANA_CONFIRMAR_SALIDA, 120, *TAMANIO_VENTANA_CONFIRMAR_SALIDA)
RECT_BOTON_SI = pygame.Rect(IZQUIERDA_BOTON_SI, 360, *TAMANIO_BOTONES_CONFIRMAR_SALIDA)
RECT_BOTON_NO = pygame.Rect(IZQUIERDA_BOTON_NO, 360, *TAMANIO_BOTONES_CONFIRMAR_SALIDA)
RECT_BOTON_VOLVER_MENU = pygame.Rect(ANCHO // 2 - 300, 480, *TAMANIO_BOTONES)
RECT_BOTON_ESTADISTICAS = pygame.Rect(ANCHO // 2 + 50, 480, *TAMANIO_BOTONES)
RECT_BOTON_VOLVER_ESTADISTICAS = pygame.Rect(ANCHO // 2, 480, *TAMANIO_BOTON_VOLVER_MENU)

BOTONES = {"comenzar": RECT_BOTON_COMENZAR,
           "opciones": RECT_BOTON_OPCIONES,
           "salir": RECT_BOTON_SALIR,
           "guardar": RECT_BOTON_GUARDAR,
           "confirmar_salida": RECT_BOTON_CONFIRMAR_SALIDA,
           "si": RECT_BOTON_SI,
           "no": RECT_BOTON_NO,
           "volver_menu": RECT_BOTON_VOLVER_MENU,
           "estadisticas": RECT_BOTON_ESTADISTICAS,
           "volver_estadisticas": RECT_BOTON_VOLVER_ESTADISTICAS}


#Flags
flags_pantallas = {"menu": True, "pause": False, "opciones": False, "estadisticas": False}
in_menu = True
in_pause = False
flag_fin = False
en_opciones = False
pantalla_estadisticas = False
timers_cargados = False



velocidad_disparo_jugador = 4
velocidad_disparo_enemigos = 4