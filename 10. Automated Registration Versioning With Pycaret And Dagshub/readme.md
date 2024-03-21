### **Que comprend l'intégration entre DagsHub et PyCaret ?**


+ **`PyCaret` fournit une intégration prête à l'emploi avec `MLflow`, permettant aux utilisateurs d'enregistrer des métriques, des données et des tracés importants sur leurs machines locales.**
+ **Cela permet d’organiser `la phase de recherche et de gérer les projets jusqu’à la production`.** 
+ **Cependant, il lui manque la possibilité de collaborer avec des coéquipiers et de partager des résultats sans passer à une plateforme tierce (par exemple, envoyer des captures d'écran sur Slack)**. 
+ **De plus, lors de l’enregistrement des données, il n’existe pas de moyen simple de voir comment les différentes méthodes de traitement qui ont affecté les données pour prendre des décisions qualitatives.**

+ C'est là que `DagsHub` entre en jeu.

<img src="https://dagshub.com/img/principles/integrations.png" width="800" height="400"/>


+ **`DagsHub fournit un serveur MLflow distant` pour chaque référentiel, permettant aux utilisateurs d'enregistrer des expériences avec MLflow et d'afficher et de gérer les résultats et les modèles entraînés à partir de l'interface utilisateur intégrée.**
+ **Le référentiel DagsHUb comprend également un stockage d'objets entièrement configuré pour stocker des données, des modèles et tout fichier volumineux. Ces fichiers sont différenciables, permettant aux utilisateurs de voir les changements entre les différentes versions de leurs données et modèles, les aidant ainsi à comprendre l'impact de ces changements sur leurs résultats.**

<img src="https://dagshub.com/blog/content/images/size/w1000/2023/01/Untitled--30-.png"/>

+ **Avec la nouvelle intégration entre `PyCaret et DagsHub`, vous pouvez désormais enregistrer des expériences sur votre serveur `MLflow` distant hébergé sur `DagsHub`, comparer des expériences et les partager avec vos amis et collègues.**
+ **En plus de cela, vous pouvez versionner vos données brutes et traitées à l'aide de `DVC`, les transmettre à `DagsHub` pour les afficher, les comparer et les partager avec d'autres.** 
+ **Tous ces éléments sont encapsulés sous le nouveau `DagsHub Logger` intégré à `PyCaret`. Cela signifie que vous devez modifier UNE ligne dans votre code.**

<img src="https://dagshub.com/blog/content/images/size/w1000/2023/01/Untitled--31-.png"/>

### **Comment utiliser DagsHub Logger avec PyCaret ?**
+ Pour utiliser `DagsHub Logger avec PyCaret`, définissez le paramètre `log_experiment` sur `dagshub` lors de l'initialisation de votre expérience PyCaret. Par exemple:

            from pycaret.datasets import get_data
            from pycaret.regression import *

            data = get_data('diamond')

            s = setup(data,
		            target = 'Price',
                    transform_target=True,
                    log_experiment="dagshub",
                    experiment_name='predict_price',
                    log_data=True)

+ **Si le `DagsHub Logger` n'est pas déjà authentifié sur votre ordinateur local, le terminal vous demandera de saisir le `repo_owner/repo_name` et de fournir un lien d'authentification.** 
+ **Le référentiel et le serveur MLflow distant seront alors automatiquement initialisés en arrière-plan.**

### **Comment utiliser DagsHub Logger par programmation ?**

+ **Pour éviter le processus d'authentification, vous pouvez définir deux variables d'environnement qui vous permettront d'exécuter votre script par programme.**

            os.environ["DAGSHUB_USER_TOKEN"] = "<enter-your-DagsHub-token>"
            os.environ['MLFLOW_TRACKING_URI'] = "<enter-your-MLflow-remote-DagsHub>"

+ **La première variable d'environnement configurera votre jeton DagsHub pour notre client, qui sera utilisé pour l'authentification et l'accès en écriture au référentiel et à la télécommande.**
+ **La seconde est que vous êtes l'URI de suivi MLflow, hébergé sur DagsHub. Nous l'utiliserons pour configurer la configuration à distance du DagsHub Logger. Voici un exemple d'un tel code :**

          import os
          os.environ["DAGSHUB_USER_TOKEN"] = "<ENTER DAGSHUB TOKEN>"
          os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/Etixi/Diamond_project"

          s = setup(data,
		           target = 'Price',
                   transform_target=True,
                   log_experiment="dagshub",
                   experiment_name='diamont_project',
                    log_data=True)

