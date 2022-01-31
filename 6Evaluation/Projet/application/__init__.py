#On importe la librairie Flask ce qui nous permet de lancer des applications flask
from flask import Flask

#On lance notre application flask
app = Flask(__name__)

#On importe notre fichier routes.py 
from application import routes