from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
# Configuração da janela e objetos do jogo
janela = Window(1920, 1080)
teclado = Window.get_keyboard()
cenario = GameImage("Sprites/MH_Background_1.png")
mouse = Window.get_mouse()
black = Sprite("Sprites/black.jpg")
a = GameImage("Sprites/MH_button_a.png")
a.x = 25
a.y = 280
d = GameImage("Sprites/MH_button_d.png")
d.x = 40 + a.width
d.y = 280
s = GameImage("Sprites/MH_button_s.png")
s.x = 1230
s.y = 400
espaco = GameImage("Sprites/MH_button_espaco.png")
espaco.x = 352
espaco.y = 280
m1 = GameImage("Sprites/MH_button_m1.png")
m1.x = 912
m1.y = 350




altura_chao = 530
# Sprites do jogador
playerR = Sprite("Sprites/MH_PlayerR.png")
playerL = Sprite("Sprites/MH_PlayerL.png")
corridaR = Sprite("Sprites/MH_Player_runR.png", frames=6)
corridaR.set_sequence_time(0, 5, 83, loop=True)
corridaL = Sprite("Sprites/MH_Player_runL.png", frames=6)
corridaL.set_sequence_time(0, 5, 83, loop=True)
atkR = Sprite("Sprites/MH_Player_attackR.png", frames=5)
atkR.set_sequence_time(0, 5, 15, loop=True)  # Sem loop no ataque
atkL = Sprite("Sprites/MH_Player_attackL.png", frames=5)
atkL.set_sequence_time(0, 5, 15, loop=True)  # Sem loop no ataque
puloR = Sprite("Sprites/MH_Player_jumpR.png", frames=3)
puloR.set_sequence_time(0, 2, 100, loop=False)
puloL = Sprite("Sprites/MH_Player_jumpL.png", frames=3)
puloL.set_sequence_time(0, 2, 100, loop=False)
esquivaR = Sprite("Sprites/MH_Player_DodgeR.png")
esquivaL = Sprite("Sprites/MH_Player_DodgeL.png")
hittrailR = Sprite("Sprites/MH_HittrailR.png", frames = 4)
hittrailR.set_sequence_time(0, 3, 15, loop=True)
hittrailL = Sprite("Sprites/MH_HittrailL.png", frames = 4)
hittrailL.set_sequence_time(0, 3, 15, loop=True)
hit = hittrailR
####
#inimigo estaca
#FASE 1
estacaR = Sprite("Sprites/MH_Inimigo_estacaR.png")
estacaL = Sprite("Sprites/MH_Inimigo_estacaL.png")
estacaCorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estacaCorridaR.set_sequence_time(0, 7, 83, loop=True)
estacaCorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estacaCorridaL.set_sequence_time(0, 7, 83, loop=True)
estacaAtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estacaAtkR.set_sequence_time(0, 4, 100, loop=True)
estacaAtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estacaAtkL.set_sequence_time(0, 4, 100, loop=True)
estacaMorto = Sprite("Sprites/MH_Inimigo_estaca_deadR.png")

estaca2R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca2L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca2CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca2CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca2CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca2CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca2AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca2AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca2AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca2AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca2Morto = Sprite("Sprites/MH_Inimigo_estaca_deadR.png")

#FASE 2
estaca3R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca3L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca3CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca3CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca3CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca3CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca3AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca3AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca3AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca3AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca3Morto = Sprite("Sprites/MH_Inimigo_estaca_deadR.png")

estaca4R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca4L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca4CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca4CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca4CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca4CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca4AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca4AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca4AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca4AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca4Morto = Sprite("Sprites/MH_inimigo_estaca_deadL.png")


estaca5R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca5L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca5CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca5CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca5CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca5CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca5AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca5AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca5AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca5AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca5Morto = Sprite("Sprites/MH_Inimigo_estaca_deadR.png")
#FASE 4
estaca6R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca6L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca6CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca6CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca6CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca6CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca6AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca6AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca6AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca6AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca6Morto = Sprite("Sprites/MH_Inimigo_estaca_deadL.png")

estaca7R = Sprite("Sprites/MH_Inimigo_estacaR.png")
estaca7L = Sprite("Sprites/MH_Inimigo_estacaL.png")
estaca7CorridaR = Sprite("Sprites/MH_Inimigo_estaca_runR.png", frames=7)
estaca7CorridaR.set_sequence_time(0, 7, 83, loop=True)
estaca7CorridaL = Sprite("Sprites/MH_Inimigo_estaca_runL.png", frames=7)
estaca7CorridaL.set_sequence_time(0, 7, 83, loop=True)
estaca7AtkR = Sprite("Sprites/MH_Inimigo_estaca_attackR.png", frames=4)
estaca7AtkR.set_sequence_time(0, 4, 100, loop=True)
estaca7AtkL = Sprite("Sprites/MH_Inimigo_estaca_atatackL.png", frames=4)
estaca7AtkL.set_sequence_time(0, 4, 100, loop=True)
estaca7Morto = Sprite("Sprites/MH_Inimigo_estaca_deadL.png")
#inimigo besta
#FASE 1
bestaR = Sprite("Sprites/MH_Inimigo_BestaR.png")
bestaL = Sprite("Sprites/MH_Inimigo_BestaL.png")
bestaCorridaR = Sprite("Sprites/MH_Inimigo_Besta_runR.png", frames=9)
bestaCorridaR.set_sequence_time(0, 9, 100, loop=True)
bestaCorridaL = Sprite("Sprites/MH_Inimigo_Besta_runL.png", frames=9)
bestaCorridaL.set_sequence_time(0, 9, 100, loop=True)
bestaAtkR = Sprite("Sprites/MH_Inimigo_Besta_attackR.png", frames=3)
bestaAtkR.set_sequence_time(0,2,100, loop=False)
bestaAtkL = Sprite("Sprites/MH_Inimigo_Besta_attackL.png", frames=3)
bestaAtkL.set_sequence_time(0,2,100, loop=False)
bestaReloadR = Sprite("Sprites/MH_Inimigo_Besta_reloadR.png",frames=5)
bestaReloadR.set_sequence_time(0,5,83, loop=False)
bestaReloadL = Sprite("Sprites/MH_Inimigo_Besta_reloadL.png",frames=5)
bestaReloadL.set_sequence_time(0,5,83, loop=False)
bestaMorto = Sprite("Sprites/MH_Inimigo_Besta_deadR.png")
#FASE 2
besta2R = Sprite("Sprites/MH_Inimigo_BestaR.png")
besta2L = Sprite("Sprites/MH_Inimigo_BestaL.png")
besta2CorridaR = Sprite("Sprites/MH_Inimigo_Besta_runR.png", frames=9)
besta2CorridaR.set_sequence_time(0, 9, 100, loop=True)
besta2CorridaL = Sprite("Sprites/MH_Inimigo_Besta_runL.png", frames=9)
besta2CorridaL.set_sequence_time(0, 9, 100, loop=True)
besta2AtkR = Sprite("Sprites/MH_Inimigo_Besta_attackR.png", frames=3)
besta2AtkR.set_sequence_time(0,2,100, loop=False)
besta2AtkL = Sprite("Sprites/MH_Inimigo_Besta_attackL.png", frames=3)
besta2AtkL.set_sequence_time(0,2,100, loop=False)
besta2ReloadR = Sprite("Sprites/MH_Inimigo_Besta_reloadR.png",frames=5)
besta2ReloadR.set_sequence_time(0,5,83, loop=False)
besta2ReloadL = Sprite("Sprites/MH_Inimigo_Besta_reloadL.png",frames=5)
besta2ReloadL.set_sequence_time(0,5,83, loop=False)
besta2Morto = Sprite("Sprites/MH_Inimigo_Besta_deadL.png")


besta3R = Sprite("Sprites/MH_Inimigo_BestaR.png")
besta3L = Sprite("Sprites/MH_Inimigo_BestaL.png")
besta3CorridaR = Sprite("Sprites/MH_Inimigo_Besta_runR.png", frames=9)
besta3CorridaR.set_sequence_time(0, 9, 100, loop=True)
besta3CorridaL = Sprite("Sprites/MH_Inimigo_Besta_runL.png", frames=9)
besta3CorridaL.set_sequence_time(0, 9, 100, loop=True)
besta3AtkR = Sprite("Sprites/MH_Inimigo_Besta_attackR.png", frames=3)
besta3AtkR.set_sequence_time(0,2,100, loop=False)
besta3AtkL = Sprite("Sprites/MH_Inimigo_Besta_attackL.png", frames=3)
besta3AtkL.set_sequence_time(0,2,100, loop=False)
besta3ReloadR = Sprite("Sprites/MH_Inimigo_Besta_reloadR.png",frames=5)
besta3ReloadR.set_sequence_time(0,5,83, loop=False)
besta3ReloadL = Sprite("Sprites/MH_Inimigo_Besta_reloadL.png",frames=5)
besta3ReloadL.set_sequence_time(0,5,83, loop=False)
besta3Morto = Sprite("Sprites/MH_Inimigo_Besta_deadR.png")
#FASE 3
besta4R = Sprite("Sprites/MH_Inimigo_BestaR.png")
besta4L = Sprite("Sprites/MH_Inimigo_BestaL.png")
besta4CorridaR = Sprite("Sprites/MH_Inimigo_Besta_runR.png", frames=9)
besta4CorridaR.set_sequence_time(0, 9, 100, loop=True)
besta4CorridaL = Sprite("Sprites/MH_Inimigo_Besta_runL.png", frames=9)
besta4CorridaL.set_sequence_time(0, 9, 100, loop=True)
besta4AtkR = Sprite("Sprites/MH_Inimigo_Besta_attackR.png", frames=3)
besta4AtkR.set_sequence_time(0,2,100, loop=False)
besta4AtkL = Sprite("Sprites/MH_Inimigo_Besta_attackL.png", frames=3)
besta4AtkL.set_sequence_time(0,2,100, loop=False)
besta4ReloadR = Sprite("Sprites/MH_Inimigo_Besta_reloadR.png",frames=5)
besta4ReloadR.set_sequence_time(0,5,83, loop=False)
besta4ReloadL = Sprite("Sprites/MH_Inimigo_Besta_reloadL.png",frames=5)
besta4ReloadL.set_sequence_time(0,5,83, loop=False)
besta4Morto = Sprite("Sprites/MH_Inimigo_Besta_deadL.png")

####
lixo = GameImage("Sprites/lixo.png")
lixo.x = 223
lixo.y = 440
casa = GameImage("Sprites/casa.png")
casa.x = 331
casa.y = 367

caixa1 = GameImage("Sprites/caixa1.png")
caixa2 = GameImage("Sprites/caixa2.png")
caixa1.x=1170
caixa1.y=890
caixa2.x=1290
caixa2.y=840

poste = GameImage("Sprites/poste.png")
poste.y=495
poste.x=60

coisa1=GameImage("Sprites/coisa.png")
coisa2=GameImage("Sprites/coisa.png")
coisa3=GameImage("Sprites/coisa.png")
coisa1.y=616
coisa1.x=256
coisa2.y=350
coisa2.x=256
coisa3.y=500
coisa3.x=440


fase1=Sprite("Sprites/fase1.png")
fase1chao = GameImage("Sprites/fase1chao.png")
fase1desnivel = GameImage("Sprites/fase1desnivel.png")
fase2 = Sprite("Sprites/fase2.png")
fase2_1andar=GameImage("Sprites/fase2_1andar.png")
fase2_2andar=GameImage("Sprites/fase2_2andar.png")
fase2_3andar=GameImage("Sprites/fase2_3andar.png")
fasechao=fase1chao
chao=fase1chao

fase1chao.y = 520
fase1desnivel.y = 580
fase1desnivel.x=500

fase2_1andar.y = 950
fase2_2andar.y = 680
fase2_2andar.x = 260
fase2_3andar.y = 350+coisa2.height
fase2_3andar.x = 260

fase3=GameImage("Sprites/fase3.png")
fase3_1chao=GameImage("Sprites/fase3_1chao.png")
fase3_2chao=GameImage("Sprites/fase3_2chao.png")
fase3_3chao=GameImage("Sprites/fase3_3chao.png")
fase3_1chao.y = 569
fase3_2chao.y = 596
fase3_2chao.x = 600
fase3_3chao.y = 862
fase3_3chao.x = 638
fase3Teto = GameImage("Sprites/MH_fase3_teto.jpg")
fase3Teto.x = 900
fase3Teto.y = fase3_2chao.y

fase4 = GameImage("Sprites/MH_Fase4_chao.png")
fase4_chao = GameImage("Sprites/fase4_chao.png")
fase4_chao.y = janela.height - fase4_chao.height

fase5 = GameImage("Sprites/MH_FaseFim_chao.jpg")
fase5_chao = GameImage("Sprites/faseFimChao.png")
fase5_chao.y = janela.height - fase5_chao.height
# Configuração inicial do jogador
player = playerR  # Sprite inicial do jogador (olhando para a direita)
player.y = 250
player.x = janela.width / 10 - 100
corridaR.y = player.y
corridaL.y = player.y
hp = 1 #vida do player
delayPlayer = 1
ultimoAtk = 2
atk_cd = False
atk_cd_timer = 0
atk_time = 0
esquiva_cd = False
esquiva_cd_timer = 0
esquiva_time = 0
####
# ESTACAS DA FASE 1
estaca = estacaL
estaca.y = 506  # Estaca no topo do chão
estaca.x = 912  # ou a posição inicial desejada
velEstaca = 100
estaca.estado = "parado"
delayEstaca = 2
estaca.atk = False
estaca.ultimoAtk = 0
estaca.vivo = True

estaca2 = estaca2L
estaca2.y = 506
estaca2.x = 1612
estaca2.estado = "parado"
estaca2.atk = False
estaca2.ultimoAtk = 0
estaca2.vivo = True

#FASE 2
estaca3 = estaca3L
estaca3.y = 886
estaca3.x = 1000
estaca3.estado = "parado"
estaca3.atk = False
estaca3.ultimoAtk = 0
estaca3.vivo = True

estaca4 = estaca4R
estaca4.y = 608
estaca4.x = 332
estaca4.estado = "parado"
estaca4.atk = False
estaca4.ultimoAtk = 0
estaca4.vivo = True

estaca5 = estaca5L
estaca5.y = 334
estaca5.x = 1712
estaca5.estado = "parado"
estaca5.atk = False
estaca5.ultimoAtk = 0
estaca5.vivo = True
#FASE 4
estaca6 = estaca6L
estaca6.y = fase4_chao.y - estaca.height
estaca6.x = 912
estaca6.estado = "parado"
estaca6.atk = False
estaca6.ultimoAtk = 0
estaca6.vivo = True

estaca7 = estaca7L
estaca7.y = fase4_chao.y - estaca.height
estaca7.x = 1612
estaca7.estado = "parado"
estaca7.atk = False
estaca7.ultimoAtk = 0
estaca7.vivo = True

#BESTA DA FASE 1
besta = bestaL
besta.y = 500
besta.x = 1212
velBesta = 100
besta.areaBesta = False
besta.vivo = True
besta.ultimaFlecha = 0     #criar isso dnv pra cada inimigo de besta
besta.tiro = True
flechaDelay = 2.5

#FASE 2
besta2 = besta2R
besta2.y = 595
besta2.x = 632
besta2.areaBesta = False
besta2.vivo = True
besta2.ultimaFlecha = 0
besta2.tiro = True

besta3 = besta3L
besta3.y = 324
besta3.x = 700
besta3.areaBesta = False
besta3.vivo = True
besta3.ultimaFlecha = 0
besta3.tiro = True

besta4 = besta4L
besta4.y = fase4_chao.y - besta.height
besta4.x = 1212
besta4.areaBesta = False
besta4.vivo = True
besta4.ultimaFlecha = 0
besta4.tiro = True


#BOSS
bossR = Sprite("Sprites/MH_Inimigo_BossR.png")
bossL = Sprite("Sprites/MH_Inimigo_BossL.png")
bossAtkR = Sprite("Sprites/MH_Inimigo_Boss_attackR.png", 8)
bossAtkR.set_sequence_time(0,8,100,True)
bossAtkL = Sprite("Sprites/MH_Inimigo_Boss_attackL.png", 8)
bossAtkL.set_sequence_time(0,8,100,True)

boss = bossL
boss.x = 1600
boss.y = 754
boss.direcao = "esquerda"
boss.vivo = True
hpBoss = 3
velBoss = 150
boss.danocd = False
boss.danotimer = 0

#GARGULA
gargulaR = Sprite("Sprites/MH_Inimigo_gargulaR.png", frames=3)
gargulaR.set_sequence_time(0,3,150, loop=True)
gargulaL = Sprite("Sprites/MH_Inimigo_gargulaL.png", frames=3)
gargulaL.set_sequence_time(0,3,150, loop=True)
gargula_preatkR = Sprite("Sprites/MH_Inimigo_gargula_preAtkR.png")
gargula_preatkL = Sprite("Sprites/MH_Inimigo_gargula_preAtkL.png")
gargulaAtkR = Sprite("Sprites/MH_Inimigo_gargula_attackR.png")
gargulaAtkL = Sprite("Sprites/MH_Inimigo_gargula_attackL.png")

gargula = gargulaL
gargula.x = 1600
gargula.y = 600
gargula.direcao = "esquerda"
gargula.vivo = True
gargula.estado = "parado"
hpGargula = 5
velGargula = 500
tempo = 0
gargula.alvoy = player.y-player.height
gargula.alvox = player.x
gargula.danocd = False
gargula.danotimer = 0

vidaFull = GameImage("Sprites/lifeFull.png")
vidaFull.set_position(janela.width/2 - vidaFull.width/2, janela.height - 100)
vida80 = GameImage("Sprites/life80.png")
vida80.set_position(janela.width/2 - vidaFull.width/2, janela.height - 100)
vida60 = GameImage("Sprites/life60.png")
vida60.set_position(janela.width/2 - vidaFull.width/2, janela.height - 100)
vida40 = GameImage("Sprites/life40.png")
vida40.set_position(janela.width/2 - vidaFull.width/2, janela.height - 100)
vida20 = GameImage("Sprites/life20.png")
vida20.set_position(janela.width/2 - vidaFull.width/2, janela.height - 100)

####
# Velocidade
velplayer = 300
gravidade = 1000
forca_pulo = -550
vel_y = 0
no_ar = False

direcao_atual = "direita"
player.estado = "idle"

musica01 = Sound("Sounds/adventures-of-baby-ghost.mp3")
musica01.loop = True
musica01.play()

missSound = Sound("Sounds/MH_atk_miss.mp3")

titulo = Sprite("Sprites/MH_Titulo.png")
titulo.x = 200
titulo.y = 200
####
arrows = []#todas as flechas do inimigo


def criaFlecha(player, besta):#passe como paremetro o inimigo especifico tipo besta, besta2, besta3 e blablabla
    if besta.x > player.x:  # flecha para a esquerda
        flecha = Sprite("Sprites/arrowL.png")
        flecha.x = besta.x - flecha.width/2
        flecha.y = besta.y + besta.height -60
        flecha.direction = -1

    else:  # flecha para direita
        flecha = Sprite("Sprites/arrowR.png")
        flecha.x = besta.x + (flecha.width / 2)
        flecha.y = besta.y + besta.height - 60
        flecha.direction = 1

    arrows.append(flecha)
    #tiroFlecha()
def tiroFlecha():#move as flechas
    global hp
    for i in arrows:
        i.move_x(1000 * dt * i.direction)
        if i.x < 0 or i.x > janela.width:
            arrows.remove(i)
        if i.collided(player):
            if player.estado != "esquiva":
                arrows.remove(i)
                hp -= 1
                print(hp)
        if i.collided(hit):
                arrows.remove(i)
                print("tankou")

####
def movEstaca(player, estaca,hit):
    global hp
    if estaca.collided(hit) or (estaca.collided(player) and player.estado == "atacando"):
        estaca.vivo = False
    if estaca.vivo:
        if estaca.atk:
            estaca.ultimoAtk += janela.delta_time()
        if estaca.ultimoAtk > delayEstaca:
            estaca.atk = False
        if player.x < estaca.x :
            estaca.estado = "andando"
        if player.x > estaca.x:
            estaca.estado = "andando"

        if estaca.estado == "andando":
            if player.x < estaca.x and not estaca.collided(player):
                estaca.x -= velEstaca * dt
                estacaCorridaL.x = estaca.x
                estacaCorridaL.y = estaca.y
                estacaCorridaL.draw()
                estacaCorridaL.update()
            if player.x > estaca.x and not estaca.collided(player):#
                estaca.x += velEstaca * dt
                estacaCorridaR.x = estaca.x
                estacaCorridaR.y = estaca.y
                estacaCorridaR.draw()
                estacaCorridaR.update()

        if estaca.collided(player) and player.estado != "atacando":
            if estaca.atk == False:
                if player.x <= estaca.x:
                    estacaAtkL.x = estaca.x
                    estacaAtkL.y = estaca.y
                    estacaAtkL.draw()
                    estacaAtkL.update()
                   #
                    if player.estado != "esquiva":
                        estaca.atk = True
                        estaca.ultimoAtk = 0
                        hp -= 1
                        print(hp)


                else:
                    estacaAtkR.x = estaca.x
                    estacaAtkR.y = estaca.y
                    estacaAtkR.play()
                    estacaAtkR.update()
                    estacaAtkR.draw()
                    if player.estado != "esquiva":
                        estaca.atk = True
                        estaca.ultimoAtk = 0
                        hp -= 1
                        print(hp)
                        estaca.ultimoAtk = 0
            if estaca.atk:
                if player.x <= estaca.x:
                    estacaAtkL.x = estaca.x
                    estacaAtkL.y = estaca.y
                    estacaAtkL.draw()
                    estacaAtkL.update()
                else:
                    estacaAtkR.x = estaca.x
                    estacaAtkR.y = estaca.y
                    estacaAtkR.draw()
                    estacaAtkR.update()
def movBesta(player, besta,hit):
    global flechaDelay
    if besta.collided(hit) or (estaca.collided(player) and player.estado == "atacando"):
        besta.vivo = False
    if besta.vivo:
        if player.x + 329 < besta.x and besta.areaBesta == False:
            besta.x -= velBesta * dt
            bestaCorridaL.x = besta.x
            bestaCorridaL.y = besta.y
            bestaCorridaL.draw()
            bestaCorridaL.update()
        if player.x + 329 > besta.x and besta.areaBesta == False:
            besta.x += velBesta * dt
            bestaCorridaR.x = besta.x
            bestaCorridaR.y = besta.y
            bestaCorridaR.draw()
            bestaCorridaR.update()
        #area de tiro do inimigo
        if besta.x > player.x:
            if besta.x - player.x <= 330:
                besta.areaBesta = True
            else:
                besta.areaBesta = False
        elif besta.x < player.x:
            if player.x - besta.x <= 330:
                besta.areaBesta = True
            else:
                besta.areaBesta = False
        if besta.areaBesta:
            besta.ultimaFlecha += dt
            if besta.ultimaFlecha < flechaDelay and besta.tiro == False:
                criaFlecha(player, besta)
                besta.ultimaFlecha = 0
                besta.tiro = True
                besta.draw()
        if besta.tiro == True:
            besta.ultimaFlecha += dt
            if player.x < besta.x:
                bestaReloadL.x = besta.x
                bestaReloadL.y = besta.y
                bestaReloadL.draw()
                bestaReloadL.update()
            if player.x > besta.x:
                bestaReloadR.x = besta.x
                bestaReloadR.y = besta.y
                bestaReloadR.draw()
                bestaReloadR.update()

        if besta.ultimaFlecha > flechaDelay:
            besta.ultimaFlecha = 0
            besta.tiro = False

def movBoss():
    global hp, hpBoss
    if hpBoss <= 0:
        boss.vivo = False
    if boss.vivo:
        if boss.direcao == "esquerda":
            boss.x -= velBoss * dt
            bossAtkL.x = boss.x
            bossAtkL.y = boss.y
            bossAtkL.draw()
            bossAtkL.update()
            if boss.x <= 715:
                boss.direcao = "direita"
            if boss.x > player.x > boss.x-48 and player.y > boss.y:
                hp -= 1
        elif boss.direcao == "direita":
            boss.x += velBoss * dt
            bossAtkR.x = boss.x
            bossAtkR.y = boss.y
            bossAtkR.draw()
            bossAtkR.update()
            if boss.x >= 1800:
                boss.direcao = "esquerda"
            if boss.x+48+boss.width > player.x > boss.x and player.y > boss.y:
                hp -= 1

        if boss.danotimer > 0:
            boss.danotimer -= 1
        else:
            boss.danocd = False

        if boss.collided(hit) or (boss.collided(player) and player.estado == "atacando"):
            if not boss.danocd:
                if boss.direcao == "direita":
                    if boss.x > player.x:
                        boss.danocd = True
                        boss.danotimer = 15
                        hpBoss -= 1
                else:
                    if boss.x < player.x:
                        boss.danocd = True
                        boss.danotimer = 15
                        hpBoss -= 1
                if boss.direcao == "esquerda":
                    boss.direcao = "direita"
                else:
                    boss.direcao = "esquerda"



def  movGargula():
    global hp, hpGargula, tempo
    if hpGargula == 0:
        gargula.vivo = False
    else:
        if gargula.estado == "parado":
            if gargula.x < player.x - gargula.width * 6:
                gargula.x += 200 * dt
                if gargula.y >= player.y - gargula.height * 2:
                    gargula.y -= 400 * dt
            elif gargula.x > player.x + gargula.width * 6:
                gargula.x -= 200 * dt
                if gargula.y >= player.y - gargula.height * 2:
                    gargula.y -= 400 * dt
            else:
                gargula.estado = "preataque"

        if gargula.estado == "parado":
            if gargula.direcao == "esquerda":
                gargulaL.draw()
                gargulaL.update()
            else:
                gargulaR.x = gargula.x
                gargulaR.y = gargula.y
                gargulaR.draw()
                gargulaR.update()

        if gargula.estado == "preataque":
            if gargula.direcao == "direita":
                gargulaR.draw()
            else:
                gargulaL.draw()

            tempo += dt
            if tempo >= 0.5:
                gargula.alvoy = player.y-player.height
                gargula.alvox = player.x
                gargula.estado = "atacando"
                tempo = 0

        if gargula.estado == "atacando":
            if gargula.alvox + gargula.width*6 >= gargula.x >= gargula.alvox - gargula.width*6:
                if gargula.alvox + gargula.width * 4 >= gargula.x >= gargula.alvox - gargula.width * 4 and gargula.y <= gargula.alvoy:
                    gargula.y += 400 * dt
                elif gargula.y >= gargula.alvoy - gargula.height * 2:
                    gargula.y -= 600 * dt
            if gargula.direcao == "esquerda":
                gargula.x -= velGargula * dt
                gargulaAtkL.x = gargula.x
                gargulaAtkL.y = gargula.y
                gargulaAtkL.draw()
                if gargula.x <= gargula.alvox - gargula.width*6 or gargula.x <= 0:
                    gargula.estado = "parado"
                    gargula.direcao = "direita"
            else:
                gargula.x += velGargula * dt
                gargulaAtkR.x = gargula.x
                gargulaAtkR.y = gargula.y
                gargulaAtkR.draw()
                if gargula.x >= gargula.alvox + gargula.width*6 or gargula.x+gargula.width >= janela.width:
                    gargula.estado = "parado"
                    gargula.direcao = "esquerda"
            if gargula.x + gargula.width > player.x > gargula.x and gargula.y + gargula.height + 32 > player.y > gargula.y - 32:
                if player.estado != "esquiva":
                    hp -= 1

        if gargula.danotimer > 0:
            gargula.danotimer -= 1
        else:
            gargula.danocd = False

        if gargula.collided(hit) or (gargula.collided(player) and player.estado == "atacando"):
            if not gargula.danocd:
                gargula.danocd = True
                gargula.danotimer = 15
                hpGargula -= 1


def verificar_colisao_caixas(player, caixa):
    global vel_y, no_ar  # Precisamos acessar essas variáveis globais

    # Checar colisão no topo da caixa (quando o jogador aterrissa na caixa)
    if player.y + player.height > caixa.y and player.y + player.height <= caixa.y + 10 and \
            player.x + player.width > caixa.x and player.x < caixa.x + caixa.width:
        player.y = caixa.y - player.height  # Corrige a posição do jogador para ficar no topo da caixa
        vel_y = 0  # Reseta a gravidade
        no_ar = False  # Define que o jogador está no chão
        return True

    # Checar colisão pelos lados da caixa (quando o jogador tenta atravessar)
    if player.x + player.width > caixa.x and player.x < caixa.x + caixa.width and \
            player.y + player.height > caixa.y and player.y < caixa.y + caixa.height:
        # Impede o jogador de atravessar pelos lados
        if player.x < caixa.x:  # Colisão no lado esquerdo da caixa
            player.x = caixa.x - player.width
        else:  # Colisão no lado direito da caixa
            player.x = caixa.x + caixa.width
        return True

    return False

def verificar_colisao_poste(player, poste):
    global vel_y, no_ar

    # 1. Colisão pelo topo do poste (somente se o jogador estiver caindo)
    if vel_y > 0 and player.y + player.height > poste.y and player.y + player.height <= poste.y + 10 and \
            player.x + player.width > poste.x and player.x < poste.x + poste.width:
        player.y = poste.y - player.height  # Ajusta posição para o topo do poste
        vel_y = 0  # Reseta a gravidade
        no_ar = False  # Define que o jogador não está mais no ar
        return True

    # 2. Colisão lateral com o poste
    if player.x + player.width > poste.x and player.x < poste.x + poste.width and \
            player.y + player.height > poste.y and player.y < poste.y + poste.height:
        # Evita atravessar pelos lados
        if player.x < poste.x:  # Colisão pelo lado esquerdo do poste
            player.x = poste.x - player.width
        else:  # Colisão pelo lado direito do poste
            player.x = poste.x + poste.width
        return True

    return False


def verificar_colisao_coisas(player, coisa):
    global vel_y, no_ar

    # Colisão no topo da coisa
    if player.y + player.height > coisa.y and player.y + player.height <= coisa.y + 10 and \
            player.x + player.width > coisa.x and player.x < coisa.x + coisa.width:
        player.y = coisa.y - player.height  # Ajuste para o topo da coisa
        vel_y = 0  # Reseta a gravidade
        no_ar = False  # Define que o jogador está no chão
        return True

    # Colisão lateral com a coisa
    if player.x + player.width > coisa.x and player.x < coisa.x + coisa.width and \
            player.y + player.height > coisa.y and player.y < coisa.y + coisa.height:
        # Evita atravessar pelos lados
        if player.x < coisa.x:  # Colisão pelo lado esquerdo da coisa
            player.x = coisa.x - player.width
        else:  # Colisão pelo lado direito da coisa
            player.x = coisa.x + coisa.width
        return True

    return False

fase=fase1
fps = 0
frames = 0
tempo_acumulado = 0
jogar = False
while True:
    print(f"Player x = {player.x} y = {player.y}")
    janela.set_title("MidnightHunt")
    dt = janela.delta_time()
    tempo_acumulado += dt
    vel_y += gravidade * dt
    player.y += vel_y * dt
    frames += 1
    if tempo_acumulado >= 1.0:
        fps = frames
        frames = 0
        tempo_acumulado = 0
    cenario.draw()
    fase.draw()
    if fase==fase1:
        fase1chao.draw()
    if player.x>530 and fase==fase1:
        if player.collided(fase1desnivel):
            player.y = fase1desnivel.y - player.height
            vel_y = 0
            no_ar = False

    if player.collided(fase1chao) and fase==fase1:
        player.y = fase1chao.y - player.height
        vel_y = 0
        no_ar = False

    if player.x > 1920 and fase == fase1:
        black.draw()
        janela.update()
        janela.delay(350)
        fase = fase2
        fasechao = fase2_1andar  # Define o novo chão da fase
        player.y=fase2_1andar.y-player.height
        player.x = 100
    if player.x > 1920 and fase == fase2:
        black.draw()
        janela.update()
        janela.delay(350)
        fase = fase3
        fasechao = fase3_1chao  # Define o novo chão da fase
        player.y = fase3_1chao.y - player.height
        player.x = 100
    if player.x > 1920 and fase == fase3:
        black.draw()
        janela.update()
        janela.delay(350)
        fase = fase4
        fasechao = fase4_chao
        player.y = fase4_chao.y - player.height
        player.x = 100

    if player.x < 400 and player.y > fase3_1chao.y - player.height + 30 and fase == fase3:
        player.y = fase3_1chao.y - player.height
        player.x = 100

    if player.x > 1920 and fase == fase4:
        black.draw()
        janela.update()
        janela.delay(350)
        fase = fase5
        fasechao = fase5_chao
        player.y = fase5_chao.y - player.height
        player.x = 100
    if fase == fase5:
        fase5_chao.draw()
    if fase == fase4:
        fase4_chao.draw()
    if fase==fase3:
        fase3_1chao.draw()
        fase3_2chao.draw()
        fase3_3chao.draw()
        coisa3.draw()
    if fase==fase2:
        poste.draw()
        caixa1.draw()
        caixa2.draw()
        coisa1.draw()
        coisa2.draw()
        fase2_1andar.draw()
        fase2_2andar.draw()
        fase2_3andar.draw()
    if fase==fase1:
        lixo.draw()
        casa.draw()
    if player.collided(fase2_1andar) and fase==fase2:
        player.y = fase2_1andar.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase2_2andar) and fase==fase2 and player.y<fase2_2andar.y:
        player.y = fase2_2andar.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase2_3andar) and fase==fase2 and player.y<fase2_3andar.y:
        player.y = fase2_3andar.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase3_1chao) and fase == fase3:
        player.y = fase3_1chao.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase3_2chao) and fase == fase3 and player. y < fase3_2chao.y:
        player.y = fase3_2chao.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase3_3chao) and fase == fase3:
        player.y = fase3_3chao.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase3Teto) and fase == fase3:
        player.y = fase3Teto.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase4_chao) and fase == fase4:
        player.y = fase4_chao.y - player.height
        vel_y = 0
        no_ar = False
    if player.collided(fase5_chao) and fase == fase5:
        player.y = fase5_chao.y - player.height
        vel_y = 0
        no_ar = False
    if teclado.key_pressed("ESC"):
        estado = "idle"
        hp = 0
        janela.close()#break
    if fase==fase1:
        colidiu_lixo = verificar_colisao_caixas(player, lixo)
        colidiu_casa = verificar_colisao_caixas(player, casa)
    if fase==fase2:
        colidiu_caixa1 = verificar_colisao_caixas(player, caixa1)
        colidiu_caixa2 = verificar_colisao_caixas(player, caixa2)
        colidiu_poste = verificar_colisao_poste(player, poste)
        colidiu_coisa1 = verificar_colisao_coisas(player, coisa1)
        colidiu_coisa2 = verificar_colisao_coisas(player, coisa2)
    if fase==fase3:
        colidiu_coisa3 = verificar_colisao_coisas(player, coisa3)

    if fase == fase3 and player.x > fase3_2chao.x and player.y > 630:
        if player.x <= 640:
            player.x += 5
    if fase == fase3 and player.y > fase3_2chao.y  and player.x <= fase3_2chao.x:
        if player.collided(fase3_2chao):
            player.x -= 5

    player_d = teclado.key_pressed("D")
    player_a = teclado.key_pressed("A")
    direcao = player_d - player_a
   # player.x += direcao * velplayer * dt
    ####
    if direcao > 0:
        if player.x < 1920 and fase != fase5 and fase != fase2:
            player.x += velplayer * dt
        elif fase == fase5:
            if player.x < 1920 - player.width:
                player.x += velplayer * dt
        elif fase == fase2:
            if player.y > 600:
                if player.x < 1920 - player.width:
                    player.x += velplayer * dt
            else:
                player.x += velplayer*dt
    elif direcao < 0:
        if player.x > 0:
            player.x -= velplayer * dt
        ####
    if player_d:
        direcao_atual = "direita"
        if not no_ar and player.estado != "atacando":
            player.estado = "correndo"
    elif player_a:
        direcao_atual = "esquerda"
        if not no_ar and player.estado != "atacando":
            player.estado = "correndo"
    elif not no_ar:
        player.estado = "idle"


    if teclado.key_pressed("SPACE") and not no_ar:
        vel_y = forca_pulo
        no_ar = True

    if no_ar and player.estado != "atacando":
        player.estado = "pulando"

    if player.estado == "correndo":
        if direcao_atual == "direita":
            corridaR.x = player.x
            corridaR.y = player.y
            corridaR.draw()
            corridaR.update()
        else:
            corridaL.x = player.x
            corridaL.y = player.y
            corridaL.draw()
            corridaL.update()

    elif player.estado == "idle":
        if direcao_atual == "direita":
            playerR.x = player.x
            playerR.y = player.y
            playerR.draw()
        else:
            playerL.x = player.x
            playerL.y = player.y
            playerL.draw()

    elif player.estado == "pulando":
        if direcao_atual == "direita":
            puloR.x = player.x
            puloR.y = player.y
            puloR.draw()
            puloR.update()
        else:
            puloL.x = player.x
            puloL.y = player.y
            puloL.draw()
            puloL.update()

    if mouse.is_button_pressed(1) and player.estado != "esquiva" and not atk_cd:
        missSound.play()
        posicaox = player.x
        posicaoy = player.y
        atk_cd = True
        atk_cd_timer = 55
        atk_time = 15
    if atk_time > 0:
        if direcao_atual == "direita":
            player.x += 5
            hit.x = posicaox+player.width+75
            hit.y = posicaoy
            hittrailR.x = hit.x
            hittrailR.y = hit.y
            hittrailR.draw()
            hittrailR.update()
        else:
            player.x -= 5
            hit.x = posicaox - 75 - hit.width
            hit.y = posicaoy
            hittrailL.x = hit.x
            hittrailL.y = hit.y
            hittrailL.draw()
            hittrailL.update()
        player.estado = "atacando"
        atk_time -= 1
    else:
        hit.y = - 64
        player.estado = "idle"
    if atk_cd_timer <= 0:
        atk_cd = False
    else:
        atk_cd_timer -= 1
    if player.estado == "atacando":
        if direcao_atual == "direita":
            atkR.x = player.x
            atkR.y = player.y
            atkR.draw()
            atkR.update()
        elif direcao_atual == "esquerda":
            atkL.x = player.x
            atkL.y = player.y
            atkL.draw()
            atkL.update()



    if player.estado != "atacando" and no_ar and not mouse.is_button_pressed(1):
        player.estado = "pulando"

    if teclado.key_pressed("s") and not no_ar and not esquiva_cd and player.estado != "atacando":
        esquiva_cd = True
        esquiva_cd_timer = 110
        esquiva_time = 15
    if esquiva_time > 0:
        player.estado = "esquiva"
        esquiva_time -= 1
    else:
        player.estado = "idle"
    if esquiva_cd_timer <= 0:
        esquiva_cd = False
    else:
        esquiva_cd_timer -= 1
    if player.estado == "esquiva":
        if direcao_atual == "direita":
            player.x += 10
            esquivaR.x = player.x
            esquivaR.y = player.y
            esquivaR.draw()
        if direcao_atual == "esquerda":
            player.x -= 10
            esquivaL.x = player.x
            esquivaL.y = player.y
            esquivaL.draw()


    # Gerando inimigos de cada fase
    if fase == fase1:
        a.draw()
        d.draw()
        s.draw()
        espaco.draw()
        m1.draw()
        #respanw
        if hp <1 or player.y > chao.y:
            arrows = []
            player.y = 250
            player.x = janela.width / 10 - 100
            estaca.vivo = True
            estaca.y = 506  # Estaca no topo do chão
            estaca.x = 912
            estaca2.vivo = True
            estaca2.y = 506
            estaca2.x = 1612
            besta.vivo = True
            besta.y = 500
            besta.x = 1212
            hp = 1
        if estaca.x - player.x < 530 and player.x > 550:
            movEstaca(player, estaca, hit)
        elif estaca.vivo:
            estaca.draw()
        if estaca2.x - player.x <= 530 and player.x > 550:
            movEstaca(player, estaca2, hit)
        elif estaca2.vivo:
            estaca2.draw()
        if besta.x - player.x < 530 and player.x > 550:
            movBesta(player, besta, hit)
        elif besta.vivo:
            besta.draw()

        if not estaca.vivo:
            estacaMorto.x = estaca.x
            estacaMorto.y = estaca.y + estaca.height - 16
            estacaMorto.draw()
        if not estaca2.vivo:
            estaca2Morto.x = estaca2.x
            estaca2Morto.y = estaca2.y + estaca.height - 16
            estaca2Morto.draw()
        if not besta.vivo:
            bestaMorto.x = besta.x
            bestaMorto.y = besta.y + besta.height- 16
            bestaMorto.draw()
    if fase == fase2:
        #reespawn
        if hp < 1:
            arrows = []
            player.x = 100
            player.y = fase2_1andar.y-player.height
            estaca3.vivo = True
            estaca3.y = 886
            estaca3.x = 1000
            estaca4.vivo = True
            estaca4.y = 608
            estaca4.x = 332
            estaca5.vivo = True
            estaca5.y = 334
            estaca5.x = 1712
            besta2.vivo = True
            besta2.y = 595
            besta2.x = 632
            besta3.vivo = True
            besta3.y = 324
            besta3.x = 700
            hp = 1
        #estacas
        if estaca3.x - player.x <= 530 and estaca3.y - player.y <= 148 and estaca3.x < 1160:
            movEstaca(player, estaca3, hit)
        elif estaca3.vivo:
            estaca3.draw()
        if player.x - estaca4.x <= 530 and player.x >= 282 and (player.y - estaca4.y <= 130 and player.y > 354):
            movEstaca(player, estaca4, hit)
        elif estaca4.vivo:
            estaca4.draw()
        if estaca5.x - player.x <= 530 and player.x >= 282 and (player.y - estaca5.y <= 130 or estaca5.y - player.y >= 140):
            movEstaca(player, estaca5, hit)
        elif estaca5.vivo:
            estaca5.draw()
        #bestas
        if player.x - besta2.x < 530 and player.x >= 282 and  (player.y - besta2.y <= 140 and player.y > 354):
             movBesta(player, besta2, hit)
        elif besta2.vivo:
            besta2.draw()
        if besta3.x - player.x <= 530 and player.x >= 282 and  (player.y - besta3.y <= 140 or besta3.y - player.y >= 140):
            movBesta(player, besta3, hit)
        elif besta3.vivo:
            besta3.draw()

        if not estaca3.vivo:
            estaca3Morto.x = estaca3.x
            estaca3Morto.y = estaca3.y + estaca.height - 16
            estaca3Morto.draw()
        if not estaca4.vivo:
            estaca4Morto.x = estaca4.x
            estaca4Morto.y = estaca4.y + estaca.height - 16
            estaca4Morto.draw()
        if not estaca5.vivo:
            estaca5Morto.x = estaca5.x
            estaca5Morto.y = estaca5.y + estaca.height - 16
            estaca5Morto.draw()
        if not besta2.vivo:
            besta2Morto.x = besta2.x
            besta2Morto.y = besta2.y + besta.height- 16
            besta2Morto.draw()
        if not besta3.vivo:
            besta3Morto.x = besta3.x
            besta3Morto.y = besta3.y + besta.height- 16
            besta3Morto.draw()
    if fase == fase3:
        if hp == 0 or player.y > janela.height:
            player.x = 100
            player.y = fase3_1chao.y - player.height
            boss.x = 1600
            boss.y = 754
            boss.direcao = "esquerda"
            hp = 1
            hpBoss = 3
        if player.y > 540 and player.x > fase3_2chao.x:
            movBoss()
        elif boss.vivo:
            boss.draw()
    if fase == fase4:
        if hp == 0:
            arrows = []
            player.y = fase4_chao.y - player.height
            player.x = 100
            estaca6.y = fase4_chao.y - estaca.height
            estaca6.x = 912
            estaca6.vivo = True
            estaca7.y = fase4_chao.y - estaca.height
            estaca7.x = 1612
            estaca7.vivo = True
            besta4.y = fase4_chao.y - besta.height
            besta4.x = 1212
            besta4.vivo = True

            hp = 1


        if estaca6.x - player.x < 530 and player.x > 550:
            movEstaca(player, estaca6, hit)
        elif estaca6.vivo:
            estaca6.draw()
        if estaca7.x - player.x <= 530 and player.x > 550:
            movEstaca(player, estaca7, hit)
        elif estaca7.vivo:
            estaca7.draw()
        if besta4.x - player.x < 700 and player.x > 550:
            movBesta(player, besta4, hit)
        elif besta4.vivo:
            besta4.draw()
        if not estaca6.vivo:
            estaca6Morto.x = estaca6.x
            estaca6Morto.y = estaca6.y + estaca.height - 16
            estaca6Morto.draw()
        if not estaca7.vivo:
            estaca7Morto.x = estaca7.x
            estaca7Morto.y = estaca7.y + estaca.height - 16
            estaca7Morto.draw()
        if not besta4.vivo:
            besta4Morto.x = besta4.x
            besta4Morto.y = besta4.y + besta.height - 16
            besta4Morto.draw()
    if fase == fase5:
        if hp == 0:
            player.y = fase5_chao.y - player.height
            player.x = 10
            gargula.x = 1600
            gargula.y = 600
            gargula.direcao = "esquerda"
            gargula.vivo = True
            gargula.estado = "parado"
            hpGargula = 5
            hp = 1
        if gargula.vivo:
            movGargula()
        else:
            missSound.stop()
            Sprite("Sprites/MH_end.png").draw()
            titulo.draw()
        if hpGargula == 5:
            vidaFull.draw()
        elif hpGargula == 4:
            vida80.draw()
        elif hpGargula == 3:
            vida60.draw()
        elif hpGargula == 2:
            vida40.draw()
        elif hpGargula == 1:
            vida20.draw()

    tiroFlecha()
    for i in arrows:
        i.draw()
    # Atualizar a janela
    janela.update()