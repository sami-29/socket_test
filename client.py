#importing modules

import pygame
from network import Network
import pickle
from player import Player

#-------------------
#windows parameters
width = 500
height = 500
win=pygame.display.set_mode((width, height))
pygame.display.set_caption('client')

def redrawWindow(win, player, player2):#draw window
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main(): #main game loop
    run = True
    n = Network()
    P1 = n.getP()
    clock = pygame.time.Clock()
    

    while run:
        clock.tick(60)
        P2 = n.send(P1)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        

        P1.move()
        redrawWindow(win, P1, P2)

main()
