import pygame


class Main():
    def __init__(self, haut=600, long=800):
        self.long = long
        self.haut = haut
        self.surf = pygame.display.set_mode((long,haut))
        self.run = True
        self.clock = pygame.time.Clock()
        self.l, self.h = long // 2, haut // 2
        self.lsnake = 10
        self.hsnake = 10
        self.direction = None

    def dessine_damier(self):
        longueur = 0
        hauteur = 0
        clair = (167,212,249)
        fonce = (49,142,240)
        while hauteur < self.haut:
            while longueur < self.long:
                if (hauteur // 20 + longueur // 20) % 2 == 0:
                    pygame.draw.rect(self.surf, clair, (longueur, hauteur, 20, 20))
                else:
                    pygame.draw.rect(self.surf, fonce, (longueur, hauteur, 20, 20))
                longueur += 20
            longueur = 0
            hauteur += 20
        self.clock.tick(60)
        pygame.display.flip()

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.direction = "up"
                    if event.key == pygame.K_DOWN:
                        self.direction = "down"
                    if event.key == pygame.K_LEFT:
                        self.direction = "left"
                    if event.key == pygame.K_RIGHT:
                        self.direction = "right"
            if self.direction == "up":
                self.h -= 1
            if self.direction == "down":
                self.h += 1
            if self.direction == "right":
                self.l += 1
            if self.direction == "left":
                self.l -= 1
            if self.h < 0:
                print("Game Over")
                self.l, self.h = self.long // 2, self.haut // 2
                self.direction = None
            if self.h > self.haut - self.hsnake:
                print("Game Over")
                self.l, self.h = self.long // 2, self.haut // 2
                self.direction = None
            if self.l > self.long - self.lsnake:
                print("Game Over")
                self.l, self.h = self.long // 2, self.haut // 2
                self.direction = None
            if self.l < 0:
                print("Game Over")
                self.l, self.h = self.long // 2, self.haut // 2
                self.direction = None
            self.clock.tick(240)
            self.dessine_damier()
            pygame.draw.rect(self.surf, (255, 255, 255), (self.l, self.h, self.lsnake, self.hsnake))
            pygame.display.flip()

        pygame.quit()


Game1 = Main()
Game1.dessine_damier()
Game1.play()
run = True