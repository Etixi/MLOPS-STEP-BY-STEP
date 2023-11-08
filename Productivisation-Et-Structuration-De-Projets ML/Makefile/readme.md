### **Makefile**
+ `Makefile` crée des commandes courtes et lisibles pour les tâches de configuration. Vous pouvez utiliser « Makefile » pour « automatiser des tâches » telles que la configuration de l'environnement.


### **Mise en Oeuvre**

        choco install make
        make activate
        make setup


### **Aide mémoire**

            # Makefile for a Python project

            # Variables
            PYTHON := python3
            PIP := pip
            PROJECT_NAME := myproject

            # Phony targets
            .PHONY: install test clean

            # Default target
            all: install

            # Install dependencies
            install:
	        $(PIP) install -r requirements.txt

            # Run tests
            test:
	        $(PYTHON) -m unittest discover tests

            # Clean the project
            clean:
	        rm -rf *.pyc __pycache__

Dans cet exemple :

+ La variable `PROJECT_NAME` peut être utilisée pour spécifier le nom de votre projet.
+ La cible `.PHONY` est utilisée pour déclarer de fausses cibles qui ne représentent pas de vrais fichiers.
+ La cible `all` est définie comme cible par défaut, qui, dans ce cas, appelle la installcible.
+ La cible `install` utilise `pip` pour installer les dépendances du projet à partir d'un requirements.txtfichier.
+ La cible `test` est utilisée pour exécuter des tests à l'aide du unittestmodule Python.
+ La cible `clean` est utilisée pour supprimer tous les fichiers de cache Python générés.

