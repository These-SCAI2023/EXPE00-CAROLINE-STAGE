import json
import re
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

import glob

def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)
        
        return dist
    
def nom_repertoire(chemin):
    for mot in glob.glob(chemin): 
        noms_rep = re.split("/", chemin)
        noms_repo = re.split("_",noms_rep[5])
        noms_repo = re.split("_",noms_repo[-1])
        noms_repo ="".join(noms_repo)
#        print("NOM FICHIER",noms_fichiers)

        return noms_repo

def nom_mod(path):
    for mot in glob.glob(path): 
        noms_mod = re.split("/", path)
        noms_mods = re.split("_",noms_mod[6])[-1]
        # nm = re.split("_",noms_mods[-2])
        # nmod ="".join(nm)
        return noms_mods
    

def diagramme_venn(liste_en_pp, liste_en_ocr,ocr):
    version_ocr=ocr
    venn2([set(liste_en_pp), set(liste_en_ocr)],set_labels = ('url-ID Réf', 'url-ID-%s'%version_ocr))
    
    
     
def stocker(nom_fichier):
    plt.rcParams.update({'font.size': 16})
    plt.savefig(nom_fichier)
    plt.clf()
    
    return nom_fichier
    

def recup_url(dico):
    liste_url=[]
    for key, value in data.items():
        # print(value)
        for cle, valeur in value.items():
            # print(cle)
            if cle=="url":
                liste_url.append(valeur)
            set_url=set(liste_url)
            
                
    return set_url

        
path_corpora = "../DATA/DATA-Fra_spaCy3.3.1_CONCAT/ADAM/*/*"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

liste_EN_ocr=[]
liste_EN_pp=[]

#for subcorpus in sorted(glob.glob("%s/*"%path_corpora)):
for subcorpus in sorted(glob.glob(path_corpora)):
#    print(subcorpus)
   
    for path in sorted(glob.glob("%s/*entity-linker.json"%subcorpus)):
        print("subsubcorpus",path )
        auteur=subcorpus.split("/")[-2]
        auteur=auteur.split("_")[0]
        # print(auteur)
        version_ocr=subcorpus.split("/")[-2]
        version_ocr=version_ocr.split("_")[-1]
        
        data = lire_fichier(path)
    #    print("************",subcorpus)
    #    print(texte)
        nomrep=nom_repertoire(path)
    #    print(nomrep)

        if nomrep == "REF" or nomrep == "PP" : 
            print(nomrep)
            liste_EN_pp.append(path)
            liste_EN_pp.append(version_ocr)
    #        liste_texte_pp.append(subcorpus)
            liste_EN_pp.append(recup_url(data))
            
            
              
        elif nomrep == "OCR" or nomrep =="MOD":
            print(nomrep)
            liste_EN_ocr.append(path)
            liste_EN_ocr.append(version_ocr)
    #         liste_texte_ocr.append(subcorpus)
            liste_EN_ocr.append(recup_url(data))
            
    
        
       
   
liste_ocr_verif=[] 
liste_pp_verif=[] 
i=0      
while i <len(liste_EN_ocr) :
    nom_mod_ocr=nom_mod(liste_EN_ocr[i])
#    print(nom_mod_ocr)
    nom_mod_pp=nom_mod(liste_EN_pp[i])
#    print(nom_mod_ocr)
    liste_ocr_verif.append(nom_mod_ocr)
    liste_pp_verif.append(nom_mod_pp)
    i=i+3
print(liste_ocr_verif)
print(liste_pp_verif)

result=True
for j in range(0,len(liste_ocr_verif)):
    if liste_ocr_verif[j]!=liste_pp_verif[j]:
        result = False
k=0
if result != False:
    while k<len(liste_EN_pp) :
        
        diagramme_venn(liste_EN_pp[k+2],liste_EN_ocr[k+2],liste_EN_pp[k+1])
        
        stocker("../DATA/DATA-Fra_spaCy3.3.1_CONCAT/ADAM/%s_%s_intersection.png"%(auteur,liste_EN_pp[k+1]))
        k=k+3
       
    
else:
    print("NOT OK")