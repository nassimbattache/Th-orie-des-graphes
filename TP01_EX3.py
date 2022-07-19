

'''on reprend la meme matrice p de l'exercice 2 pour verifier le fonctionemment du 
programme'''
p=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

#------------------------------Question 1--------------------------------------
def nonoriente(M):
    n=len(M)
    for i in range(n):
        for j in range(n):
            if( M[i][j]==M[j][i]) :
                return print("le graphe est non orienté.")
            else:
                return print("le graphe est orienté.")         



#------------------------------Question 2-DISTANCE------------------------------
''' pour cette partie j'ai utiliser la fonction qui permet de convertire la matrice 
en liste d'adjacence vu en exo 2 et puis vu ma boucle marche avec une liste mais
 le parametre d'entrer est une matrice, alors jai bien utiliser la matrice en entrée et 
puis je lai convertie en liste afin d'executer la boucle '''
def liste_adjacence(matAdjGraphe):
	d = {}
	n = len(matAdjGraphe)
	for i in range(n):
		d[int(i+1)] = []
		for j in range(n):
			if matAdjGraphe[i][j]==1:
				d[int(i+1)].append(int(j+1))
	return d

'''retourne le plus petit chemain entre i et j '''                                   
                                        
def petit_chemain(M,i,j,dist=[]):   
    dist = dist + [i]
    if i==j:
        return dist
    if i not in M:
        return None
    shortest = None
    for node in M[i]:
        if node not in dist:
            newdist = petit_chemain(M, node,j,dist)
            if newdist:
                if not shortest or len(newdist) < len(shortest):
                    shortest = newdist
    return shortest

'''on obtien la distance entre i est j par cette fonction '''

def distance(N,i,j):
    M=liste_adjacence(N)
    return len(petit_chemain(M,i,j,[]))-1


#------------------------------Question 2-Diamétre------------------------------
''' étant donner que le diamétre est la distance maximal entre les sommet et qui
est le méme que l'ecartement maximal des sommet alors dans ce cas en cherche 
le max de la  distance '''


def diametre(M) :
    v=[]
    for i in range(1,len(M)+1):
        for j in range(1,len(M)+1):
           v.append(distance(M,i,j))
    return max(v)


nonoriente(p)



i =int(input('chisisez le sommet de départ: '))
j =int(input('chisisez le sommet d arrivé: '))

print( "la distance entre le sommet "+str(i) +" et "+str(j) +" est : ",distance(p,i,j))
print("le diamétre du graphe est :",diametre(p) )

print("bonus")
print("le chemain le plus petit pour aller entre "+str(i) +" et "+str(j) +" est : ",petit_chemain(liste_adjacence(p), i, j))





















