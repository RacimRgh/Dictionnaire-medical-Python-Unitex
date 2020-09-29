#       RIGHI Racim
#       BOURENANE Rania
#       L3 ACAD A

import re, sys, urllib.request
from string import ascii_uppercase
#opening files
corpus = open(sys.argv[1], 'r')
dct = open('subst.dic', 'a+', encoding='utf-16')
dctenri = open('subst_enri.dic', 'w+', encoding='utf-16')

cpt=0     #nb des substances trouvés dans corpus-medical.txt
listCorpus = corpus.readlines()
for line in listCorpus:
    sreg = re.search(r'''
    ^[-*]?\s?  # Debut avec "* " ou "- "
    (\w+)       #La substance recherchée 
    \s:?\s?     #subts :  (GAVISCON : 1 sachet par jour.)
    (\d+|,|\d+.\d)+     # "2" ou "," ou "1.1" ... etc
    \s(mg|ml|µg|mcg|g|cp|amp|flacon).+   #unité de mesure
    ''', line, re.VERBOSE | re.I)     
    if sreg:        # si une substance est trouvée 
        if sreg.group(1).lower() != 'intraveineuse' and sreg.group(1).lower() != 'eau' and sreg.group(1).lower() != 'puis': #enlever les mots pris par erreur dans la regex
            dctenri.write(sreg.group(1).lower()+',.N+subst\n')
            dct.write(sreg.group(1).lower()+',.N+subst\n')      # ecrire la substance dans les 2 dictionnaires
            cpt+=1
            print(str(cpt)+" : "+sreg.group(1))        #affichage des substances avec un compteur
# Tri et suppression des doublons dans subst.dic
dct = open('subst.dic', 'r+', encoding='utf-16')
tri = sorted(list(set(dct.readlines())))
dct = open('subst.dic', 'w+', encoding='utf-16')
for el in tri:
    dct.write(el)           #reecrire les elements triés
# Remplissage du fichier info2.txt
info2 = open('info2.txt', 'w+', encoding='utf-8')
dctenri = open('subst_enri.dic', 'r+', encoding='utf-16')
listDctEnri = dctenri.readlines()
for letter in ascii_uppercase:       #compter le nombre de substances par lettre de l'alphabet
    nbLettre=0
    for el in list(set(listDctEnri)):
        if letter == el[0].upper():
            nbLettre+=1
    info2.write('Nombre d\'entrées dans '+letter+': '+str(nbLettre)+'\n')
info2.write('Nombre d\'entrées total: '+str(len(list(set(listDctEnri)))))