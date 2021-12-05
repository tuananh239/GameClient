import pygame, sys
from pygame.locals import *
from game_dinosaur import menu
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Game Client')

WIDTH = 1100
HEIGH = 600
SPACE = 50
WIDTH_BUTTON = 200
HEIGH_BUTTON = 50

screen = pygame.display.set_mode((WIDTH, HEIGH),0,32)
 
font_menu = pygame.font.SysFont(None, 50)
font = pygame.font.SysFont(None, 30)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        # Ve chu "Menu game"
        draw_text('Menu game', font_menu, (255, 255, 255), screen, WIDTH/2-100, HEIGH/2 - 100)
 
        mx, my = pygame.mouse.get_pos()

        # Ve 2 nut
        button_1 = pygame.Rect((WIDTH - WIDTH_BUTTON*2 - SPACE) / 2, (HEIGH - HEIGH_BUTTON)/2, 200, 50)
        button_2 = pygame.Rect((WIDTH - WIDTH_BUTTON*2 - SPACE) / 2 + WIDTH_BUTTON + SPACE, (HEIGH - HEIGH_BUTTON)/2, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.display.set_caption('Game Dinosaur')
                menu(death_count=0)
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Dino', font, (255, 255, 255), screen, (WIDTH - WIDTH_BUTTON*2 - SPACE) / 2 + 80, (HEIGH - HEIGH_BUTTON)/2 + HEIGH_BUTTON/3)
        draw_text('Snake', font, (255, 255, 255), screen, (WIDTH - WIDTH_BUTTON*2 - SPACE) / 2 + WIDTH_BUTTON + SPACE + 80, (HEIGH - HEIGH_BUTTON)/2 + HEIGH_BUTTON/3)

        # kiem tra xem nam nut gi
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Game snake', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()