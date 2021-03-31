#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
03/2021
Projet Insee
authors : 
"""

# Libs 
import pandas as pd
import psycopg2
import psycopg2.extras
import sys
import numpy as np

print("\n#### Projet INSEE // M1S2 // BDD ####")
print("############# SCRIPT 1 ##############\n")
print("### Importation des données (csv) ###\n")

# Data regions : 
region_data = pd.read_csv('data/region2020.csv', sep=',', index_col="reg")
print("** 'data/region2020.csv' exporté")
region_evo_data = pd.read_csv('data/f_region_evo.csv', sep=';', index_col="numero reg")
print("** 'data/f_region_evo.csv' exporté")
region_social_data = pd.read_csv('data/f_region_social.csv', sep=';', index_col="numero reg")
print("** 'data/f_region_social.csv' exporté")
region_eco_data = pd.read_csv('data/f_region_eco.csv', sep=';', index_col="numero reg")
print("** 'data/f_region_eco.csv' exporté\n")
# Data departement : 
dep_data = pd.read_csv('data/departement2020.csv', sep=',', index_col="dep")
print("** 'data/departement2020.csv' exporté")
dep_evo_data = pd.read_csv('data/f_dep_evo.csv', sep=';', index_col="numero dep")
print("** 'data/f_dep_evo.csv' exporté")
dep_social_data = pd.read_csv('data/f_dep_social.csv', sep=';', index_col="numero dep")
print("** 'data/f_dep_social.csv' exporté")
dep_eco_data = pd.read_csv('data/f_dep_eco.csv', sep=';', index_col="numero dep")
print("** 'data/f_dep_eco.csv' exporté\n")

print("# toutes les données sont exportées #")

print(region_data)
print(dep_evo_data)








