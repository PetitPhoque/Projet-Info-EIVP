#!/usr/bin/python
# -*- coding: utf-8 -*-



# Auteur : Renan COULANGE
# Date   : 29/11/2020

# Objet  : Lire le contenu d'un fichier de mesures (format CSV) passés en paramètre pour présenter des informations statistiques
#
# Paramètres en ligne commande
# fichierCSV : Nom du fichier CSV de mesure
# action : { 'display', 'statistique', 'humidex'}
# variable : { 'noise', 'temp', 'humidity', 'lum', 'co2' }
# start_date : 2020-01-01
# end-date : 2020-01-01

#  Exemple :
#  python BuildingMeasures.py c:/GIT/EIVP/post-32566-EIVP_KM.csv display temp 

#  Bilbiothèques à importer
# - sys
#   Pour les arguments
# - MathPlotLib
#   Pour les courbes
# - NumPy
#   Pour les courbes
# - Pandas
#   biblothèque pour ouvrir un fichier CSV et le manipuler




#function Usage
###################################################################
def Usage():
    print("Ligne de commande ")
    print("python BuildingMeasures.py <chemin fichier de données> <action> <variable> [<date début> <date fin>]")
    print("<chemin fichier de données> : Chemin du fichier de données CSV")
    print("<action>                    : Action à réaliser. { 'display', 'statistique', 'humidex'} ")
    print("<variable>                  : Variable à utliser pour 'display' ou 'statistique'. { 'noise', 'temp', 'humidity', 'lum', 'co2' } ")
    print("<date début> <date fin>     : Date de début et date de fin de la plage de données à extraire")
    print("Exemple")
    print("python BuildingMeasures.py c:/GIT/EIVP/post-32566-EIVP_KM.csv display temp ")


def preparerDonnées(indice, dfData, plt) :
    dfFilteredById = ( dfData[dfData['id'] == indice ])
    variables = dfFilteredById[[variable]]
    dates=dfFilteredById[['sent_at']]
    print(variables)
    plt.plot(dates,variables, label='id=' + str(indice))

# function affichage variable en fonction du temps
###################################################################
def displayVariable( variable, startDate, endDate ):
    dfFiltered =      ( dfMeasures[ dfMeasures['sent_at'] >= startDate ])
    dfSuperFiltered = ( dfFiltered[dfFiltered['sent_at'] < endDate ])    

    import matplotlib.pyplot as plt
    
    for i in range(1,6):
        preparerDonnées( i, dfSuperFiltered, plt )
    plt.show()


# function valeurs statistiques 
def statistique (variable):
    min = dfMeasures[variable].min()
    max = dfMeasures[variable].max()
    moyenne = dfMeasures[variable].mean()
    mediane = dfMeasures[variable].median()
    var = dfMeasures[variable].var()
    ecarttype = dfMeasures[variable].std() 
    print (min , max , ecarttype , moyenne , var , mediane)

# function calcul humidex
def humidexCalcul (variableTemp , variableHumidity):
    import math
    import numpy as np
    dfMeasures['humidex']=  dfMeasures[variableTemp] + 0.5555*(6.11*math.exp(5417.7530*(1/273.16-1/(273.15+(237.7*17.27*dfMeasures[variableTemp]/(237.7+dfMeasures[variableTemp])+np.log(dfMeasures[variableHumidity]))/(17.27-17.27*dfMeasures[variableTemp]/(237.7+dfMeasures[variableTemp])+np.log(dfMeasures[variableHumidity])))))-10)
    displayVariable("humidex", startDate, endDate)
    
#rose = (237.7*17.27*variableTemp/(237.7+variableTemp)+np.log(variableHumidity))/(17.27-17.27*variableTemp/(237.7+variableTemp)+np.log(variableHumidity))  
#humidex = variableTemp + 0.5555*(6.11*math.exp(5417.7530*(1/273.16-1/(273.15+rose)))-10) 
# function calcul indice de corrélation cople de variables


# Vérification des arguments
###################################################################
# premier argument : Fichier CSV
import sys

# 3 premier argument obligatoire
if len( sys.argv) < 4 :
    print( "Nombre d'argument incorrect" )
    Usage()
    exit()

CSVFile = sys.argv[1]
action = sys.argv[2]
variable = sys.argv[3]

# 3 premier argument obligatoire
if len( sys.argv) == 5 :
    print( "Nombre d'argument incorrect" )
    Usage()
    exit()

# argument facultatif
    
# Bibliothèque de gestion des dates
from datetime import datetime 

if len (sys.argv) == 6 :
    strStartDate  = sys.argv[4]
    strEndDate = sys.argv[5]

    startDate = datetime.fromisoformat( strStartDate )
    endDate = datetime.fromisoformat( strEndDate )
else:
    from zoneinfo import ZoneInfo
    startDate = datetime(1900, 1, 1, tzinfo= ZoneInfo("Europe/Paris"))
    endDate = datetime(2100, 12, 31, 23, 59, 59, 999999, tzinfo=ZoneInfo("Europe/Paris"))


# Run program
print ("Prêt à lire le fichier " + CSVFile + ".")
print ( "Pour la fonction " + action + ", la variable " + variable + ".")
print ( "Avec les date {startDate} et {endDate}")


#Lecture du fichier et chargement dans un DataFrame
import pandas as pd
#datetime.fromisoformat(
dfMeasures = pd.read_csv( CSVFile,  encoding="utf_8", delimiter=";", parse_dates=["sent_at"])
if action == 'display':
    # Vérification variable
    # { 'noise', 'temp', 'humidity', 'lum', 'co2' }
    displayVariable( variable, startDate, endDate )
elif action == 'statistique':
    statistique( variable ) 
elif action ==  'humidex':
    # Il faut ajouter une fonction qui va ajouter une colonne avec une valeur calculé nommé Humidex au DataFrame 
    # Appeler displayVariable( "Humidex", startDate, endDate ) 
    humidexCalcul(variable,dfMeasures["humidity"])
else:
    print( "L'argument action n'a pas une valeur attendu ! " + action )
    Usage()
    exit()





