import sys

g = {'A':{'B':3,'E':5},'B':{'C':6,'E':1},'C':{'D':2},'D':{'A':3,'C':7},'E':{'B':2,'C':3,'D':6}}

'''
    le graphe g1 est le graphe a gauche de l'exercice
    le graphe g2 est le graphe a droite de l'exercice'''
    
g1= {'A':{'A':2,'B':7,'F':4,'D':3},'B':{'C':2,'F':4},'C':{'E':1,'F':-1},'D':{'F':3,'E':1},'E':{},'F':{'E':0}}

g2= {'A':{'B':3,'C':2},'B':{'D':7,'E':1},'C':{'F':4},'D':{'C':2,'G':2,'E':3},'E':{'H':1},'F':{'G':2},'G':{'C':1,'H':3},'H':{}}


def bellmanFord(G, s):
    distances = {} 
    predecesseurs = {}
    inf=sys.maxsize 
    distances =  {x:inf for x in G.keys()}
    distances[s] = 0
    for i in range(len(G)-1):
        for j in G:
            for k in G[j]: 
                if distances[k] > distances[j] + G[j][k]:
                    distances[k]  = distances[j] + G[j][k]
                    predecesseurs[k] = j
    for i in G:
        for j in G[i]:
            assert distances[j] <= distances[i] + G[i][j]
    return distances, predecesseurs
#Liste d'ajacence du graphe

distances, predecesseurs = bellmanFord(g2,'A')

print("les couts minimum par rapport au sommet de depart 'A' du graphe g2 est  :")

for v in distances: print(str(v) + ' -> ' + str(distances[v]))



''' 

djikstra :
    dans le deuxiemme cas on aurais pu utiliser l'algorithme de djikstra puisque il ne 
contien pas de cout negatif 

sur le premier non tout les couts ne sont pas positifs 
DAG :
    on ne peut pas l'utiliser car les deux contiennent des cycles'''






