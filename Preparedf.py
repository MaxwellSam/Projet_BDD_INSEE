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

# Données propres aux régions /

## dataframe region 
r_numero = region_data["reg"].values
r_ncc = region_data["ncc"].values

# evo var_2012_2017;var_nat;var_es
r_pop_2012 = region_evo_data["pop_2012"].values
r_pop_2017 = region_evo_data["pop_2017"].values
r_est_2020 = region_evo_data["est_2020"].values
r_var_2012_2017 = region_evo_data["var_2012_2017"].values
r_var_nat = region_evo_data["var_nat"].values
r_var_es = region_evo_data["var_es"].values

# eco
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
num_dep = dep_data["dep"]
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
d_pauvrete_2019 = dep_social_data["jeune_ni_2019"].values
d_eloignement = dep_social_data["eloignement"].values
d_inondable_2013 = dep_social_data["inondable_2013"].values
d_inondable_2008 = dep_social_data["inondable_2008"].values