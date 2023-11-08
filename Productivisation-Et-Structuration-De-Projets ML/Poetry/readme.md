#### **Poetry**
***

+ ***Une alternative à l'installation de bibliothèques avec `pip` consiste à utiliser `Poetry`. La poésie permet de :***

  +  ***Séparez les dépendances principales et les sous-dépendances dans deux fichiers distincts (vs requirements.txt)***

  + ***Créer des fichiers de dépendance lisibles***

  + ***Supprimer toutes les sous-dépendances inutilisées lors de la suppression d'une bibliothèque***

  + ***Évitez d'installer de nouvelles bibliothèques en conflit avec des bibliothèques existantes***

  + ***Empaqueter le projet avec quelques lignes de code***

+ Toutes les dépendances du projet sont spécifiées dans `pyproject.toml`.

<img src = "https://miro.medium.com/v2/resize:fit:828/format:webp/1*dLxaRwmEKmolG6zh9V8PTg.png"/>

### **Cheat Sheet**

| Commandes                    | Description                                      |
|------------------------------|--------------------------------------------------|
| `poetry new [project-name]`    | Créer un nouveau projet                          |
| `poetry install`               | installer les dépendances                        |
| `poetry add <library-name>`    | Ajouter une nouvelle bibliothèque                |
| `poetry remove <library-name>` | Supprimer une bibliothèque                       |
| `poetry show`                  | Afficher les dépendances                         |
| `poetry show --tree`           | Afficher les dépendances par le biais d'un arbre |
|`poetry update <library>`| Mettre à jour une bibliothèque                   |
|`poetry run which python`| Obtenir le chemin venv                           |
|`poetry run python app.py`| Exécuter l'application                           |
|`poetry run python -m unittest discover`| Exécuter des tests                               |


