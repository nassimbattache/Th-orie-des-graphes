'''nos graphe representer en disctionnaire '''
gra1 = {  1:[2,7],
          2:[3,5,6],
          3:[4,5],
          4:[],
          5:[4,8],
          6:[1,8],
          7:[6],
          8:[]}
gra2 = {  1:[2,7],
          2:[3,5,7],
          3:[4,6,2],
          4:[3],
          5:[3,5,8],
          6:[3,5,9],
          7:[1,2,8],
          8:[7,5,9],
          9:[6,8]}

d={1: [], 2: [1, 6], 3: [1, 2, 6], 4: [1, 2, 3], 5: [2, 3, 4, 6], 6: [1]}
#------------------------------Question 1-2--------------------------------------

'''le parcour en profendeur '''        


def dfs(G,s) :
    couleur=dict()
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
               
    return P

''' le parcour en profendeur et le passage des couleurs'''

def dfsdetaille(G,s) :
    couleur=dict()
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
            print(couleur)
            print(Q)
        else :
                Q.pop()
                couleur[u]='noir'
                print(couleur)
                print(Q)
    return P




#------------------------------Question 3-4--------------------------------------
''' le parcour en largeur '''
def Bfs(G,s) :
    couleur=dict()
    for v in G :couleur[v]='blanc'
    P=dict()
    P[s]=None
    couleur[s]='gris'
    f=[s]
    
    while f :
        u=f[0]
        for y in G[u] :
            if couleur[y]=='blanc' :
                couleur[y]='gris'
                f.append(y)
                P[y]=u
           
        f.remove(u)
        couleur[u]='noir'
        
        
    return P
'''le parcours en largeur et les detailles de passage des couleurs '''

def Bfsdetaille(G,s) :
    couleur=dict()
    for v in G :couleur[v]='blanc'
    P=dict()
    P[s]=None
    couleur[s]='gris'
    f=[s]
    print(f)
    
    while f :
        u=f[0]
        for y in G[u] :
            if couleur[y]=='blanc' :
                couleur[y]='gris'
                f.append(y)
                P[y]=u
        print(couleur)
        print(f)      
        f.remove(u)
        couleur[u]='noir'
        print(f)
        
    return P
#------------------------------Question 5--------------------------------------
 
''' la distance parcouru du sommet s au sommet sf dans le graphe G avec le parcour en largeur '''
def distanceBfs(G,s,sf):
    n=Bfs(G,s)
    distance =1
    while (n[sf]!=s): 
        distance +=1
        sf=n[sf]
    return distance
''' la distance parcouru du sommet s au sommet sf dans le graphe G avec le parcour en profondeur'''

def distancedfs(G,s,sf):
    n=dfs(G,s)
    distance =1
    if n[sf]!=s: 
        distance +=1
        sf=n[sf]
    return distance

#------------------------------Question 5--------------------------------------    
''' le predecesseur du sommet sf dans le parcour en largeur qui a comme debut le sommet s'''
def predecesseurbfs(G,s,sf) :
    n=Bfs(G,s)
    return n[sf]

'''le predecesseur du sommet sf dans le parcour en profendeur qui a comme debut le sommet s'''

def predecesseurdfs(G,s,sf) :
    n=dfs(G,s)
    return n[sf]

i=int(input('entrez le sommet de debut pour le parcour en largeur et en profondeur :'))

print('le parcour en profendeur a partir du sommet '+str(i)+' est :' )
print(dfs(gra1,i))
print('')
print('le parcour en largeur a partir du sommet '+str(i)+' est :' )
print(Bfs(gra1,i))
print('')
j=int(input('entrez le sommet dont vous voulez savoir sa distance par rapport au sommet de debut, son predeceseur et le detaille de changement des couleurs :'))
print('la distance entre le sommet '+str(i)+' et le sommet '+str(j)+' dans le parcour en largeur est : ',distanceBfs(gra1, i, j))
print('la distance entre le sommet '+str(i)+' et le sommet '+str(j)+' dans le parcour en profendeur est : ',distancedfs(gra1, i, j))
print('le predecesseur de ce sommet dans le parcour en largeur est le sommet :',predecesseurbfs(gra1,i,j))
print('le predecesseur de ce sommet dans le parcour en profendeur est le sommet :' ,predecesseurdfs(gra1,i,j))



print('voici les detailles de changement des couleurs des sommets dans le parcours en largeur puis le parcour en profendeur a partir du sommet initial :')
print('')
print(Bfsdetaille(gra1,i))
print('')
print('')
print(dfsdetaille(gra1,i))














