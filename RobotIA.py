from CarteAction import CarteAction
from Plateau_Sab import Plateau
from Carte import Carte

class RobotIA:
  num = 1
  def __init__(self):
  #Initialise le robot
    self.__nom = RobotIA.num
    self.__role = None                   #String
    self.__main = []                   #Carte[]
    self.__ors = []                    #Carte Or[]
    self.__objet = [True,True,True]      #boolean[3] [Lampe, Pioche, Wagon]
    RobotIA.num += 1
 
  """ Getter """
  @property
  def role(self):  # Fins de manche
    return self.__role

  @property
  def main(self):
    return self.__main

  @property
  def ors(self):  # Fin de partie
    return self.__ors

  @property
  def objet(self):  # Si le joueur peut jouer ou pas
    return self.__objet

  """ Setter """
  @ors.setter
  def ors(self, value):  # Fin de manche
    self.__ors.append(value)

  @role.setter
  def role(self, role):  # Début de manche
    self.__role = role


  def rMain(self):
    self.__main == []

  def pioche(self,pioc):    # Durant un tour
  # Pioche une carte pour la mettre dans la main du joueur
  # @param pioc une carte de la pioche
    if isinstance(pioc,Carte):
      (self.__main).append(pioc)
    else:
      print("Impossible d'entreprendre l'action demandée.")

  def fausser(self,fausse):               # Durant un tour
  #Defausse une carte de la main du robot
  #@param fausse indice de la carte à défausser dans la main du joueur
    carteAEnlever = self.__main[fausse]
    self.__main.remove(carteAEnlever)

  def peutJouer(self):
  # Dit si le joueur peut jouer
  # @return 1 ou 0 si c'est possible
    for i in self.__objet:
      if i == False:
        return 0
    return 1

  def nbCarteEnMain(self):
  # @return le nombre de carte en main
    return len(self.__main)

  def nbCarteOr(self):
  # Permet de calculer le nombre d'or en possession du joueur
  # @return le nombre d'or au total
    cpt = 0
    for i in self.__ors:
      cpt += i.valeur
    return cpt

  def reinitObjet(self):
  # Réinitialise les objets du robot en les rendant tous True
    for i in range(0,len(self.__objet)):
      self.__objet[i] = True

  def strObjet(self):
  #Affiche les objets du robot
    if self.__objet[0] == True:
      print("Lampe en marche")
    else:
      print("Lampe cassée")
    if self.__objet[1] == True:
      print("Pioche en marche")
    else:
      print("Pioche cassée")
    if self.__objet[2] == True:
      print("Wagon en marche")
    else:
      print("Wagon cassé")

  def __str__(self):
  #Renvoie le nom du robot
  #@return res, str du nom du joueur
      res = f"Robot {self.__nom}"
      return res
  