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

def removeDoublons (labelleList, listVariables):
    """
    retire les doublons, donc les regions qui sont aussi des départements et qui 
    induisent une répétition dans le dataframe. 
    :param labelleList: la liste des labelles pour la variable donnée
    :param listVariables: la liste des listes des variables 
    :type labelleList: list
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
    for j in range(len(labelleList)):
        if labelleList[j] not in newLabelles :
            newLabelles.append(labelleList[j])
            for k in range(len(listVariables)):
                print(newVariables[k])
                print(listVariables[k][i])
                newVariables[k].append(listVariables[k][j])      
    return {"labelles":newLabelles, "variables":newVariables}

def creatDFcommunDepReg (labelleReg, labelleDep, listVarReg, listVarDep, listAnnees):
    labelleList = flatList([labelleReg, labelleDep])
    listVariables = []
    for i in range(len(listVarDep)):
        listVariables.append(flatList([listVarReg[i], listVarDep[i]]))
    dataCleaned = removeDoublons(labelleList, listVariables)
    # creation des colones : 
    coloneLabelle = []
    comp = 0
    while comp < len(dataCleaned["variables"]):
        coloneLabelle.append(dataCleaned["labelles"])
        comp += 1
    coloneAnnee = creationColAnnee(len(coloneLabelle[0]), listAnnees)
    coloneLabelle = flatList(coloneLabelle)
    colVariable = flatList(dataCleaned["variables"])
    return {"labelle":coloneLabelle, "variable":colVariable, "annee":coloneAnnee}


# def creatDFcommunDepReg2 (labelleReg, labelleDep, VarRegParAnnee, VarDepParAnnee, listAnnees):
#     labelleList = flatList([labelleReg, labelleDep])
#     listVariables = []
#     for i in range(len(listAnnees)):
#         print("#",i)
#         print(len(VarRegParAnnee))
#         print("##", len(VarRegParAnnee[i]))
#         for j in range(len(VarRegParAnnee[i])):
#             listVariables.append(flatList([VarRegParAnnee[i][j], VarDepParAnnee[i][j]]))
#     dataCleaned = removeDoublons(labelleList, listVariables)
#     # creation des colones :
#     coloneLabelle = []
#     comp = 0
#     while comp < len(dataCleaned["variables"]):
#         coloneLabelle.append(dataCleaned["labelles"])
#         comp += 1
#     coloneAnnee = creationColAnnee(len(coloneLabelle[0]), listAnnees)
#     coloneLabelle = flatList(coloneLabelle)
#     return {"labelle":coloneLabelle, "variable":dataCleaned["variables"], "annee":coloneAnnee}
    
        
        
    
    