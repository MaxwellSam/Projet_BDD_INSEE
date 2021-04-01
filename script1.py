#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
03/2021
Projet Insee

title : script1.py
authors : MAXWELL - GOMES - SOU
"""

# Libs 
import pandas as pd
import psycopg2
import psycopg2.extras
import sys
import numpy as np
# Nos API 
import MyToolBox as myTool

print("\n#### Projet INSEE // M1S2 // BDD ####")
print("############# SCRIPT 1 ##############\n")
print("### Importation des données (csv) et Preparation des DataFrame###\n")
# execution du fichier d'importation des données et de préparation des df : 
exec(open("Preparedf.py").read())
print("\n### Dataframes prêtes ###\n")
