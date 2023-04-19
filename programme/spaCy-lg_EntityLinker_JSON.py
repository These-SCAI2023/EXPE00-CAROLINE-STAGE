# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:31:17 2023

@author: dorle
"""

import json
import spacy  # version 3.5
import glob
import pandas as pd

def lire_fichier(chemin):
    with open (chemin, "r", encoding="utf-8") as fichier:
        texte=fichier.read()
        
        
        return texte
def stocker(chemin, contenu):
    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()

nlp = spacy.load("fr_core_news_lg")
nlp.add_pipe("entityLinker", last=True)

path_corpora = "../DATA/DATA-Fra_spaCy3.3.1_CONCAT/*/*/*/*.txt"



for path in glob.glob(path_corpora):
    print(path)
    txt=lire_fichier(path)
    doc = nlp(txt[:5000])        
    i=0
    dico_sent_tok ={}
    
    
    for ent in doc._.linkedEntities: 
            ide = "ID"+str(i)
            url_00 = ent.get_url()
            label_00=ent.get_label()
            description=ent.get_description()
            span_00=ent.get_span()
            span_oo=str(span_00)
            doc2=nlp(span_oo)
            for en in doc2.ents:#Pour le typage avec les labels de l'entity linking
                
                # print(en.label_)
                dico_sent_tok[ide]={}
                dico_sent_tok[ide]["url"]=url_00
                dico_sent_tok[ide]["span"]=span_oo
                dico_sent_tok[ide]["label"]=label_00
                dico_sent_tok[ide]["description"]=description
                dico_sent_tok[ide]["type"]=en.label_#Pour le typage avec les labels de l'entity linking
                i+=1
# print (dico_sent_tok)
    
# print (dico_sent_tok)
            stocker("%s_entity-linker.json"%path,dico_sent_tok)
    # with open ("resultat.json", "w", encoding="utf-8") as f:
    #       json.dump(dico_sent_tok, f)
        # Affichage des résultats ou sauvegarde dans un fichier, etc.
#print(resultats)