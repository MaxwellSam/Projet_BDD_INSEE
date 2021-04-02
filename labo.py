import MyToolBox as tool

col = tool.creationColAnnee(5, [2021, 2017, 2020])
print(col)
    
l = tool.flatList([[4,5,6],[7,8]])
print(l)

#exec(open("script.py").read())

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
    
listL = ["A","B","C","A","D"]
listV = [[1,2,3,1,4],[11,22,33,11,44],[111,222,333,111,444]]

lcleaned = removeDoublons(listL, listV)
print(lcleaned)


