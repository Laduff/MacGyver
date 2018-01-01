import pygame
from pygame.locals import *
from random import randrange


class Maze:
    def __init__(self, file):
        self.file = file
        self.maze = []
        
    def load_maze(self):
        with open(self.file, "r") as f:
            for line in f:
                cases = []
                
                for character in line:
                    if character != "\n":
                        cases.append(character)
                self.maze.append(cases)
        self.max_loot = 0
        
        while self.max_loot < 3:
            #generate a random number between 0 and 14.
            x_loot = randrange(0, 14)
            y_loot = randrange(0, 14)

            #check if the result of random is equal "O"
            if self.maze[x_loot][y_loot] == "O":
                #replace them by an "L" for loot
                self.maze[x_loot][y_loot] = "L"
                #increment +1 on the max_loot to stop at max_loot = 3
                self.max_loot += 1

    def print_maze(self, window):
        mur = pygame.image.load("IMAGES/mur.png").convert()
        fin = pygame.image.load("IMAGES/mechant.png").convert()
        loot = pygame.image.load("IMAGES/potion.png").convert()
        loot = pygame.transform.scale(loot, (30, 30))
                                 
        num_line = 0

        for line in self.maze:

            num_case = 0

            for case in line:
                x = num_case * 30
                y = num_line * 30

                if case == "X":
                    window.blit(mur, (x, y))
                elif case == "F":
                    window.blit(fin, (x, y))
                elif case == "L":
                    window.blit(loot, (x, y))

                num_case += 1
            num_line += 1

    def is_valid_case(self, y, x):
        return self.maze[y][x] != "X" 
