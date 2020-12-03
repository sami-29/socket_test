import pygame

#player class
class Player():
    def __init__(self, x, y, width, height, color):#initialisation
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height) #current state of player object
        self.val = 3 # Constant value of moving
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect) #draw player 

    def move(self): #player movements
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val
        self.update()

    #updating new player values
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
