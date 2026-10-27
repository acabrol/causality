# Design Notes

This file preserves design decisions and directions translated from the French notes. Public-facing material is translated or adapted into the main English documents.

## Key Concepts

Causality is a cooperative causal-investigation tabletop role-playing game for **2 to 5 players and one Game Master**.

In the fiction, **time does not exist**: we perceive a coherent succession of causes. Each event follows from those before it; the System can unwind this sequence and replay it. The visual analogy is reversible flow in a viscous fluid.

The **System** combines the capabilities of a quantum computer with the mass and energy properties of a micro black hole. It results from the fictional application of the **general causality theorem**, which replaces the temporal component in the unification of quantum mechanics and spacetime.

It opens the **Causality Gate**, centered on the **Main Timeline**. The Gate is the opening; the **Time Flow** is the accessible causal structure. **Branch** is the short name for **Branched Timeline**. Investigators modify causal chains in a Branch, then attempt a **Merge** onto the Main Timeline to return to the **Now**.

**Rewind Dice** represent six **dark-energy capsules**, spent when opening Branches. The percentile d10 and damage rolls consume no capsule. Introducing these setting elements changes neither existing formulas nor game costs.

Experienced but unintegrated Branches increase the Investigator's cognitive load, measured by **Mental Load**. Changing a cause can destroy evidence or erase the conditions for Investigators' existence; accumulating incompatible realities can drive them into madness.

Expanded reference and Couette cell video: [Universe and System](./universe-and-system.md).

The **Main Timeline** and all **Branched Timelines** form the **Time Flow** up to the **Now**.

The **Time Flow** always has exactly **20 Time Units**. Each **Time Unit** is **Atomic**: **Investigators** cannot **rewind** into a sub-period of a **Time Unit**, or choose a point between two **Time Units**.

The **Now** is the present instant: the observable present state of the universe, produced by past **causality**.

The **System** uses its limited energy to open the **Causality Gate** and make the **Time Flow** accessible. It lets **Investigators** **rewind causality** to reach a precise **Time Unit** in the **Time Flow**.

A **Branched Timeline** is **Branched** on a **Time Unit** of the **Time Flow**. It uses a possible state of the universe at that **Time Unit**, then the **Investigator** modifies the evolution of **causality** from that state. The **Branched Timeline** then attempts to be **Merged** onto the **Now**.

Within the **Time Flow** maintained by the **System's** total energy, all possible states of the universe at a **Time Unit** are superposed.

When the **Time Flow** consumes all **System** energy, unobservable states become inaccessible. Only the **Main Timeline** persists.

If the final **Main Timeline** state is no longer coherent with its state at the beginning of the game, according to the Game Master's defined events, the observed state is no longer the original **Now**. Reality diverges from its origin and the **Investigators'** reality is lost.

A **Time Offender** is a GM-controlled NPC used as an adversary to the **Investigators**. They have one or more objectives opposed to the players: preserve a broken **Main Timeline**, produce a divergent **Now**, hide a **Fact**, destroy **Evidence**, impose unresolved conflicts, or drive the **Investigators** to exhaust **System** energy.

A **Time Offender** uses a **System** that works exactly like the **Investigators' System**. At the table, the adversary's **System** is often called a **Counter-System** to distinguish **Time Offender** activity from **Investigator** activity. Unless a scenario has a special rule, a **Counter-System** follows the same limits as the **Investigators' System**.

A scenario may contain no **Time Offender**, one, several collaborating **Time Offenders**, or several who compete, betray one another, or seek incompatible versions of the **Now**. They are not automatically omniscient: the GM tracks each one's knowledge, objectives, resources, limits, and identified **Investigators**.

A **Time Offender** acts through normal game structures: **Facts**, **Conditions**, **Evidence**, **Branched Timelines**, conflicts, **Mental Load** pressure, and scenario rules. They do not bypass **Rewind Dice**, **Merge** checks, damage, **Mental Load**, or **Time Flow** limits unless the scenario explicitly defines a special rule.

## Mental Load

- Characters start with **Mental Load 0**.
- Percentage action rolls use a single **percentile d10**.
- Its `00` face is worth `0`, not `100`.
- Mental Load is calculated at the end of the player's turn.
- `Mental Load = turn modifier`.
- A non-Merged Branched Timeline contributes `+30`.
- An unresolved major conflict contributes `+40`.
- An unresolved minor conflict contributes `+20`.
- The player must always have Mental Load strictly below `100` at the end of their turn.
- At `100` or more, the character falls into madness.
- Subtract Mental Load from the raw result of every percentage action roll.
- The test succeeds if the final result equals or exceeds the threshold.

Example:

```text
Mental Load: 30
Raw result: 80
Final result = 80 - 30 = 50
Threshold: 50
Final result 50: success
```

### Difficulty

For an action roll without its own threshold, use these thresholds.

| Difficulty | Threshold |
|---|---:|
| Very easy | 0 |
| Easy | 20 |
| Average | 50 |
| Difficult | 70 |
| Very difficult | 90 |
| Impossible | 100 |

Always subtract Mental Load from the raw result before comparing the final result with the threshold.

## Human Scale

All player characters have human characteristics by default.

For an initial version, a human character has:

- **10 Health**;
- ordinary physical abilities, unless the scenario specifies an exception.

## Rewind Dice

The **Time Flow** always has **20 Atomic Time Units**.

Each player receives a classic D&D dice set: d4, d6, d8, d10, percentile d10, d12, and d20.

The d4, d6, d8, d10, d12, and d20 are **Rewind Dice**. The percentile d10 is used for percentage action rolls. The d4, d6, d8, and d10 are used for damage.

Any **Rewind Die** may be used for any rewind distance from `1` to `20` **Time Units**. Die size does not grant permission to attempt a rewind; it changes the chances through the **Rewind Percentage** formula.

| Rewind Die | Possible Values |
|---|---|
| d4 | 1-4 |
| d6 | 1-6 |
| d8 | 1-8 |
| d10 | 1-10 |
| d12 | 1-12 |
| d20 | 1-20 |

To create a Branched Timeline, choose a target Time Unit, calculate the rewind distance from the Now, and spend any available Rewind Die. Since Now is Time Unit 0, rewind distance equals the target Time Unit value.

Roll the die, then compare the result with the actual rewind distance.

```text
Rewind Percentage = (Rewind Die result / rewind distance) x 100
```

Higher results are better, because the die must cover the distance from the Now. The result may exceed `100%`; any value of `80%` or more remains a critical success.

| Rewind Percentage | Outcome |
|---:|---|
| 80% or more | Critical success |
| 50-79% | Partial success with a consequence |
| 21-49% | Partial failure |
| 20% or less | Critical failure |

Example: from Now at Time Unit 0 to Time Unit 2, rewind distance is `2`. On a d4, a `1` gives `50%`, a partial success. A `2`, `3`, or `4` gives at least `100%`, a critical success.

Example: from Now at Time Unit 0 to Time Unit 19, rewind distance is `19`. On a d20, `16` to `20` is a critical success; `10` to `15` is a partial success; `4` to `9` is a partial failure; and `1` to `3` is a critical failure.

A d20 can therefore be spent on a rewind of `2` Time Units if it is the only remaining Rewind Die. Conversely, a d4 can be spent on a rewind of `19` Time Units, but cannot reach `50%`, so it cannot open a stable Branched Timeline at that distance.

## Negative Consequences of Partial Success

When a Branched Timeline opening roll produces a partial success, the Branched Timeline opens, but the player rolls a d10 on this table.

| d10 | Negative Consequence |
|---|---|
| 1 | **Frightened bystanders:** nearby people panic, flee, scream, call for help, or refuse to cooperate. |
| 2 | **Attention drawn:** local authorities, guards, witnesses, or security systems react. |
| 3 | **Pursuit:** authorities, security, or another local force pursues the Investigator as the Branched Timeline begins. |
| 4 | **Wrong entry point:** the Investigator arrives in the correct Time Unit but the wrong place and must reach the relevant scene. |
| 5 | **Separated or unprepared:** the Investigator arrives separated from allies or without immediate access to an expected tool, object, or contact. |
| 6 | **Closer to the Now:** the Branched Timeline opens closer to the Now than intended. Reduce the starting Time Unit by the Rewind Die result, without passing Time Unit 0. |
| 7 | **Visible trace:** the Investigator's first action leaves evidence of the intervention, which may complicate the merge. |
| 8 | **Minor conflict:** the first action creates a minor conflict with the known Main Timeline. |
| 9 | **Changed witness:** an important witness sees the Investigator act and changes behavior in this Branched Timeline. |
| 10 | **Major conflict:** the first action creates a major conflict with the known Main Timeline. The merge is blocked until a corrective cause is created. |

## Small Gains of Partial Failure

When a **Branched Timeline** opening roll produces a partial failure, the action fails and no stable **Branched Timeline** opens. The **Rewind Die** is still spent, but the player rolls a d10 on this table for a small gain.

| d10 | Small Gain |
|---|---|
| 1 | **Evidence sensory detail:** reveal one sensory detail from relevant Evidence, without naming the Evidence. |
| 2 | **Fact participant confirmed:** confirm that one named person, place, object, or group appears in a relevant Fact. |
| 3 | **Evidence status marked:** mark one Evidence entry as false, misleading, planted, or incomplete. |
| 4 | **Fact Time Unit located:** reveal the Time Unit hosting a relevant Fact, without revealing the Fact. |
| 5 | **Condition exposed:** reveal one Condition required by the target Fact, without saying whether it is already satisfied. |
| 6 | **Missing Evidence type:** reveal the Evidence type needed to prove or merge the target Fact. |
| 7 | **Time Offender trace:** if one is involved, reveal a trace of their method, tool, route change, or awareness state. |
| 8 | **Dependency clue:** describe the required earlier event in fictional terms: who must act, what must happen, or what object or place must exist before the target Fact can be true. Do not reveal internal Fact IDs. |
| 9 | **Conflict preview:** reveal one conflict that forcing this failed branch open would create. |
| 10 | **Immediate lead:** reveal one concrete person, place, object, or record to investigate next, linked to a known Condition, Fact, Evidence, or Time Offender trace. |

## Simplified Combat

To keep play flowing, every attack hits if the action is accepted by the fiction.

There is no attack roll. Roll only damage.

| Attack Category | Damage Die | Examples |
|---|---|---|
| Bare hands | d4 | punch, kick, throw |
| Improvised object | d6 | chair, bottle, tool, heavy book |
| Blade or non-lethal weapon | d8 | knife, baton, taser, restraint tool |
| Lethal weapon | d10 | firearm, nearby explosion, deadly industrial hazard |

Subtract damage from Health.

At 0 Health, the target leaves the scene. The exact consequence depends on the weapon and fiction: unconsciousness, serious injury, dying, or death.
