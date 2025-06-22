#Les bases
from Partie import Partie
from RobotIA import RobotIA
from Joueur import Joueur
from Plateau_Sab import Plateau
from Pioche import *

#Les cartes
from Carte import Carte
from CartesChemin import *
from CarteAction import CarteAction
from CarteDefense import CarteDefense
from CarteMAP import CarteMAP
from CarteOr import CarteOr
from CartePlateau import CartePlateau
from CarteROF import CarteROF

#Autres import
import random
import time
import os
import copy

#Pour effacer la console
def clear():
  # for windows
  if os.name == 'nt':
    _ = os.system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = os.system('clear')
