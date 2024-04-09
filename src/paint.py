import pygame
from pygame.math import Vector2
import random

pygame.font.init()
pygame.display.init()

screen = pygame.display.set_mode([2200, 1300])

class Circle:
    def __init__(self, pos, color, radius):
        self.pos = pos
        self.color = color
        self.radius = radius

def run():

    circles = []

    running = True
    size = 5
    color = (255, 0, 0)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                size+=3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                size-=3

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:# red color
                color = (255, 0, 0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:# blue color
                color = (0, 0, 255)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:# green color
                color = (0, 255, 0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:# clear screen
                circles = []

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    circles.append( Circle(event.pos, color, size) )

            if event.type == pygame.MOUSEMOTION:

                buttons = pygame.mouse.get_pressed()
                b1 = buttons[0]
                if b1:
                     circles.append( Circle(event.pos, color, size) )


        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (50, 50), size)

        for c in circles:
            pygame.draw.circle(screen, c.color, c.pos, c.radius)

        pygame.display.flip()


run()