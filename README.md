# Que le meilleur gagne !
### Sujet
On cherche à déterminer la meilleure équipe parmi n;  

Chaque équipe doit rencontrer toutes les autres équipes une et une seule fois.
Le gagnant sera celui qui aura marqué le plus de points un calcul que nous n'évoquerons pas ici.
Le championnat est donc organisé en n ou n - 1 journées (en fonction de si n est pair ou impair), chaque équipe jouant au plus une fois dans une journée (exactement une fois si n est pair.)
Proposez un algorithme qui organise les matchs i.e. qui sort le planning des n - 1 journées, i.e. pour chaque journée, la liste des matchs.

##### Entrée :
- n : Le nombre d'équipe
##### Sortie :
- n(-1) lignes de n(-1)/2 paires d'entiers
##### Exemple :
Entrée  
`5`  
Sortie  
1 2 3 4  
1 4 3 5  
4 5 2 3  
1 5 4 2  
1 3 5 2  

##### Explication :
Journée 1 : (1 - 2) (3 - 4)  
Journée 2 : (1 - 4) (3 - 5)  
Journée 3 : (4 - 5) (2 - 3)  
Journée 4 : (1 - 5) (4 - 2)  
Journée 5 : (1 - 3) (5 - 2)

# Equilibre
### Sujet
Soit une liste dont les éléments sont 0 ou 1.  
Une tranche [i..j] d'éléments consécutifs est équilibrée si elle contient autant de 0 que de 1. Proposer un algorithme qui retourne la longueur maximale d'une tranche équilibrée.

##### Entrée :
- n le nombre d'élements de la liste
- la liste de n entiers (0 ou 1)
##### Sortie :
- la longueur maximale d'une tranche équilibrée
##### Exemple :
Entrée  
14  
1 0 0 1 0 1 0 0 0 0 0 0 0 1  
Sortie  
4  

Entrée  
10  
1 0 1 0 1 0 1 0 1 0  
Sortie  
10

Entrée  
1 1 1 1 1 1  
Sortie  
0  