1. Train our Model
2. Create Web App Using Flask or Streamlit
3. Commit the code Github
4. Create an Account in Heroku(PAAS)
5. Link the Github to Heroku
6. Deploy the model
7. Web App is ready

16. Docker et le cloud :
● Docker sur AWS :
AWS fournit des services tels qu'Amazon Elastic Container Service (ECS) et AWS Fargate pour exécuter des conteneurs Docker.
● Docker sur Azure :
Azure fournit Azure Kubernetes Service (AKS) pour exécuter des conteneurs Docker.
● Docker sur Google Cloud :
Google Cloud fournit Google Kubernetes Engine (GKE) pour exécuter des conteneurs Docker.

17. Meilleures pratiques Docker :
● Immuabilité du conteneur :
L'idée selon laquelle vous ne mettez jamais à jour un conteneur en cours d'exécution, mais que vous devez toujours en créer un nouveau.
● Un seul processus par conteneur :
Chaque conteneur doit répondre à une seule préoccupation et bien le faire.
● Réduire le nombre de couches dans les Dockerfiles :
Moins il y a de commandes créant des calques, plus votre image risque d'être petite.
● Exploitez le cache de build :
Docker mettra en cache les résultats de la première build d'un Dockerfile, permettant aux builds suivantes d'être ultra rapides.
● Utilisez .dockerignore :
Empêche l'envoi de fichiers inutiles au démon lors de la création d'images.
● Utilisez des balises spécifiques pour les images de production :
L'utilisation de versions spécifiques d'une image garantit que votre application fonctionne toujours comme prévu. Par : Waleed Mousa
● Utilisez toujours la dernière version de Docker :
Chaque nouvelle version de Docker inclut des améliorations de sécurité, des corrections de bugs et de nouvelles fonctionnalités.

18. Docker et microservices :
● Découverte de services :
Docker Swarm Mode dispose d'un serveur DNS intégré que d'autres conteneurs peuvent utiliser pour résoudre le nom du service en adresse IP.
● Mise à l'échelle du service :
En mode Docker Swarm, vous pouvez augmenter ou réduire vos services.
● Équilibrage de charge :
Docker dispose d'un équilibreur de charge intégré qui peut distribuer les connexions réseau
à toutes les instances d'un service répliqué.
● Communication sécurisée entre services :
Docker Swarm Mode dispose d'un maillage de routage intégré qui fournit une communication sécurisée entre les services.

19. Plugins Docker :
● Plugins de stockage :
Ces plugins offrent des capacités de stockage aux conteneurs Docker.
● Plugins réseau :
Ces plugins fournissent des capacités de mise en réseau aux conteneurs Docker.
● Plugins d'autorisation :
Ces plugins restreignent les API Docker accessibles. Par : Waleed Mousa

20. API Docker :
● API REST Docker :
Une API utilisée par les applications pour interagir avec le démon Docker.
● SDK Docker :
SDK pour Go et Python, construits sur l'API Docker REST.
● API du moteur Docker :
Les clients API Docker utilisent pour communiquer avec le démon Docker.

21. Éditions Docker :
● Docker Community Edition (CE) :
Idéal pour les développeurs individuels et les petites équipes souhaitant démarrer avec Docker et expérimenter des applications basées sur des conteneurs.
● Docker Enterprise Edition (EE) :
Conçu pour les équipes informatiques et de développement d'entreprise qui créent, expédient et exécutent des applications critiques en production à grande échelle.

22. Architecture Docker :
● Moteur Docker :
Une application client-serveur avec trois composants principaux : un serveur, une API REST et une interface de ligne de commande (CLI).
● Démon Docker :
Écoute les requêtes de l'API Docker et gère les objets Docker tels que les images, les conteneurs, les réseaux et les volumes.
● Client Docker :
Il s'agit du principal moyen utilisé par de nombreux utilisateurs de Docker pour interagir avec Docker. Lorsque vous utilisez des commandes telles que docker run, le client envoie ces commandes à dockerd, qui les exécute. Par : Waleed Mousa
● Images Docker :
La base des conteneurs. Une image est une collection ordonnée de modifications du système de fichiers racine et des paramètres d'exécution correspondants à utiliser dans un environnement d'exécution de conteneur.
● Conteneurs Docker :
Une instance exécutable d'une image. Vous pouvez créer, démarrer, arrêter, déplacer ou supprimer un conteneur à l'aide de l'API Docker ou de la CLI.
● Services Docker :
Vous permet de faire évoluer les conteneurs sur plusieurs démons Docker, qui fonctionnent tous ensemble comme un essaim avec plusieurs gestionnaires et travailleurs.

    