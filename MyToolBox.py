#! /usr/bin/env python3
# coding: utf-8
""""
BDD 
03/2021
Projet Insee

title : MyToolBox.py
authors : MAXWELL - GOMES - SOU
description : Fonctions outils pour la construction des dataframes 
"""
# Action sur les listes : 

def flatList(list): 
    """
    permet de joindre les listes d'une liste ensemble
    :param list: liste de listes
    :type list: list
    :return: list finale 
    :rtype: list
    """
    flat=[]
    for i in list:
      for j in i:
        flat.append(j)
    return flat
    
l = flatList([[4,5,6],[7,8]])

def creationColAnnee (n, listeAnnees):
    """
    Génère la colone des années
    :param n: nombre de fois que doit être généré l'année
    :param listeAnnees: liste des annees qui doivent être générées n fois chacunes
    :type n: int
    :type listeAnnees: list
    :return colAnnee: la colonne des annees
    :rtype: list
    """
    i = 0
    j = 0
    colAnnee = []
    while i < len(listeAnnees):
        colAnnee.append([])
        i+=1
    while j < n :
        for i in range(len(listeAnnees)) :
            colAnnee[i].append(listeAnnees[i])
        j +=1
    colAnnee = flatList(colAnnee)
    return colAnnee

def removeDoublons (libelleList, listVariables):
    """
    retire les doublons, donc les regions qui sont aussi des départements et qui 
    induisent une répétition dans le dataframe. 
    :param libelleList: la liste des libelles pour la variable donnée
    :param listVariables: la liste des listes des variables 
    :type libelleList: list
    :type listVariables: list
    :return dataCleaned: les nouvelles listes nétoyées
    :rtype: dict 
    """
    newLabelles = []
    newVariables = []
    i=0
    while i < len(listVariables):
        newVariables.append([])
        i+=1
    for j in range(len(libelleList)):
        if libelleList[j] not in newLabelles :
            newLabelles.append(libelleList[j])
            for k in range(len(listVariables)):
                newVariables[k].append(listVariables[k][j])      
    return {"libelles":newLabelles, "variables":newVariables}

def creatDFcommunDepReg (libelleReg, libelleDep, listVarReg, listVarDep, listAnnees):
    libelleList = flatList([libelleReg, libelleDep])
    listVariables = []
    for i in range(len(listVarDep)):
        listVariables.append(flatList([listVarReg[i], listVarDep[i]]))
    dataCleaned = removeDoublons(libelleList, listVariables)
    # creation des colones :
    coloneLabelle = []
    comp = 0
    while comp < len(dataCleaned["variables"]):
        coloneLabelle.append(dataCleaned["libelles"])
        comp += 1
    coloneAnnee = creationColAnnee(len(coloneLabelle[0]), listAnnees)
    coloneLabelle = flatList(coloneLabelle)
    colVariable = flatList(dataCleaned["variables"])
    return {"libelle":coloneLabelle, "variable":colVariable, "annee":coloneAnnee}

def creatListYear (n, year):
    """
    produit une liste contenant n fois le chiffre year
    :param n: le nombre d'éléments que doit contenir la liste
    :param year: l'élément qui doit être répété dans la liste
    :type n: int
    :type year: int
    :return listYear: la liste de n fois year
    :rtype: list
    """
    comp = 0
    listYear = []
    while comp < n :
        listYear.append(year) 
    return listYear



        
        
    
    