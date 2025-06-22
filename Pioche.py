from CartesChemin import *
from CarteAttaque import CarteAttaque
from CarteDefense import CarteDefense
from CarteMAP import CarteMAP
from CarteROF import CarteROF
from CarteOr import CarteOr

#Création d'une pioche unique
pioche = []
#Mettre les Cartes Chemins dans la pioche
for i in range(5): 
  pioche.append(CarteURDL())
pioche.append(CarteURDL_neg())
for i in range(5):
  pioche.append(CarteURD())
pioche.append(CarteURD_neg())
for i in range(5):
  pioche.append(CarteURL())
pioche.append(CarteURL_neg())
for i in range(5):
  pioche.append(CarteUR())
pioche.append(CarteUR_neg())
for i in range(4):
  pioche.append(CarteUL())
pioche.append(CarteUL_neg())
for i in range(4):
  pioche.append(CarteUD())
pioche.append(CarteUD_neg())
for i in range(3):
  pioche.append(CarteRL())
pioche.append(CarteRL_neg())
pioche.append(CarteU())
pioche.append(CarteR())


#Mettre les Carte Action dans pioche
types = ['L','W','P']
for i in types :
  for j in range (0,2):
      pioche.append(CarteDefense(i))
  for k in range (0,3):
      pioche.append(CarteAttaque(i))
pioche.append(CarteDefense('LP'))
pioche.append(CarteDefense('LW'))
pioche.append(CarteDefense('PW'))
for i in range (0,6) : 
    pioche.append(CarteMAP())
    if i%2==0 : pioche.append(CarteROF())

#Création d'une pioche pour les cartes or
listeCarteOr = []
for i in range(16):
  listeCarteOr.append(CarteOr(1))
for i in range(8):
  listeCarteOr.append(CarteOr(2))
for i in range(4):
  listeCarteOr.append(CarteOr(3))
