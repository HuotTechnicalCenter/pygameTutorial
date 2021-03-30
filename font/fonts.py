import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()


windowWidth = 800
windowHeight = 500

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Text')

font = pygame.font.SysFont("sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic", 24, True, False)
img = font.render('hello', True, (255, 0, 0))
surface.blit(img, (20, 20))
surface.blit(img, (120, 120))

pygame.display.update()

fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)

    
def quitGame():
    pygame.quit()
    sys.exit()
    
while True:
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
                
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
