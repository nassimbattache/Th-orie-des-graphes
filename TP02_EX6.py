from collections import defaultdict


''' le graphe utiliser est sur le fichier PDF !!'''

r= {1: [8], 2: [4, 7], 3: [5, 6, 11], 4: [], 5: [1, 10], 6: [10], 7: [9], 8: [1, 7], 9: [2], 10: [2, 3], 11: [3, 4]}
#------------------------------Question 1--------------------------------------
'''on calcule le tri topologique de notre graphe '''
'''avec le parcour en profendeur vu dans l'exercice precédent'''        

def tri_topologique2(G):
    visité = set()
    tri = []

    def dfs(v):
        visité.add(v)
        for u in G[v]:
            if u not in visité:
                dfs(u)
        tri.append(v)

    for u in G.keys():
        if u not in visité:
            dfs(u)
    return tri[::-1]
print('\n')
print ('le tri du graphe est :',tri_topologique2(r))
print('\n')

#------------------------------Question 2--------------------------------------
''' on calcule le graphe transposé '''
def transpose(G):
    n = defaultdict(list)
    for u in G:
        for v in G[u]:
            n[v].append(u)
    return n

print('le graphe transposer est :',transpose(r))
print('\n')

#------------------------------Question 3--------------------------------------
'''jai utiliser la méme fonction dfs du tp precedent par contre ici on adapte d'une maniére a 
avoir la liste des composants fortement connexe '''
'''on effectue un parcours en profendeur du graphe transpose on choisisant les
sources s dans l'ordre du tri topologique '''

def fortement_connexe(G, tri):
    visité = set()
    l = defaultdict(list)
    for u in tri:
        if u not in visité:
            visité.add(u)
            s = [u]
            while s:
                item = s.pop()
                for v in G[item]:
                    if v not in visité:
                        visité.add(v)
                        s.append(v)
                l[u].append(item)
    return l

def composants_fortement_connexe(G):
    return fortement_connexe(G, tri_topologique2(transpose(r)))

print ('les composante fortement connexe sont :',composants_fortement_connexe(r))
print('\n')



