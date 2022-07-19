''' on prend un graphe acyclique suivant '''

M= {1:[2,3,7],
    2:[3,4],
    3:[4,5,7],
    4:[5],
    5:[8],
    6:[],
    7:[6],
    8:[6]}

# logique :
'''     on commence par faire le parcours en profndeur puis on prend les dates 
    de changement des couleurs des sommets en noir qui veut dire dans un graphe 
    acyclique connexe (connexe :car toutes les taches sont relier comme dans le cas d'un arbre,
                       car certainement il existe au moin une tache par laquel on poura accéder
                       aux autre tache pour finaliser toutes les taches)
    que le premier sommet qui sera en noir sera la tache finale en d'autre therme le passage 
    a une autre tache a partir de ce sommet est impossible. c'est pour cela la liste
    de passaage de touts les sommet en noir serait inverser en therme de classement.
    c'est pour cette raison que dans mon programe a la fin je vais inverser la liste r
    obtenu dans le parcours en profenduer afin de classé les taches de la premiére
    a la dernniére en therme de priorité'''

# premire methode



'''le parcour en profendeur '''        


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
'''vous pouvez decoder la ligne 48 pour visualiser le passage des couleurs en noir'''

''' le tri topologique '''
def tritopologique(G,s) :
    p=dfs(G,s)[1]   
    return p[::-1]

s=1

print('le parcour en profendeur du graphe et la liste de passage des sommet en noir apartir du sommet '+str(s)+' est : ')
print (dfs(M,s))
print('')
print ('le tri topologique des sommets basé sur les dates de passage en noir est : ')
print(tritopologique(M,1))

''' et aussi avec cette deuxieme methode qui nous permet de nous renvoyer le tri topo'''

# deuxieme methode

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

print('avec la deuxieme methode', tri_topologique2(M))


'''remarque!! : si a partir d'un sommet on fait un dfs  et que en resultat on
remarque que quelque somments n'aparaissent pas cela veut dire qu'ils sont 
independant en therme de priorité '''