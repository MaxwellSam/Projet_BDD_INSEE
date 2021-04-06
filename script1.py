""""
BDD 
03/2021
Projet Insee

authors : MAXWELL - GOMES - SOU
"""

# Libs 
import pandas as pd
import psycopg2
import psycopg2.extras
import sys
import numpy as np

print("\n#### Projet INSEE // M1S2 // BDD ####")
print("############# SCRIPT 1 ##############\n")

# execution du fichier d'importation des données et de préparation des df : 
print("\n### Importation des données (csv) et Preparation des DataFrame###\n")
exec(open("PrepData.py").read())
print("\n### Dataframes prêtes ###\n")

print("### Question 2 ### PANDAS et SQL - Creation des tables à partir des Dframes ###\n\n")
# Connexion aux bases de données : 
print("\n### CONNEXION A POSTGRESQL ###\n")
USERNAME="smaxwell"
PASSWORD="SQLsam"
try:
    conn = psycopg2.connect(host="pgsql",dbname=USERNAME, user=USERNAME, password=PASSWORD)
except Exception as e : 
    exit("Connexion impossible a la base de donnees: "+str(e))

print("\n### CONNEXION REUSSIE ###\n")

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

##################################### REGION ###########################################
print("Creation table regions") 
command = (
        """
        CREATE TABLE Regions (
        num_region INT NOT NULL, 
        ncc VARCHAR(1000), 
        libelle VARCHAR(1000),
        variation_pop_2012_2017 FLOAT,
        variation_population_naturelle FLOAT,
        variation_population_entrees_sorties FLOAT,
        disparite_niveau_vie_2014 FLOAT,
        eloignement_service_sante_2016 FLOAT,
        taux_activite_2017 FLOAT, 
        part_diplomes_2017 FLOAT,
        poids_economie_2015 FLOAT
        );
        """
        )
try:
    cur.execute(command)
    print("Table regions cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

################################# DEPARTEMENT ########################################
print("Creation table Departement") 
command = (
        """
        CREATE TABLE Departements (
        num_dep INT NOT NULL,
        num_region INT NOT NULL, 
        ncc VARCHAR(1000), 
        libelle VARCHAR(1000),
        variation_pop_2012_2017 FLOAT,
        variation_population_naturelle FLOAT,
        variation_population_entrees_sorties FLOAT,
        disparite_niveau_vie_2014 FLOAT,
        eloignement_service_sante_2016 FLOAT,
        taux_activite_2017 FLOAT, 
        part_diplomes_2017 FLOAT,
        poids_economie_2015 FLOAT
        );
        """
)
try:
    cur.execute(command)
    print("Table Departements cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### POP ###########################################
print("Creation table Population_Regions") 
command = (
        """
        CREATE TABLE Population_Regions (
        num_region INT NOT NULL, 
        population FLOAT, 
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Population_regions cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    
print("Creation table Population_departements") 
command = (
        """
       CREATE TABLE Population_Departements (
       num_departement INT NOT NULL, 
       population FLOAT, 
       annee INT
       );
       """
)
try:
    cur.execute(command)
    print("Table Populations_departements cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### RECH_DEV ###########################################
print("Creation table Recherche_dev") 
command = (
        """
        CREATE TABLE Recherche_dev (
        num_region INT NOT NULL,
        Effort_recherche_dev FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Recherche_dev cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### TAUX_PAUVRETE ###########################################
print("Creation table Taux_pauvrete") 
command = (
        """
        CREATE TABLE Taux_pauvrete (
        libelle VARCHAR(100),
        pourcetage FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Taux_Pauvrete cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### ESPERANCE_VIE ###########################################
print("Creation table Esperance_vie") 
command = (
        """
        CREATE TABLE Esperances_vie (
        libelle VARCHAR(100),
        Esperance_vie_hommes FLOAT,
        Esperance_vie_femmes FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Esperance_vie cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### EMPLOI_DIMPLOMES ###########################################
print("Creation table Emploi_diplomes") 
command = (
        """
        CREATE TABLE Emploi_diplomes (
        libelle VARCHAR(100),
        Taux_emploi FLOAT,
        Part_jeunes_diplomes_18_25_ans FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Emploi_diplomes cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### INSERTION_JEUNES ###########################################
print("Creation table Insertion_jeunes") 
command = (
        """
        CREATE TABLE Insertion_jeunes (
        libelle VARCHAR(100),
        Pourcentage_jeunes_non_inseres FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Insertion_jeunes cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### ZONES_INONDABLES ###########################################
print("Creation table Zones_Inondables") 
command = (
        """
        CREATE TABLE Zones_inondables (
        libelle VARCHAR(100),
        Pourcetage_pop FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Zones_inondables cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

##################################### TRANSPORT ###########################################
print("Creation table Transport") 
command = (
        """
        CREATE TABLE Transport (
        libelle VARCHAR(100),
        Pourcentage_pop FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Transport cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

conn.commit()
cur.close()
conn.close()
print("\n### CONNEXION A POSTGRESQL FERMEE ###\n")