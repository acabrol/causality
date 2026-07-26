# Simulation de partie

Ce document illustre une partie courte de **Causality** avec quatre joueurs et un **MJ**. Le texte est en francais, mais les mots-cles de jeu restent en anglais.

## Participants

| Role | Nom | Description |
|---|---|---|
| MJ | Morgan | Prepare la structure cachee, les preuves, les conflits et les consequences. |
| Investigator | Alice | Analyste methodique, forte en deduction. |
| Investigator | Bob | Ancien agent de securite, efficace sous pression. |
| Investigator | Charlie | Technicien du **System**, specialise dans les traces numeriques. |
| Investigator | Dana | Medecin de terrain, attentive aux temoins et aux blessures. |

## Situation initiale

Le **Time Flow** possede toujours **20 Atomic Time Units**. Le **Now** correspond a la **Time Unit 20**.

Dans cette simulation, les **Investigators** peuvent **rewind** vers une **Time Unit** complete, mais jamais vers une sous-periode situee a l'interieur d'une **Time Unit**.

La **Main Timeline** connue au debut de la partie contient :

```text
Time Unit 12 : le professeur Varen disparait.
Time Unit 16 : le laboratoire explose.
Time Unit 20 : les Investigators recoivent le dossier.
```

Le **MJ** prepare une structure cachee :

| ID | Condition | Event | Preuve |
|---|---|---|---|
| F01 | Le professeur Varen est vivant a Time Unit 12 | Varen cache une cle de securite | Fragment de message chiffre |
| F02 | La cle est recuperee par Mira | Mira active le protocole d'effacement | Logs du laboratoire |
| F03 | Le protocole d'effacement est actif | Le laboratoire explose a Time Unit 16 | Debris, rapport d'assurance |
| F04 | Varen parle a un Investigator avant Time Unit 12 | Varen ne cache pas la cle au meme endroit | Memoire divergente |
| F05 | L'assistant possede un acces discret au serveur a Time Unit 8 | L'assistant peut manipuler Mira | Journal d'acces efface |

Le **Time Flow** est ouvert par le **System**. Chaque **Investigator** recoit un set de des D&D classique : d4, d6, d8, d10, d10 percentile, d12 et d20.

Dans cette simulation, les d4, d6, d8, d10, d12 et d20 servent de **Rewind Dice**. Le d10 percentile sert aux tests de **Volonte**.

## Tour 1 - Alice ouvre une Branched Timeline

Alice veut comprendre pourquoi Varen disparait.

Elle choisit de **rewind** la **causality** jusqu'a **Time Unit 12**.

Distance depuis le **Now** :

```text
20 - 12 = 8 Time Units
```

Alice depense un `d8` comme **Rewind Die**.

Elle lance le `d8` et obtient `3`.

Sur un `d8` :

```text
1 : reussite critique
2-4 : reussite mitigee
5-7 : echec mitige
8 : echec critique
```

La **Branched Timeline** s'ouvre, mais avec une consequence negative. Alice lance un `d10` sur la table des consequences et obtient `8`.

Effet :

```text
La premiere action de l'Investigator cree un conflit mineur avec la Main Timeline connue.
```

Alice arrive a **Time Unit 12** dans le couloir du laboratoire. Elle intercepte Varen avant sa disparition et lui demande pourquoi il fuit.

Le **MJ** revele dans cette **Branched Timeline** :

```text
Varen cache une cle de securite parce qu'il pense que Mira veut detruire ses recherches.
```

Alice convainc Varen de lui donner la cle. Cette action cree un conflit mineur, car la **Main Timeline** connue suppose que la cle a ete cachee puis recuperee par Mira.

Statut :

```text
Branched Timeline A
Owner : Alice
Branched on : Time Unit 12
Status : open
Conflict : minor
```

## Fin du tour d'Alice - Volonte

Alice a :

- 1 **Branched Timeline** non **Merged** : `-30`
- 1 conflit mineur non resolu : `-20`

Calcul :

```text
turn modifier = 30 + 20 = 50
Willpower = 100 - 50 = 50
```

Alice garde une Volonte superieure a `0`.

## Tour 2 - Bob ouvre une Branched Timeline corrective

Bob pense que Mira est la cle du probleme. Il veut agir plus tot.

Il choisit **Time Unit 10**.

Distance :

```text
20 - 10 = 10 Time Units
```

Bob depense un `d10` comme **Rewind Die**.

Il obtient `1`.

Resultat :

```text
Reussite critique.
```

La **Branched Timeline** s'ouvre sans consequence negative.

Bob arrive a **Time Unit 10** et observe Mira. Il decouvre qu'elle recoit un message anonyme indiquant ou trouver la cle.

Bob ne modifie rien immediatement. Il suit Mira et identifie l'expediteur probable : un assistant du laboratoire.

Statut :

```text
Branched Timeline B
Owner : Bob
Branched on : Time Unit 10
Status : open
Conflict : none
```

## Fin du tour de Bob - Volonte

Bob a :

- 1 **Branched Timeline** non **Merged** : `-30`

Calcul :

```text
turn modifier = 30
Willpower = 100 - 30 = 70
```

## Tour 3 - Charlie utilise le d12

Charlie veut verifier si la manipulation de Mira commence avant les evenements visibles.

Il choisit **Time Unit 8**.

Distance :

```text
20 - 8 = 12 Time Units
```

Charlie depense un `d12` comme **Rewind Die**.

Il lance le `d12` et obtient `4`.

Sur un `d12` :

```text
1 : reussite critique
2-6 : reussite mitigee
7-11 : echec mitige
12 : echec critique
```

La **Branched Timeline** s'ouvre, mais avec une consequence negative. Charlie lance un `d10` sur la table des consequences et obtient `2`.

Effet :

```text
Les autorites locales, les gardes, les temoins ou les systemes de securite commencent a reagir a la presence de l'Investigator.
```

Charlie arrive a **Time Unit 8** dans les archives numeriques du laboratoire. Il declenche une alerte silencieuse, mais recupere un journal d'acces efface.

Le **MJ** revele dans cette **Branched Timeline** :

```text
L'assistant possede un acces discret au serveur avant la disparition de Varen.
```

Statut :

```text
Branched Timeline C
Owner : Charlie
Branched on : Time Unit 8
Status : open
Evidence : journal d'acces efface
```

## Fin du tour de Charlie - Volonte

Charlie a :

- 1 **Branched Timeline** non **Merged** : `-30`

Calcul :

```text
turn modifier = 30
Willpower = 100 - 30 = 70
```

## Tour 4 - Charlie tente un merge

Charlie ne cree pas de nouvelle **Branched Timeline**. Il analyse la carte du **Time Flow** via le **System**.

Il remarque que la **Branched Timeline A** d'Alice modifie la possession de la cle, et que la **Branched Timeline C** fournit une cause alternative possible avant la disparition de Varen.

Charlie propose un **merge** partiel de l'information :

```text
Fait candidat : Mira cherchait la cle avant l'explosion.
```

Le **MJ** accepte ce fait comme information, mais refuse de modifier la **Main Timeline** tant que le conflit mineur d'Alice n'est pas resolu.

Charlie aide Alice a resoudre son conflit mineur.

### Test de Volonte d'Alice

Alice veut imposer la version suivante :

```text
Alice a parle a Varen, mais Varen cache quand meme une fausse cle pour Mira.
```

Volonte actuelle d'Alice : `50`.

Difficulte moyenne :

```text
effective Willpower = 50
threshold = 100 - 50 = 50
```

Alice lance le d10 percentile et obtient `60`.

```text
60 >= 50 : succes
```

Le conflit mineur est resolu. La **Branched Timeline A** peut maintenant contenir :

```text
Varen donne la vraie cle a Alice.
Varen laisse une fausse cle pour Mira.
```

## Fin du deuxieme tour de Charlie - Volonte

Charlie a toujours 1 **Branched Timeline** non **Merged** et aucun conflit personnel.

```text
turn modifier = 30
Willpower = 70
```

## Tour 5 - Dana ouvre une Branched Timeline medicale

Dana veut sauver un temoin blesse pendant l'explosion.

Elle choisit **Time Unit 16**.

Distance :

```text
20 - 16 = 4 Time Units
```

Dana depense un `d4`.

Elle obtient `2`, donc une reussite mitigee.

Elle lance le `d10` de consequence et obtient `6`.

Effet :

```text
La Branched Timeline s'ouvre plus proche du Now que prevu.
Avancer le point de depart vers Time Unit 20 de la valeur du Rewind Die.
```

Le resultat du **Rewind Die** etait `2`.

La **Branched Timeline** devait s'ouvrir a **Time Unit 16**, mais elle s'ouvre finalement a :

```text
16 + 2 = Time Unit 18
```

Dana arrive trop tard pour empecher l'explosion. Elle peut cependant sauver un technicien gravement blesse qui possede un fragment de badge de Mira.

Statut :

```text
Branched Timeline D
Owner : Dana
Branched on : Time Unit 18
Status : open
Evidence : fragment de badge de Mira
```

## Fin du tour de Dana - Volonte

Dana a :

- 1 **Branched Timeline** non **Merged** : `-30`

Calcul :

```text
turn modifier = 30
Willpower = 100 - 30 = 70
```

## Tour 6 - Merge vers le Now

Les **Investigators** mettent en commun leurs informations :

- Alice possede la vraie cle.
- Varen a laisse une fausse cle.
- Bob sait que Mira a ete dirigee vers la cle.
- Charlie possede un journal d'acces efface montrant que l'assistant avait un acces discret au serveur.
- Dana possede un fragment de badge prouvant que Mira etait presente apres l'explosion.

Le groupe propose une correction de la **Main Timeline** :

```text
Time Unit 8 : l'assistant prepare un acces discret au serveur.
Time Unit 12 : Varen disparait volontairement.
Time Unit 13 : Mira recupere une fausse cle.
Time Unit 16 : le laboratoire explose car l'assistant active le protocole, pas Mira.
Time Unit 18 : Dana sauve un technicien temoin.
Time Unit 20 : le Now reste coherent, mais la responsabilite change.
```

Le **MJ** compare avec la structure cachee.

Le fait essentiel reste coherent :

```text
Le laboratoire explose a Time Unit 16.
```

Mais la cause change :

```text
Ancienne cause : Mira active le protocole.
Nouvelle cause : l'assistant active le protocole apres avoir manipule Mira.
```

Le **MJ** accepte le **merge**.

Les **Branched Timelines** A, B, C et D sont **Merged** sur le **Now**.

## Fin de sequence - Volonte

Les **Branched Timelines** de Alice, Bob, Charlie et Dana sont maintenant **Merged**.

Alice n'a plus de conflit mineur.

Calcul final :

| Investigator | Branched Timelines non Merged | Conflits majeurs | Conflits mineurs | Willpower |
|---|---:|---:|---:|---:|
| Alice | 0 | 0 | 0 | 100 |
| Bob | 0 | 0 | 0 | 100 |
| Charlie | 0 | 0 | 0 | 100 |
| Dana | 0 | 0 | 0 | 100 |

## Etat final

La **Main Timeline** finale est coherente avec le **Now** originel :

```text
Le laboratoire explose toujours a Time Unit 16.
Les preuves initiales restent explicables.
La cause reelle est mieux comprise.
Les Investigators conservent leur coherence mentale.
```

Fin obtenue :

```text
Convergence complete.
```

Le **Now** est preserve. La realite ne diverge pas de l'origine.
