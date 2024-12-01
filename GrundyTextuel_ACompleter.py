# Jeu de Grundy

'''Le jeu consiste à séparer des ensembles d'objets. La position de départ
  consiste en un unique ensemble d'objets. Pour jouer, le seul
  coup possible consiste à séparer un ensemble d'objets
  en deux ensembles de tailles distinctes et non nulles. Les joueurs jouent
  à tour de rôle, jusqu'à ce que l'un d'entre eux ne puisse plus
  jouer.'''

##############
### Structure de données IMPOSEE
##############
''' On représente un jeu par une liste. Chaque élément de la liste est
le nombre d'objets de l'ensemble. Par exemple, [3,1,4] est le jeu qui contient 3 ensembles,
le 1er ensemble contient 3 objets, le second 1 objet et le 3ème ensemble contient 4 objets
'''


# pour que l'ordinateur puisse jouer aléatoirement
from random import randint
# pour que l'ordinateur puisse réfléchir 1 seconde
from time import sleep

###############################
### partie fournie
###############################

# Affiche le jeu sur une seule ligne
# Chaque ensemble est numéroté et affiché entre []
# Les objets sont numérotés et affichés entre ||
# Exemple: afficheJeu([3,1,4]) affiche [E1 |1|2|3| ] [E2 |1| ] [E3 |1|2|3|4| ]
#          Le 1er ensemble E1 contient 3 objets |1|2|3|,
#          le 2d ensemble E2 contient 1 objet |1| et le 3ème ensemble E3 contient
#          |1|2|3|4| 4 objets
# NOTA: dans cet affichage, les ensembles et les objets dans les ensembles
#       sont numérotés de 1 à n, même si jeu est une liste et
#       donc indexée de 0 à n-1. Il faut donc gérer correctement les indices
def afficheJeu(jeu):
    k=1
    affichage =""
    for j in jeu:
        nomEns="[E"+str(k)
        affichage+=nomEns + representationEnsemble(j) + "] "
        k+=1
    print(affichage)

# Renvoie la représentation d'un ensemble contenant k objets
# Exemple: si k=5 renvoie  |1|2|3|4|5|
def representationEnsemble(k):
    ens=" "
    for i in range(1,k+1):
        ens+="|"+str(i)
    ens+="| "
    return ens

# Renvoie le jeu initial dans lequel il y a un seul ensemble de n objets
def initJeu(n):
    return [n]


###############################
### partie à compléter
###############################

# Suivez l'énoncé du TD pas à pas.
# Il faut décommenter les def que vous complétez au fur et à mesure.
# Pour cela, enlever les '''

# Renvoie un booléen qui indique si la fin de jeu est atteinte
# Renvoie True quand on ne peut plus jouer
def finDeJeu(jeu):
    fin = True
    for elm in jeu:
        if elm >= 3:
            fin = False
    return fin

# Fonction dédiée à lire l'ensemble dans lequel le joueur veut jouer
# Demande un n° d'ensemble tant que le joueur donne un n° qui n'est pas correct
# Renvoie le n° d'ensemble
def choixEnsembleJoueur(jeu):
    choix = int(input("Dasns quel ensemble voulez-vous joué ?"))
    nbdelm = len(jeu)
    while choix == 0 or choix > nbdelm:
        choix = int(input("Dasns quel ensemble voulez-vous joué ?"))
    return choix

# Fonction dédiée à lire à quel endroit le joueur veut couper l'ensemble
# nbEltEnsemble est le nombre d'éléments de l'ensemble dans lequel on joue
# Demande un n° de coupe tant que le joueur donne un n° qui n'est pas correct
# Renvoie le n° de coupe
def choixCoupeJoueur(nbEltEnsemble):
    coupe = int(input("Ou voulez-vous couper l'ensemble ?"))
    while coupe == 0 or coupe >= nbEltEnsemble:
        print("Vous devez couper en 2 ensembles de tailles différentes")
        coupe = int(input("Ou voulez-vous couper l'ensemble ?"))
    return coupe

# fait jouer le joueur
# utilise choixEnsembleJoueur et choixCoupeJoueur
# met à jour le jeu: modifie jeu pour couper l'ensemble choisi en fonction de la coupe choisie
# Exemple: si jeu=[4,2,5,7], si l'utilisateur choisit l'ensemble 3 qu'il coupe en 4,
# jeu doit devenir [4,2,4,1,7]
def joueurJoue(jeu):
    esmb = choixEnsembleJoueur(jeu)
    coupe = choixCoupeJoueur(jeu)
    jeu = jeu[esmb].insert(coupe,1)
    return jeu

# Fait choisir un ensemble aléatoirement à l'ordinateur
# renvoie le n° de l'ensemble
# tire un n° d'ensemble tant que l'ensemble choisi est trop petit pour être découpé
def choixEnsembleOrdi(jeu):

    esmb = randint(0,len(jeu))
    while jeu[esmb] <3:
        esmb = random.randint(0,len(jeu))
    return esmb

# Fait choisir une coupe aléatoirement à l'ordinateur
# nbEltEnsemble est le nombre d'éléments de l'ensemble dans lequel on joue
# renvoie la coupe
# tire une coupe tant qu'elle divise l'ensemble en deux parties égales
# (si le nombre d'objets est pair)
def choixCoupeOrdi(nbEltEnsemble):
    coupe = randint(1,nbEltEnsemble-1)
    while coupe !=(nbEltEnsemble!/2):
        coupe = randint(1,nbEltEnsemble-1)
    return coupe

# fait jouer l'ordi, et affiche où il a joué
# utilise choixEnsembleOrdi et choixCoupeOrdi
# met à jour le jeu
'''def ordiJoue(jeu):
    print("l'ordi réfléchit ...")
    # pause d'1s pour simuler la réflexion de l'ordi
    sleep(1)
    # A COMPLETER'''


# Fait jouer alternativement le joueur et l'ordi
# tant que la fin de jeu n'est pas atteinte
# utilise les fonctions précédentes
'''
Tirer un nombre aléatoire d'objets
Créer la liste du jeu
Tant qu'il n'y a pas de perdant :
     Afficher le jeu
     Faire jouer le joueur
     Si la fin de jeu est atteinte:
        l'ordinateur est perdant
     Sinon
         Afficher le jeu
         Faire jouer l'ordinateur
         Si la fin de jeu est atteinte:
             le joueur est perdant
'''
'''def partie(n):
    # A COMPLETER'''

#############################
##### pour tester vos def
##### décommentez les tests au fur et à mesure
#############################

j = initJeu(6)
print(j)
afficheJeu(j)
print(finDeJeu(j))
#choixEnsembleJoueur(j)
#choixCoupeJoueur(j)
#joueurJoue(j)
#print(j)
print("-----------------")
j = initJeu(9)
print(len(j))
#afficheJeu(j)
#print(finDeJeu(j))
#choixEnsembleJoueur(j)
#choixCoupeJoueur(j)
#joueurJoue(j)
#print(j)
print("-----------------")
j = [2,5,2]
print(len(j))
#afficheJeu(j)
#print(finDeJeu(j))
#choixEnsembleJoueur(j)
#choixCoupeJoueur(j)
#joueurJoue(j)
#print(j)
print("-----------------")
j = [1,4,8,2,5]
afficheJeu(j)
print(finDeJeu(j))
#choixEnsembleJoueur(j)
#choixCoupeJoueur(j)
#joueurJoue(j)
#print(j)
