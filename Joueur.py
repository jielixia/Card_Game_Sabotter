from CarteAction import CarteAction
from Plateau_Sab import *
from Carte import Carte
from CartesChemin import *

class Joueur:

  def __init__(self, nom, age):
  #Initialise un joueur
    self.__nom = nom                        #String
    self.__age = age                        #int
    self.__role = None                      #String
    self.__main = []                        #Carte[]
    self.__ors = []                         #Carte Or[]
    self.__objet = [True, True, True]       #boolean[3] [Lampe, Pioche, Wagon]

  """ Getter """
  @property
  def age(self):
    return self.__age

  @property
  def main(self):  # Affichage de la main
    return self.__main

  @property
  def role(self):  # Fins de manche
    return self.__role

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
    self.__main = []

  def pioche(self, pioc):  # Durant un tour
  #Permet au joueur de piocher une carte dans la pioche
  #@param pioc, la pioche du jeux
    if isinstance(pioc, Carte):
      (self.__main).append(pioc)
    else:
      print("Impossible d'entreprendre l'action demandée.")

  def fausser(self, fausse):
  #Permet de defausser une carte dans la main d'un joueur
  #@param fausse, indice de la carte à defausser
    carteAEnlever = self.__main[fausse]
    self.__main.remove(carteAEnlever)

  def nbCarteEnMain(self):
  #@return le nombre de la main du joueur
    return len(self.__main)

  def nbCarteOr(self):
  #@return cpt la valeur total de ses cartes or
    cpt = 0
    for i in self.__ors:
      cpt += i.valeur
    return cpt

  def peutJouer(self):
  #@return 1 ou 0 si le joueur peut jouer
    for i in self.__objet:
      if i == False:
        return 0
    return 1

  def strObjet(self):
  #affiche les objets du joueur
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

  def reinitObjet(self):
  # Réinitialise les objets du joueur en les rendant tous True
    for i in range(0,len(self.__objet)):
      self.__objet[i] = True

  def __str__(self):
  #@return res le nom du joueur
    res = f"Joueur {self.__nom}"
    return res
    
  def affiche_carteMain(self):
  #affiche la carte en main du joueur
    res=''
    plat=Plateau()
    for j in range(1,len(self.__main)+1) :
      res+=f'{j}: \t\t'
    res1, res2, res3=[], [], []
  
    for i in range (len(self.__main)):
      if isinstance(self.__main[i], CarteAction) == False :
        ind = self.__main[i].num_carte()
        n1, n2, n3 = plat.nature_str(ind)
        res1.append(n1)
        res2.append(n2)
        res3.append(n3)
      else :
        n1, n2, n3=self.__main[i].__str__()
        res1.append(n1)
        res2.append(n2)
        res3.append(n3)

    print(res)
    for it in res1 :
      print(it, end='   ')
    print() 
    for it in res2 :
      print(it, end='   ')
    print() 
    for it in res3 :
      print(it, end='   ')
    print()

    