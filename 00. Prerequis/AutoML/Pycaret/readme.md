# **Les types de fonctions**

## **Initialiser l'expérience dans PyCaret**

### **1) Setup**

+ Cette fonction initialise l'expérience dans `PyCaret` et crée le pipeline de transformation basé sur les `paramètres` transmis dans la fonction.
+ La fonction `setup` doit être appelé avant d'exécuter toute autre fonction. Il faut deux paramètres obligatoires : `data et target`. Tous les autres paramètres sont facultatifs.
+ Pycaret 3.0 possède deux `API`. Vous pouvez en choisir en fonction de vos préférences. Les fonctionnalités et les résultats sont cohérents.

#### **a) API fonctionnelle**

            # load dataset
            from pycaret.datasets import get_data
            diabetes = get_data('diabetes')

            # init setup
            from pycaret.classification import *
            clf1 = setup(data = diabetes, target = 'Class variable', session_id = 123)

#### **b) API POO**

            # load dataset
            from pycaret.datasets import get_data
            diabetes = get_data('diabetes')

            # init setup
            from pycaret.classification import ClassificationExperiment
            clf1 = ClassificationExperiment()
            clf1.setup(data = diabetes, target = 'Class variable', session_id = 123)


### **Journalisation des expériences**

+ Vous pouvez suivre automatiquement des expériences entières dans Pycaret. 
+ Un paramètre dans la configuration peut être activé pour suivre automatiquement toutes les `métriques, hyperparamètres et artefacts` de modèle.
+ Par défaut PyCaret utilise `MLFlow` pour la journalisation des expériences. 
+ Les autres options disponibles sont : `wandb, cometml et dagshub`.

#### **Exemple**

            # load dataset
            from pycaret.datasets import get_data
            diabetes = get_data('diabetes')

            # init setup
            from pycaret.classification import *
            clf1 = setup(data = diabetes, 
                        target = 'Class variable', 
                        log_experiment = True,
                        experiment_name = 'diabetes1'
            )

            # model training
            best_model = compare_model()

            # init server
            !mlflow ui


## **Fonctions de formation dans PyCaret**

### **compare_models**
+ Cette fonction entraîne et évalue les performances de tous les estimateurs disponibles dans la bibliothèque de modèles à l'aide de la validation croisée.
+ Le résultat de cette fonction est une grille de notation avec des scores moyens validés de manière croisée.
+ Les métriques évaluées lors du `CV` sont accessibles à l'aide de la fonction `get_metrics`.
+ Des métriques personnalisées peuvent être ajoutées ou supprimées à l'aide de la fonction `add_metric` et `remove_metric`.


#### **Exemple**

            # load dataset
            from pycaret.datasets import get_data
            diabetes = get_data('diabetes')

            # init setup
            from pycaret.classification import *
            clf1 = setup(data = diabetes, 
                        target = 'Class variable'
            )

            # compare models
            best = compare_model()

| Critères                            | Fonctions                                                                                                                                                                                                                                                                                              |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modifier l'ordre  de tri            | `best = compare_model(sort = 'F1')`                                                                                                                                                                                                                                                                    |  
| comparer seulement quelques modèles | `best = compare_model(include = ['lr', 'dt', 'ligthgbm'])` <br/> `best = compare_model(exclude = ['lr', 'dt', 'ligthgbm'])`                                                                                                                                                                            |
| Renvoyer plusieurs modèles          | `best = compare_models(n_select = 3)`                                                                                                                                                                                                                                                                  |
| Définir le temps du budget          | `best = compare_models(budget_time = 0.5)`                                                                                                                                                                                                                                                             |
| Définir le seuil de probabilité     | `best = compare_models(probability_threshold = 0.25)`                                                                                                                                                                                                                                                  |
| Désactiver la validation croisée    | `best = compare_models(cross_validation= False)`                                                                                                                                                                                                                                                       |
| Formation distribuée sur un cluster | `# Create pyspark session` <br/> `from pyspark.sql import SparkSession` <br/> `spark = SparkSession.builbder.getOrCreate()` <br/> `# import parallel back-end` <br/> `from pycaret.parallel import FugueBackend` <br/> `# compare models` <br/> `best = compare_models(parallel = FugueBackend(spark)` |

### **create_models**

+ Cette fonction entraine et évalue les performances d'un estimateur donné à l'aide de la validation croisée. 
+ Le résultat de cette fonction est une grille de notation avec les scores CV par pli.

#### **Exemple**

            # load dataset
            from pycaret.datasets import get_data
            diabetes = get_data('diabetes')

            # init setup
            from pycaret.classification import *
            clf1 = setup(data = diabetes, 
                        target = 'Class variable'
            )

            # train logistic regression
            lr = create_model('lr')

| Critères                            | Fonctions                                                                                                                                                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Créer un modèles                    | `lr = create_model('lr')`                                                                                                                                                                                                                                 |
| Changer de paramètres de pliage     | `lr = create_model('lr', fold = 5)`                                                                                                                                                                                                                       |
| Bibliothèques de modèles            | `models()`                                                                                                                                                                                                                                                |
| Modèles avec paramètre personnalisé | `dt = create_model('dt', max_depth = 5)`                                                                                                                                                                                                                  |
| Accéder à la grille de notation     | `# train decision tree`<br/> `lr = create_model('dt', max_depth = 5)`<br/> `# access the scoring grid`<br/>`dt_results = pull()`<br/>`print(dt_results`<br/>`# check type`<br/>`type(dt_results)`<br/>`# select only Mean`<br/>`dt_results.loc[['Mean']]` |
| Désactiver la validation croisée    | `lr = create_model('lr', cross_validatiob = False)`                                                                                                                                                                                                       |
| Score du train retour               | `lr = create_model('lr', return_train_score = True)`                                                                                                                                                                                                      |
| Définir le seuil de probabilité     | `lgbs = [create_model('ligthgbm', probability_treshold = 0.25)]`                                                                                                                                                                                          |
| Entrainer des modèles an boucles    | `lgbs = [create_model('ligthgbm', learning_rate = 1) for i in np.arange(0.1, 1, 0.1) ]` <br/> `type(lgbs)` <br/>`len(lgbs)`                                                                                                                               |

## **[Fonctions d'analyse et d'explicabilité du modèle]()**
+ `plot_model(model_name, plot = 'plot_name')`
+ `plot_model(model_name, plot = 'plot_name', scale =n)`
+ `plot_model(model_name, plot = 'plot_name', save = True)`
+ `plot_model(model_name, plot = 'plot_name', plot_kwargs = {'statistic_element' : boolean})`
+ `plot_model(model_name, plot = 'plot_name', use_train_data = boolean)`
+ `evaluate_model(model_name)`
+ `interpret_model(model_name, plot=['correlation', 'pdp', 'msa', 'pfi', 'reason'], user_train_data = boolean, save = boolean, feature = 'title', observation=n)`
+ `dashboard(name_model)`
+ `check_fairness(model_name, sensivtive_features = ['column_name'])`
+ `get_leaderboard()`
+ `assign_model(model_name)`



## **[Fonctions de déploiement](https://pycaret.gitbook.io/docs/get-started/functions/deploy)**

+ `predict_model(name_model)`
+ `predict(name_model, data = new_data)`
+ `predict(name_model, raw_score = True, data=new_data)`
+ `predict_model(name_model, probability_score = n)`
+ `finalize_model(name_model)`
+ `deploy_model(final_model, model_name='model_name_aws|model_name_aws_gcp|model_name_aws_azur', platform ='aws|gcp|azur', authentification = {'bucket(if aws)': 'pycaret-test'}`
+ `save_model(model_name, 'model_name_pipeline')`
+ `load_model('model_name_pipeline')`
+ `save_experminent('my_save_experiment')`
+ `load_experminent('my_save_experiment', data=data)`
+ `check_drift(reference_data = data.head(n), current_data = data.tail(n), target = 'Class_variable')`
+ `convert_model(name_model, 'java|c|go|c#|python')`
+ `create_api(name_model, 'name_model_api')`
+ `create_docker('name_model_api')`
+ `create_api('name_model')`

## **[Autres Fonctions](https://pycaret.gitbook.io/docs/get-started/functions/others)**
+ `pull()` : renvoie la dernière grille de notation imprimée.
+ `models()` : renvoie un tableau contenant tous les modèles disponibles dans le module importé de la bibliothèque de modèles.
+ `models(internal = True)` : si vous souhaitez voir un plus d'informations.
+ `get_config()` : Cette fonction récupère les variables globales créées lors de l'initialisation de configuration.
+ `set_config()` : reinitialise les variables globales.
+ `get_metrics()` : renvoie le tableau de toutes les métriques disponibles dans le conteneur de métriques.
+ `add_metrics()` : ajout d'une métrique personnalisé au conteneur métrique.
+ `remove_metrics()` : Supprime une métrique du conteneur des métriques.
+ `automl()` : Cette fonction renvoie le meilleur modèle parmi tous les modèles entrainés dans la configuration actuelle en fonction du paramètre `optimize`.
+ `get_logs()` : Renvoie un tableau des journaux d'expérience. Fonctionne uniquement lors de l'initialisation de configuration `log_experiment = True`
+ `get_current_experiment()` : Obtenez l'objet d'expérience actuel et renvoyez une classe. Ceci est utilisé lorsque vous utilisez une `API fonctionnelle` et que vous souhaitez passer à une `API POO`.
+ `set_current_experiment()` : Définissez l'expérience actuelle créée à l'aide de l'`API POO` à utiliser avec l'`API fonctionnelle`.


