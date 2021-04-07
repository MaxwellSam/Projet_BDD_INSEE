#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
03/2021
Projet Insee

title : script1.py
authors : MAXWELL - GOMES - SOU
description : Etape de d'importation et de preparation des données et creation des tables
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

## Chargement des données dans le sql :
Regions = Regions.replace(np.nan, 'NULL')
Regions = Regions.replace(',', '.', regex=True)
for i in range(len(Regions)):
    command = ("""
    INSERT INTO Regions (
    num_region, 
    ncc, 
    libelle, 
    variation_pop_2012_2017, 
    variation_population_naturelle, 
    variation_population_entrees_sorties, 
    disparite_niveau_vie_2014, 
    eloignement_service_sante_2016, 
    taux_activite_2017,
    part_diplomes_2017,
    poids_economie_2015 
    ) VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s);
    """ % (
    Regions["reg"][i], 
    Regions["ncc"][i], 
    Regions["libelle"][i], 
    Regions["var_2012_2017"][i], 
    Regions["var_nat"][i], 
    Regions["var_es"][i],  
    Regions["disp_2014"][i],
    Regions["eloignement_2016"][i],
    Regions["ta_2017"][i],
    Regions["dipl_2017"][i],
    Regions["poids_2015"][i]
    ))
    cur.execute(command)

################################# DEPARTEMENT ########################################
print("Creation table Departement") 
command = (
        """
        CREATE TABLE Departements (
        num_dep VARCHAR(1000),
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

# Chargement des données dans le sql :
Departements = Departements.replace(np.nan, 'NULL')
Departements = Departements.replace(',', '.', regex=True)
Departements = Departements.replace({'\'':'\'\''}, regex=True)
for i in range(len(Departements)):
    command = ("""
    INSERT INTO Departements (
    num_dep,
    num_region, 
    ncc, 
    libelle, 
    variation_pop_2012_2017, 
    variation_population_naturelle, 
    variation_population_entrees_sorties, 
    disparite_niveau_vie_2014, 
    eloignement_service_sante_2016, 
    taux_activite_2017,
    part_diplomes_2017,
    poids_economie_2015 
    ) VALUES ('%s', %s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s);
    """ % (
    Departements["dep"][i],
    Departements["reg"][i], 
    Departements["ncc"][i], 
    Departements["libelle"][i], 
    Departements["var_2012_2017"][i], 
    Departements["var_nat"][i], 
    Departements["var_es"][i],  
    Departements["disp_2014"][i],
    Departements["eloignement_2016"][i],
    Departements["ta_2017"][i],
    Departements["dipl_2017"][i],
    Departements["poids_2015"][i]
    ))
    cur.execute(command)

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
    
# chargement des données dans le sql 
Pop_regions = Pop_regions.replace(np.nan, 'NULL')
Pop_regions = Pop_regions.replace(',', '.', regex=True)
Pop_regions["pop"] = Pop_regions["pop"].replace(' ', '', regex=True)
for i in range(len(Pop_regions)):
    command = ("""
    INSERT INTO Population_Regions (num_region, population, annee) 
    VALUES (%s,%s,%s);
    """ % (
    Pop_regions['numero'][i], 
    Pop_regions['pop'][i], 
    Pop_regions['annee'][i]
    ))
    cur.execute(command)
    
print("Creation table Population_departements") 
command = ("""
        CREATE TABLE Population_Departements (
        num_departement VARCHAR(1000), 
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
    
# chargement des données dans le sql 
Pop_departements = Pop_departements.replace(np.nan, 'NULL')
Pop_departements = Pop_departements.replace(',', '.', regex=True)
Pop_departements["pop"] = Pop_departements["pop"].replace(' ', '', regex=True)
for i in range(len(Pop_departements)):
    command = (
    """
    INSERT INTO Population_Departements (
    num_departement, 
    population, 
    annee
    ) VALUES ('%s',%s,%s);
    """ % (
    Pop_departements['numero'][i], 
    Pop_departements['pop'][i], 
    Pop_departements['annee'][i]
    ))
    cur.execute(command)

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

# chargement des données dans le sql
Recherche_dev = Recherche_dev.replace(np.nan, 'NULL') 
Recherche_dev = Recherche_dev.replace(',', '.', regex=True)
for i in range(len(Recherche_dev)):
    command = (
    """
    INSERT INTO Recherche_dev (
    num_region, 
    Effort_recherche_dev, 
    annee
    ) VALUES (%s,%s,%s);
    """ % (
    Recherche_dev['numero'][i], 
    Recherche_dev['effort'][i], 
    Recherche_dev['annee'][i])
    )
    cur.execute(command)

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

# chargement des données dans le sql
Pauvrete = Pauvrete.replace(np.nan, 'NULL') 
Pauvrete = Pauvrete.replace(',', '.', regex=True)
Pauvrete = Pauvrete.replace({'\'':'\'\''}, regex=True)
for i in range(len(Pauvrete)):
    libelle = Pauvrete.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Taux_pauvrete (
    libelle,
    pourcetage,
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (
    libelle, 
    Pauvrete['pauvrete'][i], 
    Pauvrete['annee'][i])
    )
    cur.execute(command)


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
    
# chargement des données dans le sql
Esperance_vie = Esperance_vie.replace(np.nan, 'NULL')
Esperance_vie = Esperance_vie.replace(',', '.', regex=True)
Esperance_vie = Esperance_vie.replace({'\'':'\'\''}, regex=True)
for i in range(len(Esperance_vie)):
    libelle = Esperance_vie.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Esperances_Vie (
    libelle,
    Esperance_vie_hommes,
    Esperance_vie_femmes,
    annee
    ) VALUES ('%s',%s,%s,%s);
    """ 
    % (
    libelle, 
    Esperance_vie['esp_vie_h'][i], 
    Esperance_vie['esp_vie_f'][i],
    Esperance_vie['annee'][i])
    )
    cur.execute(command)

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
    
# chargement des données dans le sql
Emploi_diplome = Emploi_diplome.replace(np.nan, 'NULL')
Emploi_diplome = Emploi_diplome.replace(',', '.', regex=True)
Emploi_diplome = Emploi_diplome.replace({'\'':'\'\''}, regex=True)
for i in range(len(Emploi_diplome)):
    libelle = Emploi_diplome.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Emploi_diplomes (
    libelle,
    Taux_emploi,
    Part_jeunes_diplomes_18_25_ans,
    annee
    ) VALUES ('%s',%s,%s, %s);
    """ 
    % (
    libelle, 
    Emploi_diplome['taux_emploi'][i], 
    Emploi_diplome['jeunes_diplomes'][i],
    Emploi_diplome['annee'][i]
    ))
    cur.execute(command)

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
    
# chargement des données dans le sql
Insertion_jeunes = Insertion_jeunes.replace(np.nan, 'NULL') 
Insertion_jeunes = Insertion_jeunes.replace(',', '.', regex=True)
Insertion_jeunes = Insertion_jeunes.replace({'\'':'\'\''}, regex=True)
for i in range(len(Insertion_jeunes)):
    libelle = Insertion_jeunes.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Insertion_jeunes (
    libelle,
    Pourcentage_jeunes_non_inseres,
    annee
    ) VALUES ('%s',%s,%s);
    """ 
    % (
    libelle, 
    Insertion_jeunes['jeunes_non_inseres'][i],   
    Insertion_jeunes['annee'][i]
    ))
    cur.execute(command)

##################################### ZONES_INONDABLES ###########################################
print("Creation table Zones_Inondables") 
command = (
        """
        CREATE TABLE Zones_inondables (
        libelle VARCHAR(100),
        Pourcentage_pop FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Zones_inondables cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# chargement des données dans le sql
Zones_inondables = Zones_inondables.replace(np.nan, 'NULL') 
Zones_inondables = Zones_inondables.replace(',', '.', regex=True)
Zones_inondables = Zones_inondables.replace({'\'':'\'\''}, regex=True)
for i in range(len(Zones_inondables)):
    libelle = Zones_inondables.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Zones_inondables (
    libelle,
    Pourcentage_pop,
    annee
    ) VALUES ('%s',%s,%s);
    """ 
    % (
    libelle, 
    Zones_inondables['zones_inondables'][i],   
    Zones_inondables['annee'][i]
    ))
    cur.execute(command)

##################################### TRANSPORT ###########################################
print("Creation table Transport") 
command = (
        """
        CREATE TABLE Transport (
        libelle VARCHAR(100),
        pourcentage_voiture FLOAT,
        pourcentage_transport_commun FLOAT,
        pourcentage_autre FLOAT,
        annee INT
        );
        """
)
try:
    cur.execute(command)
    print("Table Transport cree")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# chargement des données dans le sql
Transport = Transport.replace(np.nan, 'NULL')
Transport = Transport.replace(',', '.', regex=True)
Transport = Transport.replace({'\'':'\'\''}, regex=True) 
for i in range(len(Transport)):
    libelle = Transport.index[i].replace('\'','\'\'')
    command = (
    """
    INSERT INTO Transport (
    libelle,
    pourcentage_voiture,
    pourcentage_transport_commun,
    pourcentage_autre,
    annee) 
    VALUES ('%s',%s,%s,%s,%s);
    """ 
    % (
    libelle, 
    Transport['voiture'][i],
    Transport['commun'][i],
    Transport['autre'][i],   
    Transport['annee'][i])
    )
    cur.execute(command)

conn.commit()
cur.close()
conn.close()
print("\n### CONNEXION A POSTGRESQL FERMEE ###\n")