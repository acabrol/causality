# Notes de conception

Ce fichier conserve les decisions et pistes de conception en francais. La version officielle publique doit ensuite etre traduite ou adaptee en anglais dans les documents principaux.

## Concepts clefs

La **Main Timeline** et l'ensemble des **Branched Timelines** forment le **Time Flow** jusqu'au **Now**.

Le **Now** est l'instant present : l'etat present de l'univers observable, produit par la **causality** dans le passe.

Le **System** utilise son energie limitee pour ouvrir le **Time Flow**. Il permet aux **Investigators** de **rewind** la **causality** afin d'atteindre une **Time Unit** precise du **Time Flow**.

Une **Branched Timeline** est **Branched** sur une **Time Unit** du **Time Flow**. Elle utilise un etat possible de l'univers sur cette **Time Unit**, puis l'**Investigator** modifie l'evolution de la **causality** depuis cet etat. La **Branched Timeline** tente ensuite d'etre **Merged** sur le **Now**.

Au sein du **Time Flow** maintenu par l'energie totale du **System**, tous les etats possibles de l'univers sur une **Time Unit** sont superposes.

Lorsque toute l'energie du **System** est consommee par le **Time Flow**, les etats non observables ne sont plus accessibles. Seule la **Main Timeline** persiste.

Si l'etat final de la **Main Timeline** n'est plus coherent avec l'etat de la **Main Timeline** au debut de la partie, selon les events definis par le maitre de jeu, alors l'etat observe n'est plus le **Now** originel. La realite diverge de l'origine et la realite des **Investigators** est perdue.

## Volonte

- Les personnages commencent avec **100 points de Volonte**.
- Les tests de Volonte utilisent un **d100**.
- Un test reussit si le resultat est strictement inferieur a la Volonte actuelle.
- Un resultat egal ou superieur a la Volonte actuelle est un echec.

Exemple :

```text
Volonte actuelle : 97
Resultat de 1 a 96 : reussite
Resultat de 97 a 100 : echec
```

## Echelle humaine

Tous les personnages joueurs ont des caracteristiques humaines par defaut.

Pour une premiere version, un personnage humain possede :

- **10 points de vie** ;
- des capacites physiques ordinaires, sauf exception prevue par le scenario.

## Rewind Dice

Le **Time Flow** possede **20 Time Units**.

Les Rewind Dice sont :

| Rewind Die | Distance maximale de rewind |
|---|---|
| d4 | 4 Time Units |
| d6 | 6 Time Units |
| d8 | 8 Time Units |
| d10 | 10 Time Units |
| d20 | 20 Time Units |

Pour creer une Branched Timeline, le joueur choisit une Time Unit cible, calcule la distance de rewind depuis le Now, puis depense un Rewind Die dont la valeur maximale permet d'atteindre cette distance.

Le de est ensuite lance. La lecture est inversee : plus le resultat est bas, meilleur il est.

| Resultat | Effet |
|---|---|
| 1 | Reussite critique |
| Inferieur ou egal a la moitie du de | Reussite mitigee avec consequence |
| Superieur a la moitie du de | Echec mitige |
| Maximum du de | Echec critique |

Exemples :

| De | Reussite critique | Reussite mitigee | Echec mitige | Echec critique |
|---|---|---|---|---|
| d4 | 1 | 2 | 3 | 4 |
| d6 | 1 | 2-3 | 4-5 | 6 |
| d8 | 1 | 2-4 | 5-7 | 8 |
| d10 | 1 | 2-5 | 6-9 | 10 |
| d20 | 1 | 2-10 | 11-19 | 20 |

## Consequences negatives d'une reussite mitigee

Quand le jet d'ouverture de Branched Timeline donne une reussite mitigee, la Branched Timeline s'ouvre, mais le joueur lance un d10 sur cette table.

| d10 | Consequence negative |
|---|---|
| 1 | **Personnes effrayees** : les personnes proches paniquent, fuient, crient, appellent a l'aide ou refusent de cooperer. |
| 2 | **Attention attiree** : les autorites, gardes, temoins ou systemes de securite locaux commencent a reagir. |
| 3 | **Poursuite** : l'enqueteur est poursuivi par les autorites, la securite ou une force locale des le debut de la Branched Timeline. |
| 4 | **Mauvais point d'entree** : l'Investigator arrive dans la bonne Time Unit, mais au mauvais endroit. Il doit rejoindre la scene importante. |
| 5 | **Separe ou mal prepare** : l'enqueteur arrive separe de ses allies ou sans acces immediat a un outil, objet ou contact attendu. |
| 6 | **Plus proche du Now** : la Branched Timeline s'ouvre plus proche du Now que prevu. Avancer le point de depart de la Branched Timeline vers la Time Unit 20 de la valeur du Rewind Die, sans depasser la Time Unit 20. |
| 7 | **Trace visible** : la premiere action de l'enqueteur laisse une preuve de son intervention. Cela peut compliquer le merge. |
| 8 | **Conflit mineur** : la premiere action de l'enqueteur cree un conflit mineur avec la Main Timeline connue. |
| 9 | **Temoin modifie** : un temoin important voit l'enqueteur agir et change son comportement dans cette Branched Timeline. |
| 10 | **Conflit majeur** : la premiere action de l'enqueteur cree un conflit majeur avec la Main Timeline connue. Le merge est bloque tant qu'une cause corrective n'est pas creee. |

## Combat simplifie

Pour fluidifier le jeu, on part du principe que tout coup porte touche si l'action est acceptee par la fiction.

Il n'y a donc pas de jet pour toucher. Seuls les degats sont lances.

| Categorie d'attaque | De de degats | Exemples |
|---|---|---|
| Main nue | d4 | coup de poing, coup de pied, projection |
| Objet quelconque | d6 | chaise, bouteille, outil, livre lourd |
| Arme blanche ou non letale | d8 | couteau, matraque, taser, outil de neutralisation |
| Arme letale | d10 | arme a feu, explosif proche, danger industriel mortel |

Les degats sont soustraits aux points de vie.

A 0 point de vie, la cible sort de la scene. La consequence exacte depend de l'arme et de la fiction : inconscience, blessure grave, agonie ou mort.
