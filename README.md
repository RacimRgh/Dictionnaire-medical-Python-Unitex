# Projet-Unitex-L3
##Traitement des langages avec Python, Unitex et Gramlab

Projet réalisé au 1er semestre de la 3ème année informatique générale (ACAD) à l'Université des Sciences et de la Technologie Houari Boumediene, pour le module "Unitex/Gramlab et Python".

## Objectif

Le but final est de créer un dictionnaire de données médicales en utilisant différents outils de traitement des langages (Python, Unitex, Gramlab)

##
- En utilisant le Web scraping avec la bibliothèque beautifulsoup de Python, récupérer les noms de médicaments triés par substance active de A à Z encodé en UTF-16 LE avec BOM, et ce depuis le site vidal.fr
- Donner à l'utilisateur la possiblité de déterminer l'intervalle des pages à traiter par ordre alphabétique
- Analyser le fichier de sortie contenant les noms des médicaments, puis calculer le nombre d'entités médicales par substance active et pour chaque lettre de l'alphabet.
- Enrichir le fichier de sortie contenant les noms de médicaments, en analysant un fichier "corpus-medical.txt" pour ajouter de nouveaux médicaments par nom commercial ou par substance active, en prenant en compte les doublons et tri.
- Construire un graphe d'extraction sous Unitex afin d’extraire les occurrences de "posologies de traitement" (une posologie de traitement contient le nom du médicament, la dose et le rythme (ou fréquence).
- Le fichier étant très large, les posologies doivent être extraites en utilisant des expressions régulières et le dictionnaire système "delaf.bin" fourni par Unitex afin de pouvoir exploiter les masques lexicaux.

## Outils et bibliothèques
- **Python**: beautifulsoup, urllib, regex, http, os
- **Unitex**
