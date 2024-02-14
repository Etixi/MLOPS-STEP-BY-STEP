## MLOPS PROGRAMMES

| PROGRAMME                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------|
| 1. Matériel de cours                                                                                              |
| 2. Introduction à l’apprentissage automatique                                                                     |
| 3. Avantages de l’apprentissage automatique                                                                       |
| 4. Principes fondamentaux du MLOps                                                                                |
| 5. Principes fondamentaux de DevOps et DataOps                                                                    |
| 6. Problèmes résolus par MLOps                                                                                    |
| 7. Composants MLOps                                                                                               |
| 8. Boîte à outils MLOps                                                                                           |
| 9. Étapes MLOps                                                                                                   |
| 10. Comment installer des bibliothèques et préparer l’environnement                                               |
| 11. Principes de base de Jupyter Notebook                                                                         |
| 12. Installation de Docker et Ubuntu                                                                              |
| 13. Cookiecutter pour gérer la structure du modèle Machine Learning                                               |
| 14. Bibliothèques et outils de gestion de projet du début à la fin                                                |
| 15. Poésie pour la gestion des dépendances                                                                        |
| 16. Makefile pour l’exécution automatisée des tâches                                                              |
| 17. Hydra pour gérer les fichiers de configuration YAML                                                           |
| 18. Hydra appliqué à un projet de Machine Learning                                                                |
| 19. Vérifiez et corrigez automatiquement le code avant la validation dans Git                                     |
| 20. Révision du code avec Black et Flake8 dans le pré-commit                                                      |
| 21. Révision du code avec Isort et Iterrogate dans l’intégration Pre-commit et Git                                |
| 22. Générer automatiquement de la documentation pour le projet ML                                                 |
| 23. Conception et mise en œuvre de Volere                                                                         |
| 24. Principes de base d’AutoML                                                                                    |
| 25. Construire une maquette du début à la fin avec Pycaret                                                        |
| 26. EDA et prétraitement avancé avec Pycaret                                                                      |
| 27. Développement de modèles avancés (XGBoost, CatBoost, LightGBM) avec Pycaret)                                  |
| 28. Déploiement en production avec Pycaret                                                                        |
| 29. Enregistrement et versioning des modèles avec MLFlow                                                          |
| 30. Enregistrement d’un modèle Scikit-Learn avec MLFlow                                                           |
| 31. Enregistrement du modèle Pycaret auprès de MLFlow                                                             |
| 32. Principes de base de l’interprétabilité avec SHAP                                                             |
| 33. Interpréter les modèles Scikit Learn avec SHAP                                                                |
| 34. Interpréter des modèles avec SHAP dans Pycaret                                                                |
| 35. Mise en service des modèles                                                                                   |
| 36. Principes fondamentaux des API et de FastAPI                                                                  |
| 37. Fonctions, méthodes et paramètres dans FastAPI                                                                |
| 38. Méthode POST, Swagger et Pydantic dans FastAPI                                                                |
| 39. Développement d’API pour le modèle Scikit-learn avec FastAPI                                                  |
| 40. Développement automatisé d’API avec Pycaret                                                                   |
| 41. Servir le modèle via une application Web                                                                      |
| 42. Commandes Gradio de base                                                                                      |
| 43. Développement d’une application web Gradio pour l’apprentissage automatique                                   |
| 44. Développement automatisé d’applications web avec Pycaret                                                      |
| 45. Notions de base sur les flacons                                                                               |
| 46. Construire un projet du début à la fin avec Flask                                                             |
| 47. Développement back-end avec Flask et développement front-end avec HTML et CSS                                 |
| 48. Conteneurs pour isoler nos applications                                                                       |
| 49. Principes de base de Docker et Kubernetes                                                                     |
| 50. Génération d’un conteneur pour une API ML avec Docker                                                         |
| 51. Docker pour générer un conteneur d’une application web à partir de Flask, HTML                                |
| 52. Introduction à l’apprentissage automatique dans le cloud                                                      |
| 53. Mise en production de l’application ML dans Azure Container avec Docker                                       |
| 54. Kits de développement logiciel (SDK) et stockage d’objets blob Azure pour le déploiement de modèles sur Azure |
| 55. Modéliser la formation et le déploiement de production dans le stockage d’objets blob Azure                   |
| 56. Téléchargez le modèle de stockage d’objets blob Azure et obtenez des prédictions                              |

### **Paysage MLOps**

| Fonctionnalités de base des plateformes                              | Description                                                                                                                                                                                                                                                          | Exemples                                                                                                                                                         |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Suivi des expériences, stockage des métadonnées du modèle et gestion | Les outils de suivi des expériences et de gestion des modèles vous offrent la possibilité de suivre les paramètre, les métriques et les visualisations des expériences, garantissant ainsi la reproductibilité et facilitant la collaboration                        | `AimStack` <br/> `neptune.ia` <br/> `MLflow` <br/> `Comet ML`                                                                                                    |
| Etiquetage et annotation des ensembles de données                    | Les outils d'étiquetage et d'annotation des ensembles de données constituent un composant essential des systèmes d'apprentissage automatique(ML), vous permettant de préparer des données d'entrainement de haute qualité pour leurs modèles                         | `Labelbox` <br/> `Scale AI` <br/> `Snorkel Flow` <br/> `AWS SageMaker Ground Truth` <br/> `Kili` <br/> `SuperAnnotate` <br/> `Encord Annotate` <br/> `superb AI` |
| Stockage des données et versionnage                                  | Les outils de stockage et de gestion des versions permettent de maintenir l'intégrité des données, la collaboration, faciliter des expériences et des analyses et garantir le développement et le déploiement précis de modèles ML                                   | `DVC` <br/> `Dolt` <br/> `Delta Lake` <br/> `Pachyderm` <br/> `LakeFS`                                                                                           |
| Suivi et gestion de la qualité des données                           | Les outils de suivi et gestion de la qualité des données permettent d'observer en permanence la qualité, la cohérence et la distribution des données pour identifier les anomalies ou les changements susceptibles d'avoir un impact sur les performances du modèle. | `Monte Carlo` <br/> `Metaplane` <br/> `Talend Data Quality` <br/> `Great Expectations` <br/> `Databand` <br/> `Soda Core`                                        |
| Magasins de fonctionnalités                                          | Les outils de magasins de fonctionnalités fournissent un référentiel pour stocker, gérer et servir les fonctionnalités ML.                                                                                                                                           | `Feast` <br/> `Databricks` <br/> `Tecton` <br/> `Vertex AI` <br/> `Hopsworks` <br/> `FetureForm`                                                                 |
| Modèles Hubs                                                         | Les modèles hubs fournissent une plate-forme centralisée pour la gestion, le partage et le déploiement de modèles ML                                                                                                                                                 | `Hugging Face Model Hub` <br/> `Kaggle` <br/> `Tensorflow Hub`                                                                                                   |
| Optimisation des hyperparamètres                                     | -                                                                                                                                                                                                                                                                    | `Optuna` <br/> `Hyperopt` <br/> `SigOpt`                                                                                                                         |
| Tests de qualité du modèle                                           | Les outils de test de qualité des modèles fournissent des fonctionnalités permettant de garantir la fiabilité,la robutesse et la precision des modèles ML                                                                                                            | `Deepchecks` <br/> `Truera` <br/> `Kolena`                                                                                                                       |
| Outils d'orchestration et de pipeline de flux de travail             | Les outils d'orchestration et de pipeline de flux de travail sont des composants essentiels pour rationaliser et automatiser les flux de travail de ML complexes                                                                                                     | `ZenML` <br/> `Kedro` <br/> `Flyte` <br/> `Prefect` <br/> `Mage AI`                                                                                              |
| Déploiement et service de modèles                                    | Les outils de deploiement et de diffusion de modèles vous permettent de déployer des modèles entrainés dans des environnements de production et fournir des prédictions aux utilisateurs finaux ou aux systèmes en aval.                                             | `BentoML` <br/> `OctoML` <br/> `NVIDIA TensorRT`                                                                                                                 |
| Observabilité du modèle                                              | Les outils d'observabilité des modèles peuvent vous permettre d'obtneir des informations sur le comportement, les perfromances et l'état de santé de vos modèles ML déployés.                                                                                        | `Evidently AI` <br/> `Aporia` <br/> `WhyLabs` <br/> `Mona` <br/> `Arize AI` <br/> `Superwise`                                                                    |


