from Carte import Carte
from CartePlateau import CartePlateau

"""
Pour les classes suivantes :
def num_carte(self) renvoie le numéro de la carte
def tab_bool(self) renvoie le tableau de booleen (1 ou 0) qui associe s'il y a un chemin vers up, down, left, right. Le 1er indice dit si la carte est negative ou pas
def __str__(self) renvoie l'affichage de la carte
"""

class CarteDepart(CartePlateau):

  def __init__(self):
    super().__init__()

  def who(self):
    res = "Carte Départ"
    return res

  def num_carte(self):
    return 1

  def tab_bool(self):
    return [1, 1, 1, 1, 1]
  
  def __str__(self):
    super().__str__()
    res = "( | )\n(-S-)\n( | )"
    return res

class CarteEnd(CartePlateau):

  def __init__(self, ctype):
    super().__init__()
    self.__type = ctype

  def who(self):
    res = "Carte " + str(self.__type)
    return res

  def num_carte(self):
    #associe la carte à un num
    if self.__type == 'Tresor':
      return 21
    else:
      return 22

  def tab_bool(self):
    return [1, 1, 1, 1, 1]

  def __str__(self):  #affiche la carte face cachée
    res = "(   )\n(END)\n(   )"
    return res

  def __afficherCarte(self):  #affiche la carte face découverte
    if self.__type == 'Tresor':
      res = "( | )\n(-G-)\n( | )"
    elif self.type == 'Pierre':
      res = "( | )\n(-N-)\n( | )"
    return res


class CarteURDL(CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 1, 1, 1]

    def num_carte(self):
        return 3

    def __str__(self):  
        res = "( | )\n(-+-)\n( | )"
        return res

class CarteURDL_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 1, 1, 1]

    def num_carte(self):
        return 31
    
    def __str__(self):  
        res = "( | )\n(-X-)\n( | )"
        return res    

class CarteURD (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 1, 0, 1]

    def num_carte(self):
        return 4

    def __str__(self):  
        res = "( | )\n( +-)\n( | )"
        return res

class CarteURD_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 1, 0, 1]

    def num_carte(self):
        return 41

    def __str__(self):  
          res = "( | )\n( X-)\n( | )"
          return res

class CarteURL (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 0, 1, 1]

    def num_carte(self):
        return 5

    def __str__(self):  
        res = "( | )\n(-+-)\n(   )"
        return res

class CarteURL_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 0, 1, 1]

    def num_carte(self):
        return 51

    def __str__(self):  
        res = "( | )\n(-X-)\n(   )"
        return res

class CarteUR (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 0, 0, 1]

    def num_carte(self):
        return 6

    def __str__(self):  
        res = "( | )\n( +-)\n(   )"
        return res

class CarteUR_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 0, 0, 1]

    def num_carte(self):
        return 61
    
    def __str__(self):  
        res = "( | )\n( X-)\n(   )"
        return res

class CarteUL (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 0, 1, 0]

    def num_carte(self):
        return 7
    
    def __str__(self):  
        res = "( | )\n(-X )\n(   )"
        return res

class CarteUL_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 0, 1, 0]

    def num_carte(self):
        return 71

    def __str__(self):  
        res = "( | )\n(-X )\n(   )"
        return res

class CarteUD (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 1, 1, 0, 0]

    def num_carte(self):
        return 8
    
    def __str__(self):  
        res = "( | )\n( + )\n( | )"
        return res

class CarteUD_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 1, 0, 0]

    def num_carte(self):
        return 81
  
    def __str__(self):  
        res = "( | )\n( X )\n( | )"
        return res

class CarteRL (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [1, 0, 0, 1, 1]

    def num_carte(self):
        return 9

    def __str__(self):  
          res = "(   )\n(-+-)\n(   )"
          return res

class CarteRL_neg (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 0, 0, 1, 1]

    def num_carte(self):
        return 91

    def __str__(self):  
          res = "(   )\n(-X-)\n(   )"
          return res

class CarteR (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 0, 0, 0, 1]

    def num_carte(self):
        return 12
      
    def __str__(self):  
          res = "(   )\n(-X )\n(   )"
          return res

class CarteU (CartePlateau):
    def __init__(self):
      super().__init__()

    def tab_bool(self):
        return [0, 1, 0, 0, 0]

    def num_carte(self):
        return 11

    def __str__(self):  
          res = "( | )\n( X )\n(   )"
          return res

#---------------------------------------------------------------------------------
#-------------------------------Les cartes or-------------------------------------

class CarteOr(Carte):

  def __init__(self, ctype):
    super().__init__()
    if 0 < ctype < 4:
      self.__valeur = ctype  #nombre d'or de 1 à 3


  def __str__(self):
    res = f"(O R)\n({self.__valeur}G*)\n(   )"
    return res

  def who(self):
    res = f"Carte {self.__type} Or"
    return res

#----------------------Carte Role-----------------------------
class CarteRole(Carte):

  def __init__(self, role):
    super().__init__()
    if 0 <= role < 2:
      self.__role = role  # 0 :saboteur ou 1 : mineur

  def __str__(self):
    if self.__role == 0:
      res = "( S )\n(SAB)\n( B )"
    else:
      res = "( M )\n(MIN)\n( N )"
    return res

  def who(self):
    res = "Carte Rôle "
    if self.__role == 0:
      res += "Saboteur"
    else:
      res += "Mineur"
    return res
