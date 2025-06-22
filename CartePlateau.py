from Carte import Carte
from abc import ABC, abstractmethod

class CartePlateau(Carte):

  def __init__(self):
    super().__init__()
    #self.__tab = [1, 1, 1, 1, 1]  #donne la liste de booléen pour le chemin

  @abstractmethod
  def __str__(self):
    pass

  @abstractmethod
  def num_carte(self):
    pass

  @abstractmethod 
  def tab_bool (self) : 
    pass

  
