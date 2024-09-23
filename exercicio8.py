import pygame as pg

pg.init()

BLUE = pg.Color('dodgerblue3')
ORANGE = pg.Color('chocolate1')
GREEN = pg.Color('olivedrab')
YELLOW = pg.Color('goldenrod1')
PURPLE = pg.Color('darkorchid4')
PINK = pg.Color('maroon2')

pg.display.set_caption("Exercicio 8")

done = False
screen = pg.display.set_mode((700, 700))
cores = [BLUE,ORANGE,GREEN,YELLOW,PURPLE,PINK,ORANGE,YELLOW,PINK,BLUE,GREEN,PURPLE,YELLOW,PURPLE,BLUE,GREEN,PINK,ORANGE,ORANGE,PINK,GREEN,BLUE,PURPLE,YELLOW,PURPLE,GREEN,BLUE,PINK,YELLOW,ORANGE,PINK,PURPLE,YELLOW,GREEN,ORANGE,BLUE]
tamanho = 80
altura =  6*tamanho
largura = 6*tamanho
background = pg.Surface((largura, altura))  
i=0
for y in range(0, altura, tamanho):
    for x in range(0, largura, tamanho):
        rect = (x, y, tamanho, tamanho)
        pg.draw.rect(background, cores[i], rect)
        i=i+1

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.blit(background, (100, 100))

    pg.display.flip()
