### **Cheat Sheet**
<hr>

#### **Importation de Flask**
            from flask import Flask

#### **Fonctions d'importation les plus utilisées**
+ Voici quelques-unes des fonctions d'importation les plus utilisées par les developpeurs flask

            from flask import Flask, render_template, redirect, url_for, request

| Fonctions         | Explanation                                                                                                                                                                                                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Flask`           | C'est la classe principale de la bibliothèque `Flask`. Il est utilisé pour créer une instance d'application `Web Flask`. Lorsque vous créez une instance de la classe `Flask`, vous initialisez votre application Web.                                                                                               |
| `render_template` | Cette fonction est utilisée pour restituer des modèles HTML. Dans les applications Web, vous souhaitez souvent afficher du contenu HTML dynamique, et render_template, la fonction Flask vous permet d'utiliser des modèles HTML et de leur transmettre des données.                                                 |
| `redirect`        | La fonction `redirect` permet de rediriger le navigateur de l'utilisateur vers une URL différente. Ceci est souvent utilisé après avoir effectué une action spécifique, telle que le traitement d'un formulaire, puis la redirection de l'utilisateur vers une autre page.                                           |
| `url_for`         | La fonction  `url_for` est utilisée pour créer des URL de manière dynamique en fonction du nom de la fonction d'affichage. C'est un moyen pratique de garantir que vous générez des URL de manière cohérente et d'éviter de les coder en dur dans votre application.                                                 |
| `request`         | L'objet `request` représente la requête HTTP entrante envoyée par le client (par exemple, un navigateur Web). Il contient des informations sur la demande, telles que les données du formulaire, les en-têtes, etc. Vous pouvez l'utiliser pour accéder aux données envoyées par le client et répondre en conséquence. |


#### **Code passe-partout**
+ Il s'agit du modèle de base ou de la structure simple d'une application Flask.

            from flask import Flask

            app = Flask(__name__)

            @app.route("/")
            def hello_world():
                return "<p>Hello, World!</p>"

            app.run()


#### **Créer un itinéraire**

+ Il s'agit de créer différents points de terminaison dans notre application Flask.

            @app.route("/")

#### **Définition des méthodes autorisées**
+ Utilisé pour spécifier quelles méthodes sont autorisées pour une requête. Autoriser les requêtes d'obtention et de publication sur un point de terminaison.

            methods = ['GET', 'POST']

#### **Réexécuter pendant le codage**
+ Ceci est utilisé pour réexécuter automatiquement le programme lorsque le fichier est enregistré.

            app.run(debug=True)

#### **Changer d'hébergeur**
+ Ceci est utilisé pour changer d'hôte.

            app.run(host='0.0.0.0')

#### **Changer de port**
+ Ceci est utilisé pour changer de port.

            app.run(port=80)

#### **Importation de SQLAlchemy**

            from flask_sqlalchemy import SQLAlchemy


#### **URI de la base de données**
+ Il s'agit de l'adresse de la base de données.
            
            app.config['SQLALCHAEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
+ Ou

            app.config['SQLALCHAEMY_DATABASE_URI'] = 'sqlite:///test.db'


#### **Installation**

+ Ceci est utilisé pour initialiser `SQLALCHEMY`

            db = SQAlchemy(app)

#### **Creation d'un modèle**

+ Classe utilisée pour obtenir des données de la base de données et envoyer des données à la base de données.

           class TableName(db.Model):
                column_1 = db.Column(db.Integer, primary_key=True)
                column_2 = db.Column(db.String(80), nullable=False)
                column_3 = db.Column(db.String(12), nullable=False)
               
#### **Recupération de toutes les données - méthode `all()`**

+ Ceci est utilisé pour obtenir toutes les données de la base de données

            data = className.query.filter_by.all()

#### **Données filtrées - méthode first()**
+ Ceci est utilisé pour obtenir le premier ensemble de données de la liste renvoyée par la fonction `filter_by`. Vous pouvez ainsi obtenir des données ciblées.

            data = ClassName.query.filter_by().first()

#### **Envoyer/ajouter des données à la base de données**
+ Ceci est utilisé pour envoyer/ajouter des données à la base de données.

            data_to_send = ClassName(column_1=dataset1, column_2=dataset2, column_3=dataset3) 
            db.session.add(data_to_send) 
            db.session.commit()

#### **Supprimer des données de la base de données**
+ Ceci est utilisé pour supprimer des données de la base de données.

            data_to_send = ClassName(column_1=dataset1, column_2=dataset2, column_3=dataset3)
            db.session.delete(data_to_send)
            db.session.commit()

#### **Méthode de demande**
+ Ceci est utilisé pour savoir quelle demande est faite (get/post).

            request.method

#### **Modèle de rendu**
+ Ceci est utilisé pour transmettre et restituer directement un fichier HTML.

            render_template("file.html")

#### **Résolution de FSADeprecationWarning**
+ `SQLALCHEMY_TRACK_MODIFICATIONS` permet de désactiver le système de suivi des modifications grâce à cette ligne :

            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#### **Création de fichiers de base de données**
+ Ceci est utilisé pour créer des fichiers de base de données.

            from yourapplicationname import db 
            db.create_all() 
            exit()

#### **Méthode pour renvoyer les éléments de la base de données**
+ Ceci est utilisé pour renvoyer des éléments de base de données.

            def __repr__(self) -> str: 
                return f"{self.item}"

#### **Impression du contenu renvoyé par la méthode**
+ Ceci est utilisé pour imprimer les éléments de base de données renvoyés.

            data = ClassNameWithMethod.query.all() 
            print(data)