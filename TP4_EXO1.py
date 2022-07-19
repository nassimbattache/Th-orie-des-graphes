import networkx as nx
import matplotlib.pyplot as plt
import sys

INF = float('inf')
'''pour des raison d'affichage je n'ai pas utiliser la valeur infinie puisque a chaque fois que je l'utilise 
jai le sommet c qui superpose le sommet d pour cette raison jai mis 99 afin de bien visulaiser 
tout les sommet sur notre plots '''
G=nx.Graph()
A=[[0, 3, 5, 11, 9],
    [3, 0, 3, 9, 8],
    [5, 3, 0, 99,10],
    [11, 9, 99, 0, 7],
    [9, 8, 10, 7, 0]]


sommets=[i for i in range(len(A))]

#------------------------------Question 1--------------------------------------

for i in range(len(A)):

    # definition desommets noeuds
    G.add_node(i,label=sommets[i])
    for j in range(i,len(A)):
        # definition des aretes
        G.add_edge(i,j,weight=A[i][j])

labels={node:label for node,label in G.nodes(data='label')}
labels
labels_edges = {}
labels_edges = {edge:G.edges[edge]['weight'] for edge in G.edges}
labels_edges
pos = nx.spring_layout(G)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700,node_color='pink' ,alpha=0.9)             
# labels
nx.draw_networkx_labels(G, pos, labels=labels)
# edges
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_edges, font_color='red')
plt.axis('off')
plt.show()

#------------------------------Question 2--------------------------------------
'''voici l'algorithme de kruskal dans ma fonction jai pris comme parametre uniquement
la matrice d'adjacence ou les couts sont les valeurs de ma matrice '''

'''cette fonction suivante permet de  remonter jusqu'a trouver la racine de l'arbre
qui quontient le sommet i ''' 
def trouver(i):
    while sommets[i] != i:
        i = sommets[i]
    return i
'''cette fonction permet de relier les deux racine des deux sommet i et j afin 
de ne pas le compter une autre fois a nouveau '''
def union(i, j):
    a = trouver(i)# racine de l'arbre qui contient le sommet i
    b = trouver(j)# racine de l'arbre qui contient le sommet j
    sommets[a] = b# uninon des deux racine 
 
def kruskal(A):
    cout_min = 0 
    for i in range(len(A)):
        sommets[i] = i
    count = 1
    while count < len(A) :
        min = sys.maxsize
        a = -1# on initialise a -1 car 0 par exemple represente un sommet dans notre cas 
        b = -1
        for i in range(len(A)):
            for j in range(len(A)):
                if trouver(i) != trouver(j) and A[i][j] < min:
                    min = A[i][j]
                    a = i
                    b = j
        union(a, b)
        print("l'arête ({}, {}) est coupé --> {}".format( a,b, min))
        count += 1
        cout_min += min
 
    print("le cout minimum calculé de l'arbre couvrant est : ",cout_min)
    print("le nombre d'itérations est : ",count-1)

print('\n') 
print('Algorithme de kruskal :')
kruskal(A)

#------------------------------Question 3--------------------------------------
'''pour ma fonction de prim pour chaque sommet ajoutée a la fin ou celui initailaiser a true 
cahque arete contenant ce sommet est comparer avec les autres aretes et puis les mettre 
a jour dans le cas ou le cout de i a j est inferieur a la valeurs min '''


gra2=[[0, 1, 0, 20, 0, 0],
      [1, 0, 16, 4, 20, 11],
      [0, 16, 0, 0, 0, 17],
      [20, 4, 0, 0, 4, 0],
      [0, 20, 0, 4, 0, 13],
      [0, 11, 17, 0, 13, 0]]
sommets=[i for i in range(len(gra2))]

def prim(G):
    N=len(G)
    count = 0
    sommets = [0 for i in range(N)]
    cout_min = 0 
    while (count < N - 1):
        sommets[0] = True
        min = sys.maxsize
        a = 0
        b = 0
        for i in range(N):
            if sommets[i]:
                for j in range(N):
                    if ((not sommets[j]) and G[i][j]):  
                        if min > G[i][j]:
                            min = G[i][j]
                            a = i
                            b = j
        print("l'arête ({}, {}) est coupé --> {}".format( a,b, min))
        sommets[b] = True
        count += 1
        cout_min += min
    
    print("le cout minimum calculé de l'arbre couvrant est : ",cout_min)
    print("le nombre d'itérations est : ",count)

        


print('\n') 
print('Algorithme de prim sur le graphe 1 :')
prim(A)
print('\n') 
print('Algorithme de prim sur le graphe 2 :')
prim(gra2)
#------------------------------Question 4--------------------------------------


'''oui on peut adapter les deux programes precedents d'une facon a avoir le
un arbre couvrant de cout maximal'''

def kruskal_maximal(A):
    cout_min = 0 
    for i in range(len(A)):
        sommets[i] = i
    count = 1
    while count < len(A) :
        min = 0# on initialise le min cette fois a 0 pas a linfinie 
        a = -1
        b = -1
        for i in range(len(A)):
            for j in range(len(A)):
                if trouver(i) != trouver(j) and A[i][j] > min:# on inverse aussi au lieu d'avoir inferieur on met superieur 
                    min = A[i][j]
                    a = i
                    b = j
        union(a, b)
        print("l'arête ({}, {}) est coupé --> {}".format( a,b, min))
        count += 1
        cout_min += min
 
    print("le cout maximal calculé de l'arbre couvrant est : ",cout_min)
    print("le nombre d'itérations est : ",count-1)

def prim_maximal(G):
    N=len(G)
    count = 0
    sommets = [0 for i in range(N)]
    cout_min = 0 
    while (count < N - 1):
        sommets[0] = True
        min = 0
        a = 0
        b = 0
        for i in range(N):
            if sommets[i]:
                for j in range(N):
                    if ((not sommets[j]) and G[i][j]):  
                        if min < G[i][j]: #de la meme facon on inverse le 
                            min = G[i][j]
                            a = i
                            b = j
        print("l'arête ({}, {}) est coupé --> {}".format( a,b, min))
        sommets[b] = True
        count += 1
        cout_min += min
    
    print("le cout maximal calculé de l'arbre couvrant est : ",cout_min)
    print("le nombre d'itérations est : ",count)



print('\n')
print("calcule de l'arbre couvrant maximal :")
print('\n')
print("ALgorithme de kruskal")
kruskal_maximal(gra2)
print('\n')
print("ALgorithme de prim")
prim_maximal(gra2)

















