# TP1

Adam Martin-Côté 1798345
Yoan Gauthier    1871346

## Execution des test

L'utilisation des algorithmes est faite sous forme de tests unitaires pythons

Voici les étapes pour lancer ceux-ci:
 - s'assurer d'avoir accès à la librairie *numpy*, dans le cas contraire, faire:
        ```bash
            pipenv install
            pipenv shell
        ```
 - exécuter les test unitaires (`python3 -m unittest`) à la racine du projet (au même niveau que "tp1")

## Estimee3

Notre méthode de résolution finale est "Astar_prime_prime" qui utilise "estimee3" dans sa prise de décision

Estimee3 utilise les méthodes d'estimation précédentes, mais en y ajoutant un facteur de "blocage" déterminé par
le nombre de voiture se trouvant entre la voiture rouge et la sortie
