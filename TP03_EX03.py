
G ={'S0':['S1','S2'],'S1':['S3','S2'],'S2':['S4'],'S3':['S4','S5'],'S4':['Sf'],'S5':['Sf'],'Sf':[]}
liste_cout= {'S0':{'S1':0,'S2':3},'S1':{'S3':2,'S2':2},'S2':{'S4':2},'S3':{'S4':4,'S5':1},'S4':{'Sf':2},'S5':{'Sf':6},'Sf':{}}
#------------------------------Question 1--------------------------------------
'''sur les deux ordonnancements donnés dans la question 1  :c'est le premier 
ordonnancement qui est compatible avec notre graphe
car sur le deuximme on a par exemple t3=3 et par rapport a 
notre graphe t3 doit etre realiser avant t4 d'une durée de 4 c'est a dire dans ce cas la 
si t3=3 alors forcément t4 doit etre >= (3+4 =7) hormis ici il est = a 6
et puis on vas regarder l'ordonnancement au niveau du tri ci dessous'''


#------------------------------Question 2--------------------------------------

'''un programme qui calcule l'ordonnancement au plus tot du projet et sa durée
minimale 

dans ce cas on doit faire un tri topologique avec un parcours en profenduer puis
apartir de se tri la on vas parcourir tout les sommet et chercher le chemin le plus long
cette fois qui correspend a la durée minimale de la relisation du projet '''

#on commence par le parcours en profendeur

def dfs(G,s) :
    couleur=dict()
    r=list()
    for v in G :couleur[v]='blanc'
    P=dict()
    P[s]=None
    couleur[s]='gris'
    Q=[s]
    while Q :
        u=Q[-1]
        R=[y for y in G[u] if couleur[y]=='blanc']
        if R :
            v=R[0]
            couleur[v]='gris'
            P[v]=u
            Q.append(v)
        else :
                Q.pop()
                couleur[u]='noir'
                r.append(u)
#                print (couleur)
    return P, r
#puis on fait le tri topologique

def tritopologique(G,s) :
    p=dfs(G,s)[1]   
    return p[::-1]

#on initialise le sommet de depart a S0
sommet_dep='S0'
sommet_fin='Sf'
print('')
r=tritopologique(G,sommet_dep)[::-1]
# pour mon algorithme j'ai utilisé la solution proposer dans le cours slide 37

def dateAuPlusTot(liste_cout,sommet_dep,sommet_fin):
    distance =  {x:0 for x in tritopologique(G,sommet_dep)}
    for i in tritopologique(G,sommet_dep) :
        for j in liste_cout[i]:
            if liste_cout[i][j] + distance[i] > distance[j]:
                distance[j] = liste_cout[i][j] + distance[i] 
    return distance 
print("le tri topologique des taches est :",tritopologique(G,sommet_dep))  
print('\n')      
print ("l'ordonnancement au plus tot des taches est :", dateAuPlusTot(liste_cout,'S0','Sf'))
print('\n')   
print('la durée minimale est de :',dateAuPlusTot(liste_cout,'S0','Sf')['Sf'], 'jours')   
print('\n')   
#----------------------------Question 3--------------------------------------


''' afin de calculer l'ordonnancement au plus tard du projet on doit inverser 
tout les arc c'est a dire le graphe inverse
pour cela j'utilise la matrice associer puis on calcule transposer puis la convertir en liste 
d'adjacence   et aprés on SF=10 et a chaque fois on retranche la valeur des autres sommets'''




'''remarque: sur l'exercice entre le sommet S0 et S1 la dureé est de 0 j'ai pas pu la presenter 
dans la matrice si je met 0 il reconnait pas le lien entre les deux c'est pour cela que jai mis une 
valeur de 0.1 afin de reconnaitre l'arc entre les deux '''


m=[[0, 0.1, 3, 0, 0, 0, 0],
   [0, 0, 2, 2, 0, 0, 0],
   [0, 0, 0, 0, 2, 0, 0],
   [0, 0, 0, 0, 4, 1, 0],
   [0, 0, 0, 0, 0, 0, 2],
   [0, 0, 0, 0, 0, 0, 6],
   [0, 0, 0, 0, 0, 0, 0]]

s=['S0','S1','S2','S3','S4','S5','Sf']
def liste_transpose(matAdjGraphe,sommets):
    d = {}
    N = len(matAdjGraphe)
    matAdjGraphe= [[matAdjGraphe[j][i] for j in range(len(matAdjGraphe))] for i in range(len(matAdjGraphe[0]))]  
    for i in range(N):
        d[sommets[int(i)]] = {}
        for j in range(N):
              if matAdjGraphe[i][j]!=0:
                  d[sommets[int(i)]][sommets[int(j)]]=matAdjGraphe[i][j]
    return d



print('la liste transpose est : ',liste_transpose(m,s))
print('\n')   
def dateAuPlusTard(liste_cout,sommet_dep,sommet_fin):
    distance =  {x:0 for x in r}
    distance2= {x:0 for x in r}
    distance2['Sf']=10
    for i in r :
        for j in liste_cout[i]:
            if liste_cout[i][j] + distance[i] > distance[j]:
                distance[j] = liste_cout[i][j] + distance[i]
                distance2[j]=distance2['Sf']-distance[j]
    return distance2 


print ("l'ordonnancement au plus tard des tachees du projet pour le terminer en 10 jours est :", dateAuPlusTard(liste_transpose(m,s),'S0','Sf'),'ici le 0.90 de S0 correspend a 1')























