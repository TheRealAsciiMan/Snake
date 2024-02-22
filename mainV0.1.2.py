import pygame
from random import randint

class Anneau:
    """
    Classe représentant un Anneau (pour les gouverner tous)
    """
    def __init__(self, suivant=None, larg=-50.0, haut=-50.0, flarg=-50.0, fhaut=-50.0):
        """
        Constructeur : Initialisation d'un Anneau avec 5 attributs
        :param suivant: l'Anneau qui vient après, s'il n'y en a pas, reste sur None
        :param larg: la position en largeur de l'Anneau par défaut hors du cadre pour qu'il soit invisible mais bien réel
        :param haut: la position en hauteur de l'Anneau par défaut hors du cadre pour qu'il soit invisible mais bien réel
        :param flarg: la future position en largeur de l'Anneau par défaut hors du cadre pour qu'il soit invisible mais bien réel
        :param fhaut: la future position en hauteur de l'Anneau par défaut hors du cadre pour qu'il soit invisible mais bien réel
        """
        self.suivant = suivant
        self.larg = larg
        self.haut = haut
        self.flarg = flarg
        self.fhaut = fhaut

    def turn(self):
        """
        Méthode servant à passer de l'état futur à l'état présent
        """
        self.larg = self.flarg
        self.haut = self.fhaut

    def show(self):
        """
        Méthode affichant le serpent grâce à la fonction dessine_serpent() en utilisant les attributs de l'instance et des attributs globaux
        """
        dessine_serpent(self.larg, self.haut, lsnake, hsnake)

    def predict(self):
        """
        Méthode servant à donner la future position du prochain anneau grâce aux coordonnées présentes de l'anneau actuel si l'anneau actuel possède bien un anneau suivant
        """
        if self.suivant is not None:
            self.suivant.flarg = self.larg
            self.suivant.fhaut = self.haut


class Serpent:
    """
    Classe représentant un serpent à l'aide de la classe Anneau
    """
    def __init__(self, head):
        """
        Constructeur : Méthode définissant une liste d'anneaux, et plaçant en premier la tête mis en argument, le serpent a forcément une tête
        :param head: un anneau de classe Anneau
        """
        self.head = head
        self.rings = []  #  J'utilise un tableau dynamique vu en cours pour gérer les anneaux du serpent
        self.rings.append(self.head)

    def update(self):
        """
        Méthode permettant de mettre à jour le serpent d'1 frame en prévoyant la position future du chaque anneau, puis de les appliquer au présent grâce à une boucle
        """
        for ring in self.rings:
            ring.predict()
            ring.turn()

    def show(self):
        """
        Méthode servant à afficher tous les anneaux grâce à une boucle
        """
        for ring in self.rings:
            ring.show()

class Pomme():
    def __init__(self):
        self.xApp = randint(0, int((long-20)//20)) * 20
        self.yApp = randint(0, int((haut - 20)//20)) * 20
    def renew(self):
        self.xApp = randint(0, int((long - 20) // 20)) * 20
        self.yApp = randint(0, int((haut - 20) // 20)) * 20

    def show(self):
        surf.blit(apple_img, (self.xApp, self.yApp))
    def collision(self):
        global score
        if abs(self.xApp - head.larg) <= 20 and abs(self.yApp - head.haut) <= 20:
            score += 1
            eat(snake)
            self.renew()


def eat(serp, taille:int=5, sound:bool=True):
    """
    Fonction permettant d'ajouter "taille" (par défaut 5) anneaux qui se suivent de classe Anneaux à un serpent de classe Serpent
    :param serp: le serpent auquel on rajoute les "taille" anneaux
    :param taille: le nombre d'anneaux à ajouter
    :param sound: un booléen qui permet de choisir si l'on met le son du grignotage
    """
    for _ in range(4*taille):
        # 20 / 4 = 5 cela dépend de la vitesse de mouvement
        serp.rings.append(Anneau())
        serp.rings[-2].suivant = serp.rings[-1]
        if sound:
            eatSound.play()


def dead(serp):
    """
    Fonction servant à réinitialiser un serpent de classe Serpent en supprimant tous les anneaux sauf la tête
    :param serp: le serpent qui va être réinitialisé
    """
    serp.rings = [serp.head]


def dessine_serpent(posl, posh, largsnake, hautsnake):
    """
    Fonction permettant le traçage d'un anneau du serpent
    :param posl: position en largeur
    :param posh: position en hauteur
    :param largsnake: largeur du rectangle de l'anneau
    :param hautsnake: hauteur du rectangle de l'anneau
    """
    pygame.draw.rect(surf, (78, 124, 246), (posl, posh, largsnake, hautsnake))


def dessine_damier():
    """
    Fonction dessinant le damier à l'aide de boucle permettant de parcourir toute la fenêtre en dessinant des rectangles
    """
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

def rends():
    """
    Fonction affichant le score du joueur en temps réel en haut à gauche de l'écran grâce à font la police préétablie et à score la variable qui compte le score
    """
    text = font.render(str(score), True, (255, 255, 255))
    surf.blit(text, (15, 5))



# Variables globales et initialisation
pygame.init()
pygame.mixer.music.load("Outset Island.mp3")
eatSound = pygame.mixer.Sound("eat.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(loops=-1)
haut = pygame.display.Info().current_h//2  # s'adapte à la résolution de l'écran
long = haut * 16 / 9  # calcule la longueur en fonction de la hauteur avec le ratio 16:9
surf = pygame.display.set_mode((long, haut))
pygame.display.set_caption("AsciiSnake")
pygame.display.set_icon(pygame.image.load("icon.png"))
apple_img = pygame.image.load("apple.png")
apple = Pomme()
score = 0
run = True
clock = pygame.time.Clock()
centerl = long // 2
centerh = haut // 2
lsnake = 20  # modifiable
hsnake = 20  # modifiable
direction = None
head = Anneau(suivant=None, larg=centerl, haut=centerh, flarg=centerl, fhaut=centerh)
snake = Serpent(head)
eat(snake, 4, False)
pommex = None
pommey = None
font = pygame.font.Font('RnRFont.ttf', 32)

while run:  #  Boucle du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  #  Capture des touches du clavier
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
            if event.key == pygame.K_m:  #  Permet d'arrêter la musique avec la touche M, mais quel intérêt ?
                pygame.mixer.music.stop()
    if direction == "up":  #  Gestion des contrôles/vitesses
        head.fhaut -= 5
    if direction == "down":
        head.fhaut += 5
    if direction == "right":
        head.flarg += 5
    if direction == "left":
        head.flarg -= 5
    if head.fhaut < 0:  #  Gestion des morts
        dead(snake)
        eat(snake, 4, False)
        head.flarg, head.fhaut = long // 2, haut // 2
        head.larg, head.haut = long // 2, haut // 2
        direction = None
        score = 0
    if head.fhaut > haut - hsnake:
        dead(snake)
        eat(snake, 4, False)
        head.flarg, head.fhaut = long // 2, haut // 2
        head.larg, head.haut = long // 2, haut // 2
        direction = None
        score = 0
    if head.flarg > long - lsnake:
        dead(snake)
        eat(snake, 4, False)
        head.flarg, head.fhaut = long // 2, haut // 2
        head.larg, head.haut = long // 2, haut // 2
        direction = None
        score = 0
    if head.flarg < 0:
        dead(snake)
        eat(snake, 4, False)
        head.flarg, head.fhaut = long // 2, haut // 2
        head.larg, head.haut = long // 2, haut // 2
        direction = None
        score = 0
    if direction is not None:
        for i in range(1, len(snake.rings)-1):
            if snake.rings[0].flarg == snake.rings[i].larg and snake.rings[0].fhaut == snake.rings[i].haut:
                dead(snake)
                eat(snake, 4, False)
                head.flarg, head.fhaut = long // 2, haut // 2
                head.larg, head.haut = long // 2, haut // 2
                direction = None
                score = 0
                break
    clock.tick(60)   #  Boucle globale avec le nombre de fps (60)
    dessine_damier()
    rends()
    snake.update()
    snake.show()
    apple.collision()
    apple.show()
    pygame.display.flip()
pygame.quit()
