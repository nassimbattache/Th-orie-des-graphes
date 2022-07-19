import sys
''' pour resoudre le probleme de flux maximale 
on commance par un flux maximale qui est egale a 0 tant que il ya une augmentation dans 
de la source a l'arriver on ajoute cette augmentation au flow 
puis a la fin retourner le flux maximale'''

''' pour cela on aurra besoin de faire le parcours en largeur afin d'acceder aux sommets 
qu'on vas adapter par la suite pour que la fonction nous return soit true si le sommets n'est pas encore visité 
ou false si le sommet en question a deja était visité '''
g1_cours = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]


g=[[0, 2, 4, 9, 0, 0, 0, 0],
   [0, 0, 2, 0, 3, 0, 0, 0],
   [0, 1, 0, 0, 2, 0, 6, 0],
   [0, 0, 0, 0, 0, 8, 1, 0],
   [0, 0, 0, 1, 0, 0, 0, 8],
   [0, 0, 1, 0, 2, 0, 0, 4],
   [0, 0, 0, 0, 0, 1, 0, 6],
   [0, 0, 0, 0, 0, 0, 0, 0]]
 
def BFS(G, s, t, p):
    visited = [False for i in range( len(G))]
    q = []
    q.append(s)
    visited[s] = True
    while q:
        u = q.pop(0)
        for i in range(len(G[u])):
            if visited[i] is False and G[u][i] > 0:
                q.append(i)
                visited[i] = True
                p[i] = u
 
    return True if visited[t] else False
'''jai pris comme parametre le graphe représenter en matrice d'adjacence et les sommets 
de depart et d'arrivé ''' 
 
def Ford_Fulkerson(G, depart,sf):
    p = [-1] * (len(G))
    flot_max = 0
    while BFS(G, depart,sf, p):
        path_flow = sys.maxsize
        s =sf
 
        while s != depart:
            path_flow = min(path_flow, G[p[s]][s])
            s = p[s]
        flot_max += path_flow
        v =sf
        while v != depart:
            u = p[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = p[v]
    return flot_max
 
 

depart = 0
arrive = 5
print('\n')
print("le flot maximum du graphe du cours est de : " ,Ford_Fulkerson(g1_cours, depart, arrive))

print("le flot maximum du graphe de l'exercice 2 est de : " ,Ford_Fulkerson(g, 0, 7))





