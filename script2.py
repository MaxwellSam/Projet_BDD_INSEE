#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
04/2021
Projet Insee

title : script1.py
authors : MAXWELL - GOMES - SOU
description : Etape de d'importation et de preparation des données et creation des tables
"""
import pandas as pd
import psycopg2
import psycopg2.extras
import sys

print("\n#### Projet INSEE // M1S2 // BDD ####")
print("############# SCRIPT 2 ##############\n")

print('Connexion a la base de donnees...')
USERNAME="smaxwell"
PASSWORD="SQLsam"
try:
    conn = psycopg2.connect(host='pgsql',dbname=USERNAME, user=USERNAME, password=PASSWORD)
except Exception as e : 
    exit("Connexion impossible a la base de donnees: "+str(e))

print('Connecte a la base de donnees')

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Menu 
# Affichier liste region 
# Afficher liste Departement 
# Demander utilisateur region et afficher info region 
# demander utilisateur departement et theme (so, eco) et aff données 
# demander utilisateur departement et aff combien hab sous le seuil de pauv 2018

def displayMenu():
    """
    Affiche le menu à l'utilisateur avec les choix de requetes sql possibles. 
    """
    print("\nQue voulez vous faire :\n")
    print("\t1. Afficher la liste des Régions")
    print("\t2. Afficher la liste des Départements")
    print("\t3. Afficher les informations d'une Région")
    print("\t4. Afficher les informations spécifiques d'un départmement")
    print("\t5. Afficher la part des habitants vivant sous le seuil de pauvreté d'un département")
    print("\t0. Quitter le programme\n")
    

def displayRegions(cur):
    command = "SELECT DISTINCT libelle FROM Regions"
    cur.execute(command)
    res = cur.fetchall()
    print("\n*** liste des Régions :")
    for i in res: 
        print("* ", i[0])
    print("\n")
    
def displayDepartements(cur):
    command = "SELECT libelle FROM Departements"
    cur.execute(command)
    res = cur.fetchall()
    print("\n*** liste des Départements :")
    for i in res: 
        print("* ", i[0])
    print("\n")

def displaySelectedRegion(cur): 
    command = "SELECT DISTINCT libelle, num_region FROM Regions;"
    cur.execute(command)
    res = cur.fetchall()
    print("choisir une Région")
    print("*** liste des Régions :")
    listNumReg = [] # pour la vérification du choix de l'utilisateur
    for i in res: 
        listNumReg.append(i[1])
        print("* ", i[0], " - ", i[1])
    print("\n")
    while(True) :
        reg = int(input("Entrer numero de region : "))
        if reg in listNumReg : 
            break
        print("Erreur : Vous devez choisir un numero de région valide")
    # Infos de la table Regions
    command = ("""
    SELECT DISTINCT * FROM Regions WHERE num_region = %s;
    """ % (reg))
    cur.execute(command)
    res = cur.fetchall()
    res = res[0]
    libelle = res[2]
    print("*** Information ", libelle)
    print("* numero de région : ", res[0])
    print("* variation annuelle moyenne de la population entre 2012 et 2017 : ", res[3], " %")
    print("* variation anuelle moyenne de la population due au solde naturel : ", res[4], " %")
    print("* variation annuelle moyenne due au solde apparent des entrées et des sorties : ", res[5], " %")
    print("* diparité u niveau de vie en 2014 : ", res[6], " %")
    print("* part de la population éloignées à plus de 7 km d'un service de santé en 2016 : ", res[7], " %")
    print("* taux d'activité en 2017 : ", res[8], " %")
    print("* part des diplômés en 2017 : ", res[9], " %")
    print("* poids de l'économie en 2015 : ", res[10], " %")
    # Infos de la table Population
    command = ("""
    SELECT DISTINCT * FROM Population_regions WHERE num_region = %s;
    """ % (reg))
    cur.execute(command)
    res = cur.fetchall()
    print("** Population :")
    for i in res : 
        print("* en ", i[2], " : ", i[1])
    # Infos de la table Rech_dev :
    command = ("""
    SELECT DISTINCT * FROM Recherche_dev WHERE num_region = %s;
    """ % (reg))
    cur.execute(command)
    res = cur.fetchall()
    print("** Effort de recherche et de développement :")
    for i in res : 
        print("* en ", i[2], " : ", i[1])
    # Infos de la table Taux_pauvrete :
    command = ("""
    SELECT DISTINCT * FROM Taux_pauvrete WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Taux de pauvreté :")
    for i in res : 
        print("* en ", i[2], " : ", i[1])
    # Infos de la table Esperance_vie :
    command = ("""
    SELECT DISTINCT * FROM Esperances_vie WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Esperance de vie :")
    for i in res : 
        print("* en ", i[3], " : homme ", i[1], " / femme ", i[2], " ans")
    # Infos de la table Emploi_diplomes :
    command = ("""
    SELECT DISTINCT * FROM Emploi_diplomes WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Taux d'emploi et de jeunes diplomés de 18 à 25 ans :")
    for i in res : 
        print("* en ", i[3], " : emploi ", i[1], " / jeunes diplômés ", i[2], " %")
    # Infos de la table Insertion_jeunes :
    command = ("""
    SELECT DISTINCT * FROM Insertion_jeunes WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Insertion des jeunes :")
    for i in res : 
        print("* en ", i[2], " : ", i[1])
    # Infos de la table Insertion_jeunes :
    command = ("""
    SELECT DISTINCT * FROM Zones_inondables WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Part des habitants en zone inondables :")
    for i in res : 
        print("* en ", i[2], " : ", i[1])
    # Infos de la table Transport :
    command = ("""
    SELECT DISTINCT * FROM Transport WHERE libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print("** Part des types de transport utilisés pour aller au travail :")
    for i in res : 
        print("* en ", i[4], " : \n\t- Voiture ", i[1], "\n\t - Transport en commun ", i[2], "\n\t - autre ", i[3])
    print("\n")
    

def diplayDepartementSocial (cur, numDep) : 
    """
    Affiche les informations économiques du département
    :param cur:
    :param numDep: numero du département
    :type numDep: string
    """
    # info table Region
    command = ("""
    SELECT libelle, disparite_niveau_vie_2014, eloignement_service_sante_2016 
    FROM Departements WHERE num_dep = '%s';
    """ % (numDep))
    cur.execute(command)
    res = cur.fetchall()
    res = res[0]
    libelle = res[0]
    diparite = res[1]
    eloignement = res[2]
    # info table Esperances_vie
    command = ("""
    SELECT esperance_vie_hommes, esperance_vie_femmes, annee 
    FROM Esperances_vie WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    esperance_vie = cur.fetchall()
    # info table Taux_pauvrete
    command = ("""
    SELECT pourcentage, annee 
    FROM Taux_pauvrete WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    Taux_pauvrete = cur.fetchall()
    # info table Insertion_jeunes
    command = ("""
    SELECT pourcentage_jeunes_non_inseres, annee 
    FROM Insertion_jeunes WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    non_insertion = cur.fetchall()
    # info table Zones_inondables
    command = ("""
    SELECT pourcentage_pop, annee 
    FROM Zones_inondables WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    part_z_inond = cur.fetchall()
    ## Affichage : 
    print("\n*** Departement : ", libelle, "\n** Informations sociales")
    print("* disparite du niveau de vie en 2014 : ", diparite)
    print("* part de la population eloignées des services de santé en 2016 : ", eloignement)
    for i in esperance_vie :
        print("* esperance de vie en ", i[2], " : hommes ", i[0], " / femmes ", i[1], " ans")
    for j in Taux_pauvrete : 
        print("* taux de pauvreté en ", j[1], " : ", j[0], "%")
    for k in non_insertion :
        print("* part des jeunes non insérés en ", k[1], " : ", k[0], "%")
    for l in part_z_inond :
         print("* part des habitants en zones inondables en ", l[1], " : ", l[0], "%")
    print("\n")

def diplayDepartementEco (cur, numDep) : 
    """
    Affiche les informations économiques du département
    :param cur:
    :param numDep: numero du département
    :type numDep: string
    """
    # info table Region
    command = ("""
    SELECT libelle, taux_activite_2017, part_diplomes_2017, poids_economie_2015 
    FROM Departements WHERE num_dep = '%s';
    """ % (numDep))
    cur.execute(command)
    res = cur.fetchall()
    print(res)
    res = res[0]
    libelle = res[0]
    taux_act = res[1]
    part_dip = res[2]
    p_eco = res[3]
    # info table Emploi_diplomes
    command = ("""
    SELECT taux_emploi, part_jeunes_diplomes_18_25_ans, annee 
    FROM Emploi_diplomes WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    emp_dip = cur.fetchall()
    # info table Transport
    command = ("""
    SELECT pourcentage_voiture, pourcentage_transport_commun, pourcentage_autre, annee 
    FROM Transport WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    Transport = cur.fetchall()
    ## Affichage : 
    print("\n*** Departement : ", libelle, "\n** Informations Economiques")
    print("* taux d'activité en 2017 : ", taux_act)
    print("* part des diplomes en 2017 : ", part_dip)
    print("* poids de l'économie en 2015 : ", p_eco)
    for i in emp_dip :
        print("* taux d'emploi en ", i[2], " : ", i[0], "%")
        print("* part des jeunes diplomés de 18 à 25 ans en ", i[2], " : ", i[1], "%")
    for j in Transport : 
        print("* part des types de transport pour se rendre au travail en ", j[3], " : ")
        print("\t** ", j[0], "% voiture\n\t** ", j[1], "% tansport en commun\n\t** ", j[2], "% autre")
    print("\n")
    
def diplayInfoDepartement(cur, theme, numDep):
    """
    Affiche les information d'un theme donné pour département donné.
    :param cur:
    :param theme: indice du theme selectionné
    :param numDep: numero du département
    :type theme: int
    :type numDep: string 
    """
    if theme == 2: # Social
        diplayDepartementSocial (cur, numDep) # Affiche les info sociales
    else : 
        diplayDepartementEco (cur, numDep) # Affiche les info Economiques
            
            
def displaySpecificThemeSelectedDepartement(cur):
    """
    Affiche les informations d'un département selectionné par l'utilisateur sur un theme choisit :
    [1] Economie
    [2] social
    """
    command = "SELECT DISTINCT libelle, num_dep FROM Departements;"
    cur.execute(command)
    res = cur.fetchall()
    print(res)
    print("choisir un département")
    print("*** liste des Départements :")
    listNumDep = [] # pour la vérification du choix de l'utilisateur
    for i in res: 
        listNumDep.append(i[1])
        print("* ", i[0], " - ", i[1])
    print("\n")
    while(True) :
        dep = input("Entrer numero de departement : ")
        if dep in listNumDep : 
            break
        print("Erreur : Vous devez choisir un numero de département valide")
    while(True) : 
        theme = int(input("Choisir le theme (economie[1]/social[2]): "))
        if theme == 1 or theme == 2:
            break
        print("Erreur : Vous devez choisir entre [1] et [2]")
    
    diplayInfoDepartement(cur, theme, dep)

def displayPauvreteSelectedDepartement(cur):
    """
    Affiche le nombre d'habitants sous le seuil de pauvreté en 2018
    """
    command = "SELECT DISTINCT libelle, num_dep FROM Departements;"
    cur.execute(command)
    res = cur.fetchall()
    print("choisir un département")
    print("*** liste des Départements :")
    listNumDep = [] # pour la vérification du choix de l'utilisateur
    for i in res: 
        listNumDep.append(i[1])
        print("* ", i[0], " - ", i[1])
    print("\n")
    while(True) :
        dep = input("Entrer numero de departement : ")
        if dep in listNumDep : 
            break
        print("Erreur : Vous devez choisir un numero de département valide")
    command = ("SELECT libelle FROM Departements WHERE num_dep = '%s';" % (dep))
    cur.execute(command)
    libelle = cur.fetchone()
    libelle = libelle[0]
    print(libelle)
    command = ("""
    SELECT Departements.libelle, Population_departements.population, Taux_pauvrete.pourcentage 
    FROM Population_departements INNER JOIN Departements 
    ON Departements.num_dep = Population_departements.num_dep 
    INNER JOIN Taux_pauvrete ON Taux_pauvrete.libelle = Departements.libelle 
    WHERE Taux_pauvrete.annee = 2018 AND Population_departements.annee = 2018 
    AND Departements.libelle = '%s';
    """ % (libelle))
    cur.execute(command)
    res = cur.fetchall()
    print(res)
    # calucle du nombre de personne sous le seuil de pauvreté :
    pop = res[1]*(res[2]/100)
    print("\n**", res[0],"\n* Nombre d'habitants sous le seuil de pauvreté en 2018 : ", pop, "\n")

# Prog Principal 
print("######## Programme de requetes SQL ##########\n######### base de donnée INSEE #########")

print("### Reponses aux questions : ")

# Q1 : 
command = """
SELECT DISTINCT libelle FROM Taux_pauvrete WHERE annee = 2018 
AND pourcentage > 18 AND libelle in (SELECT libelle 
FROM Departements);
"""
cur.execute(command)
res = cur.fetchall()
print("\nQ1) Departement aux taux de pauvreté > 18 % en 2018 :")
for i in res : 
    print("- ", i[0])

# Q2 : 
command = """
SELECT DISTINCT libelle FROM Departements WHERE disparite_niveau_vie_2014 >= 3.5 AND libelle in (SELECT libelle 
FROM Departements);
"""
cur.execute(command)
res = cur.fetchall()
print("\nQ2) départements dont la région a une disparité de niveau de vie supérieure ou égale à 3,5 en 2014 :")
for i in res : 
    print("- ", i[0])

# Q3 : 
command = """
SELECT DISTINCT libelle, poids_economie_2015 FROM Departements ORDER BY poids_economie_2015 DESC LIMIT 5;
"""
cur.execute(command)
res = cur.fetchall()
print("\nQ3) 5 départements avec le plus grand poids de l’économie sociale dans les emplois salariés en 2015 :")
for i in res : 
    print("- ", i[0])

# Q4 : 
command = """
SELECT DISTINCT r.libelle FROM Departements AS d INNER JOIN Regions as r ON r.num_region = d.num_region WHERE d.libelle in (SELECT libelle FROM Departements ORDER BY eloignement_service_sante_2016 DESC LIMIT 1);
"""
cur.execute(command)
res = cur.fetchall()
print("\nQ4) Dans quelle région se trouve le département ayant la plus grande part de la population éloignée de plus de 7 mn des services de santé de proximité en 2016 ?")
for i in res : 
    print("- ", i[0])

# Q5 : 
# command = """
# SELECT DISTINCT libelle FROM Departements WHERE libelle in (SELECT libelle FROM Esperances_vie WHERE Esperance_vie_hommes AND annee = 2015 > Esperance_vie_hommes AND annee = 2019)
# """
# cur.execute(command)
# res = cur.fetchall()
# print("\nQ5) Dans quelle région se trouve le département ayant la plus grande part de la population éloignée de plus de 7 mn des services de santé de proximité en 2016 ?")
# for i in res :
#     print("- ", i[0])

while(True):
    displayMenu()
    rep = int(input("Entrer votre choix : "))
    if rep == 1 : 
        displayRegions(cur)
        pass
    if rep == 2 : 
        displayDepartements(cur)
        pass
    if rep == 3 : 
        displaySelectedRegion(cur)
        pass
    if rep == 4 : 
        displaySpecificThemeSelectedDepartement(cur)
        pass
    if rep == 5 : 
        displayPauvreteSelectedDepartement(cur)
        pass
    if rep == 0 : 
        sys.exit()
    if rep not in [1,2,3,4,5,0]: 
        print("Erreur choix : choisir parmis les numeros possibles")
