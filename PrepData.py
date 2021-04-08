#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
04/2021
Projet Insee

title : PrepData.py
authors : MAXWELL - GOMES - SOU
description : Importation des csv et génération des dataframes
"""

################################ Importation des csv ################################

print("# Importation des csv ...")
#1) importation des csv concernant les régions : 
region = pd.read_csv('data/region2020.csv', sep=',', index_col="nccenr")
print(region)
print("** data/region2020.csv")
r_evo = pd.read_csv('data/f_region_evo.csv', sep=';', index_col="reg")
print("** data/f_region_evo.csv")
print(r_evo)
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

### netoyage 

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

## creation Pop_regions ##

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
Pop_regions = pd.concat([
    r_pop_2012, 
    r_pop_2017, 
    r_pop_2020
])
print("\nPop_regions\n", Pop_regions) 

## Creation Recherche_dev ##

r_eff_2014 = r_eco[["numero", "effort_2014"]]
r_eff_2014 = r_eff_2014.rename(columns = {"effort_2014": "effort"})
r_eff_2014["annee"] = 2014
r_eff_2010 = r_eco[["numero", "effort_2010"]]
r_eff_2010 = r_eff_2010.rename(columns = {"effort_2010": "effort"})
r_eff_2010["annee"] = 2010
# concatenation
Recherche_dev = pd.concat([
    r_eff_2010, 
    r_eff_2014
])
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

## Creation Pop_Departements ##
d_pop_2012 = d_evo[["numero", "pop_2012"]] 
d_pop_2012 = d_pop_2012.rename(columns = {"pop_2012":"pop"})
d_pop_2012["annee"] = 2012
d_pop_2017 = d_evo[["numero","pop_2017"]] 
d_pop_2017 = d_pop_2017.rename(columns = {"pop_2017":"pop"})
d_pop_2017["annee"] = 2017
d_pop_2018 = d_evo[["numero","pop_2018"]] 
d_pop_2018 = d_pop_2018.rename(columns = {"pop_2018":"pop"})
d_pop_2018["annee"] = 2018
d_pop_2020 = d_evo[["numero","est_2020"]] 
d_pop_2020 = d_pop_2020.rename(columns = {"est_2020":"pop"})
d_pop_2020["annee"] = 2020
# Concatenation des dfs
Pop_departements = pd.concat([
    d_pop_2012, 
    d_pop_2017, 
    d_pop_2018,
    d_pop_2020
])
print("\nPop_departements\n", Pop_departements) 

############################### DF commun #################################

## creation Esperance_vie ##
# region 
r_esp_2010 = r_social[["esp_h_2010", "esp_f_2010"]]
r_esp_2010 = r_esp_2010.rename_axis("libelle").rename(columns={"esp_h_2010":"esp_vie_h", "esp_f_2010":"esp_vie_f"})
r_esp_2010["annee"] = 2010
r_esp_2015 = r_social[["esp_h_2015", "esp_f_2015"]]
r_esp_2015 = r_esp_2015.rename_axis("libelle").rename(columns={"esp_h_2015":"esp_vie_h", "esp_f_2015":"esp_vie_f"})
r_esp_2015["annee"] = 2015
r_esp_2019 = r_social[["esp_h_2019", "esp_f_2019"]]
r_esp_2019 = r_esp_2019.rename_axis("libelle").rename(columns={"esp_h_2019":"esp_vie_h", "esp_f_2019":"esp_vie_f"})
r_esp_2019["annee"] = 2019
# departement 
d_esp_2010 = d_social[["esp_h_2010", "esp_f_2010"]]
d_esp_2010 = d_esp_2010.rename_axis("libelle").rename(columns={"esp_h_2010":"esp_vie_h", "esp_f_2010":"esp_vie_f"})
d_esp_2010["annee"] = 2010
d_esp_2015 = d_social[["esp_h_2015", "esp_f_2015"]]
d_esp_2015 = d_esp_2015.rename_axis("libelle").rename(columns={"esp_h_2015":"esp_vie_h", "esp_f_2015":"esp_vie_f"})
d_esp_2015["annee"] = 2015
d_esp_2019 = d_social[["esp_h_2019", "esp_f_2019"]]
d_esp_2019 = d_esp_2019.rename_axis("libelle").rename(columns={"esp_h_2019":"esp_vie_h", "esp_f_2019":"esp_vie_f"})
d_esp_2019["annee"] = 2019
# concatenation 
Esperance_vie = pd.concat([
    r_esp_2010, 
    r_esp_2015, 
    r_esp_2019, 
    d_esp_2010, 
    d_esp_2015, 
    d_esp_2019])
print("\nEsperance_vie\n", Esperance_vie)

## creation Taux_pauvrete ## 
# region
r_pauv_2014 = r_social[["pauvrete_2014"]]
r_pauv_2014 = r_pauv_2014.rename_axis("libelle").rename(columns={"pauvrete_2014":"pauvrete"})
r_pauv_2014["annee"] = 2014
r_pauv_2018 = r_social[["pauvrete_2018"]]
r_pauv_2018 = r_pauv_2018.rename_axis("libelle").rename(columns={"pauvrete_2018":"pauvrete"})
r_pauv_2018["annee"] = 2018
# departements
d_pauv_2014 = r_social[["pauvrete_2014"]]
d_pauv_2014 = r_pauv_2014.rename_axis("libelle").rename(columns={"pauvrete_2014":"pauvrete"})
d_pauv_2014["annee"] = 2014
d_pauv_2018 = r_social[["pauvrete_2018"]]
d_pauv_2018 = r_pauv_2018.rename_axis("libelle").rename(columns={"pauvrete_2018":"pauvrete"})
d_pauv_2018["annee"] = 2018
# concatenation
Pauvrete = pd.concat([
    r_pauv_2014, 
    r_pauv_2018, 
    d_pauv_2014, 
    d_pauv_2018
])
print("\nPauvrete\n", Pauvrete)

## creation Insertion_jeunes ## 
# region 
r_inser_2009 = r_social[["jeune_ni_2009"]]
r_inser_2009 = r_inser_2009.rename_axis("libelle").rename(columns={"jeune_ni_2009":"jeunes_non_inseres"})
r_inser_2009["annee"] = 2009
r_inser_2014 = r_social[["jeune_ni_2014"]]
r_inser_2014 = r_inser_2014.rename_axis("libelle").rename(columns={"jeune_ni_2014":"jeunes_non_inseres"})
r_inser_2014["annee"] = 2014
r_inser_2017 = r_social[["jeune_ni_2017"]]
r_inser_2017 = r_inser_2017.rename_axis("libelle").rename(columns={"jeune_ni_2017":"jeunes_non_inseres"})
r_inser_2017["annee"] = 2017
# departements
d_inser_2009 = d_social[["jeune_ni_2009"]]
d_inser_2009 = d_inser_2009.rename_axis("libelle").rename(columns={"jeune_ni_2009":"jeunes_non_inseres"})
d_inser_2009["annee"] = 2009
d_inser_2014 = d_social[["jeune_ni_2014"]]
d_inser_2014 = d_inser_2014.rename_axis("libelle").rename(columns={"jeune_ni_2014":"jeunes_non_inseres"})
d_inser_2014["annee"] = 2014
d_inser_2017 = d_social[["jeune_ni_2017"]]
d_inser_2017 = d_inser_2017.rename_axis("libelle").rename(columns={"jeune_ni_2017":"jeunes_non_inseres"})
d_inser_2017["annee"] = 2017
# concatenation
Insertion_jeunes = pd.concat([
    r_inser_2009, 
    r_inser_2014, 
    r_inser_2017, 
    d_inser_2009, 
    d_inser_2014, 
    d_inser_2017
])
print("\nInsertion_jeunes\n", Insertion_jeunes)

## creation Zones_inondables ## 
# regions
r_zone_2008 = r_social[["inondable_2008"]]
r_zone_2008 = r_zone_2008.rename_axis("libelle").rename(columns={"inondable_2008":"zones_inondables"})
r_zone_2008["annee"]=2008
r_zone_2013 = r_social[["inondable_2013"]]
r_zone_2013 = r_zone_2013.rename_axis("libelle").rename(columns={"inondable_2013":"zones_inondables"})
r_zone_2013["annee"]=2013
# departements
d_zone_2008 = d_social[["inondable_2008"]]
d_zone_2008 = d_zone_2008.rename_axis("libelle").rename(columns={"inondable_2008":"zones_inondables"})
d_zone_2008["annee"]=2008
d_zone_2013 = d_social[["inondable_2013"]]
d_zone_2013 = d_zone_2013.rename_axis("libelle").rename(columns={"inondable_2013":"zones_inondables"})
d_zone_2013["annee"]=2013
# concatenation
Zones_inondables = pd.concat([
    r_zone_2008, 
    r_zone_2013, 
    d_zone_2008, 
    d_zone_2013])
print("\nZones_inondables\n", Zones_inondables)

## creation Emploi_diplome ##
# regions 
r_emp_dip_2009 = r_eco[["te_2009", "dipl_jeune_2009"]]
r_emp_dip_2009 = r_emp_dip_2009.rename_axis("libelle").rename(columns={"te_2009":"taux_emploi", "dipl_jeune_2009":"jeunes_diplomes"})
r_emp_dip_2009["annee"] = 2009
r_emp_dip_2014 = r_eco[["te_2014", "dipl_jeune_2014"]]
r_emp_dip_2014 = r_emp_dip_2014.rename_axis("libelle").rename(columns={"te_2014":"taux_emploi", "dipl_jeune_2014":"jeunes_diplomes"})
r_emp_dip_2014["annee"] = 2014
# departements
d_emp_dip_2009 = d_eco[["te_2009", "dipl_jeune_2009"]]
d_emp_dip_2009 = d_emp_dip_2009.rename_axis("libelle").rename(columns={"te_2009":"taux_emploi", "dipl_jeune_2009":"jeunes_diplomes"})
d_emp_dip_2009["annee"] = 2009
d_emp_dip_2014 = d_eco[["te_2014", "dipl_jeune_2014"]]
d_emp_dip_2014 = d_emp_dip_2014.rename_axis("libelle").rename(columns={"te_2014":"taux_emploi", "dipl_jeune_2014":"jeunes_diplomes"})
d_emp_dip_2014["annee"] = 2014
# concatenation
Emploi_diplome = pd.concat([
    r_emp_dip_2009, 
    r_emp_dip_2014, 
    d_emp_dip_2009, 
    d_emp_dip_2014
])
print("\nEmploi_diplome\n", Emploi_diplome)

## creation Transport ## 
# regions
r_transp_2009 = r_eco[["voiture_2009", "commun_2009", "autre_2009"]]
r_transp_2009 = r_transp_2009.rename_axis("libelle").rename(columns={"voiture_2009":"voiture", "commun_2009":"commun", "autre_2009":"autre"})
r_transp_2009["annee"] = 2009
r_transp_2014 = r_eco[["voiture_2014", "commun_2014", "autre_2014"]]
r_transp_2014 = r_transp_2014.rename_axis("libelle").rename(columns={"voiture_2014":"voiture", "commun_2014":"commun", "autre_2014":"autre"})
r_transp_2014["annee"] = 2014
# departements
d_transp_2009 = d_eco[["voiture_2009", "commun_2009", "autre_2009"]]
d_transp_2009 = d_transp_2009.rename_axis("libelle").rename(columns={"voiture_2009":"voiture", "commun_2009":"commun", "autre_2009":"autre"})
d_transp_2009["annee"] = 2009
d_transp_2014 = d_eco[["voiture_2014", "commun_2014", "autre_2014"]]
d_transp_2014 = d_transp_2014.rename_axis("libelle").rename(columns={"voiture_2014":"voiture", "commun_2014":"commun", "autre_2014":"autre"})
d_transp_2014["annee"] = 2014
# concatenation 
Transport = pd.concat([
    r_transp_2009,
    r_transp_2014,
    d_transp_2009,
    d_transp_2014
])
print("\nTransport\n", Transport)
print("test", Transport["voiture"][1])
##  
