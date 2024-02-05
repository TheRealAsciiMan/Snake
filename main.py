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
        i = 0
        longueur = 0
        hauteur = 0
        clair = (144, 238, 144)
        fonce = (0, 100, 0)
        while hauteur < self.haut:
            while longueur < self.long:
                if i%2 == 0 :
                    pygame.draw.rect(self.surf, clair, (longueur, hauteur, longueur + 20, hauteur + 20))
                    pygame.draw.rect(self.surf, fonce, (longueur + 20, hauteur, longueur + 40, hauteur + 20))
                else :
                    pygame.draw.rect(self.surf, fonce, (longueur, hauteur, longueur + 20, hauteur + 20))
                    pygame.draw.rect(self.surf, clair, (longueur + 20, hauteur, longueur + 40, hauteur + 20))
                longueur += 40
            longueur = 0
            hauteur += 20
        pygame.display.flip()

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.clock.tick(60)
        pygame.quit()

Game1 = Main()
Game1.dessine_damier()
Game1.play()
