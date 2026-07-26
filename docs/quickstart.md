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

Draw a Main Timeline with exactly 20 Time Units. The Time Flow always has 20 Time Units.

```text
01 -- 02 -- 03 -- 04 -- ... -- 18 -- 19 -- 20
                                      PRESENT
```

Time Unit 20 is the Now at the start of the game. Earlier Time Units are earlier causal states. Every Time Unit is Atomic: players cannot rewind into a sub-period inside a Time Unit or choose a point between two Time Units. The scenario only defines what each full Time Unit represents: hours, days, years, or centuries.

## Game Master Prep

Prepare a hidden causal table:

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | A condition that must be true | A fact that happens | Trace produced by the fact |
| F02 | F01 is true | A later fact | A file, object, witness, memory, or recording |

Keep the full table hidden. Reveal only facts that the players can prove.

Prepare an initial case file with a few clues. Use those clues to place the first confirmed facts on the Main Timeline.

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

The Time Flow always has 20 Atomic Time Units. Rewind Dice define how far back from the Now a player can open a Branched Timeline.

| Rewind Die | Maximum distance |
|---|---|
| d4 | 4 Time Units |
| d6 | 6 Time Units |
| d8 | 8 Time Units |
| d10 | 10 Time Units |
| d12 | 12 Time Units |
| d20 | 20 Time Units |

To open a Branched Timeline, choose a target Time Unit and count the rewind distance from the Now. Spend a Rewind Die whose maximum is equal to or higher than that distance.

After spending the die, roll it. Lower is better.

| Result | Outcome |
|---|---|
| 1 | Critical success |
| Less than or equal to half the die maximum | Mitigated success with a consequence |
| Greater than half the die maximum | Mitigated failure |
| Maximum die result | Critical failure |

On a mitigated success, the Branched Timeline opens, but roll a d10 for a negative consequence.

| d10 | Negative consequence |
|---|---|
| 1 | Nearby people are frightened. |
| 2 | Local authorities or security notice something is wrong. |
| 3 | The investigator is pursued. |
| 4 | The Investigator arrives in the right Time Unit, but in the wrong place. |
| 5 | The investigator arrives separated from allies or without an expected tool. |
| 6 | The Branched Timeline opens closer to the Now than planned; move it toward Time Unit 20 by the Rewind Die result. |
| 7 | The first action leaves visible evidence of the intervention. |
| 8 | The first action creates a minor conflict with the known Main Timeline. |
| 9 | An important witness changes behavior after seeing the investigator. |
| 10 | The first action creates a major conflict with the known Main Timeline. |

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
= 10 x non-Merged Branched Timelines
+ 10 x unresolved major conflicts
+ 5 x unresolved minor conflicts
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
