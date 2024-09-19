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

def draw_quad():
    glBegin(GL_QUADS)
    glVertex2f(100.0, 800.0)
    glVertex2f(200.0, 800.0)
    glVertex2f(200.0, 700.0)
    glVertex2f(100.0, 700.0)
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(500.0, 200.0)
    glVertex2f(400.0, 373.21)
    glVertex2f(600.0, 373.21)
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
    draw_point(screen_width/2, screen_height/2, 15) #dividindo esses valores por 2 posiciona o ponto no centro
    draw_quad()
    draw_triangle()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()