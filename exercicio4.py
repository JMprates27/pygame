import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exercicio 4")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)


pos_x = 0.0  # Posição no eixo X
pos_y = 0.0  # Posição no eixo Y

done = False
init_ortho()

def draw_quad():
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)
    glVertex2f(200.0, 0.0)
    glVertex2f(200.0, 200.0)
    glVertex2f(0.0, 200.0)
    glEnd()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Captura o estado das teclas
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        done = True

    # Movimentação usando WASD
    if keys[K_d]:
        pos_x += 5
    if keys[K_a]:
        pos_x -= 5
    if keys[K_w]:
        pos_y += 5
    if keys[K_s]:
        pos_y -= 5

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Move o quadrado com base nas posições X e Y
    glTranslatef(pos_x, pos_y, 0)

    draw_quad()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()