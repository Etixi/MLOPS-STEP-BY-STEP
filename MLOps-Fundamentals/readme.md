## **Défis relevés par MLOps**
<hr>

+ ### **Gestion des versions**
  + Des outils tels que **Git et Github** sont utilisés dans le contrôle de version du code. De plus, les **données et artefacts** sont versionnés pour garantir la reproductibilité.
+ ### **Suivi du modèle**
  + Les modèles en production peuvent être **dégradés** au fil du temps en raison d'une **dérive des données**.
+ ### **Génération de fonctionnalités**
  + Cela demande beaucoup de ressources. `MLOps` permet de `réutiliser des fonctions`. Ainsi, vous pouvez vous concentrer sur la conception/test du modèle.

## **Composants MLOps**
<hr>

+ ### **Magasin de fonctionnalités**
  + Stocke les fonctions qui ont été utilisées dans la formation du modèle.
+ ### **Versionnage des données**
  + Le contrôle des versions des données garantit la reproductibilité et facilite l'audit.
+ ### **Magasin de métadonnées**
  + C'est essentiel pour la reproductibilité. Tout doit être enregistré, de la graine du modèle aux métriques d'évaluation...
+ ### **Gestion des versions du modèle**
  + Vous permet de basculer entre les modèles en temps réel ou de servir différents modèles à surveiller.
+ ### **Enregistrement du modèle**
  + Une fois qu'un modèle a été entraîné, il est stocké dans un registre de modèles avec ses métadonnées.
+ ### **Service de modèle**
  + Servir un modèle signifie créer des points de terminaison qui peuvent être utilisés pour exécuter des prédictions.
+ ### **Surveillance du modèle**
  + Les modèles doivent être surveillés pour détecter les biais de dérivation et de production.
+ ### **Recyclage des modèles**
  + Les modèles peuvent être recyclés pour améliorer les performances ou lorsqu'il y a de nouvelles données.
+ ### **CI/CD**
  + Cela garantit que le code est fréquemment fusionné avec des processus et des tests automatisés.


<img src="https://ml-ops.org/img/mlops-stack.jpg"/>


### **MLOps Toolbox**
<hr>

<img src="https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/MLOps-tools-landscape-horizontal-upd.png?ssl=1" height="350" width="600"/>



## **Étapes MLOps**
<hr>

+ `Étape 1`:Contrôle de version du modèle et des données
+ `Étape 2`: `AutoML` + Contrôle de version du modèle et des données.
+ `Étape 3`: AutoML + Contrôle de version des modèles et des données + `Service de modèles`
+ `Étape 4:` AutoML + Contrôle des versions de modèles et de données + Service de modèles + `Surveillance, gouvernance et recyclage`.




