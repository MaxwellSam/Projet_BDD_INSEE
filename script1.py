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
from sqlalchemy import create_engine
import sqlalchemy as sql
# Nos API 
import MyToolBox as myTool

print("\n#### Projet INSEE // M1S2 // BDD ####")
print("############# SCRIPT 1 ##############\n")
print("### Importation des données (csv) et Preparation des DataFrame###\n")
# execution du fichier d'importation des données et de préparation des df : 
exec(open("Preparedf.py").read())
print("\n### Dataframes prêtes ###\n")

# Connexion à postgresql

print("\n### CONNEXION A POSTGRESQL ###\n")
# postgresql+psycopg2://username:password@localhost:5432/username

print("\n### CONNEXION A POSTGRESQL FERMEE ###\n")

print("### Question 2 ### PANDAS et SQL - Creation des tables à partir des Dframes ###\n\n")
# Connexion aux bases de données : 

print("\n############ Creation des tables dans le SQL ################\n")
# Try to connect to an existing database
print('Connexion a la base de donnees...')
USERNAME="smaxwell"
PASSWORD="SQLsam"

engine = create_engine('postgresql+psycopg2//smaxwell:SQLsam@pgsql:5432/smaxwell')
Regions.to_sql('Regions',engine)

print('Connecte a la base de donnees')
