### **Projets Structure ML**

+ Il est important de **structurer** le projet selon un **standard**. Mais quel type de norme devez-vous suivre?

<img src = "https://mlops-guide.github.io/assets/folders.png"/>

+ *L'image ci-dessus est la structure des dossiers du projet.*

  + **`data, models et results`: contiennent des fichiers qui sont stockés et versionnés par `DVC`.**

  + **`notebooks`: contiennent des notebooks Jupyter utilisés pour l’analyse exploratoire, le développement de modèles ou la manipulation de données.**

  + **`src`: contient des scripts pour la formation et l'évaluation du modèle ainsi que des tests et des scripts pour les pipelines et les API.**

  + **`requirements` : Le fichier d'exigences est une liste de toutes les dépendances d'un projet et de la version spécifique de chaque dépendance, y compris les dépendances nécessaires aux dépendances. Il peut également être utilisé pour créer un environnement virtuel. Ceci est extrêmement important pour éviter les conflits entre les bibliothèques Python et également garantir que les expériences peuvent être reproduites sur différentes machines.**

  + **`metadata` : Pour garder une trace des informations sur le modèle dont nous disposons dans un fichier `metadata.yaml`, cela facilite l'automatisation du `CI/CD` et du pipeline. Comme la mise à jour ou le déploiement du modèle sans avoir besoin de la contribution de l'utilisateur.**

<img src = "https://miro.medium.com/max/572/1*BKdsm-KNLzGr_tNFJst8nA.png"/>

### **Cookiecutter**

+ **`Cookiecutter` est un outil permettant de créer automatiquement une `structure de dossiers de projets` à l'aide de modèles`. Vous pouvez créer des structures de fichiers et de dossiers statiques basées sur les informations d'entrée.**


<img src = "https://carlosgrande.me/wp-content/uploads/2020/10/Cheatsheat_PyProject-1-airtheme-standard-thumb-big-1748x1240.png"/>

### **Mise en Oeuvre**

Étape 1 : Assurez-vous que les derniers **python et pip** sont installés dans votre environnement.

Étape 2 : Installer Cookiecutter

    pip install cookiecutter


Étape 3 : Créez un exemple de référentiel sur github.com (par exemple, my-test)


Étape 4 : Créer une structure de projet

        # cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science (Bonne Astuce)
        # cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
        
        project_name [project_name]: my-test
        repo_name [my-test]: my-test
        author_name [Your name (or your organization/company/team)]: Etixi  
        description [A short description of the project.]: this is a test project
        Select open_source_license:
        1 - MIT
        2 - BSD-3-Clause
        3 - No license file
        Choose from 1, 2, 3 [1]: 1
        s3_bucket [[OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')]:
        aws_profile [default]:
        Select python_interpreter:
        1 - python3
        2 - python
        Choose from 1, 2 [1]: 1


        # cookiecutter https://github.com/mlops-guide/mlops-template.git

        author [MLOpsStudyGroup]: etixi
        project_name [Australia Weather Prediction]: test
        project_slug [test]: 
        project_version [v0.1]:
        model_type [scikit-learn_0.23]:
        Select open_source_license:
        1 - MIT
        2 - BSD-3-Clause
        3 - No license file
        Choose from 1, 2, 3 [1]: 1
        use_github_actions_for_CICD [y]: n
        use_pytest [y]: y
        use_black [y]: y


        # cookiecutter https://github.com/khuyentran1401/data-science-template