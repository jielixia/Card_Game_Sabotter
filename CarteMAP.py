from CarteAction import CarteAction
from CartesChemin import CarteEnd
from Plateau_Sab import Plateau
from Joueur import Joueur
from RobotIA import RobotIA
import numpy as np
import time

class CarteMAP(CarteAction):

  def __init__(self):
    super().__init__()

  def jouer(self, plat,j):
  # Definit comment on joue la carte
  #@param plat est le plateau du jeu
  #@param j le joueur qui joue
    res = -1
    if isinstance(j,Joueur):
      while res == -1:
        index = np.where(plat.plato==21)
        coordonnees= list(zip(index[0], index[1]))
        col = coordonnees [0][1]
        ligne = int(input(f"Sur quelle ligne se situe la carte Arrivée que vous voulez voir ? (0 à {len(plat.plato)-1}) "))
        #col = int(input(f"Et quelle colonne ? (0 à {len(plat.plato[ligne])-1}) "))
  
        if plat.plato[ligne][col] != 22 and plat.plato[ligne][col] != 21:
          print("Cette carte n'est pas une carte Arrivée, veuillez sélectionner une nouvelle carte.")
  
        else :
          if plat.plato[ligne][col] == 22:
            print("Cette carte cache seulement des pierres...")
            time.sleep(5)
          elif plat.plato[ligne][col] == 21:
            print("Cette carte cache le Trésor ! ")
            time.sleep(5)
          res = 2
          return res
          
    elif isinstance(j,RobotIA):
      return 2

  def __str__(self):
    res1 = '( M )'
    res2 = '(MAP)'
    res3 = '( P )'
    return res1, res2, res3

  def who(self):
    res = str(super().who())
    res += " MAP"
    return res
