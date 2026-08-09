# Quickstart Causality

Ce guide donne assez de structure pour lancer un premier playtest de **Causality**.

Causality est inspire de [Continuum: Roleplaying in the Yet](http://www.aetherco.com/continuum/), avec une premisse differente : les joueurs enquetent sur des chaines causales et rejouent des Branched Timelines au lieu de voyager physiquement dans le temps.

## Premier scenario

Utilisez [Protocole Fievre de Verre](./scenarios/protocole-fievre-de-verre-preparation-mj.md) comme scenario recommande pour debuter. Il contient un replay starter simple sans Time Offender, puis un replay complet qui montre tout le set de regles.

## Materiel necessaire

- 1 Game Master.
- 2 a 5 joueurs.
- Un tableau blanc, une grande feuille ou un tableau numerique partage.
- Des fiches ou post-it pour les Facts, Evidence, Branched Timelines et conflits.
- Un set classique de des D&D pour chaque Investigator : d4, d6, d8, d10, d10 percentile, d12 et d20.
- Les Rewind Dice utilisent le d4, d6, d8, d10, d12 et d20.
- Les jets d'action au pourcentage utilisent le d10 percentile. La face `00` vaut `0`, pas `100`.
- Les jets de degats utilisent le d4, d6, d8 et d10.

## Mise en place de table

Dessinez une Main Timeline avec exactement 20 Time Units Atomic, puis marquez le Now comme Time Unit 0. Le Time Flow a toujours 20 Time Units preparees avant le present.

```text
TU20 -- TU19 -- TU18 -- ... -- TU02 -- TU01 -- TU00 / Now
plus ancien                                plus proche present
```

La Time Unit 20 est l'etat causal prepare le plus ancien. La Time Unit 1 est l'etat causal prepare le plus proche du present. Le Now est la Time Unit 0 au debut de la partie. Chaque Time Unit est Atomic : les joueurs ne peuvent pas rewind dans une sous-periode d'une Time Unit ni choisir un point entre deux Time Units. Le scenario definit seulement ce que chaque Time Unit complete represente : heures, jours, annees ou siecles.

## Preparation du Game Master

Preparez une Causal Table cachee :

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | Une condition qui doit etre vraie | Un Fact qui arrive | Trace produite par le Fact |
| F02 | F01 est vrai | Un Fact plus tardif | Un fichier, objet, temoin, souvenir ou enregistrement |

Gardez la table complete cachee. Ne revelez que les Facts que les joueurs peuvent prouver.

Preparez un dossier initial avec quelques indices. Utilisez ces indices pour placer les premiers Facts confirmes sur la Main Timeline.

Si le scenario utilise un **Time Offender**, definissez-le comme un PNJ adversaire controle par le Game Master avec un ou plusieurs objectifs opposes aux joueurs. Un Time Offender utilise un System qui fonctionne comme celui des Investigators ; ce System adverse est generalement appele **Counter-System**. Decidez quels Facts il protege ou attaque, quelle Evidence peut le reveler, quelles ressources de Counter-System il peut depenser, et s'il agit seul, avec d'autres Time Offenders ou contre eux.

## Creation des personnages

Donnez a chaque Investigator :

- un nom et un role ;
- une Charge mentale egale a 0 ;
- 10 Health ;
- un set classique de des D&D, dont les Rewind Dice representent l'energie personnelle du System.

Pour un premier test, tous les Investigators sont des humains de base. Ajustez seulement si le scenario demande des personnages exceptionnels.

## Fonctionnement d'un tour

A son tour, un joueur choisit une action :

1. enqueter sur la Main Timeline actuelle ;
2. ouvrir une Branched Timeline depuis une Time Unit connue ;
3. continuer une Branched Timeline ;
4. tenter un Merge ;
5. travailler sur un conflit.

### Exemple de tour

> Alice a 0 de Charge mentale, 10 Health, et possede encore son d8 et son d12. La Main Timeline montre un blanc a la Time Unit 14. Alice decide d'ouvrir une Branched Timeline sur TU14.
>
> Elle depense son **d12** et obtient **9**. La distance de rewind est 14, donc le Rewind Percentage est `(9 / 14) x 100 = 64%` : **reussite partielle avec consequence**.
>
> Le Game Master lance un **d10** sur la table des consequences negatives et obtient **4** : Alice arrive dans la bonne Time Unit, mais au mauvais endroit. Elle est dehors au lieu d'etre dans le batiment.
>
> Alice decrit ce que fait son personnage : elle trouve une entree laterale et recupere un manifeste cargo. Le Game Master note la Branched Timeline (proprietaire : Alice, depart : TU14, Rewind Die : d12, Evidence : manifeste cargo, statut : ouverte).
>
> A la fin de son tour, Alice a 1 Branched Timeline non Merged, 0 Major Conflict et 0 Minor Conflict. Sa Charge mentale est `30 x 1 = 30`.

Quand un joueur ouvre une Branched Timeline, il depense et lance un Rewind Die, dessine la Branched Timeline depuis la Time Unit choisie, puis decrit ce que son personnage fait dans cet etat rejoue.

## Rewind Dice

Le Time Flow a toujours 20 Time Units Atomic. N'importe quel Rewind Die peut etre utilise pour n'importe quelle distance de rewind de `1` a `20` Time Units. Les gros des sont plus surs sur les rewinds longs, mais ils ne sont pas requis.

| Rewind Die | Valeurs possibles |
|---|---|
| d4 | 1-4 |
| d6 | 1-6 |
| d8 | 1-8 |
| d10 | 1-10 |
| d12 | 1-12 |
| d20 | 1-20 |

Pour ouvrir une Branched Timeline, choisissez une Time Unit cible, comptez la distance de rewind depuis le Now, puis depensez un Rewind Die disponible.

Apres avoir depense le de, lancez-le et calculez le Rewind Percentage :

```text
Rewind Percentage = (resultat du Rewind Die / distance de rewind) x 100
```

Les hauts resultats sont meilleurs, car le de doit couvrir la distance depuis le Now. Le resultat peut depasser `100%`; toute valeur de `80%` ou plus reste une reussite critique.

| Rewind Percentage | Resultat |
|---:|---|
| 80% ou plus | Reussite critique |
| 50-79% | Reussite partielle avec consequence |
| 21-49% | Echec partiel |
| 20% ou moins | Echec critique |

Sur une reussite partielle, la Branched Timeline s'ouvre, mais lancez un d10 pour une consequence negative.

| d10 | Consequence negative |
|---|---|
| 1 | Les personnes proches sont effrayees. |
| 2 | Les autorites locales ou la securite remarquent quelque chose d'anormal. |
| 3 | L'Investigator est poursuivi. |
| 4 | L'Investigator arrive dans la bonne Time Unit, mais au mauvais endroit. |
| 5 | L'Investigator arrive separe de ses allies ou sans un outil attendu. |
| 6 | La Branched Timeline s'ouvre plus proche du Now que prevu ; reduisez la Time Unit cible du resultat du Rewind Die, sans passer sous Time Unit 0. |
| 7 | La premiere action laisse une preuve visible de l'intervention. |
| 8 | La premiere action cree un Minor Conflict avec la Main Timeline connue. |
| 9 | Un temoin important change de comportement apres avoir vu l'Investigator. |
| 10 | La premiere action cree un Major Conflict avec la Main Timeline connue. |

Sur un echec partiel, l'action echoue et aucune Branched Timeline stable ne s'ouvre. Le Rewind Die est quand meme depense, mais le joueur lance un d10 pour obtenir un gain mineur.

| d10 | Gain mineur |
|---|---|
| 1 | Revelez un detail sensoriel d'une Evidence pertinente, sans nommer l'Evidence. |
| 2 | Confirmez qu'une personne, un lieu, un objet ou un groupe nomme apparait dans un Fact pertinent. |
| 3 | Marquez une Evidence comme fausse, trompeuse, plantee ou incomplete. |
| 4 | Revelez la Time Unit qui contient un Fact pertinent, sans reveler le Fact. |
| 5 | Revelez une Condition requise par le Fact cible, sans dire si elle est deja satisfaite. |
| 6 | Revelez un type d'Evidence manquant necessaire pour prouver ou merger le Fact cible. |
| 7 | Si un Time Offender est implique, revelez une trace de sa methode, de son outil, d'un changement de route ou de son etat de conscience. |
| 8 | Revelez l'evenement anterieur requis en termes fictionnels : qui doit agir, ce qui doit arriver, ou quel objet/lieu doit exister avant que le Fact cible devienne vrai. Ne revelez pas les ID internes des Facts. |
| 9 | Revelez un conflit qui serait cree si l'Investigator forcait cette branche ratee a s'ouvrir. |
| 10 | Revelez une personne, un lieu, un objet ou un dossier concret que l'Investigator peut examiner ensuite, lie a une Condition, un Fact, une Evidence ou une trace de Time Offender connue. |

Sur un echec critique, aucune Branched Timeline stable ne s'ouvre, aucun gain mineur n'est lance, et le Rewind Die est depense.

## Branched Timelines

Une Branched Timeline est une execution causale alternative. Les Facts qu'elle contient sont reels pour le personnage qui les vit, mais ils ne sont pas vrais sur la Main Timeline partagee tant que la Branched Timeline n'est pas Merged.

Notez chaque Branched Timeline avec :

- proprietaire ;
- Time Unit de depart ;
- Facts nouveaux ou modifies ;
- Evidence produite ;
- conflits ;
- statut.

N'effacez pas les Branched Timelines. Elles comptent pour la memoire, le stress et la divergence finale.

## Merges

Quand un joueur tente un Merge, le Game Master verifie ce que la Branched Timeline change :

- Facts crees ;
- Facts supprimes ;
- Facts modifies ;
- Conditions changees ;
- dependencies cassees ;
- Evidence qui apparait ou disparait.

Si la Branched Timeline permet toujours au Now d'avoir du sens, les changements compatibles peuvent etre ajoutes a la Main Timeline.

## Conflits

### Minor Conflict

Un Minor Conflict change un detail local ou non essentiel.

Le joueur choisit quelle version il veut imposer, puis fait un jet d'action au pourcentage :

```text
resultat final = resultat brut du d10 percentile - Charge mentale
resultat final >= seuil = succes
resultat final < seuil = echec
```

En cas de succes, la version choisie est appliquee. En cas d'echec, la version opposee est appliquee.

### Major Conflict

Un Major Conflict casse un Fact essentiel ou rend le mystere impossible.

Les Major Conflicts ne peuvent pas etre resolus par un simple jet. Les joueurs doivent creer une autre cause, ouvrir une Branched Timeline corrective anterieure, ou changer la situation pour rendre le Fact central a nouveau possible.

## Charge mentale

A la fin du tour de chaque joueur, recalculez sa Charge mentale :

```text
Charge mentale
= modificateur du tour
```

Le modificateur du tour est :

```text
modificateur du tour
= 30 x Branched Timelines non Merged
+ 40 x Major Conflicts non resolus
+ 20 x Minor Conflicts non resolus
+ autres penalites actives de Charge mentale
```

Le joueur doit toujours garder une Charge mentale inferieure a `100` a la fin de son tour. Si le calcul atteint `100` ou plus, le personnage sombre dans la folie et ne peut plus maintenir une coherence avec le Now observable.

Pour un jet d'action au pourcentage sans seuil propre, utilisez ces seuils :

| Difficulte | Seuil |
|---|---:|
| Tres facile | 0 |
| Facile | 20 |
| Moyen | 50 |
| Difficile | 70 |
| Tres difficile | 90 |
| Impossible | 100 |

La Charge mentale est toujours soustraite au resultat brut avant comparaison au seuil.

Les realites non Merged existent encore dans la memoire du personnage. Trop de Branched Timelines non Merged rendent l'imposition d'une coherence plus difficile.

## Combat rapide

Tous les combats sont resolus a echelle humaine. Chaque attaque declaree et acceptee par la fiction touche automatiquement. Ne lancez pas pour toucher ; lancez seulement le de de degats.

Chaque Investigator commence avec 10 Health.

| Attaque | Degats |
|---|---|
| Mains nues | d4 |
| Objet improvise | d6 |
| Lame ou arme non letale | d8 |
| Arme letale | d10 |

Quand la Health atteint 0, la cible sort de la scene. La consequence exacte depend de l'arme et de la fiction : assommee, gravement blessee, mourante ou morte.

## Fin de partie

La partie se termine quand :

- le mystere est resolu ;
- toute l'energie du System representee par les Rewind Dice est depensee ;
- des Major Conflicts non resolus font s'effondrer le Now ;
- le Game Master appelle la resolution finale.

Fins possibles :

- **Convergence complete :** le mystere est resolu et le Now est coherent.
- **Convergence incomplete :** le Now est coherent, mais certaines verites restent inconnues.
- **Divergence psychologique :** la realite est stable, mais les Investigators se souviennent de trop de Branched Timelines impossibles.
- **Rupture causale :** la Main Timeline finale n'est plus coherente avec le Now originel ; la realite diverge de l'origine et la realite des Investigators est perdue.
