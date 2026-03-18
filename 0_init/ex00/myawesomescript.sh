#!/bin/sh


# EXPLICATION DE LA COMMANDE :
# 1. curl -s -I "$1" 
#    - L'option "-I" (ou --head) demande à curl de ne récupérer QUE les en-têtes HTTP (headers), sans télécharger tout le corps de la page web.
#    - L'option "-s" (silent) empêche curl d'afficher sa barre de progression de téléchargement.
#
# 2. grep -i "^Location"
#    - On cherche la ligne qui contient l'adresse de redirection.
#    - "^Location" cherche précisément la ligne qui commence (^) par "Location".
#    - "-i" permet d'ignorer la casse (majuscule/minuscule) au cas où le serveur renvoie "location:".
#
# 3. cut -d ' ' -f 2
#    - La ligne récupérée ressemble à "Location: http://42.fr/".
#    - On l'envoie à cut pour la découper.
#    - "-d ' '" définit le délimiteur comme étant un espace (le caractère qui va séparer nos colonnes).
#    - "-f 2" (field 2) permet de garder uniquement la deuxième colonne, c'est-à-dire l'URL qui se trouve juste après 
curl -s -I "$1" | grep -i "Location" | cut -d ' ' -f 2
