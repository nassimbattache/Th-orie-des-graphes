import networkx as nx

'''on vas prendre l'exemple donner au TP '''
G=[(1,3),(1,4),(2,1),(3,2)]


'''la liste d'adjacence equivalente'''
N={1:[2,3,4],2:[1,3],3:[1,2],4:[1]}


#------------------------------Question 1--------------------------------------
'''ceci est pour l'affichage du graphe, donner dans le TP'''

D=nx.Graph()
D.add_edges_from(G)
nx.draw(D)

#------------------------------Question 2--------------------------------------
'''la fonction suivante prend comme entrée une liste d'adjacence puis nous donne 
en sortie ca matrice d'adjacence conrespendente'''

def mat_adjacence(listeAdjGraphe):
	M = []
	sommets = listeAdjGraphe.keys()
	for i in sommets:
		ligne = [int(j in listeAdjGraphe[i]) for j in sommets]
		M.append(ligne)
	return M

def affiche(matrice):
    for ligne in matrice:
       print(ligne)
    return ligne

#-------------------------------Question 3-------------------------------------
'''cette fonction reciproque qui nous permet d'avoir la liste d'adjacence apartir
d'une matrice'''


def liste_adjacence(matAdjGraphe):
	d = {}
	N = len(matAdjGraphe)
	for i in range(N):
		d[int(i+1)] = []
		for j in range(N):
			if matAdjGraphe[i][j]==1:
				d[int(i+1)].append(int(j+1))
	return d

#------------------------------Question 4--------------------------------------
'''verifier la reciprocité '''
p = mat_adjacence(N)
print(affiche(p))
print("")
print(liste_adjacence(mat_adjacence(N)))











