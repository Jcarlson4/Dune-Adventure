from turtle import Screen
import pygame

class game_window():
#Create Background.
    screen = pygame.display.set_mode((800,600))
    screen.fill((0,0,0))

#Initialize the Game window.
    def initialize_window(self,screen):
        icon_image = pygame.image.load('dunes.png')
        pygame.init()
        pygame.display.set_caption("Dune Adventure")
        pygame.display.update()
        pygame.display.set_icon(icon_image)
        #start_button.draw()
        #exit_button.draw()


# Game loop
    def close_game(self):
        gameClose = False
        while not gameClose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameClose=True
        pygame.quit()
        quit()
    
#Diplay Text
    pygame.init()
    intro_image = pygame.image.load('duneth.png')
    font = pygame.font.Font('freesansbold.ttf',32)
    textx = 65
    texty = 50
    picturex = 100
    picturey = 90
    score = font.render("“God created Arrakis to train the faithful.”",True, (255,255,255))
    screen.blit(score,(textx,texty))
    screen.blit(intro_image,(picturex,picturey))


# Load buttons


#button class
class Button():
    start_img = pygame.image.load('start.png').convert_alpha()
    exit_img = pygame.image.load('exit.png').convert_alpha()

    #start_button = Button(100,200,start_img)
    #exit_button = Button(450,200,exit_img)
    
    def  __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        game_window.screen.blit(self.image,(self.rect.x,self.rect.y))

    





def main():
    initialization = game_window()
    initialization.initialize_window(initialization.screen)
    initialization.close_game()

    

if __name__ == "__main__":
    main()

Button()
game_window()
