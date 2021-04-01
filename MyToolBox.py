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