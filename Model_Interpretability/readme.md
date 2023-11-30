### **Model Interpretability**

#### **Étapes MLOps**

<img src = "https://ml-ops.org/img/mlops-loop-en.jpg"/>

#### **Boîte noire**

+ **`Les modèles ML`** sont communément appelés **« Black Box »**, en raison de leur **difficulté d’interprétation**. Cela peut poser problème dans de nombreux secteurs.

+ **Exemple d'utilisation :**

    + Un modèle prédit qu'une banque ne devrait pas prêter de l'argent à quelqu'un, et la banque est légalement tenue d'expliquer le motif de chaque refus de prêt.


<img src="https://worldline.com/content/dam/worldline/global/images/blog-content-images/prior-blogs/img-black-Box.png"/>


### **SHAP**

+ **Une technique largement utilisée pour comprendre l'impact d'une variable sur la prédiction d'un modèle est `SHAP (SHapely Additive exPlanations)`**.

<img src="https://shap.readthedocs.io/en/latest/_images/shap_header.png"/>

### **Tracés récapitulatifs SHAP**
+ **Verticalement:**
  + ***variables classées par pertinence.***
+ **Horizontalement :**
  + ***effet dans la prédiction.***
+ **Gauche :**
  + ***moins de chances de gagner.***
+ **À droite :**
  + **plus de chances de gagner.**
+ **Couleur :**
  + **Valeur de la variable.**
+ **Rose**
  + ***pour les valeurs élevées,***
+ **bleu**
  + **pour les valeurs faibles.**

<img src="https://storage.googleapis.com/kaggle-media/learn/images/Ew9X3su.png"/>


### **Valeurs SHAP**
+ `Les valeurs SHAP` interprètent l'impact d'avoir une certaine valeur pour une fonctionnalité par rapport à la prédiction que nous ferions si cette fonctionnalité prenait une valeur de référence.
+ **Exemple:**
  + Dans quelle mesure une prédiction changerait-elle si l'équipe marquait 2 buts ?

<img src="https://community.rstudio.com/uploads/default/original/3X/a/d/ad013062fb30775ac54e2f25db67ba57d2c7853e.png"/>

### **Annexes**
+ https://shap.readthedocs.io/en/latest/api.html
+ https://shap.readthedocs.io/en/latest/api_examples.html