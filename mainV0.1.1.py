import pygame

long= 960
haut= 720
surf = pygame.display.set_mode((long,haut))
run = True
clock = pygame.time.Clock()
centerl = long // 2
centerh = haut // 2
lsnake = 20
hsnake = 20
direction = None



class Anneau:
    def __init__(self, suivant=None, larg=-50, haut=-50, flarg=-50, fhaut=-50):
        self.suivant = suivant
        self.larg = larg
        self.haut = haut
        self.flarg = flarg
        self.fhaut = fhaut
    def turn(self):
        if direction != None:
            self.larg = self.flarg
            self.haut = self.fhaut
    def show(self):
        dessine_serpent(self.larg, self.haut, lsnake, hsnake)
    def predict(self):
        if self.suivant != None:
            self.suivant.flarg = self.larg
            self.suivant.fhaut = self.haut

class Serpent:
    def __init__(self, head):
        self.head = head
        self.rings = []
        self.rings.append(self.head)
    def update(self):
        for ring in self.rings:
            ring.predict()
            ring.turn()
    def show(self):
        for ring in self.rings:
            ring.show()


def eat(serp):
    for i in range(30):
        serp.rings.append(Anneau())
        serp.rings[i].suivant = serp.rings[i+1]


def dessine_serpent(posl, posh, largsnake, hautsnake):
    pygame.draw.rect(surf, (78, 124, 246), (posl, posh, largsnake, hautsnake))

def dessine_damier():
    longueur = 0
    hauteur = 0
    clair = (170, 215, 81)
    fonce = (162, 209, 73)
    while hauteur < haut:
        while longueur < long:
            if (hauteur // 20 + longueur // 20) % 2 == 0:
                pygame.draw.rect(surf, clair, (longueur, hauteur, 20, 20))
            else:
                pygame.draw.rect(surf, fonce, (longueur, hauteur, 20, 20))
            longueur += 20
        longueur = 0
        hauteur += 20

head = Anneau(suivant=None, larg=centerl, haut=centerh, flarg=centerl, fhaut=centerh)
snake = Serpent(head)
eat(snake)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != "down":
                    direction = "up"
            if event.key == pygame.K_DOWN:
                if direction != "up":
                    direction = "down"
            if event.key == pygame.K_LEFT:
                if direction != "right":
                    direction = "left"
            if event.key == pygame.K_RIGHT:
                if direction != "left":
                    direction = "right"
    if direction == "up":
        head.fhaut -= 5
    if direction == "down":
        head.fhaut += 5
    if direction == "right":
        head.flarg += 5
    if direction == "left":
        head.flarg -= 5
    if head.fhaut < 0:
        print("Game Over")
        head.flarg, head.fhaut = long // 2, haut // 2
        direction = None
    if head.fhaut > haut - hsnake:
        print("Game Over")
        head.flarg, head.fhaut = long // 2, haut // 2
        direction = None
    if head.flarg > long - lsnake:
        print("Game Over")
        head.flarg, head.fhaut = long // 2, haut // 2
        direction = None
    if head.flarg < 0:
        print("Game Over")
        head.flarg, head.fhaut = long // 2, haut // 2
        direction = None
    clock.tick(60)
    dessine_damier()
    snake.update()
    snake.show()
    pygame.display.flip()
pygame.quit()