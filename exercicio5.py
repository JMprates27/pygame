import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exercicio 5")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, screen_height, 0)


def draw_quad(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 100, y)
    glVertex2f(x + 100, y + 100)
    glVertex2f(x, y + 100)
    glEnd()


def draw_triangle(x, y):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x - 100, y + 173.21)
    glVertex2f(x + 100, y + 173.21)
    glEnd()


def draw_circle(cx, cy, radius, num_segments):
    theta = 2 * math.pi / num_segments
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)  # Centro do círculo
    for i in range(num_segments + 1):
        x = radius * math.cos(i * theta)
        y = radius * math.sin(i * theta)
        glVertex2f(x + cx, y + cy)
    glEnd()


done = False
init_ortho()

# Variáveis para controlar se os objetos serão desenhados
draw_triangle_flag = False
draw_quad_flag = False
draw_circle_flag = False

reflect_triangle = False
reflect_circle = False
reflect_quad = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == K_1:
                draw_triangle_flag = not draw_triangle_flag
            if event.key == K_2:
                draw_circle_flag = not draw_circle_flag
            if event.key == K_3:
                draw_quad_flag = not draw_quad_flag

            # Alternar reflexões
            if event.key == K_q and draw_triangle_flag:
                reflect_triangle = not reflect_triangle
            if event.key == K_w and draw_circle_flag:
                reflect_circle = not reflect_circle
            if event.key == K_e and draw_quad_flag:
                reflect_quad = not reflect_quad

    glClear(GL_COLOR_BUFFER_BIT)

    # Desenhar o triângulo e aplicar a reflexão se necessário
    if draw_triangle_flag:
        glPushMatrix()
        if reflect_triangle:
            glTranslatef(500, 286.61, 0)  # Mover para o centro do triângulo
            glScalef(1.0, -1.0, 1.0)  # Refletir sobre o eixo X
            glTranslatef(-500, -286.61, 0)  # Voltar para a posição original
        draw_triangle(500, 200)
        glPopMatrix()

    # Desenhar o círculo e aplicar a reflexão
    if draw_circle_flag:
        glPushMatrix()
        if reflect_circle:
            glTranslatef(800, 750, 0)  # Mover para o centro do círculo
            glScalef(-1.0, 1.0, 1.0)  # Refletir sobre o eixo Y
            glTranslatef(-800, -750, 0)  # Voltar para a posição original
        draw_circle(800, 750, 40, 100)
        glPopMatrix()

    # Desenhar o quadrado e aplicar a reflexão
    if draw_quad_flag:
        glPushMatrix()
        if reflect_quad:
            glTranslatef(300, 500, 0)  # Mover para o centro do quadrado
            glScalef(-1.0, -1.0, 1.0)  # Refletir sobre ambos os eixos
            glTranslatef(-300, -500, 0)  # Voltar para a posição original
        draw_quad(300, 500)
        glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
