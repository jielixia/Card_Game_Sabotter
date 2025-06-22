from CarteAction import CarteAction
from Joueur import Joueur
from RobotIA import RobotIA
import random

class CarteAttaque(CarteAction):

  def __init__(self, ctype):
    super().__init__()
    self.__type = ctype
    self.__bool = [True, True, True]  #représente les 3 objets avec un False sur l'objet qu'il détruit
    j = 0
    for c in "LPW":
      if c in ctype: self.__bool[j] = False
      j += 1

  def jouer(self, plat, j1, j2):
  # Definit comment on joue la carte
  # @param plat est le plateau du jeu
  #@param j1 le joueur qui joue
  #@param j2 le joueur que l'on attaque
    if isinstance(j1,Joueur):
      for i in range(0, 3):
        if j2.objet[i] == False and self.__bool[i] == False:
          print("L'objet de",j2,"est déjà cassé.")
          res = int(input("Que voulez vous faire ? (0: Changer de joueur, 1 : Changer de carte) "))
        elif j2.objet[i] == True and self.__bool[i] == False:
          j2.objet[i] = False
          res = 2
          
    elif isinstance(j1, RobotIA):
      for i in range(0, 3):
        if j2.objet[i] == False and self.__bool[i] == False:
          res = random.randint(0,1)
        elif j2.objet[i] == True and self.__bool[i] == False:
          j2.objet[i] = False
          res = 2
    return res

  def __str__(self):
    res1 = "(ATT)"
    res2 = f"( {self.__type} )"
    res3 = "(   )"
    return res1, res2, res3

  def who(self):
    res = str(super().who()) + " Attaque"
    if self.__type == 'P':
      res += " Pioche"
    elif self.__type == 'W':
      res += " Wagon"
    elif self.__type == 'L':
      res += " Lanterne"
    return res
