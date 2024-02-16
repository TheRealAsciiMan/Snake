import pygame

long= 960
haut= 720
surf = pygame.display.set_mode((long,haut))
run = True
clock = pygame.time.Clock()
l = long // 2
h = haut // 2
lsnake = 20
hsnake = 20
direction = None

class Anneau:
    def __init__(self, suivant=None, larg=0, haut=0, flarg=0, fhaut=0):
        self.suivant = suivant
        self.larg = larg
        self.haut = haut
        self.flarg = flarg
        self.fhaut = fhaut
    def turn(self):
        self.larg = self.flarg
        self.haut = self.fhaut
    def show(self, surf, lsnake, hsnake):
        pygame.draw.rect(surf, (78, 124, 246), (self.larg, self.haut, lsnake, hsnake))

class Serpent:
    def __init__(self, head):
        self.head = head
        self.rings = []
        self.rings.append(self.head)
    def update(self):
        for i in range(len(self.rings)):
            self.rings[i].turn()




def dessine_serpent():
    global l, h, direction, run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_RIGHT:
                direction = "right"
    if direction == "up":
        h -= 1
    if direction == "down":
        h += 1
    if direction == "right":
        l += 1
    if direction == "left":
        l -= 1
    if h < 0:
        print("Game Over")
        l, h = long // 2, haut // 2
        direction = None
    if h > haut - hsnake:
        print("Game Over")
        l, h = long // 2, haut // 2
        direction = None
    if l > long - lsnake:
        print("Game Over")
        l, h = long // 2, haut // 2
        direction = None
    if l < 0:
        print("Game Over")
        l, h = long // 2, haut // 2
        direction = None
    pygame.draw.rect(surf, (78, 124, 246), (l, h, lsnake, hsnake))

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


while run:
    clock.tick(240)
    dessine_damier()
    dessine_serpent()
    pygame.display.flip()
pygame.quit()