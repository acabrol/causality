# Causality Quickstart

This guide gives you enough structure to run a first playtest of **Causality**.

Causality is inspired by [Continuum: Roleplaying in the Yet](http://www.aetherco.com/continuum/), with a different premise: players investigate causal chains and replay Branched Timelines rather than physically traveling through time.

## You Need

- 1 Game Master.
- 2 to 5 players.
- A whiteboard, large sheet of paper, or shared digital board.
- Index cards or sticky notes for facts, evidence, Branched Timelines, and conflicts.
- One classic D&D dice set for each Investigator: d4, d6, d8, d10, percentile d10, d12, and d20.
- Rewind Dice use the d4, d6, d8, d10, d12, and d20.
- Willpower tests use the percentile d10. The `00` face is worth `0`, not `100`.
- Damage rolls use the d4, d6, d8, and d10.

## Table Setup

Draw a Main Timeline with exactly 20 Atomic Time Units, then mark the Now as Time Unit 0. The Time Flow always has 20 prepared Time Units before the present.

```text
TU20 -- TU19 -- TU18 -- ... -- TU02 -- TU01 -- TU00 / Now
oldest                                      latest   present
```

Time Unit 20 is the oldest prepared causal state. Time Unit 1 is the latest prepared causal state before the present. The Now is Time Unit 0 at the start of the game. Every Time Unit is Atomic: players cannot rewind into a sub-period inside a Time Unit or choose a point between two Time Units. The scenario only defines what each full Time Unit represents: hours, days, years, or centuries.

## Game Master Prep

Prepare a hidden causal table:

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | A condition that must be true | A fact that happens | Trace produced by the fact |
| F02 | F01 is true | A later fact | A file, object, witness, memory, or recording |

Keep the full table hidden. Reveal only facts that the players can prove.

Prepare an initial case file with a few clues. Use those clues to place the first confirmed facts on the Main Timeline.

If the scenario uses a **Time Offender**, define them as a Game Master-controlled NPC adversary with one or more objectives opposed to the players. A Time Offender uses a System that works like the Investigators' System; this adversary System is usually called a **Counter-System**. Decide which Facts they protect or attack, what Evidence can reveal them, what Counter-System resources they can spend, and whether they act alone, collaborate with other Time Offenders, or compete against them.

## Character Setup

Give each investigator:

- a name and role;
- 100 maximum Willpower;
- current Willpower equal to 100;
- 10 Health;
- one classic D&D dice set, with the Rewind Dice representing personal System energy.

For a first test, all investigators are baseline humans. Adjust only if the scenario needs exceptional characters.

## How a Turn Works

On a turn, a player chooses one action:

1. investigate the current Main Timeline;
2. open a Branched Timeline from a known Time Unit;
3. continue a Branched Timeline;
4. attempt a merge;
5. work on a conflict.

When a player opens a Branched Timeline, they spend and roll a Rewind Die, draw the Branched Timeline from the chosen Time Unit, and describe what their character does in that replayed state.

## Rewind Dice

The Time Flow always has 20 Atomic Time Units. Any Rewind Die can be used for any rewind distance from `1` to `20` Time Units. Larger dice are safer on long rewinds, but they are not required.

| Rewind Die | Possible die values |
|---|---|
| d4 | 1-4 |
| d6 | 1-6 |
| d8 | 1-8 |
| d10 | 1-10 |
| d12 | 1-12 |
| d20 | 1-20 |

To open a Branched Timeline, choose a target Time Unit, count the rewind distance from the Now, and spend any available Rewind Die.

After spending the die, roll it and calculate the Rewind Percentage:

```text
Rewind Percentage = (Rewind Die result / rewind distance) x 100
```

High results are better because the die must cover the distance back from the Now. The result can exceed `100%`; any value of `80%` or more is still a critical success.

| Rewind Percentage | Outcome |
|---:|---|
| 80% or more | Critical success |
| 50-79% | Partial success with a consequence |
| 21-49% | Partial failure |
| 20% or less | Critical failure |

On a partial success, the Branched Timeline opens, but roll a d10 for a negative consequence.

| d10 | Negative consequence |
|---|---|
| 1 | Nearby people are frightened. |
| 2 | Local authorities or security notice something is wrong. |
| 3 | The investigator is pursued. |
| 4 | The Investigator arrives in the right Time Unit, but in the wrong place. |
| 5 | The investigator arrives separated from allies or without an expected tool. |
| 6 | The Branched Timeline opens closer to the Now than planned; lower the target Time Unit by the Rewind Die result, without passing Time Unit 0. |
| 7 | The first action leaves visible evidence of the intervention. |
| 8 | The first action creates a minor conflict with the known Main Timeline. |
| 9 | An important witness changes behavior after seeing the investigator. |
| 10 | The first action creates a major conflict with the known Main Timeline. |

On a partial failure, the action fails and no stable Branched Timeline opens. The Rewind Die is still spent, but the player rolls a d10 for a small gain.

| d10 | Small gain |
|---|---|
| 1 | Reveal one sensory detail from a relevant Evidence entry, without naming the Evidence. |
| 2 | Confirm that one named person, place, object, or group appears in a relevant Fact. |
| 3 | Mark one Evidence entry as false, misleading, planted, or incomplete. |
| 4 | Reveal the Time Unit that hosts one relevant Fact, without revealing the Fact. |
| 5 | Reveal one Condition required by the target Fact, without saying whether it is already satisfied. |
| 6 | Reveal one missing Evidence type needed to prove or merge the target Fact. |
| 7 | If a Time Offender is involved, reveal one trace of their method, tool, route change, or awareness state. |
| 8 | Reveal the required earlier event in fictional terms: who must act, what must happen, or what object/place must exist before the target Fact can become true. Do not reveal internal Fact IDs. |
| 9 | Reveal one conflict that would be created if the Investigator forced this failed branch open. |
| 10 | Reveal one concrete person, place, object, or record the Investigator can investigate next, tied to a known Condition, Fact, Evidence, or Time Offender trace. |

On a critical failure, no stable Branched Timeline opens, no small gain is rolled, and the Rewind Die is spent.

## Branched Timelines

A Branched Timeline is an alternate causal execution. Facts inside it are real to the character who experiences them, but they are not true on the shared Main Timeline until the Branched Timeline merges.

Record each Branched Timeline with:

- owner;
- starting Time Unit;
- new or changed facts;
- evidence produced;
- conflicts;
- status.

Do not erase Branched Timelines. They matter for memory, stress, and final divergence.

## Merges

When a player attempts a merge, the Game Master checks what the Branched Timeline changes:

- created facts;
- removed facts;
- modified facts;
- changed conditions;
- broken dependencies;
- evidence that appears or disappears.

If the Branched Timeline still allows the Now to make sense, compatible changes can be added to the Main Timeline.

## Conflicts

### Minor Conflict

A minor conflict changes a local or non-essential detail.

The player chooses which version they want to impose, then makes a Willpower roll:

```text
threshold = 100 - effective Willpower
percentile d10 result >= threshold = success
percentile d10 result < threshold = failure
```

On success, their chosen version is applied. On failure, the opposite version is applied.

### Major Conflict

A major conflict breaks an essential fact or makes the mystery impossible.

Major conflicts cannot be solved by a roll. Players must create another cause, open an earlier corrective Branched Timeline, or change the situation so the core fact becomes possible again.

## Willpower

At the end of each player's turn, recalculate Willpower for that player:

```text
current Willpower
= 100
- turn modifier
```

The turn modifier is:

```text
turn modifier
= 30 x non-Merged Branched Timelines
+ 40 x unresolved major conflicts
+ 20 x unresolved minor conflicts
+ other active Willpower penalties
```

The player must always keep current Willpower above 0 at the end of their turn. If the calculation reaches 0 or less, the character falls into madness and can no longer maintain coherence with the observable Now.

Difficulty changes effective Willpower before the threshold is calculated:

| Difficulty | Effective Willpower |
|---|---|
| Very easy | current Willpower x 10 |
| Easy | current Willpower x 2 |
| Average | current Willpower |
| Difficult | current Willpower / 2 |
| Very difficult | current Willpower / 4 |
| Impossible | current Willpower / 100 |

Truncate the effective Willpower value before calculating the threshold.

Non-Merged realities still exist in the character's memory. Too many non-Merged Branched Timelines make it harder to impose coherence.

## Fast Combat

All combat is resolved at human scale. Every attack that is declared and accepted by the fiction hits automatically. Do not roll to hit; roll only the damage die.

Each investigator starts with 10 Health.

| Attack category | Damage |
|---|---|
| Bare hands | d4 |
| Improvised object | d6 |
| Blade or non-lethal weapon | d8 |
| Lethal weapon | d10 |

When Health reaches 0, the target is out of the scene. The exact consequence depends on the weapon and the fiction: knocked out, badly wounded, dying, or dead.

## Ending the Game

The game ends when:

- the mystery is solved;
- all System energy represented by Rewind Dice is spent;
- unresolved major conflicts make the Now collapse;
- the Game Master calls final resolution.

Possible endings:

- **Complete convergence:** the mystery is solved and the Now is coherent.
- **Incomplete convergence:** the Now is coherent, but some truths remain unknown.
- **Psychological divergence:** reality is stable, but investigators remember too many impossible Branched Timelines.
- **Causal rupture:** the final Main Timeline is no longer coherent with the original Now, so reality diverges from the origin and the Investigators' reality is lost.
