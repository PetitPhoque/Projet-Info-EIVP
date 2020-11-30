# -*- coding: utf-8 -*-

# Auteur : Renan COULANGE
# Date   : 29/11/2020

# Objet  : Lire le contenu d'un fichier de mesures (format CSV) passés en paramètre pour présenter des informations statistiques

import pandas as pd
from datetime import datetime 
from zoneinfo import zoneinfo

dfMeasures = pd.read_csv( "C:/Users/Renan/Documents/COURS EIVP/Projet Info EIVP/post-32566-EIVP_KM.csv",  encoding="utf_8", delimiter=";", parse_dates=["sent_at"])
variable = dfMeasures['temp']

#StartDate = 2019-08-11 00:00:00+00:00
#EndDate = 2019-08-14 00:00:00+00:00


def preparerDonnées(indice, dfData, plt) :
    dfFilteredById = ( dfData[dfData['id'] == indice ])
    variables = dfFilteredById[[variable]]
    dates=dfFilteredById[['sent_at']]
    print(variables)
    plt.plot(dates,variables, label='id=' + str(indice))

# function affichage variable en fonction du temps
###################################################################
def displayVariable( variable, startDate, endDate ):
    dfFiltered =      ( dfMeasures[ dfMeasures['sent_at'] >= datetime.startDate ])
    dfSuperFiltered = ( dfFiltered[dfFiltered['sent_at'] < datetime.endDate ])    

    import matplotlib.pyplot as plt
    

    preparerDonnées( 1, dfSuperFiltered, plt )
    preparerDonnées( 2, dfSuperFiltered , plt)
    preparerDonnées( 3, dfSuperFiltered , plt)
    preparerDonnées( 4, dfSuperFiltered, plt )

    plt.show()

displayVariable(variable,2019-08-11 , 2019-08-14 )