import sys
''' le graphe g est le graphe du cours
    le graphe g1 est le graphe a gauche de l'exercice
    le graphe g2 est le graphe a droite de l'exercice'''
    
    
    
g = {'A':{'B':3,'E':5},'B':{'C':6,'E':1},'C':{'D':2},'D':{'A':3,'C':7},'E':{'B':2,'C':3,'D':6}}

g1= {'A':{'B':2,'F':14},'B':{'C':6,'E':4},'C':{'D':2},'D':{'F':3},'E':{'C':1,'D':5},'F':{'C':4}}

g2= {'A':{'B':4,'C':7,'D':10},'B':{'C':2,'D':4,'F':5},'C':{'E':4,'F':10},'D':{'E':1},'E':{'F':3},'F':{'E':1}}


'''pour ma fonction dijkstra je vais avoir comme parametre le graphe et le sommet de 
depart, puis je definie inf comme l'infinie, je crée un dictionnaire vide au debut 
ou je vais inserer apres les predecesseurs des sommets traiter, j'initialise le cout 
de tout les sommets a l'infinie, puis la sommet de depart a 0''' 

def dijkstra(G, s):
 
    inf=sys.maxsize    
    predecesseur = {}
    dejaTraite = {x:False for x in G.keys()}
    distance =  {x:inf for x in G.keys()}
    distance[s] = 0
    print("Initialisation des couts des autres sommets à l'infini :")
    print(distance)
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
        
    return distance, predecesseur

print('')
distance, predecesseur = dijkstra(g,'A')
distance1, predecesseur1 = dijkstra(g1,'A')
distance2, predecesseur2 = dijkstra(g2,'A')

def pluscourtchemin(predecesseur):
    liste=['A']
    for j in range(len(predecesseur)):
        
        for keys ,values in predecesseur.items():    
            if values==liste[-1] :
                liste.append(keys)
            
    return liste
        

print('')
print("les couts minimum par rapport au sommet de depart 'A' du graphe g est  :")
for v in distance: print(str(v) + ' -> ' + str(distance[v]))
print('')
print('Liste des predecesseur ordonner de chaque sommet du graphe g est :')
print( predecesseur)
print('')
print('le plus court chemin du graphe g est :')    
print(pluscourtchemin(predecesseur))

print('')
print("les couts minimum par rapport au sommet de depart 'A' du graphe g1 est  :")
for v in distance1: print(str(v) + ' -> ' + str(distance1[v]))
print('')
print('Liste des predecesseur ordonner de chaque sommet du graphe g1 est :')
print( predecesseur1)
print('')

print('le plus court chemin du graphe g1 est :')    
print(pluscourtchemin(predecesseur1))

print('')
print("les couts minimum par rapport au sommet de depart 'A' du graphe g2 est  :")
for v in distance2: print(str(v) + ' -> ' + str(distance2[v]))
print('')
print('Liste des predecesseur ordonner de chaque sommet du graphe g2 est :')
print( predecesseur2)

print('le plus court chemin du graphe g1 est :')    
print(pluscourtchemin(predecesseur2))











