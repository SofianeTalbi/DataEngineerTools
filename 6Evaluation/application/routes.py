from re import template
from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route("/")
def base():
    return render_template("base.html")

@app.route("/liens")
def liens():
    return render_template("liens.html")

@app.route("/propos")
def propos():
    return render_template("propos.html")

@app.route("/index")
def index():

    df = pd.read_json('soso.json')
    del df['Garantie']
    del df['\nLanguage : ']
    del df['\nLangage : ']
    del df['\nMulti - Console : ']
    del df['\nMulti - Online : ']
    del df['\nNombre de joueurs : ']
    del df['\nLien :']
    del df['\nDéveloppeur : ']
    df.columns = ['Nom', 'Plate_forme', 'Genre', 'Editeur', 'Prix', 'Date_de_sortie']
    dff=df.dropna()
    indexNames1 = dff[ dff['Date_de_sortie'] == '\n' ].index
    dff.drop(indexNames1 , inplace=True)
    indexNames2 = dff[ dff['Prix'] == '--,--' ].index
    dff.drop(indexNames2 , inplace=True)
    indexNames3 = dff[ dff['Editeur'] ==  ' -' ].index
    dff.drop(indexNames3 , inplace=True)
    indexNames4 = dff[ dff['Date_de_sortie'] == 'Non' ].index
    dff.drop(indexNames4 , inplace=True)
    dff['Prix'] = dff['Prix'].str.replace(',','.')
    dff['Prix'] = dff['Prix'].astype(float)
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

    return render_template("index.html", title = "Home")

