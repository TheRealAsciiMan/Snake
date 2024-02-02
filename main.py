import pygame


class Main():
    def __init__(self, haut=600, long=800):
        self.long = long
        self.haut = haut
        self.surf = pygame.display.set_mode((long,haut))
        self.run = True
        self.clock = pygame.time.Clock()
        self.l, self.h = self.long // 2, self.haut // 2
        self.lsnake = 10
        self.hsnake = 10
        self.direction = None

    def dessine_damier(self):
        self.blit
    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.clock.tick(60)
        pygame.quit()

Game1 = Main()
Game1.play()