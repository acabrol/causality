# Contribuer a Causality

Causality est publie sous [CC0 1.0 Universal](../../LICENSE) (domaine public). Les contributions de toute nature sont bienvenues.

## Comment contribuer

### Signaler un probleme de regle

Si vous trouvez une incoherence, une formulation peu claire ou une regle qui ne fonctionne pas a la table :

1. Ouvrez une issue avec le label `rules`.
2. Decrivez le probleme et citez le document et la section concernes.
3. Si possible, decrivez la situation de jeu qui a revele le probleme.

### Proposer un changement d'equilibrage

Causality est en playtest actif. Si vous avez des donnees ou une experience indiquant qu'une mecanique doit etre ajustee :

1. Ouvrez une issue avec le label `balance`.
2. Decrivez ce qui s'est passe pendant la partie.
3. Proposez un changement et expliquez pourquoi.

### Soumettre un scenario

Les nouveaux scenarios sont bienvenus. Utilisez le [template de scenario](./guide-maitre-de-jeu.md#template-de-scenario) comme point de depart.

1. Creez la version anglaise dans `docs/scenarios/`.
2. Nommez le fichier `scenario-name-gm-prep.md`.
3. Si possible, creez la version francaise dans `i18n/fr/scenarios/`.

### Ameliorer la documentation

Corrigez les fautes, clarifiez les regles, ameliorez les exemples ou ajoutez des diagrammes.

## Langue et terminologie

- La **langue canonique** est l'anglais. Les fichiers sous `/docs/` sont les versions publiques de reference.
- La **langue de conception originale** est le francais. Les fichiers sous `/i18n/fr/` sont maintenus avec les versions anglaises.
- Les **termes de jeu** restent en anglais dans toutes les langues : Main Timeline, Branched Timeline, Time Flow, Now, Time Unit, Atomic, System, Counter-System, Investigators, Time Offender, Rewind Dice, Rewind Percentage, Merged, Branched, Minor Conflict, Major Conflict, Evidence, Fact, Condition, Causal Table.

## Workflow de synchronisation

Quand vous mettez a jour une regle ou un scenario :

1. Mettez d'abord a jour le fichier anglais canonique.
2. Repercutez le changement dans le fichier francais correspondant sous `i18n/fr/`.
3. Gardez les termes de jeu en anglais dans la version francaise.
4. Si le changement affecte les tables de des, regenerez les abaques avec `scripts/simulate_dice_rolls.py --abacus`.

## Conventions de nommage

| Type | Chemin anglais | Chemin francais |
|---|---|---|
| README | `README.md` | `i18n/fr/README.md` |
| Contribution | `CONTRIBUTING.md` | `i18n/fr/CONTRIBUTING.md` |
| Scenario | `docs/scenarios/scenario-name-gm-prep.md` | `i18n/fr/scenarios/nom-scenario-preparation-mj.md` |
| Abaque | `docs/abacus/dN.md` | `i18n/fr/abaques/dN.md` |
| Regles centrales | `docs/game-design.md` | `i18n/fr/causalite-jeu-de-role.md` |
| Guide MJ | `docs/game-master-guide.md` | `i18n/fr/guide-maitre-de-jeu.md` |
| Quickstart | `docs/quickstart.md` | `i18n/fr/quickstart.md` |
| Fiche Investigator | `docs/investigator-sheet.md` | `i18n/fr/fiche-investigator.md` |

## Style de code

Le script Python dans `scripts/` utilise :

- Python 3.8+ sans dependance externe ;
- des type hints et `dataclasses` ;
- le module `secrets` pour des jets aleatoires de qualite cryptographique.

## Questions

Si vous avez un doute sur une contribution, ouvrez une issue pour en discuter avant de soumettre une pull request.
