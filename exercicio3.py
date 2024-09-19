import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Triangulo Movel")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)


# Variáveis para armazenar o ângulo de rotação, o fator de escala e as posições de translação
rotation_angle = 0
scale_factor = 1.0  # Fator de escala
pos_x = 0.0  # Posição no eixo X
pos_y = 0.0  # Posição no eixo Y

done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Captura o estado das teclas
    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        done = True

    # Gira para esquuerda e direita utilizando as setas para direita e para esquerda
    if keys[K_RIGHT]:
        rotation_angle -= 8
    if keys[K_LEFT]:
        rotation_angle += 8

    # Aumenta e diminui a escala com as setas para cima e para baixo (com um limite minimo)
    if keys[K_UP]:
        scale_factor += 0.05
    if keys[K_DOWN]:
        scale_factor -= 0.05
        if scale_factor < 0.1:
            scale_factor = 0.1

    # Movimentação do triângulo usando WASD
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

    # Aplica a translação, rotação e escala ao triângulo
    glTranslatef(pos_x, pos_y, 0)  # Move o triângulo com base nas posições X e Y
    glRotatef(rotation_angle, 0, 0, 1)  # Rotaciona o valor rotation_angle no eixo Z
    glScalef(scale_factor, scale_factor, 1)  # Aplica a escala no eixo X e Y

    glBegin(GL_TRIANGLES)
    glVertex2i(0, 0)
    glVertex2i(100, 0)
    glVertex2i(0, 100)
    glEnd()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()