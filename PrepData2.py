#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
04/2021
Projet Insee

title : PrepData2.py
authors : MAXWELL - GOMES - SOU
description : Importation des csv et génération des dataframes
"""

################################ Importation des csv ################################

print("# Importation des csv ...")
#1) importation des csv concernant les régions : 
region = pd.read_csv('data/region2020.csv', sep=',', index_col="nccenr")
print("** data/region2020.csv")
r_evo = pd.read_csv('data/f_region_evo.csv', sep=';', index_col="reg")
print("** data/f_region_evo.csv")
r_social = pd.read_csv('data/f_region_social.csv', sep=';', index_col="reg")
print("** data/f_region_social.csv")
r_eco = pd.read_csv('data/f_region_eco.csv', sep=';', index_col="reg")
print("** data/f_region_eco.csv")
#2) importation des csv concernant les départements : 
departement = pd.read_csv('data/departement2020.csv', sep=',', index_col="nccenr")
print("** data/departement2020.csv")
d_evo = pd.read_csv('data/f_dep_evo.csv', sep=';', index_col="dep")
print("** data/f_dep_evo.csv")
d_social = pd.read_csv('data/f_dep_social.csv', sep=';', index_col="dep")
print("** data/f_dep_social.csv")
d_eco = pd.read_csv('data/f_dep_eco.csv', sep=';', index_col="dep")
print("** data/f_dep_eco.csv")

############################## DF propres aux regions ###############################

## creation Region ## 
frames = [region, r_evo, r_social, r_eco]
dfReg = pd.concat(frames, axis=1, join="inner") # concatenation par nccenr <--> reg
# selection des colones d'interet
Regions = dfReg[[
    'reg', 
    'ncc', 
    'libelle', 
    'var_2012_2017', 
    'var_nat', 
    'var_es', 
    'disp_2014', 
    'eloignement_2016', 
    'ta_2017', 
    'dipl_2017', 
    'poids_2015'
]]
print("\nRegions\n", Regions)
print(Regions.columns)

## creation Pop_region ##
# note : 1) creation dfAnnee 2) renome colonne pop 3) ajout colonne annee

r_pop_2012 = r_evo[["numero", "pop_2012"]] 
r_pop_2012 = r_pop_2012.rename(columns = {"pop_2012":"pop"})
r_pop_2012["annee"] = 2012
r_pop_2017 = r_evo[["numero","pop_2017"]] 
r_pop_2017 = r_pop_2017.rename(columns = {"pop_2017":"pop"})
r_pop_2017["annee"] = 2017
r_pop_2020 = r_evo[["numero","est_2020"]] 
r_pop_2020 = r_pop_2020.rename(columns = {"est_2020":"pop"})
r_pop_2020["annee"] = 2020
# Concatenation des dfs
Pop_region = pd.concat([r_pop_2012, r_pop_2017, r_pop_2020])#, ignore_index=True)
print("\nPop_region\n", Pop_region) 

## Creation Recherche_dev ##

r_eff_2014 = r_eco[["numero", "effort_2014"]]
r_eff_2014 = r_eff_2014.rename(columns = {"effort_2014": "effort"})
r_eff_2014["annee"] = 2014
r_eff_2010 = r_eco[["numero", "effort_2010"]]
r_eff_2010 = r_eff_2010.rename(columns = {"effort_2010": "effort"})
r_eff_2010["annee"] = 2010

Recherche_dev = pd.concat([r_eff_2010, r_eff_2014])
print("\nRecherche_Dev\n", Recherche_dev)

############################## DF propres aux regions ###############################

## Creation Departement ##
frames = [departement, d_evo, d_social, d_eco]
dfDep = pd.concat(frames, axis=1, join="inner")
# selection des colones d'interet
Departements = dfDep[[
    'reg',
    'dep', 
    'ncc', 
    'libelle', 
    'var_2012_2017', 
    'var_nat', 
    'var_es', 
    'disp_2014', 
    'eloignement_2016', 
    'ta_2017', 
    'dipl_2017', 
    'poids_2015'
]]
print("\nDepartemens\n", Departements)

############################### DF commun #################################

## 
