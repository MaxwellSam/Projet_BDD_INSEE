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

## Chargement des données dans le sql :
Regions = Regions.replace(np.nan, 'NULL')
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
    ) VALUES (%s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s)
    """ % (
    Regions.loc[i, "reg"], 
    Regions.loc[i, "ncc"], 
    Regions.loc[i, "libelle"], 
    Regions.loc[i, "var_2012_2017"], 
    Regions.loc[i, "var_nat"], 
    Regions.loc[i, "var_es"],  
    Regions.loc[i, "disp_2014"],
    Regions.loc[i, "eloignement_2016"],
    Regions.loc[i, "ta_2017"],
    Regions.loc[i, "dipl_2017"],
    Regions.loc[i, "poids_2015"],
    ))
    cur.execute(command)


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

# Chargement des données dans le sql :
Departements = Departements.replace(np.nan, 'NULL')
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
    ) VALUES (%s, %s, '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s)
    """ % (
    Departements.loc[i, "dep"],
    Departements.loc[i, "reg"], 
    Departements.loc[i, "ncc"], 
    Departements.loc[i, "libelle"], 
    Departements.loc[i, "var_2012_2017"], 
    Departements.loc[i, "var_nat"], 
    Departements.loc[i, "var_es"],  
    Departements.loc[i, "disp_2014"],
    Departements.loc[i, "eloignement_2016"],
    Departements.loc[i, "ta_2017"],
    Departements.loc[i, "dipl_2017"],
    Departements.loc[i, "poids_2015"]
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
for i in range(len(Pop_regions)):
    command = ("""
    INSERT INTO Population_Regions (num_region, population, annee) 
    VALUES (%s,%s,%s);
    """ % (
    Pop_region.loc[i,'numero'], 
    Pop_region.loc[i,'pop'], 
    Pop_region.loc[i,'annee']
    ))
    cur.execute(command)
    
print("Creation table Population_departements") 
command = ("""
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
    
# chargement des données dans le sql 
Pop_departements = Pop_departements.replace(np.nan, 'NULL')
for i in range(len(Pop_departements)):
    command = (
    """
    INSERT INTO Population_Departements (
    num_departement, 
    population, 
    annee
    ) VALUES (%s,%s,%s);
    """ % (
    Pop_departements.loc[i,'numero'], 
    Pop_departements.loc[i,'pop'], 
    Pop_departements.loc[i,'annee']
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
for i in range(len(Recherche_dev)):
    command = (
    """
    INSERT INTO Recherche_dev (num_region, Effort_recherche_dev, annee) 
    VALUES (%s,%s,%s,'%s','%s','%s','%s');
    """ % (Recherche_dev.loc[i,'numero'], Recherche_dev.loc[i,'effort'], Recherche_dev.loc[i,'annee'])
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
for i in range(len(Pauvrete)):
    command = (
    """
    INSERT INTO Taux_pauvrete (
    libelle,
    pauvrete,
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (Pauvrete.index[i], 
    Pauvrete.loc[i,'pauvrete'], 
    Pauvrete.loc[i,'annee'])
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
for i in range(len(Esperance_vie)):
    command = (
    """
    INSERT INTO Esperances_Vie (
    Esperance_vie_hommes,
    Esperance_vie_femmes,
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (Esperance_vie.index[i], 
    Esperance_vie.loc[i,'esp_vie_h'], 
    Esperance_vie.loc[i,'esp_vie_f']),
    Esperance_vie.loc[i,'annee']
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
for i in range(len(Emploi_diplome)):
    command = (
    """
    INSERT INTO Emploi_diplomes (
    Taux_emploi,
    Part_jeunes_diplomes_18_25_ans,
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (Esperance_vie.index[i], 
    Emploi_diplome.loc[i,'taux_emploi'], 
    Emploi_diplome.loc[i,'jeunes_diplomes']),
    Emploi_diplome.loc[i,'annee']
    )
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
for i in range(len(Insertion_jeunes)):
    command = (
    """
    INSERT INTO Insertion_jeunes (
    libelle,
    pourcentage_pop
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (Insertion_jeunes.index[i], 
    Insertion_jeunes.loc[i,'jeunes_non_inseres'],   
    Insertion_jeunes.loc[i,'annee']
    ))
    cur.execute(command)

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

# chargement des données dans le sql
Zones_inondables = Zones_inondables.replace(np.nan, 'NULL') 
for i in range(len(Zones_inondables)):
    command = (
    """
    INSERT INTO Zones_inondables (
    libelle,
    pourcentage_pop
    annee) 
    VALUES ('%s',%s,%s);
    """ 
    % (Zones_inondables.index[i], 
    Zones_inondables.loc[i,'zones_inondabes'],   
    Zones_inondables.loc[i,'annee']
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
for i in range(len(Transport)):
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
    % (Transport.index[i], 
    Transport.loc[i,'voiture'],
    Transport.loc[i,'commun'],
    Transport.loc[i,'autre'],   
    Transport.loc[i,'annee'])
    )
    cur.execute(command)

conn.commit()
cur.close()
conn.close()
print("\n### CONNEXION A POSTGRESQL FERMEE ###\n")