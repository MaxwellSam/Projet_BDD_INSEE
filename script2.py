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
    print("\t0. Quitter le programme")
    

def displayRegions(cur):
    command = "SELECT DISTINCT libelle FROM Regions"
    cur.execute(command)
    res : cur.fetchall()
    print("*** liste des Régions :")
    for i in res: 
        print("* ", i)
    print("\n")
    
def displayDepartements(cur):
    command = "SELECT libelle FROM Departements"
    cur.execute(command)
    res = cur.fetchall()
    print("*** liste des Départements :")
    for i in res: 
        print("* ", i)
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
    print("\n** departement : ", libelle, "\n** Informations sociales")
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
    SELECT pourcentage_voiture, pourcentage_transport_commun, pourcentage_transport_autre, annee 
    FROM Transport WHERE libelle = '%s';
    """ % libelle)
    cur.execute(command)
    Transport = cur.fetchall()
    ## Affichage : 
    print("\n** departement : ", libelle, "\n** Informations Economiques")
    print("* taux d'activité en 2017 : ", taux_act)
    print("* part des diplomes en 2017 : ", part_dip)
    print("* poids de l'économie en 2015 : ", p_eco)
    for i in emp_dip :
        print("* taux d'emploi en ", i[2], " : ", i[0] "%")
        print("* part des jeunes diplomés de 18 à 25 ans en ", i[2], " : ", i[1] "%")
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
    command = "SELECT DISTINCT libelle, num_departement FROM Departements"
    cur.execute(command)
    res : cur.fetchall()
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
        theme = input("Choisir le theme (economie[1]/social[2]): ")
        if theme == 1 or theme == 2:
            break
        print("Erreur : Vous devez choisir entre [1] et [2]")
    
    diplayInfoDepartement(cur, theme, dep)

def displayPauvreteSelectedDepartement():
    """
    Affiche le nombre d'habitants sous le seuil de pauvreté en 2018
    """
    command = "SELECT DISTINCT libelle, num_departement FROM Departements"
    cur.execute(command)
    res : cur.fetchall()
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
    command = ("""
    SELECT Departements.libelle, Population_departements.population, Taux_pauvrete.pourcetage 
        FROM Population_departements INNER JOIN Departements 
        ON Departements.num_dep = Population_departements.num_departement 
        INNER JOIN Taux_pauvrete ON Taux_pauvrete.libelle = Departements.libelle 
        WHERE Taux_pauvrete.annee = 2018 AND Population_departements.annee = 2018 
        AND Departements.num_dep = '%s';
    """ % (dep))
    cur.execute(command)
    res = cur.fetchall()
    # calucle du nombre de personne sous le seuil de pauvreté :
    pop = res[1]*res[2]
    print("\n**", res[0],"\n* Nombre d'habitants sous le seuil de pauvreté en 2018 : ", pop, "\n")

# Prog Principal 
print("######## Programme de requetes SQL ##########\n######### base de donnée INSEE #########")
while(True):
    diplayMenu()
    rep = input("\t\tMenu\nEntrer votre choix : ")
    if rep == 1 : 
        displayRegions()
    if rep == 2 : 
        displayDepartements()
    if rep == 3 : 
        displaySelectedRegion()
    if rep == 4 : 
        displaySpecificThemeSelectedDepartement()
    if rep == 5 : 
        displayPauvreteSelectedDepartement
    if rep == 0 : 
        sys.exit()
    else : 
        print("Erreur choix : choisir parmis les numeros possibles")
