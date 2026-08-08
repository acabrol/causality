# Guide du maitre de jeu

Ce guide explique comment creer et faire jouer un scenario de **Causality**. Il est destine au maitre de jeu et s'appuie sur les regles principales du document [Game Design](./causalite-jeu-de-role.md).

Utilise [Preparation MJ - Protocole Fievre de Verre](./scenarios/protocole-fievre-de-verre-preparation-mj.md) comme scenario recommande pour debuter. Il contient un mode simple sans `Time Offender`, puis un mode complet qui montre les mecaniques importantes.

## Objectif de conception

Un scenario de Causality est une enquete causale, pas un scenario lineaire. Le maitre de jeu prepare la structure cachee de ce qui a produit le `Now`; les `Investigators` decouvrent, testent, endommagent, corrigent et `Merged` des morceaux de cette structure au moyen de `Branched Timelines`.

Le but est de preparer assez de verite pour que la table puisse raisonner:

- ce qui est visible sur la `Main Timeline`;
- ce qui est cache dans la `Causal Table`;
- quelle `Evidence` peut prouver chaque `Fact`;
- quelles `Conditions` et dependances rendent chaque `Fact` possible;
- quelles modifications creent un `Minor Conflict` ou un `Major Conflict`;
- ce qui doit rester coherent quand une branche est `Merged` sur le `Now`.

Ne prepare pas toutes les solutions possibles. Prepare les causes, les indices, les contraintes et la pression, puis laisse les joueurs creer des causes de remplacement.

## Processus de creation d'un scenario

1. Definir le `Now`: l'etat present observable que le scenario doit expliquer.
2. Definir la question centrale: que doivent comprendre, prouver, empecher, conserver ou exposer les `Investigators`?
3. Choisir l'echelle du scenario: les 20 `Atomic` `Time Units` peuvent representer des heures, des jours, des annees ou des siecles.
4. Construire la `Main Timeline`: exactement 20 `Atomic` `Time Units`, de `TU20` comme evenement prepare le plus ancien a `TU01` comme dernier evenement avant le present, plus `TU00 / Now`.
5. Construire la `Causal Table` cachee: chaque `Fact` important recoit des `Conditions`, des dependances et de l'`Evidence`.
6. Preparer le briefing initial des joueurs: assez d'indices pour commencer, pas la solution cachee.
7. Construire les PNJ importants: leur role causal, ce qu'ils savent, ce qu'ils veulent, et comment ils peuvent produire ou cacher de l'`Evidence`.
8. Decider si le scenario utilise un ou plusieurs `Time Offenders`.
9. Preparer les conflits attendus et les conditions de merge.
10. Faire jouer les tours, mettre a jour les branches, recalculer la Charge mentale, puis auditer la `Main Timeline` finale.

## Construire la Main Timeline

La `Main Timeline` est la carte visible partagee par la table. Elle possede toujours 20 `Atomic` `Time Units` avant le present, plus le `Now`.

```text
TU20 -- TU19 -- TU18 -- ... -- TU02 -- TU01 -- TU00 / Now
le plus ancien                              recent   present
```

Chaque `Time Unit` est `Atomic`. Les joueurs ne peuvent pas entrer dans une sous-periode d'un `Time Unit`. Si `TU08` represente "la fenetre d'acces au laboratoire", le joueur peut faire un rewind vers `TU08`, pas vers "cinq minutes avant l'ouverture du congelateur" sauf si cette precision correspond a toute l'echelle de `TU08`.

Une bonne entree de `Time Unit` contient:

- un evenement visible ou decouvrable;
- un role causal cache;
- au moins une piste vers de l'`Evidence`;
- une raison pour laquelle l'evenement compte pour le `Now` final.

Format conseille:

| Time Unit | Visible or Discoverable Event | Objectif cache du MJ | Visibilite initiale |
|---|---|---|---|
| TU20 | Le premier evenement causal prepare. | Pose la premiere condition. | Cache, suspecte ou confirme. |
| TU08 | Le suspect obtient l'objet critique. | Permet une catastrophe ulterieure. | Cache jusqu'a preuve. |
| TU00 / Now | L'etat present observable. | Etat qui doit rester coherent. | Confirme. |

Garde la `Main Timeline` initiale incomplete. Les joueurs doivent voir des faits confirmes, des indices forts et des zones vides, pas toute la reponse.

## Construire la Causal Table

La `Causal Table` est la verite cachee du maitre de jeu. Elle n'est pas destinee aux joueurs. Elle indique ce qui doit etre vrai pour chaque `Fact` important et quelle `Evidence` peut le prouver.

Format conseille:

| ID | Time Unit | Condition Type | Conditions | Fact | Evidence | Notes MJ |
|---|---|---|---|---|---|---|
| F01 | TU18 | Simple | La porte du laboratoire est ouverte. | Le virologue entre dans le laboratoire. | Badge log, image camera. | Ouvre la chaine d'acces. |
| F02 | TU12 | Dependency | Dependency: F01. Le congelateur d'echantillons est actif. | L'echantillon est retire. | Ecart d'inventaire, alarme. | Necessaire pour l'epidemie finale. |
| F03 | TU05 | Dependency | Dependency: F02. La securite aeroportuaire rate le conteneur. | L'echantillon atteint la chaine de depart. | Billet, scan bagage. | Le bloquer peut creer un Major Conflict. |

Il existe deux types de conditions.

**Simple conditions** decrivent un etat requis du monde:

- la porte est ouverte;
- le temoin est vivant;
- l'echantillon existe;
- le dossier de police est falsifie;
- le `Time Offender` a acces a un lieu, une personne ou un objet.

**Dependency conditions** relient un `Fact` a un `Fact` antecedent:

- `F02` exige `F01`;
- le temoignage existe seulement si le temoin a vu l'evenement;
- l'epidemie existe seulement si l'echantillon sort du confinement;
- le `Now` existe seulement si la catastrophe historique a encore eu lieu.

Ecris les `Facts` comme des affirmations jouables. Un bon `Fact` peut etre empeche, remplace, prouve, protege, cache ou dangereux a modifier. Evite les faits vagues comme "la situation empire"; ecris plutot "les dossiers de securite identifient Alice comme l'assaillante".

## Preparer les indices et Evidence

Les joueurs decouvrent la structure cachee par l'`Evidence`. Chaque `Fact` important doit avoir au moins deux routes d'indice, afin qu'une branche ratee ou un temoin manque ne bloque pas la partie.

Types d'`Evidence` utiles:

- traces physiques: objet, cicatrice, debris, arme, echantillon biologique;
- documents: fichier, article, badge log, billet, inventaire;
- temoins: declaration, memoire, changement de comportement, contradiction;
- enregistrements: image camera, audio, radio, archive corrompue;
- traces du System: timestamp impossible, residu de `Counter-System`, nom repete, route modifiee;
- preuve negative: fichier manquant, trou camera, absence impossible.

Au debut de la partie, donne 3 a 6 indices a la table. De bons indices initiaux indiquent une action possible:

- un `Fact` confirme sur la `Main Timeline`;
- un `Time Unit` vide mais suspect;
- une personne, un lieu, un objet ou un dossier a examiner;
- une contradiction entre deux sources;
- une phrase, un symbole ou un evenement qui peut etre une fausse piste;
- une memoire, archive ou trace du System instable.

Pendant la partie, revele l'`Evidence` par:

- enquete sur la `Main Timeline` actuelle;
- `Branched Timelines` reussies;
- gains d'echec partiel;
- consequences de reussite partielle;
- analyse d'un merge echoue;
- traces de `Time Offender`;
- reactions de PNJ.

Ne donne pas les ID internes des `Facts` pendant la partie. Donne ce que les personnages peuvent comprendre dans la fiction: "le billet prouve que le suspect a change de porte apres l'alarme du laboratoire", pas "cela confirme F07".

## Construire les PNJ

La plupart des PNJ n'ont pas besoin d'une fiche complete. Construis-les d'abord comme des outils causaux: ils savent quelque chose, veulent quelque chose, bloquent quelque chose, produisent de l'`Evidence` ou incarnent une consequence.

Format conseille:

| PNJ | Role | Linked Facts | Conditions affectees | Evidence fournie | Ce qu'il sait | Ce qu'il veut | Health | Charge mentale |
|---|---|---|---|---|---|---|---:|---:|
| Temoin | A vu l'evenement. | F03, F04 | Doit etre vivant et accessible. | Declaration, memoire, photo. | Verite partielle. | Survivre. | 10 | 100 ou non suivie. |
| Suspect | Fausse piste. | F05 | Detourne de la vraie cause. | Manifeste, symbole, alibi. | Verite utile mais mal comprise. | Eviter l'arrestation. | 10 | 100 ou valeur de scenario. |

Les PNJ humains ordinaires ont generalement `10 Health`. Change cette valeur seulement si la fiction le justifie clairement.

Les PNJ n'ont pas de `Rewind Dice`. Leur Charge mentale est suivie seulement si l'histoire les expose a des `Branched Timelines`, des contradictions, de la pression memoire ou un effet direct du scenario. Si tu la suis, calcule-la a partir de ce que le PNJ a vraiment vecu ou observe.

Bons roles de PNJ:

- source d'indice;
- obstacle;
- faux coupable;
- victime;
- temoin;
- pression institutionnelle;
- ancre emotionnelle;
- gardien d'une condition;
- personne dont la survie ou la mort controle une dependance.

## Construire les Time Offenders

Un `Time Offender` est un PNJ adversaire controle par le maitre de jeu, avec un ou plusieurs objectifs opposes aux `Investigators`. Un scenario peut contenir un seul `Time Offender`, plusieurs `Time Offenders` qui collaborent, ou plusieurs `Time Offenders` qui se concurrencent.

Un `Time Offender` utilise un `System` qui fonctionne exactement comme celui des `Investigators`. On l'appelle souvent `Counter-System` pour distinguer les actions adverses a la table.

Prepare un `Time Offender` avec cette table:

| Champ | Question de preparation |
|---|---|
| Identite | Qui est-il dans l'histoire visible? |
| Vrai role | Quel probleme causal cree-t-il ou protege-t-il? |
| Objectifs | Que veut-il qui s'oppose aux joueurs? |
| Facts proteges | Quels `Facts` doit-il conserver? |
| Facts vises | Quels `Facts` veut-il effacer, falsifier ou corrompre? |
| Ressources Counter-System | Quels `Rewind Dice` possede-t-il, et sont-ils a usage unique? |
| Awareness | Que sait-il au debut? |
| Declencheurs d'identification | Quelles actions des joueurs revelent une anomalie temporelle? |
| Methodes | Comment met-il la pression par les facts, evidence, temoins ou conflits? |
| Traces | Quelle `Evidence` prouve son intervention? |
| Limites | Que ne peut-il pas savoir ou faire? |

Ne rends pas un `Time Offender` omniscient. Suis son niveau d'awareness.

| Awareness State | Declencheur | Usage MJ |
|---|---|---|
| Unaware of identities | Debut de partie ou avant qu'une preuve relie les joueurs aux anomalies. | Il suit son plan et protege ses facts clefs. |
| Alerted | Les joueurs creent des contradictions visibles, du timing impossible ou un savoir anormal. | Il cache l'evidence, change une route, trompe des temoins ou prepare la pression. |
| Identified target | Le `Time Offender` relie un joueur a une interference temporelle. | Il cible cet Investigator avec conflits, cadrage policier, routes modifiees ou pression de ressources. |

## Jouer les Time Offenders

Joue un `Time Offender` comme un adversaire dans les regles, pas comme une force illimitee du MJ. Il doit creer une pression que la table peut enqueter et contrer.

A chaque tour MJ pertinent, demande-toi:

1. Que sait actuellement le `Time Offender`?
2. Quel objectif est menace?
3. Quel `Fact`, `Evidence`, PNJ ou `Investigator` peut-il affecter?
4. L'action demande-t-elle le `Counter-System`, ou est-elle ordinaire?
5. Si elle demande le `Counter-System`, quel `Rewind Die` est depense et quel est le `Rewind Percentage`?
6. Quelle trace ou contradiction l'action laisse-t-elle?
7. Quel choix joueur devient plus interessant apres cette action?

Actions de `Time Offender` justes:

| Action | Usage mecanique | Evidence laissee |
|---|---|---|
| Cacher une preuve | Retarder la preuve d'un `Fact`. | Fichier manquant, trou camera, temoignage modifie. |
| Contaminer une preuve | Rendre un indice inutilisable pour un merge jusqu'a correction. | Timestamp contradictoire, dossier altere. |
| Accuser un Investigator | Ajouter un `Minor Conflict` a cet Investigator. | Rapport de police, description de temoin, alerte securite. |
| Aggraver un conflit | Transformer un `Minor Conflict` non resolu en `Major Conflict` si la fiction le soutient. | Dossier officiel, dependance brisee, fausse preuve. |
| Proteger une dependance | Deplacer, remplacer ou proteger une cause requise. | Route changee, objet substitue, nouveau garde. |
| Forcer la depense de ressources | Rendre une resolution propre dependante d'une nouvelle branche. | Indice qui pointe vers un autre `Time Unit`. |

### Heuristique de decision

Utilise ce tableau pour decider ce que le `Time Offender` fait a un tour MJ donne:

| Etat d'Awareness | Regle de depense | Action preferee |
|---|---|---|
| Unaware of identities | Ne depense aucun de de `Counter-System`. | Suivre son plan et proteger les `Facts` cles par des moyens ordinaires. |
| Alerted | Depenser le plus petit `Rewind Die` disponible, defensivement. | Cacher ou contaminer de l'`Evidence`, proteger une dependance, ajouter un `Minor Conflict`. |
| Identified target | Depenser le `Rewind Die` optimal pour la situation, offensivement. | Accuser un `Investigator`, aggraver un conflit, forcer la depense de ressources. |

Quand plusieurs objectifs sont menaces, priorise celui dont la perte exposerait le `Time Offender` le plus directement.

Le meilleur coup de `Time Offender` blesse et revele en meme temps. S'il efface un fichier, le fichier efface doit laisser un manque, un temoin incoherent ou un residu de `Counter-System`.

## Lancer la partie

A la table:

1. Annonce le `Now`.
2. Dessine les 20 `Atomic` `Time Units`.
3. Place seulement les facts d'ouverture confirmes sur la `Main Timeline`.
4. Donne le dossier initial.
5. Donne a chaque Investigator `0` de Charge mentale, `10 Health` et un set de des D&D classique.
6. Marque les `Rewind Dice` disponibles: d4, d6, d8, d10, d12, d20.
7. Explique que le d10 percentile sert aux jets de tentative d'action au de de pourcentage, que `00` vaut `0`, et que la Charge mentale est soustraite au resultat brut.
8. Garde la `Causal Table` cachee.
9. Demande quel indice les joueurs examinent en premier.

## Jouer les tours

L'ordre conseille est:

```text
MJ quand necessaire, puis Alice, Bob, Charlie, Dana, puis repetition.
```

Remplace les noms par ceux de ta table. Le MJ n'a pas besoin d'un tour rigide complet a chaque round; il intervient quand l'etat du jeu, les PNJ, un `Time Offender`, l'analyse de conflit ou la procedure de merge le demande.

Pendant le tour d'un joueur:

1. Rappelle sa branche actuelle, ses conflits, sa Health, sa Charge mentale et ses `Rewind Dice` restants.
2. Demande une action claire.
3. S'il enquete, revele seulement l'evidence accessible.
4. S'il ouvre une `Branched Timeline`, choisis le `Time Unit`, depense un `Rewind Die`, lance-le, calcule le `Rewind Percentage` et applique le resultat.
5. Si la branche s'ouvre, maintiens la coherence locale et joue la scene.
6. Note chaque nouveau `Visible or Discoverable Event` important cree dans la branche. Une seule branche peut creer plusieurs evenements.
7. Marque l'evidence produite et les conflits.
8. Si le joueur demande un merge, compare les facts, conditions, dependances et evidence modifies.
9. Resous les `Minor Conflicts` par choix et jet de tentative d'action au de de pourcentage.
10. Bloque les `Major Conflicts` tant qu'une cause corrective n'existe pas.
11. Recalcule la Charge mentale du joueur actif a la fin de son tour.

Calcul visible:

```text
Charge mentale
= 30 x non-Merged Branched Timelines
+ 40 x unresolved Major Conflicts
+ 20 x unresolved Minor Conflicts
+ other active Charge mentale penalties
```

Si le resultat est `100` ou plus, le personnage sombre dans la folie.

## Gerer les branches et merges

Suis chaque `Branched Timeline`. N'efface pas la pression fictionnelle simplement parce qu'une branche n'a pas merge.

Format conseille:

| Branch | Owner | Start Time Unit | Rewind Die | Rewind Result | Events Created | Evidence Produced | Conflicts | Status |
|---|---|---:|---|---|---|---|---|---|
| Alice_TU14 | Alice | 14 | d12 | 75%, partial success | Temoin deplace; fichier retrouve. | Declaration, copie de fichier. | Minor: alarme publique. | Open. |
| Bob_TU08 | Bob | 8 | d20 | 100%, critical success | Cause remplacee. | Lab log propre. | Aucun. | Merged. |

Statuts utiles:

- Open;
- Merged;
- blocked by `Minor Conflict`;
- blocked by `Major Conflict`;
- closed without merge;
- failed to open.

Un `Major Conflict` peut etre resolu par la branche d'un autre joueur. Une fois la cause corrective creee, l'ancienne branche peut devenir mergeable meme si son proprietaire ne peut plus agir. C'est important pour le jeu cooperatif.

## Checklist de merge

Quand un joueur demande un merge, verifie:

- Quels `Facts` ont ete crees?
- Quels `Facts` ont ete retires?
- Quels `Facts` ont ete modifies?
- Quelles `Conditions` ont change?
- Quelles dependency conditions sont brisees?
- Quelle `Evidence` apparait, disparait ou devient contradictoire?
- Le `Now` reste-t-il coherent?
- Est-ce un `Minor Conflict` ou un `Major Conflict`?
- Une autre branche peut-elle fournir une cause de remplacement?
- Que montre le System aux joueurs?

Merge seulement ce qui est coherent. Une branche peut reussir dans la fiction mais rester bloquee hors de la `Main Timeline`.

## Best practices du maitre de jeu

- Commence par un `Now` clair. Si l'etat present est flou, les joueurs ne peuvent pas raisonner causalement.
- Construis les facts comme des causes, pas comme du lore. Chaque entree importante doit affecter une autre entree.
- Garde la `Main Timeline` visible lisible. Mets la complexite dans les notes cachees.
- Donne de l'evidence aux joueurs, pas des reponses.
- Prevois au moins deux routes d'evidence pour chaque `Fact` critique.
- Rends les echecs partiels utiles. Ils doivent rater l'action mais donner une piste liee a `Condition`, `Fact`, `Evidence` ou `Time Offender`.
- Reserve les `Major Conflicts` aux contradictions structurelles. Trop de blocages majeurs rendent la partie immobile.
- Utilise les `Minor Conflicts` pour creer pression, temoins, dossiers, problemes de reputation et contradictions locales.
- Montre le calcul de Charge mentale a la fin de chaque tour joueur.
- Laisse les joueurs resoudre les gros problemes avec des causes de remplacement.
- Laisse la branche d'un joueur reparer le conflit d'un autre joueur.
- Garde les `Time Offenders` justes, limites et tracables.
- Ne punis pas les joueurs parce qu'ils n'ont pas devine la table cachee. Donne de nouvelles pistes quand ils testent une mauvaise theorie.
- Prefere l'evidence concrete: billet, cicatrice, log, fichier, personne, route, objet manquant.
- Utilise les [Abaques Rewind Dice](./abaques/README.md) pendant la partie pour ne pas ralentir la table.
- Utilise le scenario starter du `Protocole Fievre de Verre` avant les scenarios plus complexes.
- Termine clairement quand l'energie du `System` est depensee, le mystere resolu, la `Main Timeline` finale divergente du `Now` originel, ou la table arrive a un etat final fort.

## Template de scenario

Copie cette structure pour preparer un nouveau cas.

```markdown
# Nom du scenario - Preparation MJ

## Scenario Premise

## Core Game Master Truth

## Now

## Mystery Question

## Main Timeline

| Time Unit | Visible or Discoverable Event | Hidden GM Note |
|---|---|---|
| 20 |  |  |
| 19 |  |  |
| ... |  |  |
| 1 |  |  |
| 0 | Now:  |  |

## Initial Player Briefing

## Hidden Causal Table

| ID | Time Unit | Condition Type | Conditions | Fact | Evidence |
|---|---|---|---|---|---|

## Key Characters

| Character | Public Role | Real Function | Health | Charge mentale |
|---|---|---|---:|---:|

## Time Offenders

| Time Offender | Objectives | Counter-System Resources | Awareness | Traces |
|---|---|---|---|---|

## Expected Conflicts

| Trigger | Conflict Type | Why It Matters | How It Can Be Resolved |
|---|---|---|---|

## Merge Requirements

## Ending Conditions

## Play Trackers
```

## Checklist minimale avant de jouer

Avant de lancer la partie, assure-toi d'avoir:

- un `Now` clair;
- 20 `Atomic` `Time Units`;
- 8 a 15 `Facts` caches importants;
- au moins une route d'`Evidence` pour chaque `Fact`, et deux pour chaque `Fact` critique;
- des `Simple conditions` et `Dependency conditions` claires;
- 3 a 6 indices de depart;
- des PNJ avec un role dans la structure causale;
- des `Time Offenders` optionnels avec ressources de `Counter-System` limitees;
- des `Minor Conflicts` et `Major Conflicts` attendus;
- un tracker de branches;
- un tracker de Charge mentale;
- une regle de resolution finale pour succes, rupture, folie ou divergence non resolue.
