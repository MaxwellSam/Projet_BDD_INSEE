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
    command = """
        SELECT DISTINCT libelle FROM Regions
    
    """

def displayDepartements():

def displaySpecificThemeSelectedDepartement():
    
def displayPauvreteSelectedDepartement():

# Prog Principal 
print("######## Programme de requetes SQL ##########\n######### base de donnée INSEE #########")
while(True):
    diplayMenu()
    rep = input("Entrer votre choix : ")
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
