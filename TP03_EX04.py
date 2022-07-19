import sys


'''pour recuperer le trésor au plus vite possible le preince n'est pas obliger 
de passer par tout les chemains il suffit de chercher le plus court chemin entre 
le depart et le trésor'''


''' pour cela je vais utiliser un programme qui va me calculer le plus courts chemein
entre le depart et le trésor'''




''' modelisation du probleme en un graphe '''
recherche_tresor = {'départ':{'ville du marche':4,'foret':1},'ville du marche':{'col du nord':5,'capital provinciale':3},
                    'foret':{'ville du marche':2,'capital provinciale':7},'capital provinciale':{'refuge devin':4,'palais':10},
                    'col du nord':{'refuge devin':3},'refuge devin':{'palais':5,'épée':20,'dragon':32},'palais':{'bibliothéque':6},
                    'bibliothéque':{'épée':7,'trésor':30},'épée':{'dragon':8,'trésor':18},'dragon':{'trésor':9},'trésor':{}}



'''on est dans le cas ou le graphe n'a ni de cycle absorbant ni de cout des arcs negatif dans ce cas 
on peut utiliser l'algorithle de djikstra et l'adapter pour ne renvoyer le plus court chemin
entre s et sf et la liste des predecesseurs '''


def plus_petit_chemin(G, s, sf):
 
    inf=sys.maxsize    
    predecesseur = {}
    dejaTraite = {x:False for x in G.keys()}
    distance =  {x:inf for x in G.keys()}
    distance[s] = 0
    a_traiter = [(0, s)]
    while a_traiter:
        di_sommet, sommet = a_traiter.pop()
        if not dejaTraite[sommet]:
            dejaTraite[sommet] = True
            for voisin in G[sommet].keys():
                dist_voisin = di_sommet + G[sommet][voisin]
                if dist_voisin < distance[voisin]:
                    distance[voisin] = dist_voisin
                    predecesseur[voisin] = sommet
                    a_traiter.append((dist_voisin, voisin))
        a_traiter.sort(reverse=True)
        
    return predecesseur , distance[sf]

le_chemin , la_durée = plus_petit_chemin(recherche_tresor, 'départ','trésor')

def pluscourtchemin(predecesseur):
    liste=['départ']
    for j in range(len(predecesseur)):
        
        for keys ,values in predecesseur.items():    
            if values==liste[-1] :
                liste.append(keys)
            
    return liste

print("\n")
print("le plus petit chemin est :  ", pluscourtchemin(le_chemin))
print('')
print ('ca durée est de : '+str(la_durée)+' jours')



