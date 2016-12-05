"""
Filename_rev: final project.py

Author: Drake Burgess

Email Address: drakehedoc@gmail.com

Date: 2016-06-13

Summary of Requirements: To make a final project that can make a vally with a house

Description: My code can make a house, plant, clouds, road, and a vally.

"""
"""
Building Code

this is the code thats builds the vally.
"""
import pygame, sys, random

# The Colurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 160, 0)
PLANT = (0, 100, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
DRAKE_BLUE = (0, 0, 50)
BROWN = (139, 69, 19)

# Place for imgies
def sky():
     pygame.draw.rect(screen, BLUE,( 0, 0, 600, 252))

def ground():
    pygame.draw.rect(screen, GREEN,( 0, 251, 600, 400))
    pygame.draw.circle(screen, GREEN, [30, 300], 120)
    pygame.draw.circle(screen, GREEN, [160, 290], 75)
    pygame.draw.circle(screen, GREEN, [460, 280], 60)

def sun():
    rand_x_diff = random.randrange(1, 600)
    rand_y_diff = random.randrange(0, 20)
    pygame.draw.circle(screen, YELLOW, [rand_x_diff, rand_y_diff], 60)

def clouds(x, y):
    rand_x_diff = random.randrange(1, 60)
    rand_y_diff = random.randrange(0, 10)
    pygame.draw.circle(screen, WHITE, [x + rand_x_diff, y + rand_y_diff], 30)
    rand_x_diff = random.randrange(1, 60)
    rand_y_diff = random.randrange(0, 10)
    pygame.draw.circle(screen, WHITE, [x + rand_x_diff, y + rand_y_diff], 30)

def home():
    # House and out line
    pygame.draw.circle(screen, BLACK, [300, 230], 52)
    pygame.draw.rect(screen, BLACK,(249, 227, 103, 76))
    pygame.draw.rect(screen, BROWN,(252, 230, 98, 70))
    # Window
    pygame.draw.line(screen, WHITE, [325, 275], [325, 250], 30)
    pygame.draw.line(screen, BLACK, [325, 275], [325, 250], 3)
    pygame.draw.line(screen, BLACK, [311, 263], [340, 263], 3)
    pygame.draw.line(screen, BLACK, [311, 250], [340, 250], 3)
    pygame.draw.line(screen, BLACK, [311, 275], [340, 275], 3)
    pygame.draw.line(screen, BLACK, [311, 275], [311, 250], 3)
    pygame.draw.line(screen, BLACK, [340, 275], [340, 250], 3)
    # door
    pygame.draw.line(screen, RED, [280, 300], [280, 250], 30)
    pygame.draw.circle(screen, DRAKE_BLUE, [290, 275], 5)
    pygame.draw.line(screen, BLACK, [265, 300], [265, 250], 3)
    pygame.draw.line(screen, BLACK, [295, 250], [265, 250], 3)
    pygame.draw.line(screen, BLACK, [295, 300], [295, 250], 3)

def road():
    pygame.draw.line(screen, BLACK, [280, 300], [280, 337], 30)
    pygame.draw.line(screen, BLACK, [0, 350], [280, 320], 30)
    pygame.draw.line(screen, WHITE, [0, 350], [265, 320], 3)

def plant():
    #PLANT 1
    rand_x_diff = random.randrange(370, 500)
    rand_y_diff = random.randrange(290, 340)
    pygame.draw.line(screen, PLANT, [rand_x_diff, rand_y_diff +50], [rand_x_diff, rand_y_diff], 8)
    pygame.draw.circle(screen, YELLOW, [rand_x_diff, rand_y_diff], 15)
    pygame.draw.circle(screen, BLACK, [rand_x_diff, rand_y_diff], 5)
    #PLANT 2
    rand_x_diff = random.randrange(500, 580)
    rand_y_diff = random.randrange(250, 350)
    pygame.draw.line(screen, PLANT, [rand_x_diff, rand_y_diff +50], [rand_x_diff, rand_y_diff], 8)
    pygame.draw.circle(screen, YELLOW, [rand_x_diff, rand_y_diff], 15)
    pygame.draw.circle(screen, BLACK, [rand_x_diff, rand_y_diff], 5)

'''
MAIN PROGRAM

the main part of my code.
'''

pygame.init()
clock = pygame.time.Clock()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Log House")

clock.tick(1)
# Here is thing at make the clouds not spawn even 10 sodies
drawn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if drawn == False:
        sky()
        clouds(20, 30)
        clouds(179, 100)
        clouds(389, 60)
        clouds(500, 150)
        sun()
        ground()
        home()
        road()
        plant()
        pygame.display.flip()
    drawn = True
