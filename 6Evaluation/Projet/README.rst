Projet DataEngineering
=======
Contexte
----------

Cette année, dans le cadre de l’évaluation de l’unité Data Engineering, il nous a été demandé de créer une application web en nous basant sur le package Flask.

Notre application devait récupérer des données sur le web. Soit des données Open Data soit des données scrapées grâce à ce que nous avons appris durant ce cours. Notre devait afficher les données de façon optimale avec la mise en place d’un moteur de recherche, de graphiques, etc. On devait également utiliser une ou plusieurs bases de données abordées dans ce cours et enfin fournir une documentation technique et fonctionnelle.

C’est donc ce qu’on a fait.  Pour que notre application puisse être déployée partout, nous avons utilisé Docker. Nous avons récupéré les données scrappées du site web Gamecash. Vous pouvez ainsi visualiser les données à travers les graphiques en utilisant le moteur de recherche ou en naviguant sur notre application.

En ce qui concerne le site scrapé, gamecash.fr est un site de commerce électronique français crée en 2003 sur lequel sont vendus des jeux vidéo et films d'occasion. Nous avons choisis ce site car nous avions déjà réalisé des achats de jeux videos dessus. Nous voulions en savoir plus sur la vente des jeux vidéos.

User guide
----------
-> Tout d'abord, il faut que vous cloniez le projet en effectuant la commande suivante sur votre terminal: 

        git clone https://github.com/SofianeTalbi/DataEngineerTools.git
	
-> Veuillez, avant de continuer, taper les commandes suivantes sur votre terminal:

pip install flask

pip install pandas

pip install pd
				
-> Ensuite, toujours sur votre terminal, il faut que vous fassiez:

cd DataEngineerTools

-> puis

cd 6Evaluation

-> puis

cd Projet

-> Enfin vous pourrez lancer l'application Web en tapant toujours sur votre terminal:

python "run.py"

-> Vous pouvez ensuite visualiser notre application en tapant sur votre moteur de recherche:

http://127.0.0.1:5000/

*2eme méthode (avec Docker)*

-> Tout d'abord, vous devez avoir Docker sur votre machine

-> Aprés que vous vous soyez mis dans le dossier du projet, lancez la commande suivante:

docker-compose up

-> Vous pouvez acceder à notre application web en tapant sur votre navigateur:

localhost:5001

Developper Guide
----------

*Comment est organisé le code ?*

Le fichier principal est celui nommé run.py. C'est celui qu'il faut lancer depuis le terminal.

L'application Flask est ensuite activée dans le fichier __init__.py qui permet la lecture du fichier routes.py et dans lequel est importé Flask. Cette importation permet 
le lancement de notre application.

Dans le fichier routes.py, on commence par importer application qui contient le reste de nos fichier. On importe pd de la bibliotèque pandas afin de pouvoir manipuler notre 
base de données par la suite.

@app.route("/") nous permet de créer des nouvelles pages webs. Il suffit ensuite de créer le fichier html relié. Nous avons crée 5 fichier html:

• layout.html est le fichier html principal et permet l'affichage de la barre de navigation et son bon fonctionnement. Il permet également de gérer les animations.

  .. image:: https://github.com/SofianeTalbi/DataEngineerTools/blob/master/6Evaluation/Projet/application/static/images/navbar.png

• base.html permet l'affichage de la page "Accueil"

• index.html permet l'affichage de la page "Analyse des données"

• propos.html permet l'affichage de la page "A propos de GameCash". Il est relié et affiche le fichier logo.png.

• liens.html permet l'affichage de la page "liens et contact"

le fichier main.css permet de gerer la police d'écriture ainsi que la couleur du texte et du fond.

le fichier soso.json a été créé en scrapant le site GameCash.fr. Pour scrapper le site, nous avons utilisé le dossier scrape présent sur le git. Dans ce dossier se trouve un fichier 
game.py. Pour récuperer le fichier soso.json, on a réalisé les commandes suivantes sur notre terminale:

1) cd EngineerTools

2) cd 6Evaluation

3) cd Projet

4) cd scrape

5) cd gamecash

6) cd gamecash

puis

7) scrapy crawl game -o soso.json

Docker
Le docker-compose.yml et le Dockerfile permettent de lancer une version du projet qui marche correctement. Le projet qui possède tout pour les installations, permet de lancer l'app.py automatiquement.

Rapport d'analyse
----------
*Conclusion*

Pour conclure, ce projet nous a permis d'en apprendre plus sur un site de vente de jeu.

Ce que l'on sait maintenant:

• Les plates-formes les plus représentées

• Les éditeurs les plus représentées

• Les préférences des éditeurs en termes de type de jeu crée

• Le prix des jeux en fonction de l'éditeurs ou de l'année

Ce projet nous a permis d'apprendre également:

• Le package Flask

• Le scraping

• Mongo

• Docker

*Axe de développement*

Un axe de développement serait de réaliser le même travail sur un autre site de vente de jeux vidéos afin de déterminer si les tendances sont les mêmes.

Contact
----------
Perrin Thomas: perrin.thomas@edu.esiee.fr

Talbi Sofiane: talbi.sofiane@edu.esiee.fr

lien vers notre projet: https://github.com/SofianeTalbi/DataEngineerTools.git
