#On importe app, render_template et pandas pour manipuler notre dataframe 
from application import app
from flask import render_template
import pandas as pd

#On crée nos pages web

#Celle ci renvoie à la page d'accueil
@app.route("/")
def base():
    return render_template("base.html")

#Celle ci à la page lien et contact
@app.route("/liens")
def liens():
    return render_template("liens.html")

#Celle ci à la page a propos de GameCash
@app.route("/propos")
def propos():
    return render_template("propos.html")

#Celle ci à la page Analyse des données
@app.route("/analyse")
def analyse():

#On manipule notre base de données
#On commence par lire notre fichier soso.json
    df = pd.read_json('soso.json')

#On supprime les colonnes que l'on ne désire pas
    del df['Garantie']
    del df['\nLanguage : ']
    del df['\nLangage : ']
    del df['\nMulti - Console : ']
    del df['\nMulti - Online : ']
    del df['\nNombre de joueurs : ']
    del df['\nLien :']
    del df['\nDéveloppeur : ']

#On renomme les colonnes
    df.columns = ['Nom', 'Plate_forme', 'Genre', 'Editeur', 'Prix', 'Date_de_sortie']

#On retire les Nan de notre dataframe
    dff=df.dropna()

#On retire les lignes avec les caractères qui nous gène dans nos colonnes    
    indexNames1 = dff[ dff['Date_de_sortie'] == '\n' ].index
    dff.drop(indexNames1 , inplace=True)
    indexNames2 = dff[ dff['Prix'] == '--,--' ].index
    dff.drop(indexNames2 , inplace=True)
    indexNames3 = dff[ dff['Editeur'] ==  ' -' ].index
    dff.drop(indexNames3 , inplace=True)
    indexNames4 = dff[ dff['Date_de_sortie'] == 'Non' ].index
    dff.drop(indexNames4 , inplace=True)

#On remplace les virgules par des points dans notre colonne prix
    dff['Prix'] = dff['Prix'].str.replace(',','.')

#On convertie la colonne prix en floattant afin de pouvoir faire des moyennes dans les prix
    dff['Prix'] = dff['Prix'].astype(float)

#On crée des dataframes. Chaque dataframe est composés seulement de jeu d'une même console
    dfXboxX = dff[dff['Plate_forme'] == "XBOX séries X"] 
    dfVita = dff[dff['Plate_forme'] == "Playstation Vita"]
    dfSwitch = dff[dff['Plate_forme'] == "Switch"] 
    dfXboxOne	= dff[dff['Plate_forme'] == "Xbox One"] 
    dfPlaystation5 = dff[dff['Plate_forme'] == "Playstation 5"] 
    dfWiiU = dff[dff['Plate_forme'] == "Wii U"] 
    dfWii = dff[dff['Plate_forme'] == "Wii"] 
    dfXbox360 = dff[dff['Plate_forme'] == "Xbox 360"]
    dfDS = dff[dff['Plate_forme'] == "DS"]  
    dfPlaystationPortable = dff[dff['Plate_forme'] == "Playstation Portable"]  
    dfJeuxPC = dff[dff['Plate_forme'] == "Jeux PC"] 
    dfPlaystation4 = dff[dff['Plate_forme'] == "Playstation 4 "]
    dfPlaystation3 = dff[dff['Plate_forme'] == "Playstation 3"]  
    df3DS = dff[dff['Plate_forme'] == "3DS"]
    
#On crée notre liste qui contient le nombre de jeu par console et la moyenne de prix d'un jeu par console    
    L1= [len(dfXboxX), len(dfVita), len(dfSwitch), len(dfXboxOne), len(dfPlaystation5), len(dfWiiU), len(dfWii), len(dfXbox360), len(dfDS), len(dfPlaystationPortable), len(dfJeuxPC), len(dfPlaystation4), len(dfPlaystation3), len(df3DS) ]

    L2= [dfXboxX.mean(), dfVita.mean(), dfSwitch.mean(), dfXboxOne.mean(), dfPlaystation5.mean(), dfWiiU.mean(), dfWii.mean(), dfXbox360.mean(), dfDS.mean(), dfPlaystationPortable.mean(), dfJeuxPC.mean(), dfPlaystation4.mean(), dfPlaystation3.mean(), df3DS.mean() ]


#De même pour les éditeurs  
    dfElectronicArts = dff[dff['Editeur'] == "Electronic Arts"] 
    dfBandaiNamco = dff[dff['Editeur'] == "Bandai Namco"]
    dfActivision = dff[dff['Editeur'] == "Activision"] 
    dfUbisoft	= dff[dff['Editeur'] == "Ubisoft"] 
    dfSquareEnix = dff[dff['Editeur'] == "Square Enix"] 
    dfSony = dff[dff['Editeur'] == "Sony"] 
    dfSega = dff[dff['Editeur'] == "Sega"] 
    dfRockstar = dff[dff['Editeur'] == "Rockstar"]
    dfNintendo = dff[dff['Editeur'] == "Nintendo"]  
    dfMicrosoft = dff[dff['Editeur'] == "Microsoft"]  
    dfLevel5	 = dff[dff['Editeur'] == "Level-5"] 
    dfKonami = dff[dff['Editeur'] == "Konami"]
    dfEASports = dff[dff['Editeur'] == "EA Sports"]  
    dfCapcom = dff[dff['Editeur'] == "Capcom"]

    L3= [len(dfElectronicArts), len(dfBandaiNamco), len(dfActivision), len(dfUbisoft), len(dfSquareEnix), len(dfSony), len(dfSega), len(dfRockstar), len(dfNintendo), len(dfMicrosoft), len(dfLevel5), len(dfKonami), len(dfEASports), len(dfCapcom) ]

    L4= [dfElectronicArts.mean(), dfBandaiNamco.mean(), dfActivision.mean(), dfUbisoft.mean(), dfSquareEnix.mean(), dfSony.mean(), dfSega.mean(), dfRockstar.mean(), dfNintendo.mean(), dfMicrosoft.mean(), dfLevel5.mean(), dfKonami.mean(), dfEASports.mean(), dfCapcom.mean() ]


#On ajoute une colonne date et en trie les jeux par années en créant des dataframes pour chaque année 
    dff['date'] = [x[6:] for x in dff['Date_de_sortie']]
    df1999 = dff[dff['date'] == "1999"] 
    df2002 = dff[dff['date'] == "2002"]
    df2003 = dff[dff['date'] == "2003"] 
    df2004	= dff[dff['date'] == "2004"] 
    df2005 = dff[dff['date'] == "2005"] 
    df2006 = dff[dff['date'] == "2006"] 
    df2007 = dff[dff['date'] == "2007"] 
    df2008 = dff[dff['date'] == "2008"]
    df2009 = dff[dff['date'] == "2009"]  
    df2010 = dff[dff['date'] == "2010"]  
    df2011 = dff[dff['date'] == "2011"] 
    df2012 = dff[dff['date'] == "2012"]
    df2013 = dff[dff['date'] == "2013"]  
    df2014 = dff[dff['date'] == "2014"] 
    df2015 = dff[dff['date'] == "2015"]
    df2016 = dff[dff['date'] == "2016"]  
    df2017 = dff[dff['date'] == "2017"]  
    df2018	= dff[dff['date'] == "2018"] 
    df2019 = dff[dff['date'] == "2019"]
    df2020 = dff[dff['date'] == "2020"]  
    df2021 = dff[dff['date'] == "2021"]

#On crée une liste dans laquelle on a le nombre de jeu par année
    L5= [len(df1999), len(df2002), len(df2003), len(df2004), len(df2005), len(df2006), len(df2007), len(df2008), len(df2009), len(df2010), len(df2011), len(df2012), len(df2013), len(df2014) , len(df2015), len(df2016), len(df2017), len(df2018), len(df2019), len(df2020), len(df2021)]


#Toutes ces étapes nous permettent de récuperer les listes que nous allons mettre dans la partie data de nos graphes 

#On renvoie vers la page index (page analyse des données)
    return render_template("analyse.html", title = "Home", L1=L1, L2=L2, L3=L3, L4=L4, L5=L5)

