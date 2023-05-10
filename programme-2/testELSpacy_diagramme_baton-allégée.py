import os
import json
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn2_circles
import glob


    # spécifiez le chemin vers votre dossier contenant les fichiers
path_corpora = "../DATA/DATA-Fra_spaCy3.3.1_CONCAT/ADAM/*/*/*.json"

    # créez une liste pour stocker les ensembles d'URL communs
liste = []
liste_fichier = []
url_communs = []
liste_loc = []
liste_autre = []
liste_a = []
liste_b = []
    # bouclez à travers tous les fichiers dans le dossier
for nom_fichier in glob.glob(path_corpora):
    i=0
    liste_loc = []
    liste_autre = []

    if "entity-linker" in str(nom_fichier):
        liste_fichier= ['Kraken', 'le texte de référence', 'Tesseract binarisé', 'le texte de référence', 'Tesseract PNG','le texte de référence', 'TesseractFra PNG', 'le texte de référence']
        # ouvrez le fichier et chargez les dictionnaires JSON
        with open(nom_fichier) as f:
            dictionnaires = json.load(f)

            # créez un ensemble pour les URL du fichier courant
            set_url = set()

            # bouclez à travers tous les dictionnaires dans le fichier
            for cle, dico in dictionnaires.items():
                # obtenez l'URL du dictionnaire
                typed = dico.get("type")
            if typed == "LOC":
                #dico_sent_tok[ide]["type"] = True
                liste_loc.append(typed)
            else:
                #dico_sent_tok[ide]["type"] = False
                liste_autre.append(typed)
    a=len(liste_loc)
        # nb de dictionnaire qui contiennent des loc
    b=len(liste_autre)
        #nb de dictionnaire qui ne contiennent pas des loc
    liste_a.append(a)
    liste_b.append(b)
        #stocker("%s_entity-linker.json"%path,dico_sent_tok)
                    

largeur_barre = 0.8


x = range(len(liste_a)) # position en abscisse des barres

    # # Tracé

plt.bar(x, liste_a, width = largeur_barre, color = "#3ED8C9")

plt.bar(x, liste_b, width = largeur_barre, bottom = liste_a, color = "#EDFF91")

plt.xticks(range(len(liste_a)), ['Kraken', 'référence', 'Tesseract binarisé', 'référence', 'Tesseract PNG','référence', 'TesseractFra PNG', 'reference'], rotation=90)
    
plt.show()
    