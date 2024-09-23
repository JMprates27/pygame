import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

triangle_points1 = [(400, 100), (300, 400), (500, 400)]
triangle_points2 = [(600, 100), (500, 400), (700, 400)]

view_mode = 'filled'

def draw_triangle(mode):
    if mode == 'filled' or mode == 'all':
        pygame.draw.polygon(screen, green, triangle_points1)
        pygame.draw.polygon(screen, red, triangle_points2)

    if mode == 'outline' or mode == 'all':
        pygame.draw.polygon(screen, green, triangle_points1, 2)
        pygame.draw.polygon(screen, red, triangle_points2, 2)

    if mode == 'points' or mode == 'all':
        for point in triangle_points1:
            pygame.draw.circle(screen, green, point, 5)
        for point in triangle_points2:
            pygame.draw.circle(screen, red, point, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                view_mode = 'filled'
            elif event.key == pygame.K_a:
                view_mode = 'outline'
            elif event.key == pygame.K_s:
                view_mode = 'points'
            elif event.key == pygame.K_d:
                view_mode = 'all'

    screen.fill(black)

    draw_triangle(view_mode)

    pygame.display.flip()
