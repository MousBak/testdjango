#BooksApp

BookApp est application django avec PostgreSQL pour enregistrer et rechercher un livre.
Elle utiluse Docker pour effectuer une prostgression locale.
Elle conçcoit et implemente des API à l'aide de django rest framework.

#Installation
1-Accédez au dossier avec la commande cd BooksApp

2-Construisez les images Docker avec la commande "docker-compose build.

3-Lancez les conteneurs Docker avec la commande 'docker-compose up.

4-Créez un superutilisateur avec la commande docker-compose run web python manage.py createsuperuser et suivez les instructions.

5-Créez un environnement virtuel
python -m venv venv source venv/bin/activate

6-Installez les dépendances
pip install -r requirements.txt

7-Configurez la base de données PostgreSQL dans settings.py

#Utilisation

1-Appliquez les migrations
python manage.py migrate

2-Lancez le serveur de développement :
python manage.py runserver

3-Ouvrez votre navigateur et accédez à 1'URL http://localhost: 8000/admin/ 
pour accéder à l'interface d'administration de
Django.

4-Accédez à l’API à l’URL : http://localhost:8000/api
pour accéder à l'API de la liste des livres.

#Endpoints de l’API
Liste des livres (GET)
http://localhost:8000/api
pour accéder à l'API de la liste des livres.

Détails d’un livre (GET, PUT, DELETE) :
http://localhost:8000/api/{id}
pour accéder à l'API du détail d'un livre

Création d’un livre (POST)
http://localhost:8000/api
pour créer un livre

#Modèle de données

Books :
ID : Entier (clé primaire générée automatiquement)
Title : Chaîne de caractères
Author : Chaîne de caractères
Description : Chaîne de caractères (facultatif)
ISBN : Chaîne de caractères (unique)
Date de publication : Date (facultatif)
