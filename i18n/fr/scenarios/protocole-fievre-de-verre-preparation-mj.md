# Protocole Fievre de Verre - Preparation MJ

Ce scenario original est le scenario recommande pour debuter avec **Causality**. Il existe en deux modes: une partie starter sans `Time Offender`, puis une partie complete avec adversaire temporel.

## Premisse

Dans le `Now` de 2142, les cites scellees survivent encore aux consequences d'une maladie de cristallisation pulmonaire apparue en 2117, la Fievre de Verre. Les `Investigators` recoivent une mission simple: comprendre si l'epidemie etait inevitable, identifier la vraie source, et revenir avec assez d'`Evidence` pour stabiliser un `Now` ou le remede existe sans effacer leur realite.

Le faux coupable visible est le `Meridian Choir`, un mouvement de liberation animale. Le vrai responsable est le docteur Ilya Voss, medecin materiaux venu du `Now`, qui utilise un `Counter-System` pour proteger sa propre origine.

## Verite du MJ

- Le `Meridian Choir` n'a pas libere la maladie.
- Voss est un `Time Offender` conscient et capable d'identifier les `Investigators`.
- Les ampoules de la Fievre de Verre passent par Morrow Pier.
- Supprimer completement l'epidemie sans cause de remplacement peut rendre le `Now` originel incoherent.
- La victoire stable consiste a exposer Voss, proteger l'`Evidence` medicale, et creer une cause de remede coherente.

## Main Timeline

| Time Unit | Visible or Discoverable Event | Note MJ |
|---:|---|---|
| 20 | Voss accede a une archive interdite du `System`. | Racine du `Counter-System`. |
| 19 | Une etude pulmonaire cotiere est lancee. | Premiere couverture medicale. |
| 18 | Le `Meridian Choir` organise des rituels publics. | Fausse piste. |
| 17 | Voss devient consultant d'une clinique portuaire. | Acces logistique. |
| 16 | Alice retrouve un dossier d'admission degrade. | Premier indice joueur. |
| 15 | Bob repere un conflit de cargaison a Morrow Pier. | Route des ampoules. |
| 14 | Charlie trouve des horodatages impossibles. | Trace du `Counter-System`. |
| 13 | Dana interroge une survivante du `Meridian Choir`. | Fausse piste fragilisee. |
| 12 | Le `Meridian Choir` est accuse publiquement. | Le faux coupable devient solide. |
| 11 | Voss securise une cargaison medicale. | Vraie preparation. |
| 10 | Un docker tousse des filaments de verre. | Premier cas. |
| 9 | Morrow Pier ferme. | L'`Evidence` devient difficile. |
| 8 | La premiere autopsie revele les cristaux. | Preuve medicale. |
| 7 | Voss cree une identite de voyage. | Fuite. |
| 6 | Trois villes declarent des cas. | Propagation. |
| 5 | Les `Investigators` convergent vers Morrow Pier. | Point de pression. |
| 4 | Voss deplace les ampoules par une clinique mobile. | Derniere fenetre. |
| 3 | Les cites se ferment. | Catastrophe observable. |
| 2 | Le conseil des survivants autorise la mission. | Cause des `Investigators`. |
| 1 | Le `System` ouvre le dossier Protocole Fievre de Verre. | Briefing. |
| 0 | `Now`: l'enquete commence. | Etat present. |

## Causal Table cachee

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | Simple: Voss a acces aux archives interdites. | Voss comprend comment proteger sa propre origine. | Journal d'acces, clef cryptee. |
| F02 | Dependency: F01. | Voss active un `Counter-System`. | Horodatages impossibles. |
| F03 | Simple: le `Meridian Choir` agit publiquement. | Les archives futures accusent le mauvais groupe. | Affiches, temoins, coupures. |
| F04 | Dependency: F02. | Voss place les ampoules sur Morrow Pier. | Inventaire portuaire. |
| F05 | Dependency: F04. | Le premier cas apparait chez un docker. | Dossier medical, prelevement. |
| F06 | Dependency: F03 et F05. | Les autorites blament le `Meridian Choir`. | Article officiel. |
| F07 | Dependency: F05. | L'autopsie revele la cristallisation. | Lame de microscope. |
| F08 | Dependency: F02. | Voss attaque les `Investigators` identifies. | Filature, fausse preuve. |
| F09 | Dependency: F07. | Une formule de remede devient deduisible. | Notes biologiques. |
| F10 | Dependency: F04 et F09. | La `Main Timeline` peut `Merged` vers un `Now` stable. | Dossier complet. |

## Personnages

| Personnage | Role | Willpower | Health | Rewind Dice |
|---|---|---:|---:|---|
| Alice | Investigator medicale | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Bob | Investigator logistique | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Charlie | Investigator technique | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Dana | Investigator sociale | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Ilya Voss | `Time Offender` | 100 | 10 | `Counter-System` |
| Mira Senn | Survivante temoin | 80 | 10 | Aucun |

## Conseils de deroule

En mode starter, Voss n'agit pas comme `Time Offender`: il est seulement la cause cachee. En mode complet, Voss utilise son `Counter-System` pour augmenter les conflits des `Investigators`, detruire l'`Evidence`, et proteger la fausse accusation du `Meridian Choir`.

Utilise les `Rewind Dice` avec la formule officielle: `Rewind Die result / rewind distance x 100`. Calcule la `Willpower` a la fin de chaque tour: `100 - 30 par Branched Timeline non Merged - 20 par Minor Conflict non resolu - 40 par Major Conflict non resolu`.

## Statistiques de reference

| Joueur | Branches | Merged | Minor restants | Major restants | Reussites critiques | Reussites partielles | Echecs partiels | Echecs critiques |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Alice | 2 | 1 | 0 | 1 | 1 | 1 | 0 | 0 |
| Bob | 2 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| Charlie | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| Dana | 2 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |

## GitGraph

Les points blancs correspondent aux `Merge` sur le `Now` de la branche `main`. Le carre blanc represente le `Now`.

```mermaid
gitGraph
  commit id: "TU20 Voss archive access"
  commit id: "TU19 Coastal lung study"
  commit id: "TU18 Meridian Choir public rituals"
  commit id: "TU17 Voss joins port clinic"
  commit id: "TU16 Alice finds intake record"
  branch Alice
  checkout Alice
  commit id: "Alice proves medical cover"
  checkout main
  commit id: "TU15 Bob traces Morrow cargo"
  branch Bob
  checkout Bob
  commit id: "Bob secures port manifest"
  checkout main
  commit id: "TU14 Charlie finds impossible timestamps"
  commit id: "TU13 Dana interviews survivor"
  commit id: "TU12 Choir blamed"
  branch Dana
  checkout Dana
  commit id: "Dana exposes false culprit" tag: "Minor witness panic"
  checkout main
  commit id: "TU11 Voss secures shipment"
  commit id: "TU10 First glass cough"
  branch Charlie
  checkout Charlie
  commit id: "Charlie isolates sample"
  checkout main
  commit id: "TU09 Pier closes"
  commit id: "TU08 Autopsy evidence"
  commit id: "TU07 Voss travel identity"
  commit id: "TU06 Three cities infected"
  commit id: "TU05 Investigators converge"
  commit id: "TU04 Voss moves ampoules" tag: "Major source hidden"
  commit id: "TU03 Sealed cities form"
  commit id: "TU02 Council authorizes mission"
  commit id: "TU01 System opens case"
  commit id: "Now"
  merge Bob
  merge Charlie
  merge Alice
```
