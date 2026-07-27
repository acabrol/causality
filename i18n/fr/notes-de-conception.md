# Notes de conception

Ce fichier conserve les decisions et pistes de conception en francais. La version officielle publique doit ensuite etre traduite ou adaptee en anglais dans les documents principaux.

## Concepts clefs

La **Main Timeline** et l'ensemble des **Branched Timelines** forment le **Time Flow** jusqu'au **Now**.

Le **Time Flow** possede toujours exactement **20 Time Units**. Chaque **Time Unit** est **Atomic** : les **Investigators** ne peuvent pas **rewind** vers une sous-periode d'une **Time Unit**, ni choisir un point entre deux **Time Units**.

Le **Now** est l'instant present : l'etat present de l'univers observable, produit par la **causality** dans le passe.

Le **System** utilise son energie limitee pour ouvrir le **Time Flow**. Il permet aux **Investigators** de **rewind** la **causality** afin d'atteindre une **Time Unit** precise du **Time Flow**.

Une **Branched Timeline** est **Branched** sur une **Time Unit** du **Time Flow**. Elle utilise un etat possible de l'univers sur cette **Time Unit**, puis l'**Investigator** modifie l'evolution de la **causality** depuis cet etat. La **Branched Timeline** tente ensuite d'etre **Merged** sur le **Now**.

Au sein du **Time Flow** maintenu par l'energie totale du **System**, tous les etats possibles de l'univers sur une **Time Unit** sont superposes.

Lorsque toute l'energie du **System** est consommee par le **Time Flow**, les etats non observables ne sont plus accessibles. Seule la **Main Timeline** persiste.

Si l'etat final de la **Main Timeline** n'est plus coherent avec l'etat de la **Main Timeline** au debut de la partie, selon les events definis par le maitre de jeu, alors l'etat observe n'est plus le **Now** originel. La realite diverge de l'origine et la realite des **Investigators** est perdue.

Un **Time Offender** est un PNJ controle par le **MJ** et utilise comme adversaire des **Investigators**. Il possede un ou plusieurs objectifs opposes aux joueurs : preserver une **Main Timeline** brisee, produire un **Now** divergent, cacher un **Fact**, detruire une **Evidence**, imposer des conflits non resolus ou pousser les **Investigators** a epuiser l'energie du **System**.

Un **Time Offender** utilise un **System** qui fonctionne exactement comme le **System** des **Investigators**. A la table, ce **System** adversaire est souvent appele **Counter-System** pour differencier l'activite du **Time Offender** de celle des **Investigators**. Sauf regle speciale de scenario, un **Counter-System** suit les memes limites que le **System** des **Investigators**.

Un scenario peut contenir aucun **Time Offender**, un seul **Time Offender**, plusieurs **Time Offenders** qui collaborent, ou plusieurs **Time Offenders** qui se concurrencent, se trahissent ou poursuivent des versions incompatibles du **Now**. Ils ne sont pas automatiquement omniscients : le **MJ** suit ce que chacun sait, ce qu'il veut, ses ressources, ses limites et les **Investigators** qu'il a identifies.

Un **Time Offender** agit a travers les structures normales du jeu : **Facts**, **Conditions**, **Evidence**, **Branched Timelines**, conflits, pression de **Volonte** et regles de scenario. Il ne contourne pas les **Rewind Dice**, les tests de **merge**, les degats, la **Volonte** ou les limites du **Time Flow**, sauf si le scenario definit explicitement une regle speciale.

## Volonte

- Les personnages commencent avec **100 points de Volonte**.
- Les tests de Volonte utilisent un seul **d10 percentile**.
- La face `00` du d10 percentile vaut `0`, pas `100`.
- La Volonte est reduite par un modificateur calcule a la fin du tour du joueur.
- `Volonte actuelle = 100 - modificateur du tour`.
- Une Branched Timeline non Merged pese `-30`.
- Un conflit majeur non resolu pese `-40`.
- Un conflit mineur non resolu pese `-20`.
- Le joueur doit toujours avoir une Volonte actuelle strictement superieure a `0` a la fin de son tour.
- Si le calcul donne une Volonte actuelle inferieure ou egale a `0`, le personnage sombre dans la folie.
- Le seuil du test est `100 - Volonte effective`.
- Le test reussit si le resultat du d10 percentile est superieur ou egal au seuil.

Exemple :

```text
Volonte actuelle : 97
Seuil = 100 - 97 = 3
Resultat 00 : echec
Resultat 10, 20, 30, 40, 50, 60, 70, 80 ou 90 : reussite
```

### Difficulte

Le niveau moyen utilise la Volonte actuelle sans modification.

| Difficulte | Volonte effective |
|---|---|
| Tres facile | Volonte actuelle x 10 |
| Facile | Volonte actuelle x 2 |
| Moyenne | Volonte actuelle |
| Difficile | Volonte actuelle / 2 |
| Tres difficile | Volonte actuelle / 4 |
| Impossible | Volonte actuelle / 100 |

Pour faciliter les calculs, la Volonte effective est tronquee avant de calculer le seuil.

## Echelle humaine

Tous les personnages joueurs ont des caracteristiques humaines par defaut.

Pour une premiere version, un personnage humain possede :

- **10 points de vie** ;
- des capacites physiques ordinaires, sauf exception prevue par le scenario.

## Rewind Dice

Le **Time Flow** possede toujours **20 Atomic Time Units**.

Chaque joueur recoit un set de des D&D classique : d4, d6, d8, d10, d10 percentile, d12 et d20.

Les d4, d6, d8, d10, d12 et d20 servent de **Rewind Dice**. Le d10 percentile sert aux tests de **Volonte**. Les d4, d6, d8 et d10 servent aux degats.

N'importe quel **Rewind Die** peut etre utilise pour n'importe quelle distance de rewind de `1` a `20` **Time Units**. La taille du de ne donne pas l'autorisation d'essayer le rewind ; elle change les chances de reussite avec la formule de **Rewind Percentage**.

| Rewind Die | Valeurs possibles |
|---|---|
| d4 | 1-4 |
| d6 | 1-6 |
| d8 | 1-8 |
| d10 | 1-10 |
| d12 | 1-12 |
| d20 | 1-20 |

Pour creer une Branched Timeline, le joueur choisit une Time Unit cible, calcule la distance de rewind depuis le Now, puis depense n'importe quel Rewind Die disponible.

Le de est ensuite lance. Le resultat est compare a la distance reelle du rewind.

```text
Rewind Percentage = (resultat du Rewind Die / distance de rewind) x 100
```

Les hauts resultats sont meilleurs, car le de doit couvrir la distance depuis le Now. Le resultat peut depasser `100%` ; toute valeur de `80%` ou plus reste une reussite critique.

| Rewind Percentage | Effet |
|---:|---|
| 80% ou plus | Reussite critique |
| 50-79% | Reussite partielle avec consequence |
| 21-49% | Echec partiel |
| 20% ou moins | Echec critique |

Exemple : depuis la Time Unit 20 vers la Time Unit 18, la distance de rewind est `2`. Avec un d4, un resultat de `1` donne `50%`, donc une reussite partielle. Un resultat de `2`, `3` ou `4` donne au moins `100%`, donc une reussite critique.

Exemple : depuis la Time Unit 20 vers la Time Unit 1, la distance de rewind est `19`. Avec un d20, un resultat de `16` a `20` donne au moins `80%`, donc une reussite critique. Un resultat de `10` a `15` donne une reussite partielle. Un resultat de `4` a `9` donne un echec partiel. Un resultat de `1` a `3` donne un echec critique.

Un d20 peut donc etre depense pour un rewind de `2` Time Units si c'est le seul Rewind Die restant. A l'inverse, un d4 peut etre depense pour un rewind de `19` Time Units, mais le calcul ne peut pas atteindre `50%` ; il ne peut donc pas ouvrir une Branched Timeline stable a cette distance.

## Consequences negatives d'une reussite partielle

Quand le jet d'ouverture de Branched Timeline donne une reussite partielle, la Branched Timeline s'ouvre, mais le joueur lance un d10 sur cette table.

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

## Gains mineurs d'un echec partiel

Quand le jet d'ouverture de **Branched Timeline** donne un echec partiel, l'action echoue et aucune **Branched Timeline** stable ne s'ouvre. Le **Rewind Die** est quand meme depense, mais le joueur lance un d10 sur cette table pour obtenir une petite reussite.

| d10 | Petite reussite |
|---|---|
| 1 | **Detail sensoriel d'Evidence** : revele un detail sensoriel tire d'une Evidence pertinente, sans nommer l'Evidence. |
| 2 | **Participant de Fact confirme** : confirme qu'une personne, un lieu, un objet ou un groupe nomme apparait dans un Fact pertinent. |
| 3 | **Statut d'Evidence marque** : marque une Evidence comme fausse, trompeuse, plantee ou incomplete. |
| 4 | **Time Unit du Fact localisee** : revele la Time Unit qui heberge un Fact pertinent, sans reveler le Fact. |
| 5 | **Condition exposee** : revele une Condition requise par le Fact cible, sans dire si elle est deja satisfaite. |
| 6 | **Type d'Evidence manquant** : revele le type d'Evidence manquant pour prouver ou merge le Fact cible. |
| 7 | **Trace de Time Offender** : si un Time Offender est implique, revele une trace de sa methode, de son outil, d'un changement de route ou de son etat de conscience. |
| 8 | **Indice de Dependency** : revele l'evenement anterieur requis en termes de fiction : qui doit agir, ce qui doit arriver, ou quel objet/lieu doit exister avant que le Fact cible puisse devenir vrai. Ne revele pas les ID internes des Facts. |
| 9 | **Conflit annonce** : revele un conflit qui serait cree si l'Investigator forcait l'ouverture de cette branche ratee. |
| 10 | **Piste immediate** : revele une personne, un lieu, un objet ou un dossier concret que l'Investigator peut examiner ensuite, lie a une Condition, un Fact, une Evidence ou une trace de Time Offender connue. |

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
