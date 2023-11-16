import pygame
from funciones_interfaz import *
from funciones_sonidos import *
from funciones_enemigos import *
from funciones_acciones import *
from utils import *
from random import *
from sys import exit
from config import *
from pygame.locals import *
from enemies import *

##########     Inicializar los modulos de pygame     ##########

pygame.mixer.pre_init(44100, -16, 1, 4096)

pygame.init()

pygame.font.init()

##########     Configuracion pantalla principal     ##########

# Pantalla
pygame.display.set_caption("Ship Defender")



# Sonidos

archivo_musica = r"assets\battleship.mp3"

volumen_musica = 0.5

pygame.mixer.music.load(archivo_musica)

pygame.mixer.music.set_volume(volumen_musica)

pygame.mixer.music.play(-1)



volumen_sonidos = 0.5

sonido_bala = pygame.mixer.Sound(r"assets\bullet-shot.mp3")

sonido_cannon_shot = pygame.mixer.Sound(r"assets\cannon-shot.mp3")

sonido_explosion_1 = pygame.mixer.Sound(r"assets\explosion-1.mp3")

sonido_explosion_2 = pygame.mixer.Sound(r"assets\explosion-2.mp3")

sonido_impacto_municion = pygame.mixer.Sound(r"assets\impacto-municion.mp3")

pygame.mixer.Sound.set_volume(sonido_bala, volumen_sonidos)

pygame.mixer.Sound.set_volume(sonido_cannon_shot, volumen_sonidos)

pygame.mixer.Sound.set_volume(sonido_explosion_1, volumen_sonidos)

pygame.mixer.Sound.set_volume(sonido_explosion_2, volumen_sonidos)

pygame.mixer.Sound.set_volume(sonido_impacto_municion, volumen_sonidos)

#diccionario_archivos_musica = {"menu": r"Programación - Laboratorio\Ship Defender\assets\menu.mp3", "juego": r"Programación - Laboratorio\Ship Defender\assets\battleship.mp3"}



player_dimensions = (40, 60)
image_player = pygame.image.load(r"assets\Imagenes\bote.png").convert_alpha()

image_player = pygame.transform.scale(image_player, player_dimensions)

image_player_rect = image_player.get_rect()

image_player_rect.center = center_screen

mask_player = pygame.mask.from_surface(image_player)

player = {"mask": mask_player, "imagen": image_player, "rect": image_player_rect, "disparo": None, "velocidad": 4, "vidas": 3}



enemigos = []

disparos_jugador = []

disparos_enemigos = []

is_running = True

cooldown_disparo_jugador = 0

milisegundos_ultimo_disparo_jugador = 0

##########     Configuro la direccion     ##########

move_right = False
move_left = False
move_up = False
move_down = False



fuente_vidas = pygame.font.Font(fuente_textos, 20)

texto_vidas = fuente_vidas.render(f"Vidas:", True, black)
rect_texto_vidas = texto_vidas.get_rect()
rect_texto_vidas.topleft = (10, 10)



contadores_enemigos_destruidos_por_tipo = {"velero": 0, "barco": 0, "fragata": 0, "lancha": 0, "portaaviones": 0}

puntuacion_por_tiempo = 0

move_up = False
move_down = False

angulo_jugador = 0

aumentar_angulo = False
disminuir_angulo = False

player_twinkle = False

player_hit = False



# Eventos
EVENTO_INVOCAR_VELERO = USEREVENT + 1
pygame.time.set_timer(EVENTO_INVOCAR_VELERO, 3000)
flag_primer_velero = False
vacio_para_invocar_velero = True

EVENTO_INVOCAR_BARCO = USEREVENT + 2
pygame.time.set_timer(EVENTO_INVOCAR_BARCO, 15000)
flag_primer_barco = False
vacio_para_invocar_barco = True

EVENTO_INVOCAR_FRAGATA = USEREVENT + 3
pygame.time.set_timer(EVENTO_INVOCAR_FRAGATA, 50000)
flag_primera_fragata = False
vacio_para_invocar_fragata = True

EVENTO_INVOCAR_LANCHA = USEREVENT + 4
pygame.time.set_timer(EVENTO_INVOCAR_LANCHA, 80000)
flag_primera_lancha = False
vacio_para_invocar_lancha = True

EVENTO_INVOCAR_PORTAAVIONES = USEREVENT + 5
pygame.time.set_timer(EVENTO_INVOCAR_PORTAAVIONES, 120000)
flag_primer_portaaviones = False
vacio_para_invocar_portaaviones = True

while is_running:

    clock.tick(FPS)

    milisegundos = pygame.time.get_ticks()

    ##########     Menu principal    ##########

    if in_menu:
        invocar_menu_inicio(rect_comenzar, rect_opciones, rect_salir)
        in_menu = False

    ##########     Juego     ##########

    for event in pygame.event.get():
        if event.type == QUIT:
            salir()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                salir()
            if event.key == K_p:
                pause()
            if event.key == K_UP:
                move_up = True
            if event.key == K_RIGHT:
                aumentar_angulo = True
            if event.key == K_DOWN:
                move_down = True
            if event.key == K_LEFT:
                disminuir_angulo = True
            if event.key == K_w:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "forward", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    sonido_cannon_shot.play()
                    print("Sonido de disparo del jugador")
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            if event.key == K_d:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "right", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    sonido_cannon_shot.play()
                    print("Sonido de disparo del jugador")
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            if event.key == K_a:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "left", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    sonido_cannon_shot.play()
                    print("Sonido de disparo del jugador")
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            

        
        if event.type == KEYUP:
            if event.key == K_UP:
                move_up = False
            if event.key == K_RIGHT:
                aumentar_angulo = False
            if event.key == K_DOWN:
                move_down = False
            if event.key == K_LEFT:
                disminuir_angulo = False
            
            
        
        if event.type == EVENTO_INVOCAR_VELERO:
            if flag_primer_velero == False:
                velero = invocar_enemigo("velero", 200)
                enemigos.append(velero)
                flag_primer_velero = True
            else:
                x_invocacion_velero = randint(50, 750)
                for enemigo in enemigos:
                    if x_invocacion_velero >= enemigo["rect"].left and x_invocacion_velero <= enemigo["rect"].right:
                        vacio_para_invocar_velero = False
                        break

                if vacio_para_invocar_velero:
                    velero = invocar_enemigo("velero", x_invocacion_velero)
                    enemigos.append(velero)
            
            contador_invocacion_velero = randint(5000, 10000)
            pygame.time.set_timer(EVENTO_INVOCAR_VELERO, contador_invocacion_velero)
        
        if event.type == EVENTO_INVOCAR_BARCO:
            x_invocacion_barco = randint(50, 750)
            for enemigo in enemigos:
                if x_invocacion_barco >= enemigo["rect"].left and x_invocacion_barco <= enemigo["rect"].right:
                    vacio_para_invocar_barco = False
                    break

            if vacio_para_invocar_barco:
                barco = invocar_enemigo("barco", x_invocacion_barco)
                enemigos.append(barco)

            pygame.time.set_timer(EVENTO_INVOCAR_BARCO, randint(4000, 8000))
        
        if event.type == EVENTO_INVOCAR_FRAGATA:
            x_invocacion_fragata = randint(50, 750)
            for enemigo in enemigos:
                if x_invocacion_fragata >= enemigo["rect"].left and x_invocacion_fragata <= enemigo["rect"].right:
                    vacio_para_invocar_fragata = False
                    break

            if vacio_para_invocar_fragata:
                fragata = invocar_enemigo("fragata", x_invocacion_fragata)
                enemigos.append(fragata)

            pygame.time.set_timer(EVENTO_INVOCAR_FRAGATA, randint(12000, 20000))
        
        if event.type == EVENTO_INVOCAR_LANCHA:
            x_invocacion_lancha = randint(50, 750)
            for enemigo in enemigos:
                if x_invocacion_lancha >= enemigo["rect"].left and x_invocacion_lancha <= enemigo["rect"].right:
                    vacio_para_invocar_lancha = False
                    break

            if vacio_para_invocar_lancha:
                lancha = invocar_enemigo("lancha", x_invocacion_lancha)
                enemigos.append(lancha)

            pygame.time.set_timer(EVENTO_INVOCAR_LANCHA, randint(5000, 20000))
        
        if event.type == EVENTO_INVOCAR_PORTAAVIONES:
            x_invocacion_portaaviones = randint(50, 750)
            for enemigo in enemigos:
                if x_invocacion_portaaviones >= enemigo["rect"].left and x_invocacion_portaaviones <= enemigo["rect"].right:
                    vacio_para_invocar_portaaviones = False
                    break

            if vacio_para_invocar_portaaviones:
                portaaviones = invocar_enemigo("portaaviones", x_invocacion_portaaviones)
                enemigos.append(portaaviones)

            pygame.time.set_timer(EVENTO_INVOCAR_PORTAAVIONES, randint(30000, 60000))

    #reproducir_musica_de_fondo(diccionario_archivos_musica["juego"],volumen_musica)



    ##########     Actualizar elementos     ##########
    
    for enemigo in enemigos:
        
        if enemigo["tipo"] == "velero":
            if (milisegundos - enemigo["milisegundos"]) >= 3000:
                if player["rect"].centerx >= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midright, 6, enemigo["velocidad_disparo"])
                elif player["rect"].centerx <= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midleft, 4, enemigo["velocidad_disparo"])
                else:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midbottom, 8, enemigo["velocidad_disparo"])
                disparos_enemigos.append(disparo_enemigo)
                
                if disparo_enemigo["tipo"] == "bala":
                    sonido_bala.play()
                else:
                    sonido_cannon_shot.play()
                enemigo["milisegundos"] = milisegundos
        
        if enemigo["tipo"] == "barco":
            if (milisegundos - enemigo["milisegundos"]) >= 3000:
                if player["rect"].centerx >= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midright, 6, enemigo["velocidad_disparo"])
                elif player["rect"].centerx <= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midleft, 4, enemigo["velocidad_disparo"])
                else:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midbottom, 8, enemigo["velocidad_disparo"])
                disparos_enemigos.append(disparo_enemigo)

                if disparo_enemigo["tipo"] == "bala":
                    sonido_bala.play()
                else:
                    sonido_cannon_shot.play()
                enemigo["milisegundos"] = milisegundos
        
        if enemigo["tipo"] == "fragata":
            if (milisegundos - enemigo["milisegundos"]) >= 2000:
                if player["rect"].centerx >= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midright, 6, enemigo["velocidad_disparo"])
                elif player["rect"].centerx <= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midleft, 4, enemigo["velocidad_disparo"])
                else:
                    disparo_enemigo = disparar_al_jugador("cannonball", cannonball, enemigo["rect"].midbottom, 8, enemigo["velocidad_disparo"])
                disparos_enemigos.append(disparo_enemigo)

                if disparo_enemigo["tipo"] == "bala":
                    sonido_bala.play()
                else:
                    sonido_cannon_shot.play()
                enemigo["milisegundos"] = milisegundos
        
        if enemigo["tipo"] == "lancha":
            if (milisegundos - enemigo["milisegundos"]) >= 1000:
                if player["rect"].centerx >= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midright, 6, enemigo["velocidad_disparo"])
                elif player["rect"].centerx <= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midleft, 4, enemigo["velocidad_disparo"])
                else:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midbottom, 8, enemigo["velocidad_disparo"])
                disparos_enemigos.append(disparo_enemigo)

                if disparo_enemigo["tipo"] == "bala":
                    sonido_bala.play()
                else:
                    sonido_cannon_shot.play()
                enemigo["milisegundos"] = milisegundos
        
        if enemigo["tipo"] == "portaaviones":
            if (milisegundos - enemigo["milisegundos"]) >= 1000:
                if player["rect"].centerx >= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midright, 6, enemigo["velocidad_disparo"])
                elif player["rect"].centerx <= enemigo["rect"].centerx:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midleft, 4, enemigo["velocidad_disparo"])
                else:
                    disparo_enemigo = disparar_al_jugador("bala", bala, enemigo["rect"].midbottom, 8, enemigo["velocidad_disparo"])
                disparos_enemigos.append(disparo_enemigo)

                if disparo_enemigo["tipo"] == "bala":
                    sonido_bala.play()
                else:
                    sonido_cannon_shot.play()
                enemigo["milisegundos"] = milisegundos
        

        
        if enemigo["rect"].top >= 600:
            enemigos.remove(enemigo)

        offset = (enemigo["rect"].x - player["rect"].x, enemigo["rect"].y - player["rect"].y) 
        if player["mask"].overlap(enemigo["mask"], offset):
            print("Colision")
        


        enemigo["rect"].top += enemigo["velocidad_movimiento"]
    
    

    # Manejar disparos del jugador(direccion, colisiones, cooldown y eliminarlos cuando se salen de la pantalla)
    for disparo_jugador in disparos_jugador:
        
        if disparo_jugador:

            if disparo_jugador["direccion"] == "forward":
                disparo_jugador["rect"].centerx += disparo_jugador["angulo"][0]
                disparo_jugador["rect"].centery += disparo_jugador["angulo"][1]
            if disparo_jugador["direccion"] == "right":
                disparo_jugador["rect"].centerx += disparo_jugador["angulo"][0]
                disparo_jugador["rect"].centery += disparo_jugador["angulo"][1]
            if disparo_jugador["direccion"] == "left":
                disparo_jugador["rect"].centerx += disparo_jugador["angulo"][0]
                disparo_jugador["rect"].centery += disparo_jugador["angulo"][1]
            
            if out_of_screen(disparo_jugador["rect"], width, height):
                disparos_jugador.remove(disparo_jugador)
            

        
        for enemigo in enemigos:
            offset = (disparo_jugador["rect"].x - enemigo["rect"].x, disparo_jugador["rect"].y - enemigo["rect"].y)

            if not enemigo["hit"]:
                if enemigo["mask"].overlap(disparo_jugador["mask"], offset):
                    enemigo["vidas"] -= 1
                    sonido_impacto_municion.play()
                    if enemigo["vidas"] == 0:
                        enemigos.remove(enemigo)
                        contar_nave_destruida(enemigo["tipo"], contadores_enemigos_destruidos_por_tipo)
                        print(contadores_enemigos_destruidos_por_tipo)
                    else:
                        enemigo["hit"] == True
                        contador_enemigo_hit = milisegundos
            
            if enemigo["hit"] == True:
                if milisegundos % 1000 < 500:
                    enemigo["imagen"].set_alpha(60)
                else:
                    enemigo["imagen"].set_alpha(255)
                
                if milisegundos - contador_enemigo_hit >= 3000:
                    enemigo["hit"] = False
                    player["imagen"].set_alpha(255)



            if enemigo["tipo"] == "velero" or enemigo["tipo"] == "barco" or enemigo["tipo"] == "lancha":
                sonido_explosion_1.play()
            elif enemigo["tipo"] == "fragata" or enemigo["tipo"] == "portaaviones":
                sonido_explosion_2.play()


    
    if milisegundos - milisegundos_ultimo_disparo_jugador >= 1500:
        cooldown_disparo_jugador = False
    

    
    ##########     Mover el bloque segun direccion     ##########

    # Manejar angulo
    if aumentar_angulo:
        angulo_jugador = angulo_jugador - 1 % 360
        player_rotado = pygame.transform.rotate(image_player, angulo_jugador)
        player_rotado_rect = player_rotado.get_rect(center = player["rect"].center)
        player["imagen"] = player_rotado
        player["rect"] = player_rotado_rect
        player["mask"] = pygame.mask.from_surface(player["imagen"])
    if disminuir_angulo:
        angulo_jugador = angulo_jugador + 1 % 360
        player_rotado = pygame.transform.rotate(image_player, angulo_jugador)
        player_rotado_rect = player_rotado.get_rect(center = player["rect"].center)
        player["imagen"] = player_rotado
        player["rect"] = player_rotado_rect
        player["mask"] = pygame.mask.from_surface(player["imagen"])


    
    # Avanzar o retroceder segun angulo
    if move_up and player["rect"].top >= 0:
        player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
        player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    if move_down and player["rect"].bottom <= height:
        player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
        player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    


    # Manejar disparos de enemigos(direccion, velocidad, colision con jugador y elimilarlo cuando salga de la pantalla)
    for disparo_enemigo in disparos_enemigos:
        if disparo_enemigo["direccion"] == 6:
            disparo_enemigo["rect"].centerx += disparo_enemigo["velocidad_disparo"]
        if disparo_enemigo["direccion"] == 4:
            disparo_enemigo["rect"].centerx -= disparo_enemigo["velocidad_disparo"]
        if disparo_enemigo["direccion"] == 2:
            disparo_enemigo["rect"].centery += disparo_enemigo["velocidad_disparo"]

        if not player_hit:
            offset = (player["rect"].x - disparo_enemigo["rect"].x, player["rect"].y - disparo_enemigo["rect"].y)
            if disparo_enemigo["mask"].overlap(player["mask"], offset):
                player_hit = True
                player["vidas"] -= 1
                sonido_impacto_municion.play()

                contador_player_hit = milisegundos
        
        if out_of_screen(disparo_enemigo["rect"], width, height):
            disparos_enemigos.remove(disparo_enemigo)

    ##########     EFECTOS ESPECIALES     ##########
    
    if player_hit:
        if milisegundos % 1000 < 500:
            player["imagen"].set_alpha(60)
        else:
            player["imagen"].set_alpha(255)
        
        if milisegundos - contador_player_hit >= 3000:
            player_hit = False
            player["imagen"].set_alpha(255)

    ##########     DIBUJAR PANTALLA     ##########
    
    screen.blit(background_game, origin)

    screen.blit(player["imagen"], player["rect"].topleft)

    for disparo_enemigo in disparos_enemigos:
        if disparo_enemigo:
            screen.blit(disparo_enemigo["imagen"], disparo_enemigo["rect"])

    for disparo in disparos_jugador:
        if disparo:
            screen.blit(disparo["imagen"], disparo["rect"])

    for enemigo in enemigos:
        screen.blit(enemigo["imagen"], enemigo["rect"])
    
    ##########     FIN DEL JUEGO     ##########

    if player["vidas"] == 0:
        fin_del_juego(screen, "El bote ha sido botado", button_fill_color, RECT_VENTANA_FIN, color_fuente_botones, fuente_textos, CENTER_RECT_TITULO_VENTANA_FIN, RECT_BOTON_VOLVER_MENU_DESDE_FIN, ancho_contorno, title_outline_color)


    pygame.display.flip()

salir()

    