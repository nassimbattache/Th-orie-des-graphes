import numpy as np

g=[[1,2],[1,3],[1,4],[1,6],[1,7],[2,3],[2,4],[2,5],[2,6],[3,5],[3,6],[3,7],[4,5],[4,6],[4,7],[5,6],[6,7]]

#------------------------------Question 1--------------------------------------
'''ici j’ai utilisé la fonction "Len" pour calculer la taille qui correspond 
au nombre d'arrêtes '''

def taille(listeGraphe):
   return len(listeGraphe)


#------------------------------Question 2--------------------------------------
''' pour cette fonction je me suis servi de la bibliothèque numpy qui est connu
pour faciliter la manipulation des listes toute en essayant d'optimiser le 
programme le plus possible ,j'ai cherché np.unique(g) = array([1, 2, 3, 4, 5, 6, 7])
qui est le nombre de sommet dans la List et puis j’ai calculé sa taille'''

def ordre(listeGraphe):
    return (len(np.unique(listeGraphe)))


#-------------------------------Question 3-------------------------------------
'''pour bien comprendre ce qui suit voici a quoi ces valeurs sont égales
np.ravel(g) = array([1, 2, 1, 3, 1, 4, 1, 6, 1, 7, 2, 3, 2, 4, 2, 5, 2, 6, 3, 5, 3, 6,
       3, 7, 4, 5, 4, 6, 4, 7, 5, 6, 6, 7])
renvois la même liste que g si vous regardez bien vous allez remarquer que
c'est les mêmes éléments
np.bincount(m) = array([0, 5, 5, 5, 5, 4, 6, 4] sauf le 0 au début, ça représente
le nombre de répétition de chaque somment dans l'ordre croissant respectivement du 
sommet 1 au 7'''

def degre(listeGraphe, n):
   m=np.ravel(listeGraphe)
   s=np.bincount(m)
   return s[n]


#------------------------------Question 4--------------------------------------
'''on utilisant la boucle for qu'on a vu en salle '''

def voisins(listeGraphe, n):
    x=[]
    for i in listeGraphe:
        if (i[0]==n):
            x.append(i[1])
        elif (i[1]==n):
            x.append(i[0])
    return x


#------------------------------Question 5--------------------------------------
def complet(listeGraphe):
    b=max(max(listeGraphe))
    o=b*(b-1)/2
    f=len(listeGraphe)
    if o == f:
        return True
    else:
        return False


#----------------------------Question 6----------------------------------------    
'''dans cette équation j’ai utilisé une fonction que j’ai rajouter de ma part 
degre_chaque_sommet(listeGraphe)qui est définie si dessous qui me permet de 
me renvoyer les différents degrés des sommets et puis les avoir sans répétition 
avec l'aide de la fonction set, dans le cas où la taille est égale a deux, autrement 
dis le 0 du début et la valeur du nombre de tous les degrés qui serons égaux 
dans le cas du graphe régulier, dans le cas où il n'Ya pas des degrés similaires 
donc la taille sera systématiquement supérieure à 2 ce qui veut dire  que le
graphe n'est pas régulier '''

def regulier(listeGraphe):
    r=set(degre_chaque_sommet(listeGraphe))
    if (len(r) ==2):
        return True
    else:
        return False


#----------------------------Question ***----------------------------------------

def degre_chaque_sommet(listeGraphe):
   m=np.ravel(listeGraphe)
   s=np.bincount(m)
   return s

    
    
print("La taille du graphe G est :", taille(g))
print("")
print("L'ordre du graphe G est :", ordre(g))
print("")
n = int(input('introduisez le somment dont vous voulez savoir le nombre de voisins et la liste de ces derniers  : '))   
print("Le nombre de voisins du sommet " +str( n)+ " est :", degre(g,n))
print("")
print("les voisins du sommet " +str( n)+ " sont les suivants :", voisins(g,n))
print("")
print("Le graphe G est-il complet ?  ", complet(g))
print("Le graphe G est-il regulier ?  ", regulier(g))

''' conclusion: le graphe ne peut être complet s’il n'est pas régulier
par contre il peut être régulier sans être complet '''