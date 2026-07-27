# Contributing to Causality

Causality is released under [CC0 1.0 Universal](./LICENSE) (public domain). Contributions of any kind are welcome.

## How to Contribute

### Report a Rule Issue

If you find an inconsistency, unclear wording, or a rule that does not work at the table:

1. Open an issue with the label `rules`.
2. Describe the problem and reference the specific document and section.
3. If possible, describe the situation that exposed the issue during play.

### Suggest a Balance Change

Causality is in active playtest. If you have data or experience suggesting a mechanic needs tuning:

1. Open an issue with the label `balance`.
2. Describe what happened during play.
3. Suggest a change and explain why.

### Submit a Scenario

New scenarios are welcome. Use the [Scenario Template](./docs/game-master-guide.md#scenario-template) as a starting point.

1. Create the English version in `docs/scenarios/`.
2. Name the file `scenario-name-gm-prep.md`.
3. If you can, create the French version in `i18n/fr/scenarios/`.

### Improve Documentation

Fix typos, clarify rules, improve examples, or add diagrams.

## Language and Terminology

- The **canonical language** is English. All files under `/docs/` are the authoritative versions.
- The **original design language** is French. Files under `/i18n/fr/` are maintained alongside the English versions.
- **Game terms** stay in English in every language: Main Timeline, Branched Timeline, Time Flow, Now, Time Unit, Atomic, System, Counter-System, Investigators, Time Offender, Rewind Dice, Rewind Percentage, Merged, Branched, Minor Conflict, Major Conflict, Evidence, Fact, Condition, Causal Table.

## Synchronization Workflow

When updating a rule or scenario:

1. Update the English canonical file first.
2. Propagate the change to the corresponding French file in `i18n/fr/`.
3. Keep game terms in English in the French version.
4. If the change affects dice tables, regenerate the abacus files using `scripts/simulate_dice_rolls.py --abacus`.

## File Naming Conventions

| Type | English Path | French Path |
|---|---|---|
| Scenario | `docs/scenarios/scenario-name-gm-prep.md` | `i18n/fr/scenarios/nom-scenario-preparation-mj.md` |
| Abacus | `docs/abacus/dN.md` | `i18n/fr/abaques/dN.md` |
| Core rules | `docs/game-design.md` | `i18n/fr/causalite-jeu-de-role.md` |
| GM guide | `docs/game-master-guide.md` | `i18n/fr/guide-maitre-de-jeu.md` |

## Code Style

The Python script in `scripts/` uses:

- Python 3.8+ with no external dependencies.
- Type hints and `dataclasses`.
- `secrets` module for cryptographic-quality random rolls.

## Questions

If you are unsure about a contribution, open an issue to discuss before submitting a pull request.
