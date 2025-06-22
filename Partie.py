import random
from Joueur import Joueur
from RobotIA import RobotIA
from CarteAction import CarteAction
from Pioche import *
from CarteAttaque import CarteAttaque
from CarteDefense import CarteDefense
import time


class Partie:
  def __init__(self,listeJoueur,plat):
  #Initialise la partie
    self.__joueur = listeJoueur
    self.__plateau = plat
    self.__tour = []
    self.__manche = 1

  """ Getter """
  @property
  def manche(self):
    return self.__manche

  @property
  def tour(self):
    return self.__tour

  """ Setter """
  def nouvelleManche(self):
    self.__manche += 1

  
  def definirTour(self):
  #Definit le tour de jeu des joueurs
    ageMin = 100
    petit = 0
    tour = []
    for i in range(0,len(self.__joueur)):
      if isinstance(self.__joueur[i],RobotIA):
        pass
      if isinstance(self.__joueur[i],Joueur):
        if (self.__joueur[i]).age < ageMin:
          ageMin = (self.__joueur[i]).age
          petit = i
    for i in range(petit,len(self.__joueur)):
      tour.append(self.__joueur[i])
    for i in range(0,petit):
      tour.append(self.__joueur[i])
    print("Tour de rôle : ")
    for i in tour:
      print(i)
    self.__tour = tour

  
  def majTour(self):
  #Met à jour le tour de jeu des joueurs à la fin d'une manche en fonction du gagnant
    tour = [self.__tour[1]]
    for i in range(2,len(self.__tour),1):
      tour.append(self.__tour[i])
    tour.append(self.__tour[0])
    self.__tour = tour
    
  def distribuerRoles(self):
  #Distribue le rôle des joueurs, saboteur ou chercheur
    cpt = len(self.__joueur)
    if cpt == 3 or cpt == 4:
      sab = 1
      chr = cpt
    elif cpt == 5 or cpt == 6:
      sab = 2
      chr = cpt - 1
    elif cpt == 7 or cpt == 8 or cpt == 9:
      sab = 3
      chr = cpt - 2
    elif cpt == 10:
      sab = 4
      chr = 7

    for i in self.__tour:
      if random.random() > 0.6 and sab > 0 and i.role == None :
        i.role = 'Saboteur'
        sab -= 1
      else :
        if chr > 0 and i.role == None:
          i.role = 'Chercheur'
          chr -= 1
        else : 
          i.role = 'Saboteur'
          sab -= 1
  

  def reinitRole(self):
  #Remet le rôle à 0
    for i in self.__joueur:
      i.role = None

  def distribuerCartes(self,pioc):
  #Distribue les cartes aux joueurs
  #@param pioc est le tableau representant la pioche
    carte = 0
    if len(self.__joueur) == 3 or len(self.__joueur) == 4 or len(self.__joueur) == 5 :
      cpt = 6
    elif len(self.__joueur) == 6 or len(self.__joueur) == 7 :
      cpt = 5
    elif len(self.__joueur) == 8 or len(self.__joueur) == 9 or len(self.__joueur) == 10 :
      cpt = 4
    while carte < cpt:
      for i in self.__joueur:
        jsp = len(pioc)
        aEnlever = random.randint(0,len(pioc)-1)
        i.pioche(pioc[aEnlever])
        pioc.remove(pioc[aEnlever])        
      carte += 1

  def reinitMain(self):
  #Remet à 0 la main du joueur
    for i in self.__joueur:
      i.rMain()

  def reinitObj(self):
    for i in self.__joueur:
      i.reinitObjet()

  def reinitPlat(self, plat):
    self.__plateau = plat

  def strOr(self,listeOr):
      for i in listeOr:
          print(i)
          print()
      print("\n")

  def distribuerOrCher(self,listeOr,listeGagnant):
  #Sert à distribuer l'or à la fin d'une manche pour les chercheurs
  #@param listOr, la pioche d'or
  #@param listeGagnant, les joueurs gagnants de la manche
    listeDistribution = [listeGagnant[0]]
    for i in range(len(listeGagnant)-1,0,-1):
      listeDistribution.append(listeGagnant[i])
    while len(listeOr) != 0:
      for i in listeDistribution:
        if len(listeOr) == 0:
            break
        self.strOr(listeOr)
        
        if isinstance(i,Joueur):
          print(i,"\n")
          prendre = int(input(f"Quelle carte Or voulez-vous ? (1 à {len(listeOr)}) "))
          i.ors = listeOr[prendre-1]
          listeOr.remove(listeOr[prendre-1])
        elif isinstance(i,RobotIA):
          print("C'est au tour de", i,"de choisir une carte.")
          prendre = random.randint(0,len(listeOr)-1)
          i.ors = listeOr[prendre]
          listeOr.remove(listeOr[prendre])
          
          
  def distribuerOrSab(self,listeOr, listeGagnant):
  #Sert à distribuer l'or à la fin d'une manche pour les Sabotteurs
  #@param listOr, la pioche d'or
  #@param listeGagnant, les joueurs gagnants de la manche
    if len(listeGagnant) == 0:
        pass
    elif len(listeGagnant) == 1:
      recu = 0
      while recu < 4:
        if len(listeOr) == 0:
          break
        i = random.choice(listeOr)
        if i.valeur == 3 and recu <= 1:
          recu += i.valeur
          listeGagnant[0].ors = i
          listeOr.remove(i)
        elif i.valeur == 2 and recu <=2:
          recu += i.valeur
          listeGagnant[0].ors = i
          listeOr.remove(i)
        elif i.valeur == 1:
          recu += i.valeur
          listeGagnant[0].ors = i
          listeOr.remove(i)
    elif len(listeGagnant) == 2 or len(listeGagnant) == 3:
      for j in range(len(listeGagnant)):
          recu = 0
          while recu < 3:
            if len(listeOr) == 0:
              break
            i = random.choice(listeOr)
            if i.valeur == 3 and recu == 0:
              recu += i.valeur
              listeGagnant[j].ors = i
              listeOr.remove(i)
            elif i.valeur == 2 and recu <=1:
              recu += i.valeur
              listeGagnant[j].ors = i
              listeOr.remove(i)
            elif i.valeur == 1:
              recu += i.valeur
              listeGagnant[j].ors = i
              listeOr.remove(i)
    elif len(listeGagnant) == 4:
      for j in range(len(listeGagnant)):
          recu = 0
          while recu < 2:
            if len(listeOr) == 0:
              break
            i = random.choice(listeOr)
            if i.valeur == 2 and recu == 0:
              recu += i.valeur
              listeGagnant[j].ors = i
              listeOr.remove(i)
            elif i.valeur == 1:
              recu += i.valeur
              listeGagnant[j].ors = i
              listeOr.remove(i)
    
  def carteEnMainTotal(self):
  #Pour avoir le nombre total des cartes en main de tous les joueurs
    res = 0
    for i in self.__joueur:
      res += i.nbCarteEnMain()
    return res

  def strJoueur(self):
  #Affiche le nom des joueurs
    for i in self.__joueur:
      print(i,end="   ")
    print("\n")

  def demande_quelCarteJouer(self, joueurTurn):
  # Demande au joueur de jouer une carte de sa main
  # @param joueurTurn est un joueur
    self.__plateau.maj_platoB() 
  
    if len(joueurTurn.main) == 0:
      print("Plus de carte en main. Passe son tour.")
    else:
      joueurTurn.affiche_carteMain()
      print(f"{len(joueurTurn.main)+1}: Defausser une carte")
      i = input(f"Quelle carte voulez-vous jouer ? (1 à {len(joueurTurn.main)} ou {len(joueurTurn.main)+1}) ")
      print()
      while i.isnumeric() == False:
        print("Entrez un chiffre")
        i = input("Quelle carte voulez-vous jouer ? ")
      i = int(i)
      i = i-1
    # Pour une défausse
      if i==len(joueurTurn.main) :
          i=input(f"Quelle carte voulez-vous défausser  ? (1 à {len(joueurTurn.main)}) ")
          while i.isnumeric() == False:
            print("Entrez un chiffre")
            i = input("Quelle carte voulez-vous défausser ? ")
          i = int(i)-1
          joueurTurn.fausser(i)

    # Pour une carte Action
      elif isinstance(joueurTurn.main[i], CarteAction) == True :
          if isinstance(joueurTurn.main[i], CarteAttaque) or isinstance(joueurTurn.main[i], CarteDefense):
            alors = 0
            while alors == 0:
              self.strJoueur()
              jAction = int(input(f"Sur quel joueur voulez-vous utiliser votre carte ? (1 à {len(self.__joueur)}) : "))
              alors = joueurTurn.main[i].jouer(self.__plateau, joueurTurn, self.__joueur[jAction-1])
              if alors == 1:
                self.demande_quelCarteJouer(joueurTurn)
              if alors == 2:
                joueurTurn.fausser(i)
                break
          elif isinstance(joueurTurn.main[i], CarteROF):
            alors = 0
            while alors == 0:
              alors = joueurTurn.main[i].jouer(self.__plateau,joueurTurn)
              if alors == 1:
                self.acteChercheur(joueurTurn,cpt)
              if alors == 2:
                print(joueurTurn, "a décidé de jouer une carte ROF.")
                joueurTurn.fausser(i)
                break
            
          else:
            joueurTurn.main[i].jouer(self.__plateau,joueurTurn)
            joueurTurn.fausser(i)
        
    # Pour une carte Chemin
      else :
        alors = 1
        Jcarte = joueurTurn.main[i].num_carte()
        tourne = int(input("Voulez-vous tourner la carte ? (1 pour oui et 0 pour non) "))
        if tourne==1 :
          Jcarte*=10  
        print("Où voulez-vous placer la carte (x, y)? (Si en dessous de 0, entrer -1)")
        x = int(input("Abscisse x : "))
        y = int(input("Ordonnée y : "))
        if x<0:
            self.__plateau.update_plato_x(x)
            x=0
        if x>=self.__plateau.colonne :
            self.__plateau.update_plato_x(x)
            x=self.__plateau.colonne
            
        if y<0:
            self.__plateau.update_plato_y(y)
            y=0
        if y>=self.__plateau.ligne :
            self.__plateau.update_plato_y(y)
            y=self.__plateau.ligne  
         
        b=self.__plateau.verif_carte_autour(Jcarte,x, y)
        while b==0 and alors == 1:
          print("Impossible de placer la carte ici.")
          alors = int(input("Voulez-vous quand même la poser ? (1 pour oui, sinon 0) "))
          if alors == 0:
            self.demande_quelCarteJouer(joueurTurn)
            break
          elif alors == 1:
            x = int(input("Abscisse x : "))
            y = int(input("Ordonnée y : "))
            if x<0:
              self.__plateau.update_plato_x(x)
              x=0
            if x>=self.__plateau.colonne :
              self.__plateau.update_plato_x(x)
              x=self.__plateau.colonne
                
            if y<0:
              self.__plateau.update_plato_y(y)
              y=0
            if y>=self.__plateau.ligne :
              self.__plateau.update_plato_y(y)
              y=self.__plateau.ligne
            b = self.__plateau.verif_carte_autour(Jcarte, x, y)
          else:
            print("Désolé, je n'ai pas compris.")
            alors=1
            
        if b==1 :
          self.__plateau.plato[y][x] = Jcarte
          
        self.__plateau.verif_carte_end_atteint()
        joueurTurn.fausser(i)
 

  def acteChercheur(self, robotTurn, cpt, cptPourCher):
  #Définit l'action a faire lors son tour de jouer d'un robot avec le role chercheur
  #@param robotTurn, robot qui joue
  #@param cpt, permet de définir sur quelle partie du plateau il va jouer
    if len(robotTurn.main) == 0:
      print("Plus de carte en main. Passe son tour.")
    else:
      i = random.randint(0,len(robotTurn.main))
    
    # Pour une défausse
      if i==len(robotTurn.main) :
        print(robotTurn," a défaussé une carte.")
        i = random.randint(0,len(robotTurn.main)-1)
        robotTurn.fausser(i)
      
    # Pour une carte Action
      elif isinstance(robotTurn.main[i], CarteAction) == True :
        if isinstance(robotTurn.main[i], CarteAttaque):
          alors = 0
          while alors == 0:
            jAction = random.randint(0,len(self.__joueur)-1)
            while self.__joueur[jAction] == robotTurn:
              jAction = random.randint(0,len(self.__joueur)-1)
            alors = robotTurn.main[i].jouer(self.__plateau, robotTurn, self.__joueur[jAction])
            if alors == 1:
              self.acteChercheur(robotTurn,cpt,cptPourCher)
              break
            elif alors == 2:
              print(robotTurn, "a décidé de jouer une carte Attaque sur", self.__joueur[jAction])
              robotTurn.fausser(i)

        elif isinstance(robotTurn.main[i], CarteDefense):
          alors = 0
          while alors == 0:
            listePourDef = []
            for joue in self.__joueur:
              if joue.peutJouer() == 0:
                listePourDef.append(joue)
            if len(listePourDef) == 0 :
              self.acteChercheur(robotTurn,cpt,cptPourCher)
              break
            else:
              jAction = random.randint(0,len(listePourDef)-1)
              alors = robotTurn.main[i].jouer(self.__plateau, robotTurn, listePourDef[jAction])
              if alors == 1:
                self.acteChercheur(robotTurn,cpt,cptPourCher)
                break
              if alors == 2:
                print(robotTurn, "a décidé de jouer une carte Défense sur",self.__joueur[jAction])
                robotTurn.fausser(i)
                break
        elif isinstance(robotTurn.main[i], CarteROF):
          alors = 0
          while alors == 0:
            alors = robotTurn.main[i].jouer(self.__plateau,robotTurn)
            if alors == 1:
              self.acteChercheur(robotTurn,cpt,cptPourCher)
              break
            if alors == 2:
              print(robotTurn, "a décidé de jouer une carte ROF.")
              robotTurn.fausser(i)
              break
        else:
          robotTurn.main[i].jouer(self.__plateau,robotTurn)
          print(robotTurn, "a décidé de jouer une carte Action.")
          robotTurn.fausser(i)
        
    # Pour une carte Chemin
      else :
        Jcarte = robotTurn.main[i].num_carte()
        b = 0
        x = int( self.__plateau.colonne/2 )
        while x >= 0 and b == 0:
          y = self.__plateau.ligne - 2
          while y >= 0:
            if x<0:
              self.__plateau.update_plato_x(x)
              x=0
            if x>=self.__plateau.colonne :
              self.__plateau.update_plato_x(x)
              x=self.__plateau.colonne
                
            if y<0:
              self.__plateau.update_plato_y(y)
              y=0
            if y>=self.__plateau.ligne :
              self.__plateau.update_plato_y(y)
              y=self.__plateau.ligne
            
            b = self.__plateau.verif_carte_autour(Jcarte,x, y)
            if b == 1:
              break
            y -=1

          if b == 1:
            break 

          if cpt < cptPourCher:
            x -= 1
          if cpt >= cptPourCher:
            x += 1
        
        if b == 1:
          self.__plateau.plato[y][x] = robotTurn.main[i].num_carte()
          print(robotTurn, "a décidé de jouer une carte chemin.")
          robotTurn.fausser(i)
        elif b == 0:
          self.acteChercheur(robotTurn,cpt,cptPourCher)
        self.__plateau.verif_carte_end_atteint()
        


  def acteSaboteur(self,robotTurn):
  #Définit l'action a faire lors son tour de jouer d'un robot avec le role Sabotteur
  #@param robotTurn, robot qui joue
    if len(robotTurn.main) == 0:
      print("Plus de carte en main. Passe son tour.")
    else:
      i = random.randint(0,len(robotTurn.main))
  
    # Pour une défausse
      if i==len(robotTurn.main) :
        print(robotTurn," a défaussé une carte.")
        i = random.randint(0,len(robotTurn.main)-1)
        robotTurn.fausser(i)
    
    # Pour carte Action
      elif isinstance(robotTurn.main[i], CarteAction) == True :
        if isinstance(robotTurn.main[i], CarteAttaque):
          alors = 0
          while alors == 0:
            jAction = random.randint(0,len(self.__joueur)-1)
            while self.__joueur[jAction] == robotTurn:
              jAction = random.randint(0,len(self.__joueur)-1)
            alors = robotTurn.main[i].jouer(self.__plateau, robotTurn, self.__joueur[jAction])
            if alors == 1:
              self.acteSaboteur(robotTurn)
              break
            if alors == 2:
              print(robotTurn, "a décidé de jouer une carte Attaque sur",self.__joueur[jAction])
              robotTurn.fausser(i)
        elif isinstance(robotTurn.main[i], CarteDefense):
          print(robotTurn," a défaussé une carte.")
          robotTurn.fausser(i)
        else:
          robotTurn.main[i].jouer(self.__plateau,robotTurn)
          print(robotTurn, "a décidé de jouer une carte Action.")
          robotTurn.fausser(i)
  
    # Pour carte Chemin
      else:
        Jcarte = robotTurn.main[i].num_carte()
        b = 0
        x = int( self.__plateau.colonne/2 )
        while x >= 0:
          y = self.__plateau.ligne-2
          while y >= 0:
            if x<0:
              self.__plateau.update_plato_x(x)
              x=0
            if x>=self.__plateau.colonne :
              self.__plateau.update_plato_x(x)
              x=self.__plateau.colonne
                
            if y<0:
              self.__plateau.update_plato_y(y)
              y=0
            if y>=self.__plateau.ligne :
              self.__plateau.update_plato_y(y)
              y=self.__plateau.ligne
            
            b = self.__plateau.verif_carte_autour(Jcarte,x,y)
            if b == 1:
              break
            y -=1
  
          if b == 1:
            break
          x -= 1
  
        if b == 1:
          self.__plateau.plato[y][x] = robotTurn.main[i].num_carte()
          print(robotTurn, "a décidé de jouer une carte chemin.")
          robotTurn.fausser(i)
        else:
          self.acteSaboteur(robotTurn)
        self.__plateau.verif_carte_end_atteint()
        
        

       
  def determinerGagnantFinal(self):
  #Determine le gagnant à la fin d'une Partie
  #@return gagnant, le(s) gagnants de la partie
    max = 0
    gagnant = []
    for i in self.__joueur:
      if i.nbCarteOr() > max:
        max = i.nbCarteOr()
        gagnant = []
    for i in self.__joueur:
      if i.nbCarteOr() == max:
        gagnant.append(i)
    return gagnant

    