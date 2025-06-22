from CarteAction import CarteAction
from Joueur import Joueur
from RobotIA import RobotIA
from Plateau_Sab import Plateau
import random

class CarteDefense(CarteAction):

  def __init__(self, ctype):
    super().__init__()
    self.__type = ctype
    self.__bool = [False, False, False]  #représente les 3 objets avec un True sur le ou les objet(s) qu'il répare
    j = 0
    for c in "LPW":
      if c in ctype: self.__bool[j] = True
      j += 1

  def jouer(self, plat, j1, j2):
  # Definit comment on joue la carte
  #@param plat est le plateau du jeu
  #@param j1 le joueur qui joue
  #@param j2 le joueur pour lequel on va réparer l'objet
    if isinstance(j1,Joueur):
      res = 2
      for i in range(0, 3):
        if j2.objet[i] == False and self.__bool[i] == True:
          j2.objet[i] = True
          break  #pour que ça ne répare qu'un seul objet
        elif j2.objet[i] == True and self.__bool[i] == True:
          print("Ce joueur ne peut pas bénéficier de cette carte.")
          res = int(input("Que voulez vous faire ? (0: Changer de joueur, 1 : Changer de carte) "))
          break
          
    elif isinstance(j1,RobotIA):
      res = 2
      for i in range(0, 3):
        if j2.objet[i] == False and self.__bool[i] == True:
          j2.objet[i] = True
          break
        elif j2.objet[i] == True and self.__bool[i] == True:
          res = random.randint(0,1)
          break
    return res


  def __str__(self):
    res1 = "(DEF)"
    if self.__type == 'P':
      res2 = "( P )"
    elif self.__type == 'W':
      res2 = "( W )"
    elif self.__type == 'L':
      res2 = "( L )"
    elif self.__type == 'LP':
      res2 = "(L P)"
    elif self.__type == 'LW':
      res2 = "(L W)"
    elif self.__type == 'PW':
      res2 = "(P W)"
    res3 = '(   )'
    return res1, res2, res3

  def who(self):
    res = str(super().who()) + " Défense"
    if "P" in self.__type:
      res += " Pioche"
    if "W" in self.__type:
      res += " Wagon"
    if "L" in self.__type:
      res += " Lanterne"
    return res
