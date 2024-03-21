# Base de données
L'ensemble de données est collecté à partir de [Kaggle Speed Dating Experiment](https://www.kaggle.com/annavictoria/speed-dating-experiment)

# Comment exécuter ce référentiel
```

python train_pipeline.py

python predict.py
```
# Fichiers dans ce référentiel
* [preprocessors.py](./preprocessors.py) : classes de prétraitement
* [pipeline.py](./pipeline.py) : pipeline d'estimateurs et de transformateurs pour les valeurs numériques et catégorielles
* [train_pipeline.py](./train_pipeline.py) : pour la formation
* [predict.py](./predict.py) : pour la préprédiction
* [config.py](./config.py) : pour enregistrer des informations sur l'ensemble de données, les variables et le nom du pipeline

# Modèle
Classificateur d'arbre de décision

# Résultat
Obtenez un score de précision parfait


### **Hydra Notes**

|Annotations| Descriptions                                                                                                                                                                     |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`@hydra.main `| Utilisé pour marquer le point d’entrée de votre application Hydra. <br/> Fournit un moyen de spécifier le schéma de configuration et les valeurs par défaut de votre application. |
|`@hydra.compile(overrides=...)`|Utilisé pour annoter des fonctions ou des méthodes afin d'appliquer dynamiquement des remplacements à la configuration. <br/>Vous permet d'appliquer des modifications ou des ajustements spécifiques à la configuration pendant l'exécution.|
|`@dataclass`|Utilisé pour annoter les classes de données au sein de votre application. <br/>Aide à définir la structure de vos classes de configuration.|
|`@hydra.hydra_annotations`|Utilisé pour annoter votre code afin de fournir des conseils ou des informations supplémentaires au système Hydra. <br/>Permet de garantir qu'Hydra interprète correctement la configuration et le code.|


