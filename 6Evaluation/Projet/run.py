#On importe notre fichier application
from application import app

#On lance notre fichier __init__.py flask
if __name__ == "__main__":
    app.run(debug=True)