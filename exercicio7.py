import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_width = 1200
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exercicio 7")


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, screen_height, 0)

def draw_line():
    glLineWidth(5.0)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(110, 775)
    glVertex2f(190, 775)
    glEnd()

def draw_quad():
    glColor3f(0.5,0.5,0.5)
    glBegin(GL_QUADS)
    glVertex2f(100.0, 800.0)
    glVertex2f(200.0, 800.0)
    glVertex2f(200.0, 700.0)
    glVertex2f(100.0, 700.0)
    glEnd()

def draw_triangle():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 700.0)
    glVertex2f(200.0, 700.0)
    glVertex2f(150.0, 630.0)
    glEnd()

def draw_circle(cx, cy, radius, num_segments):
    glColor3f(0.0, 0.0, 1.0)  # Cor azul (R = 0.0, G = 0.0, B = 1.0)
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

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT)

    draw_quad()
    draw_triangle()
    draw_circle(180, 730, 15, 100)  # Circulo com centro (175, 750), raio 30 e 100 segmentos
    draw_circle(120, 730, 15, 100)
    draw_line()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()