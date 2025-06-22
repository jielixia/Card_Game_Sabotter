from CarteAction import CarteAction
from Plateau_Sab import Plateau
from Joueur import Joueur
from RobotIA import RobotIA
import numpy as np
import random

#-------------------Carte RockFall-----------------------
class CarteROF(CarteAction):

  def __init__(self):
    super().__init__()

  def jouer(self, plat,j):
  # Definit comment on joue la carte
  #@param plat est le plateau du jeu
  #@param j le joueur qui joue la carte 
    res = -1
    if isinstance(j,Joueur):
      while res == -1:
        col = int(input("Sur quelle colonne se trouve la carte que vous voulez détruire ? "))
        ligne = int(input("Et sur quelle ligne ? "))
        if plat.plato[ligne][col] == 0:
          print(
            "Il n'y a pas de carte à cet endroit, veuillez modifier votre numéro de ligne et de colonne."
          )
        elif plat.plato[ligne][col] == 1 or 20 < plat.plato[ligne][col] < 23:
          print(
            "Vous ne pouvez pas supprimer les cartes Départ et Arrivées."
          )
          val = int(input("Que voulez vous faire ? (0: Sélectionner un autre emplacement, 1 : Changer de carte) "))
          if val == 1 : 
            res = 1
            break
        else:
          plat.plato[ligne][col] = 0
          plat.afficher()
          res = 2
    elif isinstance(j,RobotIA):
      while res == -1:
        index = np.where( (plat.plato != 0) & (plat.plato!=21) & (plat.plato!=22) & (plat.plato!=1) )
        coordonnees= list(zip(index[0], index[1]))
        if len(coordonnees) == 0:
          res = 1
        else:
          choix = random.randint(0,len(coordonnees)-1)
          (ligne,col) = coordonnees[choix]
          plat.plato[ligne][col] = 0
          res = 2
        
    return res

  def __str__(self):
    res1 = '( R )'
    res2 = '(ROF)'
    res3 = '( F )'
    return res1, res2, res3

  def who(self):
    res = str(super().who())
    res += "Rockfall"
    return res
