from random import randint
import colorama
import time



def remplissage(n,jeu):
    while n>0:
        i,j=randint(0,len(jeu)-1),randint(0,len(jeu[0])-1)
        if jeu[i][j] == 0:
            n-=1
            jeu[i][j] = 1
            
def nombre_de_vivants(i,j,jeu):
    nb=0
    voisin= [(i-1,j),(i,j-1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j),(i,j+1),(i+1,j+1)]
    for e in voisin:
        if 0 <= e[0] < len(jeu) and 0 <= e[1] < len(jeu[0]):
            nb += jeu[e[0]][e[1]]
    return nb

def transfo_cellule(i,j,jeu):
    nb = nombre_de_vivants(i,j,jeu)
    if jeu[i][j] == 1 and nb != 2 and nb != 3:
        return 0
    if jeu[i][j] == 0 and nb == 3 :
        return 1
    return jeu[i][j]

def affichage(tab):
    res = ""
    for i in range(len(tab)):
        res += "\n"
        for j in range(len(tab)):
            if tab[i][j] == 1 :
                res += colorama.Back.RED + f"  " + colorama.Style.RESET_ALL
            else :
                res += colorama.Back.WHITE + f"  " + colorama.Style.RESET_ALL
    return print(res)
            
                
def jeu(nb_vivant,taille_tab):
    jeu = [[0]*taille_tab for i in range(taille_tab)]
    remplissage(nb_vivant,jeu)
    
    while True :
        affichage(jeu)
        tmp = [[0]*taille_tab for i in range(taille_tab)]
        for i in range(taille_tab):
            for j in range(taille_tab):
                tmp[i][j] = transfo_cellule(i,j,jeu)
        jeu = tmp
                
        
        time.sleep(0.1)
    
                
                

                