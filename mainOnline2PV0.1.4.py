import pygame
import socket
from random import randint


class Anneau:
    """
    Classe représentant un Anneau (pour les gouverner tous)
    """
    def __init__(self, color, suivant=None, larg=-50.0, haut=-50.0, flarg=-50.0, fhaut=-50.0):
        """
        Constructeur : Initialisation d'un Anneau avec 5 attributs
        :param color: la couleur de l'anneau au format RVB (rrr,vvv,bbb)
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
        self.color = color

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
        dessine_serpent(self.larg, self.haut, lsnake, hsnake, self.color)

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


class Pomme:
    def __init__(self):
        self.xApp = None
        self.yApp = None

    def renew(self):
        self.xApp = randint(0, int((long - 20) // 20)) * 20
        self.yApp = randint(0, int((haut - 20) // 20)) * 20

    def show(self):
        surf.blit(apple_img, (self.xApp, self.yApp))

    def collision(self):
        global score1, score2
        if abs(self.xApp - head1.larg) <= 20 and abs(self.yApp - head1.haut) <= 20:
            score1 += 1
            eat(snake1)
            if joueur == 2:
                self.renew()
        if abs(self.xApp - head2.larg) <= 20 and abs(self.yApp - head2.haut) <= 20:
            score2 += 1
            eat(snake2)
            if joueur == 2:
                self.renew()


def eat(serp, taille: int = 5, sound: bool = True):
    """
    Fonction permettant d'ajouter "taille" (par défaut 5) anneaux qui se suivent de classe Anneaux à un serpent de classe Serpent
    :param serp: le serpent auquel on rajoute les "taille" anneaux
    :param taille: le nombre d'anneaux à ajouter
    :param sound: un booléen qui permet de choisir si l'on met le son du grignotage
    """
    for _ in range(4*taille):
        # 20 / 4 = 5 cela dépend de la vitesse de mouvement
        serp.rings.append(Anneau(serp.head.color))
        serp.rings[-2].suivant = serp.rings[-1]
        if sound:
            eatSound.play()


def dead(serp):
    """
    Fonction servant à réinitialiser un serpent de classe Serpent en supprimant tous les anneaux sauf la tête
    :param serp: le serpent qui va être réinitialisé
    """
    serp.rings = [serp.head]


def dessine_serpent(posl, posh, largsnake, hautsnake, color):
    """
    Fonction permettant le traçage d'un anneau du serpent
    :param posl: position en largeur
    :param posh: position en hauteur
    :param largsnake: largeur du rectangle de l'anneau
    :param hautsnake: hauteur du rectangle de l'anneau
    :param color: la couleur du serpent en rvb (rrr,vvv,bbb)
    """
    pygame.draw.rect(surf, color, (posl, posh, largsnake, hautsnake))


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
    text1 = font.render("J1 : "+str(score1), True, (255, 255, 255))
    text2 = font.render("J2 : "+str(score2), True, (255, 255, 255))
    surf.blit(text1, (15, 5))
    surf.blit(text2, (long-120, 5))


# Variables globales et initialisation
joueur = int(input("Veuillez rentrer le numero du joueur 1 ou 2 (Ex : 1) : "))
lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sending_ip = input("Veuillez rentrer l'adresse IPv4 de l'autre joueur (Ex: 192.168.0.127) : ")
if sending_ip == "":
    sending_ip = "127.0.0.1"
if joueur == 1:
    listening_port, sending_port = 15, 16
    lSocket.bind(('', listening_port))
    lSocket.listen(15)
    conn, address = lSocket.accept()
    print("Un client vient de se connecter")
    sSocket.connect((sending_ip, sending_port))
    print("Client connecté")
elif joueur == 2:
    listening_port, sending_port = 16, 15
    sSocket.connect((sending_ip, sending_port))
    print("Client connecté")
    lSocket.bind(('', listening_port))
    lSocket.listen(15)
    conn, address = lSocket.accept()
    print("Un client vient de se connecter")
else:
    raise ValueError("Ce n'est pas un chiffre qui soit 1 ou 2")

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
apple.renew()
score1 = 0
score2 = 0
run = True
clock = pygame.time.Clock()
centerl = long // 2
centerh = haut // 2
lsnake = 20  # modifiable
hsnake = 20  # modifiable
direction1 = None
direction2 = None
head1 = Anneau(suivant=None, larg=centerl, haut=centerh, flarg=centerl, fhaut=centerh, color=(78, 124, 246))
head2 = Anneau(suivant=None, larg=centerl, haut=centerh, flarg=centerl, fhaut=centerh, color=(255, 100, 100))
snake1 = Serpent(head1)
snake2 = Serpent(head2)
eat(snake1, 4, False)
eat(snake2, 4, False)
font = pygame.font.Font('RnRFont.ttf', 32)


while run:  #  Boucle du jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  #  Capture des touches du clavier des 2 joueurs
            if event.key == pygame.K_z:
                if direction1 != "down":
                    direction1 = "up"
            if event.key == pygame.K_s:
                if direction1 != "up":
                    direction1 = "down"
            if event.key == pygame.K_q:
                if direction1 != "right":
                    direction1 = "left"
            if event.key == pygame.K_d:
                if direction1 != "left":
                    direction1 = "right"
            if event.key == pygame.K_m:  #  Permet d'arrêter la musique avec la touche M, mais quel intérêt ?
                pygame.mixer.music.stop()
    if direction1 == "up":  #  Gestion des contrôles/vitesses du joueur 1
        head1.fhaut -= 5
    if direction1 == "down":
        head1.fhaut += 5
    if direction1 == "right":
        head1.flarg += 5
    if direction1 == "left":
        head1.flarg -= 5
    if direction1 is not None and direction2 is not None:  # Gestion des morts en cas de collision de tête
        if snake2.rings[0].flarg == snake1.rings[0].flarg and snake2.rings[0].fhaut == snake1.rings[0].fhaut:
            dead(snake1)
            eat(snake1, 4, False)
            head1.flarg, head1.fhaut = long // 2, haut // 2
            head1.larg, head1.haut = long // 2, haut // 2
            direction1 = None
            score1 = 0
            dead(snake2)
            eat(snake2, 4, False)
            head2.flarg, head2.fhaut = long // 2, haut // 2
            head2.larg, head2.haut = long // 2, haut // 2
            direction2 = None
            score2 = 0
    if head1.fhaut < 0:  #  Gestion des morts du joueur 1
        dead(snake1)
        eat(snake1, 4, False)
        head1.flarg, head1.fhaut = long // 2, haut // 2
        head1.larg, head1.haut = long // 2, haut // 2
        direction1 = None
        score1 = 0
    if head1.fhaut > haut - hsnake:
        dead(snake1)
        eat(snake1, 4, False)
        head1.flarg, head1.fhaut = long // 2, haut // 2
        head1.larg, head1.haut = long // 2, haut // 2
        direction1 = None
        score1 = 0
    if head1.flarg > long - lsnake:
        dead(snake1)
        eat(snake1, 4, False)
        head1.flarg, head1.fhaut = long // 2, haut // 2
        head1.larg, head1.haut = long // 2, haut // 2
        direction1 = None
        score1 = 0
    if head1.flarg < 0:
        dead(snake1)
        eat(snake1, 4, False)
        head1.flarg, head1.fhaut = long // 2, haut // 2
        head1.larg, head1.haut = long // 2, haut // 2
        direction1 = None
        score1 = 0
    if direction1 is not None:
        for i in range(1, len(snake1.rings)-1):
            if snake1.rings[0].flarg == snake1.rings[i].larg and snake1.rings[0].fhaut == snake1.rings[i].haut:
                dead(snake1)
                eat(snake1, 4, False)
                head1.flarg, head1.fhaut = long // 2, haut // 2
                head1.larg, head1.haut = long // 2, haut // 2
                direction1 = None
                score1 = 0
                break
        for i in range(1, len(snake2.rings)-1):
            if snake1.rings[0].flarg == snake2.rings[i].larg and snake1.rings[0].fhaut == snake2.rings[i].haut:
                dead(snake1)
                eat(snake1, 4, False)
                head1.flarg, head1.fhaut = long // 2, haut // 2
                head1.larg, head1.haut = long // 2, haut // 2
                direction1 = None
                score1 = 0
                break
    if head2.fhaut < 0:  #  Gestion des morts du joueur 2
        dead(snake2)
        eat(snake2, 4, False)
        head2.flarg, head2.fhaut = long // 2, haut // 2
        head2.larg, head2.haut = long // 2, haut // 2
        direction2 = None
        score2 = 0
    if head2.fhaut > haut - hsnake:
        dead(snake2)
        eat(snake2, 4, False)
        head2.flarg, head2.fhaut = long // 2, haut // 2
        head2.larg, head2.haut = long // 2, haut // 2
        direction2 = None
        score2 = 0
    if head2.flarg > long - lsnake:
        dead(snake2)
        eat(snake2, 4, False)
        head2.flarg, head2.fhaut = long // 2, haut // 2
        head2.larg, head2.haut = long // 2, haut // 2
        direction2 = None
        score2 = 0
    if head2.flarg < 0:
        dead(snake2)
        eat(snake2, 4, False)
        head2.flarg, head2.fhaut = long // 2, haut // 2
        head2.larg, head2.haut = long // 2, haut // 2
        direction2 = None
        score2 = 0
    for i in range(1, len(snake2.rings)-1):
        if snake2.rings[0].flarg == snake2.rings[i].larg and snake2.rings[0].fhaut == snake2.rings[i].haut:
            dead(snake2)
            eat(snake2, 4, False)
            head2.flarg, head2.fhaut = long // 2, haut // 2
            head2.larg, head2.haut = long // 2, haut // 2
            direction2 = None
            score2 = 0
            break
    for i in range(1, len(snake1.rings)-1):
        if snake2.rings[0].flarg == snake1.rings[i].larg and snake2.rings[0].fhaut == snake1.rings[i].haut:
            dead(snake2)
            eat(snake2, 4, False)
            head2.flarg, head2.fhaut = long // 2, haut // 2
            head2.larg, head2.haut = long // 2, haut // 2
            direction2 = None
            score2 = 0
            break
    clock.tick(60)   #  Boucle globale avec le nombre de fps (60)

    if joueur == 1:
        lData = conn.recv(512)
        lData = lData.decode("utf8")
        lData = eval(lData)
        head2.flarg = lData[0]
        head2.fhaut = lData[1]
        apple.xApp = lData[2]
        apple.yApp = lData[3]
        sData = str([head1.flarg, head1.fhaut, apple.xApp, apple.yApp])
        sData = sData.encode("utf8")
        sSocket.sendall(sData)
    if joueur == 2:
        sData = str([head1.flarg, head1.fhaut, apple.xApp, apple.yApp])
        sData = sData.encode("utf8")
        sSocket.sendall(sData)
        lData = conn.recv(512)
        lData = lData.decode("utf8")
        lData = eval(lData)
        head2.flarg = lData[0]
        head2.fhaut = lData[1]
        apple.xApp = lData[2]
        apple.yApp = lData[3]

    dessine_damier()
    rends()
    snake1.update()
    snake2.update()
    snake1.show()
    snake2.show()
    apple.collision()
    apple.show()
    pygame.display.flip()
conn.close()
lSocket.close()
sSocket.close()
pygame.quit()
