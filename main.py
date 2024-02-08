import pygame


class Main():
    def __init__(self, long=1920, haut=1080):
        self.long = long
        self.haut = haut
        self.surf = pygame.display.set_mode((long,haut))
        self.clock = pygame.time.Clock()
        self.l, self.h = long // 2, haut // 2
        self.lsnake = 20
        self.hsnake = 20
        self.run = True
        self.direction = None

    def dessine_damier(self):
        longueur = 0
        hauteur = 0
        clair = (170, 215, 81)
        fonce = (162, 209, 73)
        while hauteur < self.haut:
            while longueur < self.long:
                if (hauteur // 20 + longueur // 20) % 2 == 0:
                    pygame.draw.rect(self.surf, clair, (longueur, hauteur, 20, 20))
                else:
                    pygame.draw.rect(self.surf, fonce, (longueur, hauteur, 20, 20))
                longueur += 20
            longueur = 0
            hauteur += 20

    def play(self):
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
            self.h -= 10
        if self.direction == "down":
            self.h += 10
        if self.direction == "right":
            self.l += 10
        if self.direction == "left":
            self.l -= 10
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
        pygame.draw.rect(self.surf, (82, 130, 238), (self.l, self.h, self.lsnake, self.hsnake))
        self.clock.tick(30)
        pygame.display.flip()

    def start(self):
        while self.run == True:
            self.dessine_damier()
            self.play()
        pygame.quit()


Game1 = Main()
Game1.start()