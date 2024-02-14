
### **BentoML**
<hr>

+ `BentoML` est un framework open source permettant `de 
créer, d'expédier et de déployer` des services d'apprentissage 
automatique. 

+ Il fournit un ensemble de commandes et de fonctionnalités 
pour vous aider à gérer vos services et modèles ML.

+ Vous trouverez ci-dessous une liste de commandes BentoML 
courantes :

+ `bentoml new`: 
  + Créez un nouveau projet BentoService avec un modèle.


            bentoml new <project_name>

+ `bentoml serve`: 
  + démarrez le serveur API BentoService.

          bentoml serve <service_name>:<service_version>

+ `bentoml serve-gunicorn`: 
  + Démarrez le serveur API BentoService avec Gunicorn pour une utilisation en production.
  
          bentoml serve-gunicorn <service_name>:<service_version>
    
+ `bentoml predict` : 
   + effectuez des prédictions à l'aide d'une API BentoService déployée.


        bentoml predict <service_name>:<service_version> <input_data>

+ `bentoml list`: Répertorie tous les services et versions BentoService disponibles.


       bentoml list

+ `bentoml info`: 

  + Afficher des informations détaillées sur un BentoService.

        bentoml info <service_name>:<service_version>

+ `bentoml version`: 
  + Afficher la version BentoML.

        bentoml version

+ `bentoml deploy`: 
  + déployez un BentoService en tant que serveur API REST, conteneur Docker, AWS Lambda ou autres plates-formes.


      bentoml deploy <service_name>:<service_version> --platform <platform_name>

+ `bentoml delete` : 
  + Supprimez un BentoService déployé.

        bentoml delete <service_name>:<service_version>


+ `bentoml serve-fastapi`: 
  + démarrez le serveur API BentoService à l'aide de FastAPI pour une utilisation en production.


        bentoml serve-fastapi <service_name>:<service_version>

+ `bentoml serve-clipper`: 
  + Déployez un BentoService sur le système de desserte Clipper.


        bentoml serve-clipper <service_name>:<service_version> --name <deployment_name>


+ `bentoml containerize` : 
  + Créez un conteneur Docker pour un BentoService.

          bentoml containerize <service_name>:<service_version> -t <image_tag>

+ `bentoml open-api-spec`: 
  + Générez une spécification OpenAPI pour un BentoService.

          bentoml open-api-spec <service_name>:<service_version> -o <output_file>

+ Voici quelques-unes des commandes BentoML courantes. 
+ Vous pouvez exécuter `bentoml --help` ou `bentoml <command> --help` pour obtenir plus d'informations sur chaque commande spécifique et ses options.