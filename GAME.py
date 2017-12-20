"""
Welcome to the MacGyver game !

Use controls to drive the MacGyver's character directly to the end.

Script Python
Files : GAME.py, classes.py, constantes.py + images
"""

import pygame
from pygame.locals import *

from classes import *

"#Init Pygame"
my_pygame = Pygame()

"#Init background"
fond = my_pygame.load_image("IMAGES/fond.jpg").convert()
my_pygame.blit(fond)
my_pygame.timer_tick(30)

"#Init maze"
maze = Maze("maze.txt")
maze.load_maze()
maze.print_maze(my_pygame)

"#Init hero"
hero = Macgyver(maze)
hero_image = my_pygame.load_image("IMAGES/macgyver.png").convert()
my_pygame.blit(hero_image)

"#font"
myfont = pygame.font.SysFont("Comic", 100)
myfont_counter = pygame.font.SysFont("Arial", 25)
"#Init nb loot and counter"
nb_loot = 0
counter = myfont_counter.render("x 0", False, (255, 255, 255))
counter_image = my_pygame.load_image("IMAGES/potion.png").convert()
counter_image = pygame.transform.scale(counter_image, (30, 30))

"#End message"
win = myfont.render("Victory !", False, (255, 255, 255))
loose = myfont.render("You loose !", False, (255, 255, 255))

"#refresh"
my_pygame.flip()

continuer = 1
while continuer:

    for event in my_pygame.get_event():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.move("right")
            elif event.key == K_LEFT:
                hero.move("left")
            elif event.key == K_UP:
                hero.move("up")
            elif event.key == K_DOWN:
                hero.move("down")

    if maze.maze[hero.case_y][hero.case_x] == "L":
        maze.maze[hero.case_y][hero.case_x] = "O"
        nb_loot += 1
        counter = myfont_counter.render("x " + str(nb_loot), False, (255,255,255))
    
    my_pygame.blit(fond, (0, 0))
    maze.print_maze(my_pygame)
    my_pygame.blit(hero_image, (hero.x, hero.y))
    my_pygame.blit(counter, (30, 30 * 14))
    my_pygame.blit(counter_image, (0, 30*14))
    
    my_pygame.flip()
        
    #END. if hero is on the "F" case : stop music and display message"
    if maze.maze[hero.case_y][hero.case_x] == "F":
        if nb_loot == 4:
            my_pygame.blit(win, (100, 200))
            my_pygame.flip()
            my_pygame.stop_music()
            continuer = 0

        else:
            my_pygame.blit(loose, (45, 200))
            my_pygame.flip()
            my_pygame.stop_music()
            continuer = 0
