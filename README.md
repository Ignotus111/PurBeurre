# Projet 5 Openclassrooms
## Utilisation des données publiques d'OpenFoodFacts

La startup Pur Beurre nous demande de créer un programme interagissant avec la base de données d'OpenFoodFacts afin d'en __récupérer les aliments__ et leurs descriptions, et de donner la possibilité aux utilisateurs de lui __trouver un substitut__.


### Installation

Type python main.py to start the program.


### Description
Si l'utilisateur ouvre le programme pour la première fois, il crée une nouvelle base de donnée, sinon il selectionne automatiquement la base de donnée existante.

Deux choix s'offrent à l'utilisateur :
  1. "Substituer un aliment."

  2. "Mettre à jour la base de donnée"

Si l'utilisateur choisi "Substituer un aliment", il a trois nouveaux choix :
  1. Substituer un aliment.

  2. Retrouver les aliments substitués.

  3. Supprimer un des éléments sauvegardé.

  Si l'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

    - Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]

    - Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]

    - Le programme propose un substitut, sa description, un magasin où l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.

    - L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.






++++++++++ comment instaler les fichiers dans requirement.txt et comment le lancer
