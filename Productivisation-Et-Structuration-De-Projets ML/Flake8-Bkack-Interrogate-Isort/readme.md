## **Vérifiez les problèmes dans votre code avant de vous engager**

+ Lorsque vous validez votre code `Python sur Git`, vous devez vous assurer que votre code :

     + **est correct**

     + **est organisé**

    + **est conforme au guide de style PEP 8**

    + **inclut des docstrings**

+ ***Cependant, il peut être difficile de vérifier tous ces critères avant de valider votre code. pre-commit est un framework qui vous permet d'identifier des problèmes simples dans votre code avant de le valider.***

+ ***Vous pouvez ajouter différents plugins à votre pipeline de pré-validation. Une fois vos fichiers validés, ils seront vérifiés par ces plugins. Si toutes les vérifications ne sont pas réussies, aucun code ne sera validé.***

<img src = "https://miro.medium.com/max/484/1*j42hQq5ai7PU0q_BZaKrHA.png"/>

+ Dans ce modèle, nous utilisons 5 plugins différents spécifiés dans .pre-commit-config.yaml. Ils sont:

    + `Black` — formate le code Python

    + `flake8` — vérifie le style et la qualité de votre code Python

    + `isort` — trie automatiquement les bibliothèques importées par ordre alphabétique et les sépare en sections et types.

    + `Interrogate` - vérifie le code pour les docstrings manquants.