#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
03/2021
Projet Insee

title : Preparedf.py
authors : MAXWELL - GOMES - SOU
description : Importation et génération des dataframes
"""
# Action sur les listes : 

# Data regions : 
region_data = pd.read_csv('data/region2020.csv', sep=',') #index_col="reg")
print("** 'data/region2020.csv' exporté")
print(region_data)
region_evo_data = pd.read_csv('data/f_region_evo.csv', sep=';') #index_col="numero")
print("** 'data/f_region_evo.csv' exporté")
region_social_data = pd.read_csv('data/f_region_social.csv', sep=';') #index_col="numero")
print("** 'data/f_region_social.csv' exporté")
region_eco_data = pd.read_csv('data/f_region_eco.csv', sep=';') # index_col="numero")
print("** 'data/f_region_eco.csv' exporté\n")

# Data departement : 
dep_data = pd.read_csv('data/departement2020.csv', sep=',') #  index_col="dep")
print("** 'data/departement2020.csv' exporté")
dep_evo_data = pd.read_csv('data/f_dep_evo.csv', sep=';') #  index_col="numero")
print("** 'data/f_dep_evo.csv' exporté")
dep_social_data = pd.read_csv('data/f_dep_social.csv', sep=';') #  index_col="numero")
print("** 'data/f_dep_social.csv' exporté")
dep_eco_data = pd.read_csv('data/f_dep_eco.csv', sep=';') #  index_col="numero")
print("** 'data/f_dep_eco.csv' exporté\n")

print("# toutes les données sont exportées #")

print("\n### Preparation des dataframes ###\n")

################## Stockage dans les variables ####################

# Données propres aux régions /

## dataframe region 
r_numero = region_data["reg"].values
r_ncc = region_data["ncc"].values
r_libelle = region_data["libelle"].values

# evo var_2012_2017;var_nat;var_es
r_pop_numero = region_evo_data["numero"].values
r_pop_2012 = region_evo_data["pop_2012"].values
r_pop_2017 = region_evo_data["pop_2017"].values
r_est_2020 = region_evo_data["est_2020"].values

# eco
r_eco_libelle = region_eco_data["reg"].values
r_eco_numero = region_eco_data["numero"].values
r_te_2014 = region_eco_data["te_2014"].values
r_te_2009 = region_eco_data["te_2009"].values
r_dipl_jeune_2014 = region_eco_data["dipl_jeune_2014"].values
r_dipl_jeune_2009 = region_eco_data["dipl_jeune_2009"].values
r_voiture_2014 = region_eco_data["voiture_2014"].values
r_voiture_2009 = region_eco_data["voiture_2009"].values
r_commun_2014 = region_eco_data["commun_2014"].values
r_commun_2009 = region_eco_data["commun_2009"].values
r_autre_2014 = region_eco_data["autre_2014"].values
r_autre_2009 = region_eco_data["autre_2009"].values
r_effort_2014 = region_eco_data["effort_2014"].values
r_effort_2010 = region_eco_data["effort_2010"].values


# social
r_social_libelle = region_social_data["reg"].values
r_esp_h_2019 = region_social_data["esp_h_2019"].values
r_esp_h_2015 = region_social_data["esp_h_2015"].values
r_esp_h_2010 = region_social_data["esp_h_2010"].values
r_esp_f_2019 = region_social_data["esp_f_2019"].values
r_esp_f_2015 = region_social_data["esp_f_2015"].values
r_esp_f_2010 = region_social_data["esp_f_2010"].values
r_pauvrete_2018 = region_social_data["pauvrete_2018"].values
r_pauvrete_2014 = region_social_data["pauvrete_2014"].values
r_jeune_ni_2017 = region_social_data["jeune_ni_2017"].values
r_jeune_ni_2014 = region_social_data["jeune_ni_2014"].values
r_jeune_ni_2009 = region_social_data["jeune_ni_2009"].values
r_inondable_2013 = region_social_data["inondable_2013"].values
r_inondable_2008 = region_social_data["inondable_2008"].values

## dataframe departement 

d_numero = dep_data["dep"].values
d_ncc = dep_data["ncc"].values

#evo
d_pop_numero = dep_evo_data["numero"].values
d_pop_2012 = dep_evo_data["pop_2012"].values
d_pop_2017 = dep_evo_data["pop_2017"].values
d_pop_2018 = dep_evo_data["pop_2018"].values
d_est_2020 = dep_evo_data["est_2020"].values

#eco
d_eco_libelle = dep_eco_data["dep"].values
d_te_2014 = dep_eco_data["te_2014"].values
d_te_2009 = dep_eco_data["te_2009"].values
d_dipl_jeune_2014 = dep_eco_data["dipl_jeune_2014"].values
d_dipl_jeune_2009 = dep_eco_data["dipl_jeune_2009"].values
d_voiture_2014 = dep_eco_data["voiture_2014"].values
d_voiture_2009 = dep_eco_data["voiture_2009"].values
d_commun_2014 = dep_eco_data["commun_2014"].values
d_commun_2009 = dep_eco_data["commun_2009"].values
d_autre_2014 = dep_eco_data["autre_2014"].values
d_autre_2009 = dep_eco_data["autre_2009"].values

#social
d_social_libelle = dep_social_data["dep"].values
d_esp_h_2019 = dep_social_data["esp_h_2019"].values
d_esp_h_2015 = dep_social_data["esp_h_2015"].values
d_esp_h_2010 = dep_social_data["esp_h_2010"].values
d_esp_f_2019 = dep_social_data["esp_f_2019"].values
d_esp_f_2015 = dep_social_data["esp_f_2015"].values
d_esp_f_2010 = dep_social_data["esp_f_2010"].values
d_pauvrete_2018 = dep_social_data["pauvrete_2018"].values
d_pauvrete_2014 = dep_social_data["pauvrete_2014"].values
d_jeune_ni_2017 = dep_social_data["jeune_ni_2017"].values
d_jeune_ni_2014 = dep_social_data["jeune_ni_2014"].values
d_jeune_ni_2009 = dep_social_data["jeune_ni_2009"].values
d_inondable_2013 = dep_social_data["inondable_2013"].values
d_inondable_2008 = dep_social_data["inondable_2008"].values

#############################################################################
###################### Creation des dataframes ##############################
#############################################################################

#### POP_REGION

## creation de la colonne des numero_regions pour la table population
r_pop_num = myTool.flatList([r_pop_numero, r_pop_numero, r_pop_numero])

## creation de la colonne des annee pour la table population
r_pop_annees = myTool.creationColAnnee (len(r_pop_2012), [2012, 2017, 2020])

## creation de la colonne des population pour la table population
r_pop = myTool.flatList([r_pop_2012, r_pop_2017, r_est_2020])

data_pop_reg ={'numero_region':r_pop_num, 'population':r_pop, 'annee':r_pop_annees}
population_regions_df = pd.DataFrame(data=data_pop_reg)
print("\nPop Region\n",population_regions_df)

#### RECH_DEV

r_eco_num = myTool.flatList([r_eco_numero, r_eco_numero])
r_eco_annees = myTool.creationColAnnee (len(r_effort_2010), [2010, 2014])
r_eco_effort = myTool.flatList([r_effort_2010, r_effort_2014])

data_effort_reg = {'numero_region':r_eco_num, 'effort':r_eco_effort, 'annee':r_eco_annees}
effort_region_df = pd.DataFrame(data=data_effort_reg)
print("\nEffort Region\n",effort_region_df)

#### POP_DEP

## creation de la colonne des numero_regions pour la table population
d_pop_num = myTool.flatList([d_pop_numero, d_pop_numero, d_pop_numero, d_pop_numero])

## creation de la colonne des annee pour la table population
d_pop_annees = myTool.creationColAnnee (len(d_pop_2012), [2012, 2017, 2018, 2020])

## creation de la colonne des population pour la table population
d_pop = myTool.flatList([d_pop_2012, d_pop_2017,d_pop_2018, d_est_2020])

data_pop_dep ={'numero_departement':d_pop_num, 'population':d_pop, 'annee':d_pop_annees}

population_departement_df = pd.DataFrame(data=data_pop_dep)
print("\nPop Departement\n",population_departement_df)

#### ESPERANCE_VIE

data_esp_vie_h = myTool.creatDFcommunDepReg (
                        r_social_libelle, 
                        d_social_libelle, 
                        [r_esp_h_2010, r_esp_h_2015, r_esp_h_2019], 
                        [d_esp_h_2010, d_esp_h_2015, d_esp_h_2019], 
                        [2010, 2015, 2019]
                        )
                        
data_esp_vie_f = myTool.creatDFcommunDepReg (
                        r_social_libelle, 
                        d_social_libelle, 
                        [r_esp_f_2010, r_esp_f_2015, r_esp_f_2019],
                        [d_esp_f_2010, d_esp_f_2015, d_esp_f_2019], 
                        [2010, 2015, 2019]
                        )
                        
libelle = data_esp_vie_h["libelle"] 
esp_vie_h = data_esp_vie_h["variable"]
esp_vie_f = data_esp_vie_f["variable"]
annee = data_esp_vie_h["annee"]
data_esp = {'libelle':libelle, 'esperance_homme':esp_vie_h, 'esperance_femme':esp_vie_f, 'annee':annee}
Esperance_vie_df = pd.DataFrame(data=data_esp)
print("\nEsperance Vie\n",Esperance_vie_df)

# VarRegParAnnee = []
# VarRegParAnnee.append([r_esp_h_2010, r_esp_h_2015, r_esp_h_2019])
# VarRegParAnnee.append([r_esp_f_2010, r_esp_f_2015, r_esp_f_2019])
# VarDepParAnnee = []
# VarDepParAnnee.append([d_esp_h_2010, d_esp_h_2015, d_esp_h_2019])
# VarDepParAnnee.append([d_esp_f_2010, d_esp_f_2015, d_esp_f_2019])
#
# data_cleaned_esp = myTool.creatDFcommunDepReg2(r_social_libelle, d_social_libelle,VarRegParAnnee, VarDepParAnnee, [2010, 2015, 2019])

#### TAUX_PAUVRETE

data_t_a = myTool.creatDFcommunDepReg(
                        r_social_libelle, 
                        d_social_libelle, 
                        [r_pauvrete_2014, r_pauvrete_2018],
                        [d_pauvrete_2014, d_pauvrete_2018],
                        [2014, 2018]
                        )
libelle = data_t_a["libelle"]
t_a = data_t_a["variable"]
annee = data_t_a["annee"]
data_t_a = {'libelle': libelle, 'taux_pauvrete':t_a, 'annee':annee}
Taux_pauvrete_df = pd.DataFrame(data_t_a)
print("\nTaux Pauvrete\n",Taux_pauvrete_df)

#### INSERTION_JEUNES

data_inser_jeune = myTool.creatDFcommunDepReg(
                        r_social_libelle, 
                        d_social_libelle,
                        [r_jeune_ni_2009, r_jeune_ni_2014, r_jeune_ni_2017],
                        [d_jeune_ni_2009, d_jeune_ni_2014, d_jeune_ni_2017],
                        [2009, 2014, 2017]
                        )
libelle = data_inser_jeune["libelle"]
t_in_jeunes = data_inser_jeune["variable"]
annee = data_inser_jeune["annee"]
data_inser_jeune = {'libelle':libelle, 'taux_inser_jeunes':t_in_jeunes, 'annee':annee}
Taux_insertion_jeunes_df = pd.DataFrame(data_inser_jeune)
print("\nTaux Insertion Jeunes\n",Taux_insertion_jeunes_df)

#### ZONE_INONDABLE

data_zone_in = myTool.creatDFcommunDepReg(
                        r_social_libelle, 
                        d_social_libelle,
                        [r_inondable_2008, r_inondable_2013],
                        [d_inondable_2008, d_inondable_2013],
                        [2008, 2013]
                        )
libelle = data_zone_in["libelle"]
pourc_zone_in = data_zone_in["variable"]
annee = data_zone_in["annee"]
data_zone_in = {'libelle':libelle, 'pourcentage_zone_inondable':pourc_zone_in, 'annee':annee}
Zone_inondable = pd.DataFrame(data_zone_in)
print("\nZone Inondable\n", Zone_inondable)

#### Emploi Diplomes 

data_emploi = myTool.creatDFcommunDepReg(
                        r_eco_libelle, 
                        d_eco_libelle, 
                        [r_dipl_jeune_2009, r_dipl_jeune_2014],
                        [d_dipl_jeune_2009, d_dipl_jeune_2014],
                        [2009, 2014]
                        )
data_diplome = myTool.creatDFcommunDepReg(
                        r_eco_libelle, 
                        d_eco_libelle, 
                        [r_dipl_jeune_2009, r_dipl_jeune_2014],
                        [d_dipl_jeune_2009, d_dipl_jeune_2014],
                        [2009, 2014]
                        )
libelle = data_emploi["libelle"]
emploi = data_emploi["variable"]
jeunes_diplomes = data_diplome["variable"]
annee = data_emploi["annee"]

data_emploi_diplome = {'libelle':libelle, 'emploi':emploi, 'jeunes_diplomes':jeunes_diplomes, 'annee':annee}
Emploi_dimplome = pd.DataFrame(data_emploi_diplome)
print("\nEmploi Diplome\n", Emploi_dimplome)

#### TRANSPORT 
data_voiture = myTool.creatDFcommunDepReg(
                        r_eco_libelle, 
                        d_eco_libelle, 
                        [r_voiture_2009, r_voiture_2014],
                        [d_voiture_2009, d_voiture_2014], 
                        [2009,2014]
                        )
data_commun = myTool.creatDFcommunDepReg(
                        r_eco_libelle, 
                        d_eco_libelle, 
                        [r_commun_2009, r_commun_2014],
                        [d_commun_2009, d_commun_2014], 
                        [2009,2014]
                        )
data_autre = myTool.creatDFcommunDepReg(
                        r_eco_libelle, 
                        d_eco_libelle, 
                        [r_autre_2009, r_autre_2014],
                        [d_autre_2009, d_autre_2014], 
                        [2009,2014]
                        )
libelle = data_autre["libelle"]
voiture = data_voiture["variable"]
commun = data_commun["variable"]
autre = data_autre["variable"]
annee = data_autre["annee"]

data_transport = {'libelle':libelle, 'voiture':voiture, 'transport_commun':commun, 'autre':autre, 'annee':annee}
Transport = pd.DataFrame(data_transport)
print("\nTransport\n", Transport)

#### Region 

# Merging dataframes
region = pd.read_csv('data/region2020.csv', sep=',', index_col="nccenr")
evo = pd.read_csv('data/f_region_evo.csv', sep=';', index_col="reg")
social = pd.read_csv('data/f_region_social.csv', sep=';', index_col="reg")
eco = pd.read_csv('data/f_region_eco.csv', sep=';', index_col="reg")

frames = [region, evo, social, eco]
dfReg = pd.concat(frames, axis=1, join="inner") # concatenation par nccenr <--> reg
# creation df Region 
Regions = dfReg[['reg', 'ncc', 'libelle', 'var_2012_2017', 'var_nat', 'var_es', 'disp_2014', 'eloignement_2016', 'ta_2017', 'dipl_2017', 'poids_2015']]
print("\nRegions\n", Regions)

#### Departement 

# Merging dataframes
departement = pd.read_csv('data/departement2020.csv', sep=',', index_col="nccenr")
evo = pd.read_csv('data/f_dep_evo.csv', sep=';', index_col="dep")
social = pd.read_csv('data/f_dep_social.csv', sep=';', index_col="dep")
eco = pd.read_csv('data/f_dep_eco.csv', sep=';', index_col="dep")

frames = [departement, evo, social, eco]
dfDep = pd.concat(frames, axis=1, join="inner")

Departements = dfDep[['reg','dep', 'ncc', 'libelle', 'var_2012_2017', 'var_nat', 'var_es', 'disp_2014', 'eloignement_2016', 'ta_2017', 'dipl_2017', 'poids_2015']]
print("\nDepartemens\n", Departements)





