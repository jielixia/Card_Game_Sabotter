from CartesChemin import *
from Carte import Carte
import numpy as np
import random

class Plateau :
  
    def __init__ (self) :
    #Initialise le plateau de depart
        plato = np.zeros((5, 9)) #plateau du jeu sous forme de matrice flaot
        platoB=np.zeros(np.shape(plato)) #plateau du jeu pour savoir si un chemin est continu
        memo=[(2,0)] #memoire pour les differents chemin
        carte_dep = CarteDepart()
        plato[2][0] = carte_dep.num_carte()
        platoB[2][0] = 2
        ind = random.randint(1, 3)
        carte_arv_tres = CarteEnd('Tresor')
        carte_arv_pierre = CarteEnd('Pierre')  
        if ind ==1 :
            plato[0][8]=carte_arv_tres.num_carte()
            plato[2][8]=carte_arv_pierre.num_carte()
            plato[4][8]=carte_arv_pierre.num_carte()
            
        elif ind==2 :
            plato[0][8]=carte_arv_pierre.num_carte()
            plato[2][8]=carte_arv_tres.num_carte()
            plato[4][8]=carte_arv_pierre.num_carte()
        
        else :
            plato[0][8]=carte_arv_pierre.num_carte()
            plato[2][8]=carte_arv_pierre.num_carte()
            plato[4][8]=carte_arv_tres.num_carte()
            
        self.plato = plato
        ligne, colonne = np.shape(plato)
        self.ligne = ligne 
        self.colonne = colonne 
        self.platoB= platoB
        self.memo=memo

      
    
    def nature_str(self, indice):
    #Renvoie les 3 lignes d'affichages en fonction de l'indice de la carte du plateau
        
        n1,n2,n3='     ','     ','     '
        if 1<=indice<=8 or indice ==11 or indice==31 or indice==41 or indice==51 or indice==61 or indice==71 or indice==81 or indice==21.5 or indice==22.5 or indice==30 or indice==40 or indice==80:
            n1='( | )'
        elif indice !=0 :
            n1='(   )'
        else :
            n1='     '
            
        if 3<=indice<=4 or indice==1 or indice==8 or indice==81 or indice==31 or indice==41 or indice==21.5 or indice==22.5 or indice==30 or indice==40 or indice==80 or indice==50 or indice==60 or indice==70 or indice==110 :
            n3='( | )'
        elif indice==0 :
            n3='     '
        else : 
            n3='(   )'
            
        if indice==3 or indice==5 or indice==9 or indice==50 or indice==90 or indice==30:
            n2='(-+-)'
        elif indice==31 or indice==51 or indice==91:
            n2='(-X-)'
        elif indice==4 or indice==6 or indice==70 :
            n2='( +-)'
        elif indice==41 or indice==61 or indice==12:
            n2='( X-)'
        elif indice==7 or indice==40 or indice==60:
            n2='(-+ )'
        elif indice==71 or indice==120:
            n2='(-X )'
        elif indice==8 :
            n2='( + )'
        elif indice==81 or indice==11 :
            n2='( X )' 
        elif indice==1 :
            n2='(-S-)'
        elif 21==indice or indice==22 :
            n2='(END)'
        elif 21.5==indice:
            n2='(-G-)'
        elif indice == 22.5 :
            n2='(-N-)'
        else :
            n2='     '
        return n1, n2, n3

    
    def conv_plato_str (self) :
    #Convertit le plateau en tableau de str
  
        board=[]
        row1=[]
        row2=[]
        row3=[]
        for i in range (self.ligne):
            row1=[' |']
            row2=[str(i)+'|']
            row3=[' |']
            for j in range (self.colonne):
                n1, n2, n3=self.nature_str(self.plato[i][j])
                row1.append(n1)
                row2.append(n2)
                row3.append(n3)
            board.append(row1)
            board.append(row2)
            board.append(row3)
        return board

    
    def afficher (self) :
    #Affiche le plateau
        
        board=self.conv_plato_str()
       
        print("L'état actuel de la mine :")
        
        texte_board=" |"
        for i in range(self.colonne):
            texte_board+=2*" "+str(i)+2*" "
        texte_board+="\n-+"+5*self.colonne*"-"
        
        print(texte_board)
        for row in board :
            for item in row :
                print(item, end='')
            print()
            
        print('-+'+self.colonne*'-----')

    
    def update_plato_x(self, x):
    # Met à jour la taille du tableau selon l'axe x des abscisse
    # @param x cordonnée (abscisse) donnée par le joueur 
  
        if x==-1:
            self.plato=np.insert(self.plato, 0,0, axis=1)
            self.ligne, self.colonne=np.shape(self.plato)
        elif x>=self.colonne:
            self.plato=np.insert(self.plato,self.colonne,0, axis=1)
            self.ligne, self.colonne=np.shape(self.plato)
        
    def update_plato_y(self, y):
    # Met à jour la taille du tableau selon l'axe y des ordonnees
    # @param y cordonnée (ordonnée) donnée par le joueur
        if y==-1:
            self.plato=np.insert(self.plato, 0,0, axis=0)
            self.ligne, self.colonne=np.shape(self.plato)
        elif y>=self.ligne:
            self.plato=np.insert(self.plato,self.ligne,0, axis=0)
            self.ligne, self.colonne = np.shape(self.plato)

    def ifPoserPossible (self, indice_J, indice_P, ind):
    #Verifie si les 2 cartes peuvent être poseées à côté
    # @param indice_J, indice_P sont les numéros des cartes du joueur et celui deja mis sur le plateau
    # @param ind indice qui indique si la verification se fait en haut, en bas, à droite ou à gauche de la carte du joueur
    # @return True ou False (True si possible ou pas) et 1 ou 0 (1 si possible avec un chemin connecté)
      
        indice=indice_J
        if indice_J%10==0:
          indice=indice_J/10
        carteJ = self.associeNumaCarte(indice)
        indicep=indice_P
        if indice_P%10==0:
          indicep=indice_P/10
        carteP = self.associeNumaCarte(indicep)
        tab1=carteJ.tab_bool() #carte du joueur
        tab2=carteP.tab_bool() #carte du plateau
        if indice_J%10==0:
          tabm=tab1
          tab1[1], tab1[2], tab1[3], tab1[4] = tabm[2], tabm[1], tabm[4], tabm[3]
        if indice_P%10==0:
          tabm2=tab2
          tab2[1], tab2[2], tab2[3], tab2[4] = tabm2[2], tabm2[1], tabm2[4], tabm2[3] 
          
        #si carte plateau est non negatif
        if tab1[1]==tab2[2]==1 and ind==1 and tab2[0]==1: #up et down
          return True,1
        elif tab1[2]==tab2[1]==1 and ind==2 and tab2[0]==1 : #down et up
          return True,1 
        elif tab1[4]==tab2[3]==1  and ind==4 and tab2[0]==1: #Right et Left
          return True,1 
        elif tab1[3]==tab2[4]==1 and ind==3 and tab2[0]==1: #left et right
          return True,1    
        elif tab1[1]==tab2[2]==0 and ind==1 :
          return True,0
        elif tab1[2]==tab2[1]==0 and ind==2 :
          return True,0
        elif tab1[4]==tab2[3]==0  and ind==4 :
          return True,0
        elif tab1[3]==tab2[4]==0 and ind==3 :
          return True,0 
        else :
          return False,0
   
          

    def associeNumaCarte (self, num):
    # Associe le numero dans la matrice plato à une Classe Carte
    # @param num le numero relié à une carte
    # @return carte la carte associée au numero
        carte = CarteDepart()
        if num==3:
            carte = CarteURDL()
        elif num==4:
            carte = CarteURD()
        elif num==5:
            carte = CarteURL()
        elif num==6:
            carte = CarteUR()
        elif num==7:
            carte = CarteUL()
        elif num==8:
            carte = CarteUD()
        elif num==9:
            carte = CarteRL()     
        elif num==12:
            carte = CarteR()
        elif num==11:
            carte = CarteU()     
        elif num==31:
            carte = CarteURDL_neg()
        elif num==41:
            carte = CarteURD_neg()
        elif num==51:
            carte = CarteURL_neg()
        elif num==61:
            carte = CarteUR_neg()
        elif num==71:
            carte = CarteUL_neg()
        elif num==81:
            carte = CarteUD_neg()
        elif num==91:
            carte = CarteRL_neg()
        elif num==21:
            carte = CarteEnd('Tresor')
        elif num==22:
            carte = CarteEnd('Pierre')
        return carte


    def verif_carte_autour(self, carteJ, x, y) : #x=abscisse => colonne, y=ordonne => ligne
    # Vérifie si la carte du joueur peut être posée à l'emplacement (x,y)
    # @param carteJ la carte du joueur
    # @param x (abscisse) et y (ordonnée)
    # @return bol (1 ou 0) (1 si possible de poser la carte)
        bol, sum=1,0
        cpt,b=0,0
        #self.maj_platoB()
        if self.plato[y][x]==0 or carteJ==21 or carteJ==22 : #verif si l'emplacement est vide
        
            if 0<x<self.colonne-1 and 0<y<self.ligne-1 : # si au milIeu du plateau
            
                if self.plato[y-1][x]==0 and self.plato[y+1][x]==0 and self.plato[y][x-1]==0 and self.plato[y][x+1]==0 :
                    return 0
                if self.plato[y-1][x]!=0 : # en haut de (x,y)
                    carteP=self.plato[y-1][x] #self.associeNumaCarte(self.plato[y-1][x])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 1)
                    sum=sum+cpt
                    bol=bol*b
                if self.plato[y+1][x]!=0 : # en bas de (x,y)
                    carteP=self.plato[y+1][x] #self.associeNumaCarte(self.plato[y+1][x])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 2)
                    sum=sum+cpt
                    bol=bol*b
                if self.plato[y][x-1]!=0 : # a gauche de (x,y)
                    carteP=self.plato[y][x-1] #self.associeNumaCarte(self.plato[y][x-1])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 3)
                    sum+=cpt
                    bol=bol*b
                if self.plato[y][x+1]!=0 : # a droite de (x,y)
                    carteP=self.plato[y][x+1] #self.associeNumaCarte(self.plato[y][x+1])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 4)
                    sum+=cpt
                    bol=bol*b
            
            
            elif x==0 : #verif bord à gauche
                if y==0 :
                    if self.plato[y+1][x]==0 and self.plato[y][x+1]==0 :
                        return 0
                elif y==self.ligne-1 :
                    if self.plato[y-1][x]==0 and self.plato[y][x+1]==0 :
                        return 0
                else :
                    if self.plato[y-1][x]==0 and self.plato[y+1][x]==0 and self.plato[y][x+1]==0 :
                        return 0
                
                if self.plato[y][x+1]!=0 : # a droite de (x,y)
                    carteP=self.plato[y][x+1] #self.associeNumaCarte(self.plato[y][x+1])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 4)
                    sum+=cpt
                    bol=bol*b
                if y<self.ligne-1 : #exept coin en bas
                    if self.plato[y+1][x]!=0 : # en bas de (x,y)
                        carteP=self.plato[y+1][x] #self.associeNumaCarte(self.plato[y+1][x])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 2)
                        sum+=cpt
                        bol=bol*b
                if y>0 : #exept coin en haut
                    if self.plato[y-1][x]!=0 : # en haut de (x,y)
                        carteP=self.plato[y-1][x] #self.associeNumaCarte(self.plato[y-1][x])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 1)
                        sum+=cpt
                        bol=bol*b
                
                
            elif x==(self.colonne-1) : #verif bord à droite
                if y==0 :
                    if self.plato[y+1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                elif y==self.ligne-1 :
                    if self.plato[y-1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                else :
                    if self.plato[y-1][x]==0 and self.plato[y+1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                
                if self.plato[y][x-1]!=0 : # a droite de (x,y)
                    carteP=self.plato[y][x-1] #self.associeNumaCarte(self.plato[y][x-1])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 3)
                    sum+=cpt
                    bol=bol*b
                if y<self.ligne-1 : #exept coin en bas
                    if self.plato[y+1][x]!=0 : # en bas de (x,y)
                        carteP=self.plato[y+1][x] #self.associeNumaCarte(self.plato[y+1][x])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 2)
                        sum+=cpt
                        bol=bol*b
                if y>0 : #exept coin en haut
                    if self.plato[y-1][x]!=0 : # en haut de (x,y)
                        carteP=self.plato[y-1][x] #self.associeNumaCarte(self.plato[y-1][x])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 1)
                        sum+=cpt
                        bol=bol*b
            
            
            elif y==0 : #verif bord en haut
                if x==0 :
                    if self.plato[y+1][x]==0 and self.plato[y][x+1]==0 :
                        return 0
                elif x==self.colonne-1 :
                    if self.plato[y+1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                else :
                    if self.plato[y][x+1]==0 and self.plato[y+1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                
                if self.plato[y+1][x]!=0 : # en bas de (x,y)
                    carteP=self.plato[y+1][x] #self.associeNumaCarte(self.plato[y+1][x])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 2)
                    sum+=cpt
                    bol=bol*b
                if x<self.colonne-1 : #exept coin a droite
                    if self.plato[y][x+1]!=0 : # a droite de (x,y)
                        carteP=self.plato[y][x+1] #self.associeNumaCarte(self.plato[y][x+1])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 4)
                        sum+=cpt
                        bol=bol*b
                if x>0 : #exept coin a gauche
                    if self.plato[y][x-1]!=0 : # a gauche de (x,y)
                        carteP=self.plato[y][x-1] #self.associeNumaCarte(self.plato[y][x-1])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 3)
                        sum+=cpt
                        bol=bol*b
                        
            elif y==(self.ligne-1) : #verif bord en bas
                if x==0 :
                    if self.plato[y-1][x]==0 and self.plato[y][x+1]==0 :
                        return 0
                elif x==self.colonne-1 :
                    if self.plato[y-1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                else :
                    if self.plato[y][x+1]==0 and self.plato[y-1][x]==0 and self.plato[y][x-1]==0 :
                        return 0
                
                if self.plato[y-1][x]!=0 : # en haut de (x,y)
                    carteP=self.plato[y-1][x] #self.associeNumaCarte(self.plato[y-1][x])
                    b, cpt =self.ifPoserPossible(carteJ, carteP, 1)
                    sum+=cpt
                    bol=bol*b
                if x<self.colonne-1 : #exept coin a droite
                    if self.plato[y][x+1]!=0 : # a droite de (x,y)
                        carteP=self.plato[y][x+1] #self.associeNumaCarte(self.plato[y][x+1])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 4)
                        sum+=cpt
                        bol=bol*b
                if x>0 : #exept coin a gauche
                    if self.plato[y][x-1]!=0 : # a gauche de (x,y)
                        carteP=self.plato[y][x-1] #self.associeNumaCarte(self.plato[y][x-1])
                        b, cpt =self.ifPoserPossible(carteJ, carteP, 3)
                        sum+=cpt
                        bol=bol*b
            
            if sum==0 or self.platoB[y][x]==0:
              return 0
            return bol 
        else :
            return 0
        

    def verif_carte_end_atteint(self) :
    # Vérifie si une carte end a été atteinte et ajoute 0.5 au numero de la carte dans plato
      self.maj_platoB()
      for i,j in enumerate(self.plato):
        for k,l in enumerate(j):
          if l==22 or l==21:
            carteE=self.plato[i][k] 
            b=self.verif_carte_autour(carteE, k, i)
            if b==1:
              self.plato[i][k]+=0.5

  
    def verif_UDLR (self, i, j):
    #Met à jour platoB selon si c'est possible de mettre une carte (si possible =1)
    #@param i, j indice du platoB
      l, c=self.ligne, self.colonne
      if i+1<l :
        if self.platoB[i+1][j]!=2 :
            self.platoB[i+1][j]=1  
      if i-1>=0:      
          if self.platoB[i-1][j]!=2 : 
            self.platoB[i-1][j]=1
      if j-1>=0 :
        if self.platoB[i][j-1]!=2 :
            self.platoB[i][j-1]=1
      if j+1<c:
        if self.platoB[i][j+1]!=2 :
            self.platoB[i][j+1]=1


    def verif_unchemin(self,i,j):
    #Verifie si le chemin est continue et met à jour platoB
    #@param i, j indice du platoB
      fini=0
      self.verif_UDLR(i,j)
      while fini==0 :
          ih,ip,ine= i, i+1, i-1
          jh,jp, jne= j, j+1, j-1
          l, c=np.shape(self.plato)
          cpt=0
          m=[]
          if ine<0:
              ine=0
          if ine>=0:
              if self.plato[ine][jh]>0 and self.platoB[ine][jh]!=2:
                  self.platoB[ine][jh]=2
                  self.verif_UDLR(ine,jh)
                  i,j=ine,jh
                  m.append((i,j))
              else:
                  cpt+=1
      
          if jp<=c :
              if jp==c:
                  jp=c-1
              if self.plato[ih][jp]>0 and self.platoB[ih][jp]!=2:
                  self.platoB[ih][jp]=2
                  self.verif_UDLR(ih,jp)
                
                  i,j=ih,jp
                  m.append((i,j))
              else:
                  cpt+=1
  
          if ip<=l :
              if ip==l:
                  ip=l-1
              if self.plato[ip][jh]>0 and self.platoB[ip][jh]!=2:
                  self.platoB[ip][jh]=2
                  self.verif_UDLR(ip,jh)
                  i,j=ip,jh 
                  m.append((i,j))
              else:
                  cpt+=1
           
          if jne<0:
              jne=0
          if jne>=0:
              if self.plato[ih][jne]>0  and self.platoB[ih][jne]!=2:
                  self.platoB[ih][jne]=2
                  self.verif_UDLR( ih,jne)
                  i,j=ih,jne
                  m.append((i,j))
              else:
                  cpt+=1
  
          if cpt<3:
              for e,k in enumerate(m):
                  self.memo.append(k)
          if cpt==4:
              fini=1

  
    def maj_platoB(self):
    #Met à jour platoB
      self.platoB=np.zeros(np.shape(self.plato))
      
      for i,j in enumerate(self.plato):
          for k,l in enumerate(j):
              if l==1:
                  dx, dy=k,i
      i , j= dy, dx 
      self.platoB[i][j]=2
      long=len(self.memo)
      ok=0
      i=0
      im,jm=self.memo[i]
      while ok==0:
          im,jm=self.memo[i]
          self.verif_unchemin(im, jm)
          long=len(self.memo)
          if i==long-1:
              ok=1
          i+=1
    