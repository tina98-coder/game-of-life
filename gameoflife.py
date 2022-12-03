# BELKESSA Thinhinane

#------------------------------------------------------------------------------
#                               Extrait ensemble des voyelles


def extrait_ensemble_des_voyelles(mot): 
    mot_min = mot.lower()
    list_voyelles = ["a","e","i" , "o" , "u", "y"]
    voyelles=set()
    for i in mot_min:
        if(i in list_voyelles):
            if(i not in voyelles):
                voyelles.add(i)
            
    return voyelles
#------------------------------------------------------------------------------
#                               Transforme en numéros


def transforme_en_numeros(mot):
    mot_min = mot.lower()
    dict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,
          "g":7,"h":8,"i":9,"j":10,"k":11,"l":12,
          "m":13,"n":14,"o":15,"p":16,"q":17,"r":18,
          "s":19,"t":20,
          "u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    L=[]
    for i in mot_min:
        for ( key, value ) in dict.items() :
            if(i == key ):
                L.append(value)
    s = ".".join(str(e) for e in L)
    
    return s

#------------------------------------------------------------------------------
#                               JEU DE LA VIE


def contenu_cellule(colonne, ligne, univers):
    return (univers[ligne][colonne])


def est_vivante(colonne, ligne, univers):
    for i in range(len(univers)):
        if(ligne == i ):
           if( univers[ligne][colonne] == "*"):
               return True
           else: 
                return False


def largeur(univers):
    return len(univers)


def nombre_cases_vivantes_voisines(colonne, ligne, univers):
    voisins = 0
    for i in (colonne-1, colonne, colonne+1):
        for j in (ligne-1, ligne, ligne+1):
            if 0 <= i < len(univers) and 0 <= j < len(univers):
                if contenu_cellule(i, j, univers) == "*":
                    voisins += 1
    return voisins


def prochain_univers(univers):
    univers2 = univers
    for i in range(len(univers)):
        for j in range(len(univers)):
            if((not est_vivante(j,i,univers))
               and (nombre_cases_vivantes_voisines(j, i, univers)==3)):
                line=list(univers[i])
                line[j]="*"
                univers[i]="".join(line)
                
            elif (est_vivante(j,i,univers)
                  and 2>nombre_cases_vivantes_voisines(j, i, univers)>3):
                line=list(univers[i])
                line[j]="_"
                univers[i]="".join(line)
    return univers

def iter_univers(univers):
    yield univers
    while True:
        univers2 = prochain_univers(univers)
        yield  univers2 

#------------------------------------------------------------------------------
#                               TESTS : ne rien modifier dans ce qui suit
#------------------------------------------------------------------------------
if extrait_ensemble_des_voyelles("Toto le heros") != {"o", "e"}:
    print("Erreur de extrait_ensemble_des_voyelles('Toto le heros')")

if extrait_ensemble_des_voyelles("bcdE") != set():
    print("Erreur de extrait_ensemble_des_voyelles('bcd')")

if transforme_en_numeros("abz") != "1.2.26":
    print("Erreur de transforme_en_numeros('abz')")

if transforme_en_numeros("c") != "3":
    print("Erreur de transforme_en_numeros('c')")

def affiche_univers(univers):
    for ligne in univers:
        print(ligne)

univers_1 = [
    "____",
    "_**_",
    "_**_",
    "____"]

univers_2 = [
    "______",
    "______",
    "___*__",
    "_*_*__",
    "__**__",
    "______"]

if largeur(univers_1) != 4:
    print("Erreur de largeur(univers_1)")
if largeur(univers_2) != 6:
    print("Erreur de largeur(univers_2)")
if contenu_cellule(1, 1, univers_1) != "*":
    print("Erreur de contenu_cellule(1, 1, univers_1)")
if contenu_cellule(3, 3, univers_1) != "_":
    print("Erreur de contenu_cellule(3, 3, univers_1)")
if contenu_cellule(3, 1, univers_1) != "_":
    print("Erreur de contenu_cellule(3, 1, univers_1)")

if nombre_cases_vivantes_voisines(4, 0, univers_2) != 0:
    print("Erreur nombre_cases_vivantes_voisines(4, 0, univers_2)")

if nombre_cases_vivantes_voisines(2, 3, univers_2) != 5:
    print("Erreur nombre_cases_vivantes_voisines(2, 3, univers_2))")

univ_2 = univers_1
for _ in range(8):
    univ_2 = prochain_univers(univ_2)
if univ_2 != univers_1:
    print("Erreur prochain_univers")

it = iter_univers(univers_2)

liste_etats = []
for _ in range(7):
    univ_2 = next(it)
    liste_etats.append(univ_2)

for univ_2 in liste_etats:
    affiche_univers(univ_2)
    print("")
