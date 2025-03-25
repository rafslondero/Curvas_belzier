import pygame
import random
import math

# Cores fixas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class DesenhaCurvas:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Curvas de Bézier Dinâmicas")

        self.screen.fill(WHITE)

        self.points = []
        self.curve_color = self.random_color()  # Cor inicial aleatória

    def random_color(self):
        """ Gera uma cor aleatória no formato RGB. """
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def binomial_coefficient(self, n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def bezier_point(self, points, t):
        n = len(points) - 1
        x, y = 0, 0

        for i, (px, py) in enumerate(points):
            coefficient = self.binomial_coefficient(n, i)
            bernstein = coefficient * ((1 - t) ** (n - i)) * (t ** i)
            x += px * bernstein
            y += py * bernstein

        return int(x), int(y)

    def draw(self):
        self.screen.fill(WHITE)

        # Desenha os pontos de controle
        for p in self.points:
            pygame.draw.circle(self.screen, BLACK, p, 5)

        if len(self.points) == 2:
            pygame.draw.line(self.screen, self.curve_color, self.points[0], self.points[1], 3)

        elif len(self.points) > 2:
            bezier_curve = [self.bezier_point(self.points, t / 1000) for t in range(1001)]
            
            # Desenha a curva com cor aleatória
            pygame.draw.lines(self.screen, self.curve_color, False, bezier_curve, 3)

    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.points and self.points[-1] == pos:
                        continue

                    self.points.append(pos)
                    self.curve_color = self.random_color()  # Gera uma nova cor para cada curva
                    self.draw()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    app = DesenhaCurvas()
    app.main()
