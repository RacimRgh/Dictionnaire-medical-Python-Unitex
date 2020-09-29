#lancer le site en local avec python webserver
from http import server, HTTPStatus
import sys

handler = server.SimpleHTTPRequestHandler
adresse = '127.0.0.1'
arg2 = int(sys.argv[1])      #port
serveur = server.HTTPServer((adresse,arg2), handler)
serveur.serve_forever()