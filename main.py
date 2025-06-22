from aImporter import *

print("Bienvenue ! Voici le jeu du SabOOtters !")
print("(Jeu créé par Christine, Claire et Jieli !)")

""" Variable globale """
# Même plateau de début pour toutes les parties/manches
plat = Plateau()

# time.sleep(2)

jouer = "o"
while(jouer == "o"):

  # Initialisation de la partie
  cbJoueur = input("Combien y a-t-il de joueurs ? ")
  while cbJoueur.isnumeric() == False:
    print("Entrez un chiffre")
    cbJoueur = input("Combien y a-t-il de joueurs ? ")
  cbJoueur = int(cbJoueur)
  
  while 10 < cbJoueur or cbJoueur < 3:
    if cbJoueur < 3:
      print("OH ! Pas assez de joueurs !")
      cbJoueur = int(input("Combien y a-t-il de joueurs ? "))
    elif cbJoueur > 10:
      print("OH ! Trop de joueurs !")
      cbJoueur = int(input("Combien y a-t-il de joueurs ? "))
  cbRobot = cbJoueur + 1
  while cbRobot > cbJoueur:
    cbRobot = input("Combien de robot(s) ? ")
    while cbRobot.isnumeric() == False:
      print("Entrez un chiffre")
      cbRobot = input("Combien y a-t-il de robots ? ")
    cbRobot = int(cbRobot)
    if cbRobot > cbJoueur:
      print(f"Trop de robots pour {cbJoueur} joueurs.")

  listeJoueur = []
  for i in range(0,cbJoueur-cbRobot):
    nom = str(input(f"Joueur {i+1}, veuillez donner un nom : "))
    age = input("Maintenant, veuillez donner un âge : ")
    while age.isnumeric() == False:
      print("Entrez un chiffre")
      age = input("Donnez un âge ? ")
    age = int(age)
    listeJoueur.append(Joueur(nom,age))
  for i in range(0,cbRobot):
    listeJoueur.append(RobotIA())

  random.shuffle(listeJoueur)

  """ Création d'une partie grâce aux données qu'on vient de collecter ! """
  p = Partie(listeJoueur,plat)
  p.definirTour()

  """---------------------------------------------------------------------------"""
  """----------------------------- Jouer une Partie ----------------------------"""
  """---------------------------------------------------------------------------"""
  while p.manche <= 3:
    # Même pioche par manche
    laPioche = pioche.copy()
    lesOrs = listeCarteOr      
    random.shuffle(laPioche)      
    random.shuffle(lesOrs)
    
    p.distribuerRoles()
    listeSab = []
    listeCher = []
    for i in listeJoueur:
      if i.role == 'Saboteur':
        listeSab.append(i)
      elif i.role == 'Chercheur':
        listeCher.append(i)



    for t in range(0,len(p.tour)):
      
# ----------------------------------------------- Affichage des rôles
      if t == 0:
        if isinstance(p.tour[0],Joueur):
          print("Affichage des rôles !")
          print("Veuillez fermer les yeux sauf", p.tour[0], "!")
          time.sleep(4)
      if isinstance(p.tour[t],Joueur):
        print(p.tour[t],end="")
        print(", voici votre rôle :",p.tour[t].role)
        time.sleep(4)
        clear()
      if t != len(p.tour)-1:
        for po in range(t+1,len(p.tour)):
          if isinstance(p.tour[po],Joueur):
            print("Veuillez fermer les yeux et demander à", p.tour[po],"d'ouvrir ses yeux")
            t = po
            time.sleep(4)
            break
        clear()

#--------------------------------------------------------------------
    
    p.distribuerCartes(laPioche)
    gagner=0
    cpt_JoueurPeutJouer = 0

    """---------------------------------------------------------------------"""
    """-------------------------DEROULEMENT D'UNE MANCHE--------------------"""
    """---------------------------------------------------------------------"""
    while p.carteEnMainTotal() > 0 and cpt_JoueurPeutJouer < len(listeJoueur) and gagner==0 :
      print("Carte en main total: ",p.carteEnMainTotal())
      cpt_JoueurPeutJouer = 0
      for i in listeJoueur:
        if i.peutJouer() == 0:
          cpt_JoueurPeutJouer += 1
        if i.nbCarteEnMain() == 0:
          cpt_JoueurPeutJouer += 1

      print("cpt_JoueurPeutJouer: ",cpt_JoueurPeutJouer)
      
      cpt = 0
      cptPourCher = cbRobot*10+1

  #-----------------------Tour d'un Joueur--------------------------------
      for j in p.tour:
        print("Nombre de cartes dans la pioche: ", len(laPioche))
        gagnant = j
        #Si joueur humain
        if isinstance(j,Joueur):
          if j.peutJouer() == 0:
            j.strObjet()
            print("Désolée",j,", tu ne peux pas jouer")
            time.sleep(4)
                
          elif j.peutJouer() == 1 :
            plat.afficher()
            plat.maj_platoB()
            print("C'est au tour de", j,":")
            j.strObjet()
            p.demande_quelCarteJouer(j)
            if len(laPioche) != 0:
              aPrendre = random.choice(laPioche)
              j.pioche(aPrendre)
              laPioche.remove(aPrendre)
              
        #Si joueur robot
        elif isinstance(j,RobotIA):
          cpt += 1
          if j.peutJouer() == 0:
            j.strObjet()
            print("Désolée",j,", tu ne peux pas jouer")
            time.sleep(4)
          elif j.peutJouer() == 1:
            plat.afficher()
            plat.maj_platoB()
            print("C'est au tour de ", j)
            j.strObjet()
            print()
            if j.role == "Chercheur":
              p.acteChercheur(j,cpt,cptPourCher)
              if len(laPioche) != 0:
                aPrendre = random.choice(laPioche)
                j.pioche(aPrendre)
                laPioche.remove(aPrendre)
            elif j.role == 'Saboteur':
              p.acteSaboteur(j)
              if len(laPioche) != 0:
                aPrendre = random.choice(laPioche)
                j.pioche(aPrendre)
                laPioche.remove(aPrendre)
                
              
        #verif si gagner la manche
        for i,j in enumerate(plat.plato):
            for k,l in enumerate(j):
              if l==21.5:
                gagner=1
        
        time.sleep(4)
        clear()
        if gagner==1:
          break


    if gagner==1 :
      print("Trésor trouvé ! Les chercheurs ont gagné !\n")
      time.sleep(4)
    else :
      print("Haha vous n'avez pas trouvé le trésor ! Les Saboteurs ont gagné !\n")
      time.sleep(4)
            
    print("Passons à la distribution de l'or !\n")
    time.sleep(4)
    
    """ Distribution de l'or """
    while p.tour[0] != gagnant:
      p.majTour()
    if gagner == 1 and gagnant.role == 'Chercheur':
      listOR = []
      if cbJoueur != 10:
        for i in range(0,9):
          carteOrAEnlever = random.choice(lesOrs)
          listOR.append(carteOrAEnlever)
          lesOrs.remove(carteOrAEnlever)
      else:
        for i in range(cbJoueur):
          carteOrAEnlever = random.choice(lesOrs)
          listOR.append(carteOrAEnlever)
          lesOrs.remove(carteOrAEnlever)
      p.distribuerOrCher(listOR,listeCher)
    else:
      p.distribuerOrSab(lesOrs,listeSab)

    print("Les cartes Or ont été distribuées !\n \n")
            
    """ Fin de manche, on reinitialise tout """
    print("Fin de manche !")
    plat=Plateau()
    p.reinitRole()
    p.reinitMain()
    p.reinitObj()
    p.majTour()
    p.nouvelleManche()
    p.reinitPlat(plat)
    gagner = 0

  
  """------------------------- Fin de partie-------------------------------- """
  """----------------------------------------------------------------------- """
  
  print("Et une fin de partie !\n")
  for i in listeJoueur:
    print(f"{i} a {i.nbCarteOr()} cartes Or.")
    
  print("Voici le(s) gagnant(s) : ")
  gagnantFinal = p.determinerGagnantFinal()
  for i in gagnantFinal:
    print(i)
  jouer = str(input("Voulez-vous refaire une partie ? (o/n) "))
  while jouer != "o" and jouer != "n":
    jouer = char(input("Désolé, je n'ai pas compris\nVoulez-vous refaire une partie ? (o/n) "))

