#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:07:50 2023

@author: obtic2023
"""
import json
import glob
import matplotlib.pyplot as plt

def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)
    return dist


def stocker_graph(nomfich): 
    
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
    plt.ylabel("nombre d'entités liées")
    plt.xlabel("OCR Version")
    plt.xticks(fontsize=10,rotation=25)
    # plt.axis([-1,7,0,1])  
    # plt.legend(loc="lower left",ncol=2, bbox_to_anchor=(0,0.98))
    # plt.legend 
    plt.gcf().set_size_inches(8, 9)
    plt.savefig(nomfich)
    plt.clf()
    
    return nomfich 

path_corpora = "../DATA/DATA-Fra_spaCy3.3.1_entity-linking_PROPRE/*"

for subcorpus in glob.glob(path_corpora):
    x=["Réf"]
    
    # print(subcorpus)
    
  
    for path_version in glob.glob("%s/*"%subcorpus):   
        version_OCR = path_version.split("/")[-1]
        version_OCR = version_OCR.split("_")[-1]
        x.append(version_OCR)
        liste_loc = []
        liste_autre = []
        liste_loc_ref=[]
        liste_autre_ref=[] 
        liste_res=[]
        output=path_version.split("/")[-1]
        output=output.split("_")[0]
        
        #print(x)
        for path in glob.glob("%s/*/*/*_entity-linker.json"%subcorpus):
   
            data=lire_fichier(path)
          
            
            Loc = 0
            autre = 0
         
            for key, value in data.items():
                # print(value)
                for cle, valeur in value.items():
                    # print(cle)
                    if cle == "type" and valeur =="LOC":
                        # print(valeur)
                        Loc+=1
                    else:
                        autre+=1
            if "PP" in path:       
                # #nb de dictionnaire qui ne contiennent pas des loc
                liste_loc_ref.append(Loc)
                liste_autre_ref.append(autre)
                # break
            else:
                liste_loc.append(Loc)
                liste_autre.append(autre)
        # liste_res.append([liste_loc_ref,liste_autre_ref,liste_loc,liste_autre])
   
    liste_loc.insert(0,liste_loc_ref[0])
    liste_autre.insert(0,liste_autre_ref[0])
        

    largeur_barre = 0.8
    ax=range(len(liste_loc))
    
    
    
    # # # Tracé
    
    plt.bar(x,liste_loc, width = largeur_barre, color = "red")
     
    plt.bar(x, liste_autre, width = largeur_barre, bottom = liste_loc, color = "blue")
     
    plt.xticks(ax, x, rotation=90)
       
    # plt.show()
    print(path)
    stocker_graph("../DATA/%s_spaCylg-linking.png"%output)
        

   
  