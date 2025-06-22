from abc import abstractmethod
from Carte import Carte

class CarteAction(Carte):

  def __init__(self):
    super().__init__()

  @abstractmethod
  def jouer(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

  def who(self):
    res = "Carte Action"
    return res
