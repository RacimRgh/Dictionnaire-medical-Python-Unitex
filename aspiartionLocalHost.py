import urllib.request, re, sys, os
from http import server, HTTPStatus
from string import ascii_uppercase
#ouverture des fichiers
info = open('info.txt', 'w+', encoding='utf-8')
dct = open('subst.dic', 'w+', encoding='utf-16')
arg1 = sys.argv[1].upper()       #intervalle
port = sys.argv[2]          #port



#commencer l'aspiration
nbtotal=0
if re.match(r'[A-Z]-[A-Z]', arg1):
    for c in ascii_uppercase:
        if c>=arg1[0] and c<=arg1[2]:
            url = urllib.request.urlopen('http://localhost:'+port+'/vidal-Sommaires-Substances-'+c+'.htm')
            res = url.read().decode('utf-8')
            fin = re.findall(r'href="Substance/.*-.*.htm">(\w*)', res)
            inf = ",.N+subst\n".join(fin)
            for line in inf:
                dct.write(line)
            info.write("Nombre d'entrées dans "+c+": "+str(len(fin))+"\n")
            nbtotal+=len(fin)
    info.write("Nb total d'entrées: "+str(nbtotal))
else:
    print("L'intervalle donné n'est pas valable.")
