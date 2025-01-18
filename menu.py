from PPlay.window import *
from PPlay.gameimage import *


janela = Window(1920, 1080)
cenario = GameImage("Sprites/MH_Menu_fundo.png")
logo = GameImage("Sprites/MH_Titulo.png")
logo.x = janela.width/2 - logo.width/2
logo.y = 130
play = GameImage("Sprites/MH_botao_PLay.png")
play.x = janela.width/2 - play.width/2
play.y = 140 + 400
sair = GameImage("Sprites/MH_botao_sair.png")
sair.x = janela.width/2 - sair.width/2
sair.y = 210 + 400
mouse = Window.get_mouse()

while True:
    janela.set_title("MidnightHunt")
    cenario.draw()
    logo.draw()
    play.draw()
    sair.draw()
    if mouse.is_over_area([play.x, play.y],[play.x + play.width, play.y + play.height]) and mouse.is_button_pressed(1):
        #começa o jogo
    if mouse.is_over_area([sair.x, sair.y],[sair.x + sair.width, sair.y + sair.height]) and mouse.is_button_pressed(1):
        janela.close()

        janela.update()