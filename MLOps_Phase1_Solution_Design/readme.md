#### **Catalogue des exigences pour les produits d'IA**
+ **Il s'agit d'un `catalogue d'exigences pour les produits d'IA` qui se veut le plus complet possible. L'objectif du catalogue est d'aider les équipes de science des données à collecter toutes les exigences à prendre en compte lors de la construction d'un modèle ML et de sa production.**

+ **Chaque exigence oubliée augmente la probabilité que vous deviez ultérieurement reconstruire une partie de votre solution, ou dans le pire des cas, la reconstruire à partir de zéro. Cela signifie gaspiller des efforts, ne pas livrer à temps et perdre la confiance de vos clients.**

+ **`L’ingénierie des exigences` est une discipline établie dans le processus de développement logiciel. Pour les projets logiciels, il existe également des modèles et des listes de contrôle qui permettent de ne négliger aucune partie prenante ou exigence. On le sait, les solutions de machine learning présentent certaines particularités non présentes dans d’autres projets :**

  + ***tout ce qui concerne l'ensemble de données***
  + ***reproductibilité de l'expérience***
  + ***préoccupations éthiques***
  + ***dérive du contexte***
  + ***etc.***

+ **Ainsi, il serait bien d’avoir un catalogue d’exigences pour une solution d’IA. Tout ce que j'ai pu trouver sur le Web ne contenait que certaines des questions que vous devez poser. J'ai donc créé un nouveau catalogue se voulant le plus complet possible.**

+ **Remarque importante : ce catalogue couvre tout s'il est utilisé avec un autre catalogue/modèle qui inclut les exigences du système logiciel standard. De tels catalogues existent depuis longtemps, il n’y a donc aucune raison de reproduire ce travail. Je recommande `le modèle Volere ( ancienne version gratuite , version payante )`, mais vous pouvez également utiliser une autre option. Voici un aperçu de haut niveau du modèle Volere :**

#### **Modèle Volère**

+ **Le catalogue présenté ici devrait combler l'écart en ajoutant la partie spécifique à l'apprentissage automatique aux exigences logicielles courantes.**

+ **La manière d'utiliser ce catalogue (et le modèle Volere) dépend généralement de l'utilisateur. L'approche qui me paraît pragmatique est de passer par des questions au lancement de votre projet DS (pour certains besoins, une clarification en cours de projet peut avoir plus de sens.) Essayez de trouver la réponse à chaque question. Des réponses telles que « n'a pas d'importance dans notre contexte » sont explicitement autorisées. Pour le reste des éléments, recherchez les parties prenantes concernées, posez-leur des questions et documentez ce qu'elles vous disent.**

+ **Les demandes d'amélioration de ce catalogue et de modifications sont les bienvenues – veuillez soit soumettre une pull request, soit ouvrir un problème GitHub.**

#### **Problème**
+ **Quel est le problème que nous voulons résoudre ?**
+ **À quel objectif commercial (stratégique) est-il lié ?**
+ **Quelles sont les solutions/solutions de contournement actuelles (le cas échéant) ?**
+ **Pourquoi pensons-nous que l’utilisation du machine learning apportera une valeur ajoutée ? (Liens vers des cas similaires dans l'industrie, des articles, des recherches)**
+ **Quelles parties du système utiliseront les prédictions ?**
+ **Quelles décisions/actions sont possibles sur la base des prédictions du modèle ?**  
+ **Quel(s) parcours utilisateur incluent l'utilisation du modèle et quel(s) impact(s) a-t-il ?**
+ **Quelle entrée le modèle doit-il accepter et quelle sortie doit-il produire ?**


#### **Métrique**
+ **Quelle(s) métrique(s) seront utilisées pour mesurer les performances du modèle ?**
+ **Quelle(s) est(sont) la(les) valeur(s) minimale(s) des métriques pour exécuter le modèle en production ?**
+ **Comment les mesures de performance sont-elles alignées sur les objectifs commerciaux ?**
+ **Quelles sont les performances de la solution actuelle ?**
+ **Existe-t-il un moyen d’estimer la valeur ajoutée du machine learning en utilisant des données historiques ?**


#### **Base de données**
+ **Un biais de sélection lors de la collecte des données ? (explication)**
+ **Y a-t-il des valeurs manquantes ? Le cas échéant:**
  + **Connaissez-vous les causes ?**
  + **Se produisent-ils au hasard ? (explication)**
+ **Existe-t-il des problèmes connus concernant l'exactitude/la précision des données ?**
  + **Où sont stockées les données ?**
  + **Est-il accessible depuis l'infrastructure que l'équipe DS utilise pour la formation et le service ?**
+ **Si les données sont structurées ou semi-structurées : disposez-vous d'une documentation pour chaque attribut ?**

#### **Éthique**
+ **Les décisions prises par votre modèle pourraient-elles être discriminatoires à l'égard d'un groupe d'utilisateurs ?**
+ **Si oui : que faut-il faire**
  + **concernant l'ensemble de données ?**
  + **concernant l'ingénierie et la modélisation des fonctionnalités ?**
  + **concernant le post-traitement des décisions ?**


#### **Interprétation**
+ **Devons-nous interpréter le modèle de l’un des points de vue suivants ?**

  + **Confiance** : montrer que le modèle peut prendre des décisions précédemment prises par des humains
  + **Causalité** : découvrez quels prédicteurs ont un impact sur la cible de quelle manière
  + **Transférabilité** : montrer que le modèle peut prédire des résultats raisonnables pour différentes entrées, y compris celles qui ne sont pas similaires aux échantillons d'apprentissage
  + **Caractère informatif** : si le modèle est créé non pas pour faire des prédictions mais pour mesurer l’impact des prédicteurs, sert-il cet objectif ?
  + **Équité** : montrer que le modèle est sans biais


#### **Exigences légales et réglementaires**
+ **Lors de la formation du modèle, existe-t-il des restrictions concernant la préservation de la confidentialité des utilisateurs ?**
+ **Existe-t-il des restrictions concernant l’utilisation des ensembles de données dans le but défini ?**
+ **Y a-t-il des restrictions concernant l'approche de modélisation ?**
+ **Existe-t-il des réglementations concernant le processus de développement ?**

#### **Reproductibilité**
+ **Quels artefacts de votre formation souhaitez-vous conserver ou/et historiser ?**
  + ***code et configuration***
  + ***base de données***
  + ***métrique***
  + ***modèle entraîné***
  + ***métadonnées (date, personne qui a mené l'expérience, informations sur le logiciel/matériel, etc.)***
+ **Comment allez-vous y parvenir ?**
+ **Comment éviterez-vous le biais de formation/diffusion du code ? (explication)**

#### **Testabilité**
+ **De quels contrôles et rapports avons-nous besoin pour l'ensemble de données avant de construire le modèle ?**
  + **vérifier l'exactitude et l'exhaustivité de la collecte de données**
  + **découvrir la dérive des données (explication)**
+ **De quels contrôles et rapports avons-nous besoin pour le modèle formé ?**
  + **concernant les métriques**
  + **concernant les différences par rapport aux versions précédentes ou autres du modèle**
+ **De quel niveau d’automatisation avons-nous besoin pour chacun des contrôles/rapports définis ?**
  + **entièrement automatisé, y compris. décision de poursuivre le projet ou de l'arrêter**
  + **semi-automatique : générez un rapport pertinent, mais laissez l'humain décider s'il doit continuer**
  + **exécuté manuellement et décidé par l'humain**

#### **Mise à jour du modèle**
+ **Une dérive conceptuelle est-elle attendue ? (explication)**
+ **à quelle fréquence un modèle doit-il être recyclé/mis à jour pour l'atténuer ?**
+ **toute autre idée d'atténuation, par exemple le post-traitement**
+ **À quelle vitesse un changement dans le système source doit-il être reflété dans une nouvelle version du modèle ?**

#### **Production**
+ **Quelles informations enregistrerez-vous lorsque vous ferez des prédictions ?**
+ **Quelles mesures surveillerez-vous en permanence en production ?**
+ **Quels seuils et alertes définirez-vous en fonction de ces métriques ?**
+ **Comment découvrirez-vous une dégradation des performances en production ?**

#### **Etapes MLOps**

<img src = "https://ml-ops.org/img/mlops-loop-en.jpg"/>


#### **Modèle Volère**

<img src="https://github.com/ttzt/catalog_of_requirements_for_ai_products/raw/main/volere.png" width="800" height="450" title="Modèle Volère"/>

+ [catalog_of_requirements_for_ai_products](https://github.com/ttzt/catalog_of_requirements_for_ai_products)