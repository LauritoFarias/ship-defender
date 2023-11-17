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

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()

##########     Configuracion pantalla principal     ##########

# Pantalla
pygame.display.set_caption("Ship Defender")

PANTALLA = pygame.display.set_mode((TAMANIO_PANTALLA))



pygame.mixer.music.load(ARCHIVO_MUSICA_BATALLA)

pygame.mixer.music.set_volume(VOLUMEN_MUSICA)

pygame.mixer.music.play(-1)


for sonido in SONIDOS:
    pygame.mixer.Sound.set_volume(sonido, VOLUMEN_SONIDOS)

player = {"mask": mask_jugador, "imagen": imagen_jugador, "rect": rect_imagen_jugador, "disparo": None, "velocidad": 2, "vidas": 3}

disparos_jugador = []

enemigos = []

disparos_enemigos = []

is_running = True

cooldown_disparo_jugador = 0

milisegundos_ultimo_disparo_jugador = 0

##########     Configuro la direccion     ##########

move_right = False
move_left = False
mover_proa = False
mover_popa = False

#fuente_vidas = pygame.font.Font(fuente_textos, 20)

#texto_vidas = fuente_vidas.render(f"Vidas:", True, black)
#rect_texto_vidas = texto_vidas.get_rect()
#rect_texto_vidas.topleft = (10, 10)

contador_enemigos_muertos = {"velero": 0, "barco": 0, "fragata": 0, "lancha": 0, "portaaviones": 0}

puntuacion_por_tiempo = 0

angulo_jugador = 0

aumentar_angulo = False

disminuir_angulo = False

moviendo_hacia_arriba = False

moviendo_hacia_abajo = False

player_hit = False

siguiente_musica = False

milisegundos = 0

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

while True:

    clock.tick(FPS)

    milisegundos += clock.get_time()

    ##########     Menu principal    ##########

    if flags_pantallas["menu"]:
        invocar_menu_inicio(PANTALLA, ORIGEN, ESTILO_INTERFAZ, ESTILO_TITULO, FONDO_MENU, BOTONES, RECT_VENTANA_OPCIONES, CENTRO_TITULO_OPCIONES, RECT_VENTANA_CONFIRMAR_SALIDA, CENTRO_TITULO_VENTANA_CONFIRMAR_SALIDA, ARCHIVO_MUSICA_MENU, VOLUMEN_MUSICA)
        flags_pantallas["menu"] = False
        en_opciones = True

    ##########     Juego     ##########

    if not siguiente_musica:

        pygame.mixer.music.load(ARCHIVO_MUSICA_BATALLA)

        pygame.mixer.music.set_volume(VOLUMEN_MUSICA)

        pygame.mixer.music.play(-1)

        siguiente_musica = True
    
    #player["vidas"] = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            salir()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                salir()
            if event.key == K_p:
                pausa(PANTALLA, ESTILO_INTERFAZ, BOTONES)
            if event.key == K_UP:
                mover_proa = True
            if event.key == K_RIGHT:
                disminuir_angulo = True
            if event.key == K_DOWN:
                mover_popa = True
            if event.key == K_LEFT:
                aumentar_angulo = True
            if event.key == K_w:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "forward", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    SONIDO_DISPARO_CANION.play()
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            if event.key == K_d:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "right", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    SONIDO_DISPARO_CANION.play()
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            if event.key == K_a:
                if not cooldown_disparo_jugador:
                    disparo_jugador = disparar(cannonball, player["rect"].center, angulo_jugador, "left", velocidad_disparo_jugador)
                    cooldown_disparo_jugador = True
                    SONIDO_DISPARO_CANION.play()
                    print("sonido")
                    milisegundos_ultimo_disparo_jugador = pygame.time.get_ticks()
                    disparos_jugador.append(disparo_jugador)
            

        
        if event.type == KEYUP:
            if event.key == K_UP:
                mover_proa = False
            if event.key == K_RIGHT:
                disminuir_angulo = False
            if event.key == K_DOWN:
                mover_popa = False
            if event.key == K_LEFT:
                aumentar_angulo = False
            
            
        
        if event.type == EVENTO_INVOCAR_VELERO:
            if flag_primer_velero == False:
                velero = invocar_enemigo("velero", 200)
                enemigos.append(velero)
                flag_primer_velero = True
            else:
                x_invocacion_velero = randint(50, 750)
                #for enemigo in enemigos:
                    #if x_invocacion_velero >= enemigo["rect"].left and x_invocacion_velero <= enemigo["rect"].right:
                        #vacio_para_invocar_velero = False
                        #break

                #if vacio_para_invocar_velero:
                velero = invocar_enemigo("velero", x_invocacion_velero)
                enemigos.append(velero)
            
            contador_invocacion_velero = randint(5000, 10000)
            pygame.time.set_timer(EVENTO_INVOCAR_VELERO, contador_invocacion_velero)
        
        if event.type == EVENTO_INVOCAR_BARCO:
            x_invocacion_barco = randint(50, 750)
            #for enemigo in enemigos:
                #if x_invocacion_barco >= enemigo["rect"].left and x_invocacion_barco <= enemigo["rect"].right:
                    #vacio_para_invocar_barco = False
                    #break

            #if vacio_para_invocar_barco:
            barco = invocar_enemigo("barco", x_invocacion_barco)
            enemigos.append(barco)

            pygame.time.set_timer(EVENTO_INVOCAR_BARCO, randint(4000, 8000))
        
        if event.type == EVENTO_INVOCAR_FRAGATA:
            x_invocacion_fragata = randint(50, 750)
            #for enemigo in enemigos:
                #if x_invocacion_fragata >= enemigo["rect"].left and x_invocacion_fragata <= enemigo["rect"].right:
                    #vacio_para_invocar_fragata = False
                    #break

            #if vacio_para_invocar_fragata:
            fragata = invocar_enemigo("fragata", x_invocacion_fragata)
            enemigos.append(fragata)

            pygame.time.set_timer(EVENTO_INVOCAR_FRAGATA, randint(12000, 20000))
        
        if event.type == EVENTO_INVOCAR_LANCHA:
            x_invocacion_lancha = randint(50, 750)
            #for enemigo in enemigos:
                #if x_invocacion_lancha >= enemigo["rect"].left and x_invocacion_lancha <= enemigo["rect"].right:
                    #vacio_para_invocar_lancha = False
                    #break

            #if vacio_para_invocar_lancha:
            lancha = invocar_enemigo("lancha", x_invocacion_lancha)
            enemigos.append(lancha)

            pygame.time.set_timer(EVENTO_INVOCAR_LANCHA, randint(5000, 20000))
        
        if event.type == EVENTO_INVOCAR_PORTAAVIONES:
            x_invocacion_portaaviones = randint(50, 750)
            #for enemigo in enemigos:
                #if x_invocacion_portaaviones >= enemigo["rect"].left and x_invocacion_portaaviones <= enemigo["rect"].right:
                    #vacio_para_invocar_portaaviones = False
                    #break

            #if vacio_para_invocar_portaaviones:
            portaaviones = invocar_enemigo("portaaviones", x_invocacion_portaaviones)
            enemigos.append(portaaviones)

            pygame.time.set_timer(EVENTO_INVOCAR_PORTAAVIONES, randint(30000, 60000))

    #reproducir_musica_de_fondo(diccionario_archivos_musica["juego"],volumen_musica)



    ##########     Actualizar elementos     ##########

    for enemigo in enemigos:
        disparar_al_jugador(player, enemigo, milisegundos, disparos_enemigos, SONIDO_BALA, SONIDO_DISPARO_CANION)
        
        if enemigo["rect"].top >= 600:
            enemigos.remove(enemigo)
        
        if not player_hit:
            offset = (enemigo["rect"].x - player["rect"].x, enemigo["rect"].y - player["rect"].y) 
            if player["mask"].overlap(enemigo["mask"], offset):
                player_hit = True
                player["vidas"] -= 1
                SONIDO_IMPACTO_MUNICION.play()

                contador_player_hit = milisegundos

        enemigo["rect"].top += enemigo["velocidad_movimiento"]
    
    

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
            
            if out_of_screen(disparo_jugador["rect"], ANCHO, ALTO):
                disparos_jugador.remove(disparo_jugador)
            

        
        for enemigo in enemigos:
            offset = (disparo_jugador["rect"].x - enemigo["rect"].x, disparo_jugador["rect"].y - enemigo["rect"].y)

            if not enemigo["hit"]:
                if enemigo["mask"].overlap(disparo_jugador["mask"], offset):
                    disparos_jugador.remove(disparo_jugador)
                    enemigo["vidas"] -= 1
                    SONIDO_IMPACTO_MUNICION.play()
                    if enemigo["vidas"] == 0:
                        enemigos.remove(enemigo)
                        contar_nave_destruida(enemigo["tipo"], contador_enemigos_muertos)
                        print(contador_enemigos_muertos)
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
                    SONIDO_EXPLOSION_1.play()
                elif enemigo["tipo"] == "fragata" or enemigo["tipo"] == "portaaviones":
                    SONIDO_EXPLOSION_2.play()


    
    if milisegundos - milisegundos_ultimo_disparo_jugador >= 1500:
        cooldown_disparo_jugador = False
    

    
    ##########     Mover el bloque segun direccion     ##########

    # Manejar angulo
    
    if disminuir_angulo:
        angulo_jugador = abs((angulo_jugador - 1) % 360)
        player_rotado = pygame.transform.rotate(imagen_jugador, angulo_jugador)
        player_rotado_rect = player_rotado.get_rect(center = player["rect"].center)
        player["imagen"] = player_rotado
        player["rect"] = player_rotado_rect
        player["mask"] = pygame.mask.from_surface(player["imagen"])
    if aumentar_angulo:
        angulo_jugador = (angulo_jugador + 1) % 360
        player_rotado = pygame.transform.rotate(imagen_jugador, angulo_jugador)
        player_rotado_rect = player_rotado.get_rect(center = player["rect"].center)
        player["imagen"] = player_rotado
        player["rect"] = player_rotado_rect
        player["mask"] = pygame.mask.from_surface(player["imagen"])
    
    

    if mover_proa:
        if angulo_jugador <= 90 or angulo_jugador >= 270:
            moviendo_hacia_arriba = True
            moviendo_hacia_abajo = False
        if angulo_jugador > 90 and angulo_jugador < 270:
            moviendo_hacia_arriba = False
            moviendo_hacia_abajo = True
        if angulo_jugador >= 0 and angulo_jugador <= 180:
            moviendo_hacia_izquierda = True
            moviendo_hacia_derecha = False
        if angulo_jugador > 180 and angulo_jugador < 360:
            moviendo_hacia_izquierda = False
            moviendo_hacia_derecha = True
    if mover_popa:
        if angulo_jugador <= 90 or angulo_jugador >= 270:
            moviendo_hacia_arriba = False
            moviendo_hacia_abajo = True
        if angulo_jugador > 90 and angulo_jugador < 270:
            moviendo_hacia_arriba = True
            moviendo_hacia_abajo = False
        if angulo_jugador >= 0 and angulo_jugador <= 180:
            moviendo_hacia_izquierda = False
            moviendo_hacia_derecha = True
        if angulo_jugador > 180 and angulo_jugador < 360:
            moviendo_hacia_izquierda = True
            moviendo_hacia_derecha = False
    if not mover_proa and not mover_popa:
        moviendo_hacia_arriba = False
        moviendo_hacia_abajo = False
        moviendo_hacia_izquierda = False
        moviendo_hacia_derecha = False
    
    

    # Manejar movimiento del jugador
    #if mover_proa and player["rect"].top >= 0 and player["rect"].bottom <= ALTO:
        #player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
        #player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    #if mover_popa and player["rect"].bottom <= ALTO and player["rect"].top >= 0:
        #player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
        #player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    
    if moviendo_hacia_arriba and player["rect"].top >= 0:
        if (moviendo_hacia_izquierda and player["rect"].left >= 0) or (moviendo_hacia_derecha and player["rect"].right <= ANCHO):
            if mover_proa:
                player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
                player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
            if mover_popa:
                player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
                player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    if moviendo_hacia_abajo and player["rect"].bottom <= ALTO:
        if (moviendo_hacia_izquierda and player["rect"].left >= 0) or (moviendo_hacia_derecha and player["rect"].right <= ANCHO):
            if mover_proa:
                player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
                player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
            if mover_popa:
                player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
                player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    #if moviendo_hacia_izquierda and player["rect"].left >= 0:
        #if mover_proa:
            #player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
            #player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
        #if mover_popa:
            #player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
            #player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
    #if moviendo_hacia_derecha and player["rect"].right <= ANCHO:
        #if mover_proa:
            #player["rect"].centerx += mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
            #player["rect"].centery += mover_segun_angulo(angulo_jugador, player["velocidad"])[1]
        #if mover_popa:
            #player["rect"].centerx -= mover_segun_angulo(angulo_jugador, player["velocidad"])[0]
            #player["rect"].centery -= mover_segun_angulo(angulo_jugador, player["velocidad"])[1]

    


    # Manejar disparos de enemigos(direccion, velocidad, colision con jugador y eliminarlos cuando salgan de la pantalla)
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
                SONIDO_IMPACTO_MUNICION.play()

                contador_player_hit = milisegundos
        
        if out_of_screen(disparo_enemigo["rect"], ANCHO, ALTO):
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
    
    PANTALLA.blit(FONDO_PARTIDA, ORIGEN)

    PANTALLA.blit(player["imagen"], player["rect"].topleft)

    for disparo_enemigo in disparos_enemigos:
        if disparo_enemigo:
            PANTALLA.blit(disparo_enemigo["imagen"], disparo_enemigo["rect"])

    for disparo in disparos_jugador:
        if disparo:
            PANTALLA.blit(disparo["imagen"], disparo["rect"])

    for enemigo in enemigos:
        PANTALLA.blit(enemigo["imagen"], enemigo["rect"])
    
    ##########     FIN DEL JUEGO     ##########

    if player["vidas"] == 0:
        flags_pantallas["fin"] = True
    
    while flags_pantallas["fin"]:
        if not flags_pantallas["puntajes_guardados"]:
            diccionario_puntajes = contar_puntaje(contador_enemigos_muertos, milisegundos)

            guardar_puntajes(diccionario_puntajes)

            flags_pantallas["puntajes_guardados"] = True
    
        flags_pantallas = fin_del_juego(PANTALLA, ORIGEN, ESTILO_INTERFAZ, RECT_VENTANA_FIN, CENTRO_RECT_TITULO_VENTANA_FIN, "El bote ha sido botado", BOTONES, diccionario_puntajes, ARCHIVO_MUSICA_FIN, VOLUMEN_MUSICA, flags_pantallas)
    
        if flags_pantallas["estadisticas"]:
            flags_pantallas = estadisticas(PANTALLA, ESTILO_INTERFAZ, RECT_VENTANA_FIN, diccionario_puntajes, CENTRO_RECT_TITULO_VENTANA_FIN, "Estadisticas", BOTONES, flags_pantallas)

    pygame.display.flip()

salir()

    