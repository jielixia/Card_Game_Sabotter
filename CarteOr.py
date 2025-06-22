from Carte import Carte

class CarteOr(Carte):

  def __init__(self, ctype):
    super().__init__()
    if 0 < ctype < 4:
      self.__valeur = ctype  #nombre d'or de 1 à 3

  @property
  def valeur(self):
    return self.__valeur

  def __str__(self):
    res = f"(O R)\n({self.__valeur}G*)\n(   )"
    return res

  def who(self):
    res = f"Carte {self.__type} Or"
    return res
