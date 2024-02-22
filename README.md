# Snake en Python

On retrouve différentes versions de ce Snake en Python :
- mainV0.1.0.py : C'est une version très simple de Snake, on possède un carré que l'on peut déplacer avec les flèches directionnelles, attention, les bords vous tuent, évidemment il y a le damier derrière.
- mainV0.1.1.py : Une version bien meilleure est la 0.1.1, elle rajoute la queue du Serpent grâce à un tableau dynamique et l'ajout de différentes classes, elle rajoute un fond musical que l'on peut éteindre en appuyant sur M.
- mainV0.1.2.py : La version finale pour la version Solo de Snake, elle rajoute la gestion du Score et donc aussi l'ajout d'une Pomme aléatoirement disposée dans le damier et qui une fois touchée vous rajoutera 1 de score et agrandira votre serpent, par défaut le serpent possède 5 anneaux, et à chaque pomme il en récupère 5 autres. De plus la collision avec lui-même a été rajoutée.
- mainOffline2PV0.1.3.py : La version 2 joueurs en hors-ligne, c'est-à-dire qu'il y a une seule fenêtre avec 2 serpents, le premier serpent est géré par les touches haut, bas, gauche, droite et le second par Z, Q, S, D. Les 2 scores est affichés et attention, si la tête d'un serpent touche l'autre serpent, c'est la mort. Une seule pomme pour 2 serpents ! Battez-vous !
- mainOnline2PV0.1.4.py : La version 2 joueurs mais en ligne qui reprend exactement les mêmes fonctionnalités que la version hors-ligne, mais sur 2 ordinateurs différents, c'est du p2p donc pas besoin de serveur de disponible, c'est une transmission habile grâce au module socket qui envoie certaines variables en continue ! Bon jeu !
