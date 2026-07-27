# Simulation de partie

Ce fichier est conserve comme index francais des simulations de partie.

Les deroules jouables officiels sont maintenus dans les scenarios, car ils doivent utiliser strictement les regles actuelles de **Causality** :

- [Protocole Fievre de Verre](scenarios/protocole-fievre-de-verre-preparation-mj.md) : scenario recommande pour debuter. Il contient un mode starter et un mode complet.
- [Bataillon Cendre](scenarios/bataillon-cendre-preparation-mj.md)
- [L'enfant de l'horloger](scenarios/enfant-de-l-horloger-preparation-mj.md)
- [Temoin de fer](scenarios/temoin-de-fer-preparation-mj.md)
- [Piege des archives publiques](scenarios/piege-des-archives-publiques-preparation-mj.md)

Chaque deroule de scenario utilise le script `scripts/simulate_dice_rolls.py`, applique la formule actuelle des **Rewind Dice**, puis recalcule les statistiques de partie a la fin du scenario.
