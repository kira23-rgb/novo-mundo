import pygame
import math
import sys

# Classe Vetor


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def subtract(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def scale(self, s):
        return Vector(self.x * s, self.y * s)


# Inicialização
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coração Polar Animado")
clock = pygame.time.Clock()

origin = Vector(width // 2, height // 2)
mouse = Vector(width // 2, height // 2)  # valor inicial

# Função polar


def polar(rad, time, mouse_pos):
    rad += math.sin(time / 100)

    x = 16 * math.sin(rad) ** 3
    y = 13 * math.cos(rad) \
        - 5 * math.cos(2 * rad) \
        - 2 * math.cos(3 * rad) \
        - math.cos(4 * rad)

    scale = (math.sin(time / 10) + 3) * 4

    point = Vector(x * scale, -y * scale)
    mouse_vector = Vector(*mouse_pos)
    return point.add(origin.add(mouse_vector.subtract(origin).scale(0.5)))


# Loop principal
time = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))  # Fundo preto

    for i in range(0, 360, 2):
        rad = math.radians(i)
        pos = polar(rad, time, mouse)
        pygame.draw.circle(screen, (255, 0, 100), (int(pos.x), int(pos.y)), 2)

    pygame.display.flip()
    time += 1
    clock.tick(60)
