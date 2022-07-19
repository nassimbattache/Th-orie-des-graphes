import sys 

g=[[0, 40, 70, 30, 0, 0, 0, 0],
   [0, 0, 15, 0, 0, 50, 0, 0],
   [0, 0, 0, 20, 30, 20, 0, 0],
   [0, 0, 0, 0, 24, 0, 40, 0],
   [0, 0, 0, 0, 0, 0, 12, 48],
   [0, 0, 0, 0, 22, 0, 0, 36],
   [0, 0, 0, 0, 18, 0, 0, 60],
   [0, 0, 0, 0, 0, 0, 0, 0]]

#------------------------------Question 1-2--------------------------------------
'''afin de le convaicre le patron je lui montrearit le resultat du flot maximal 
qui n'est pas 138'''

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
print('\n')
print("le flot maximum du graphe est de : " ,Ford_Fulkerson(g, 0, 7))

