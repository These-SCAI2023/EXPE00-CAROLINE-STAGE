import json
import spacy  # version 3.5
import glob 

# initialize language model
nlp = spacy.load("fr_core_news_lg")

# add pipeline (declared through entry_points in setup.py)
nlp.add_pipe("entityLinker", last=True)

def run (texte):
    doc = nlp(texte)
    ents = [(e.text, e.label_, e.kb_id_) for e in doc.ents]
    ents.sort()
    return ents

# Chemin du répertoire contenant les fichiers JSON à traiter
path_corpora ="C:/Users/dorle/Documents/GitHub/EXPE00-CAROLINE-STAGE/DATA/DATA-Fra_spaCy3.3.1_CONCAT/ADAM"

# Expression régulière pour sélectionner uniquement les fichiers JSON
expression_reguliere = "*.json"

# Liste des fichiers correspondant à l'expression régulière dans le répertoire
liste_fichiers = glob.glob(path_corpora + expression_reguliere)

# Parcours de chaque fichier de la liste et application de la fonction run()
for fichier in liste_fichiers:
    with open(fichier, "r") as f:
        # Chargement du contenu JSON
        contenu = json.load(f)
        
        # Application de la fonction run()
        resultats = run(contenu)
        
        # Affichage des résultats ou sauvegarde dans un fichier, etc.
        print(resultats)