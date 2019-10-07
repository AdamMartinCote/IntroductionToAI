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

## Résultat

Les mesure effectuée montre une amélioration constante du nombre d'états visitées avec les différents algorithmes, ce
qui démontre que les fonctions d'estimée aide à prendre une meilleur décision

Toutefois, l'utilisation d'estimee3 entraine une perte de performance en terme de temps d'execution. Son utilisation
est donc appropriée si on veut minimiser le nombre d'états visités, mais si on préfère la rapidité d'exécution, 
"estimee2" est préférable.
