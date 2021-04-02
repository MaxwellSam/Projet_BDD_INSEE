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

print("region_data :", region_data.columns.values)
print("region_evo_data :", region_evo_data.columns.values)
print("region_social_data :", region_social_data.columns.values)
print("region_eco_data :", region_eco_data.columns.values)

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
r_var_2012_2017 = region_evo_data["var_2012_2017"].values
r_var_nat = region_evo_data["var_nat"].values
r_var_es = region_evo_data["var_es"].values

# eco
r_eco_numero = region_eco_data["numero"].values
r_te_2014 = region_eco_data["te_2014"].values
r_te_2009 = region_eco_data["te_2009"].values
r_dipl_2017 = region_eco_data["dipl_2017"].values
r_dipl_2014 = region_eco_data["dipl_2014"].values
r_dipl_jeune_2009 = region_eco_data["dipl_jeune_2009"].values
r_voiture_2014 = region_eco_data["voiture_2014"].values
r_voiture_2009 = region_eco_data["voiture_2009"].values
r_commun_2014 = region_eco_data["commun_2014"].values
r_commun_2009 = region_eco_data["commun_2009"].values
r_autre_2014 = region_eco_data["autre_2014"].values
r_autre_2009 = region_eco_data["autre_2009"].values
r_poids_2015 = region_eco_data["poids_2015"].values
r_effort_2014 = region_eco_data["effort_2014"].values
r_effort_2010 = region_eco_data["effort_2010"].values


# social
r_social_labelle = region_social_data["reg"].values
r_esp_h_2019 = region_social_data["esp_h_2019"].values
r_esp_h_2015 = region_social_data["esp_h_2015"].values
r_esp_h_2010 = region_social_data["esp_h_2010"].values
r_esp_f_2019 = region_social_data["esp_f_2019"].values
r_esp_f_2015 = region_social_data["esp_f_2015"].values
r_esp_f_2010 = region_social_data["esp_f_2010"].values
r_disp_2014 = region_social_data["disp_2014"].values
r_pauvrete_2018 = region_social_data["pauvrete_2018"].values
r_pauvrete_2014 = region_social_data["pauvrete_2014"].values
r_jeune_ni_2017 = region_social_data["jeune_ni_2017"].values
r_jeune_ni_2014 = region_social_data["jeune_ni_2014"].values
r_jeune_ni_2009 = region_social_data["jeune_ni_2009"].values
r_eloignement_2016 = region_social_data["eloignement_2016"].values
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
d_var_2012_2017 = dep_evo_data["var_2012_2017"].values
d_var_nat = dep_evo_data["var_nat"].values
d_var_es = dep_evo_data["var_es"].values

#eco
d_ta_2017 = dep_eco_data["ta_2017"].values
d_ta_2014 = dep_eco_data["ta_2014"].values
d_te_2009 = dep_eco_data["te_2009"].values
d_dipl_2017 = dep_eco_data["dipl_2017"].values
d_dipl_jeune_2014 = dep_eco_data["dipl_jeune_2014"].values
d_dipl_jeune_2009 = dep_eco_data["dipl_jeune_2009"].values
d_voiture_2014 = dep_eco_data["voiture_2014"].values
d_voiture_2009 = dep_eco_data["voiture_2009"].values
d_commun_2014 = dep_eco_data["commun_2014"].values

#social
d_social_labelle = dep_social_data["dep"].values
d_esp_h_2019 = dep_social_data["esp_h_2019"].values
d_esp_h_2015 = dep_social_data["esp_h_2015"].values
d_esp_h_2010 = dep_social_data["esp_h_2010"].values
d_esp_f_2019 = dep_social_data["esp_f_2019"].values
d_esp_f_2015 = dep_social_data["esp_f_2015"].values
d_esp_f_2010 = dep_social_data["esp_f_2010"].values
d_disp_2014 = dep_social_data["disp_2014"].values
d_pauvrete_2018 = dep_social_data["pauvrete_2018"].values
d_pauvrete_2014 = dep_social_data["pauvrete_2014"].values
d_jeune_ni_2017 = dep_social_data["jeune_ni_2017"].values
d_jeune_ni_2014 = dep_social_data["jeune_ni_2014"].values
d_jeune_ni_2019 = dep_social_data["jeune_ni_2019"].values
d_eloignement = dep_social_data["eloignement"].values
d_inondable_2013 = dep_social_data["inondable_2013"].values
d_inondable_2008 = dep_social_data["inondable_2008"].values


###################### Creation des dataframes ##############################

#### Tables POP_REGION

## creation de la colonne des numero_regions pour la table population
r_pop_num = myTool.flatList([r_pop_numero, r_pop_numero, r_pop_numero])
print(r_pop_num)
print(len(r_pop_num))
## creation de la colonne des annee pour la table population
r_pop_annees = myTool.creationColAnnee (len(r_pop_2012), [2012, 2017, 2020])
print(r_pop_annees)
print(len(r_pop_annees))
## creation de la colonne des population pour la table population
r_pop = myTool.flatList([r_pop_2012, r_pop_2017, r_est_2020])
print(r_pop)
print(len(r_pop))

data_pop_reg ={'numero_region':r_pop_num, 'population':r_pop, 'annee':r_pop_annees}
population_regions_df = pd.DataFrame(data=data_pop_reg)
print(population_regions_df)

#### Tables RECH_DEV

r_eco_num = myTool.flatList([r_eco_numero, r_eco_numero])
print(r_eco_num)
print(len(r_eco_num))
r_eco_annees = myTool.creationColAnnee (len(r_effort_2010), [2010, 2014])
print(r_eco_annees)
print(len(r_eco_annees))
r_eco_effort = myTool.flatList([r_effort_2010, r_effort_2014])
print(r_eco_effort)
print(len(r_eco_effort))
data_effort_reg = {'numero_region':r_eco_num, 'effort':r_eco_effort, 'annee':r_eco_annees}
effort_region_df = pd.DataFrame(data=data_effort_reg)

print(effort_region_df)

#### Tables POP_DEP

## creation de la colonne des numero_regions pour la table population
d_pop_num = myTool.flatList([d_pop_numero, d_pop_numero, d_pop_numero, d_pop_numero])
print(d_pop_num)
print(len(d_pop_num))
## creation de la colonne des annee pour la table population
d_pop_annees = myTool.creationColAnnee (len(d_pop_2012), [2012, 2017, 2018, 2020])
print(d_pop_annees)
print(len(d_pop_annees))
## creation de la colonne des population pour la table population
d_pop = myTool.flatList([d_pop_2012, d_pop_2017,d_pop_2018, d_est_2020])
print(d_pop)
print(len(d_pop))

data_pop_dep ={'numero_departement':d_pop_num, 'population':d_pop, 'annee':d_pop_annees}

population_departement_df = pd.DataFrame(data=data_pop_dep)
print(population_departement_df)

#### Tables ESPERANCE_VIE

data_esp_vie_h = myTool.creatDFcommunDepReg (
                        r_social_labelle, 
                        d_social_labelle, 
                        [r_esp_h_2010, r_esp_h_2015, r_esp_h_2019], 
                        [d_esp_h_2010, d_esp_h_2015, d_esp_h_2019], 
                        [2010, 2015, 2019]
                        )
                        
data_esp_vie_f = myTool.creatDFcommunDepReg (
                        r_social_labelle, 
                        d_social_labelle, 
                        [r_esp_f_2010, r_esp_f_2015, r_esp_f_2019],
                        [d_esp_f_2010, d_esp_f_2015, d_esp_f_2019], 
                        [2010, 2015, 2019]
                        )
                        
labelle = data_esp_vie_h["labelle"] 
esp_vie_h = data_esp_vie_h["variable"]
esp_vie_f = data_esp_vie_f["variable"]
annee = data_esp_vie_h["annee"]
data_esp = {'labelle':labelle, 'esperance_homme':esp_vie_h, 'esperance_femme':esp_vie_f, 'annee':annee}
Esperance_vie_df = pd.DataFrame(data=data_esp)
print(Esperance_vie_df)

# VarRegParAnnee = []
# VarRegParAnnee.append([r_esp_h_2010, r_esp_h_2015, r_esp_h_2019])
# VarRegParAnnee.append([r_esp_f_2010, r_esp_f_2015, r_esp_f_2019])
# VarDepParAnnee = []
# VarDepParAnnee.append([d_esp_h_2010, d_esp_h_2015, d_esp_h_2019])
# VarDepParAnnee.append([d_esp_f_2010, d_esp_f_2015, d_esp_f_2019])
#
# data_cleaned_esp = myTool.creatDFcommunDepReg2(r_social_labelle, d_social_labelle,VarRegParAnnee, VarDepParAnnee, [2010, 2015, 2019])

#### TAUX_PAUVRETE

data_t_a = myTool.creatDFcommunDepReg(
                        r_social_labelle, 
                        d_social_labelle, 
                        [r_pauvrete_2014, r_pauvrete_2018],
                        [d_pauvrete_2014, d_pauvrete_2018],
                        [2014, 2018]
                        )
labelle = data_t_a["labelle"]
t_a = data_t_a["variable"]
annee = data_t_a["annee"]
data_t_a = {'labelle': labelle, 'taux_pauvrete':t_a, 'annee':annee}
Taux_pauvrete_df = pd.DataFrame(data_t_a)
print(Taux_pauvrete_df)



