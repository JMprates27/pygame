import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exercicio 1")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, screen_height, 0)

def draw_point(x, y, size): #esses parametros vão servir para a função de desenhar as linhas
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_line():
    if len(clicks) >= 2:
        glBegin(GL_LINES)
        for click in clicks:
            glVertex2f(click[0], click[1])
        glEnd()

done = False
init_ortho()
clicks = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == MOUSEBUTTONDOWN:
            clicks.append(pygame.mouse.get_pos())

    glClear(GL_COLOR_BUFFER_BIT)

    for click in clicks:
        draw_point(click[0], click[1], 1)

    draw_line()
    draw_point(screen_width/2, screen_height/2, 15)
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()