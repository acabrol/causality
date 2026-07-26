# Causality Quickstart

This guide gives you enough structure to run a first playtest of **Causality**.

Causality is inspired by [Continuum: Roleplaying in the Yet](http://www.aetherco.com/continuum/), with a different premise: players investigate causal chains and replay branches rather than physically traveling through time.

## You Need

- 1 Game Master.
- 2 to 5 players.
- A whiteboard, large sheet of paper, or shared digital board.
- Index cards or sticky notes for facts, evidence, branches, and conflicts.
- A small pool of dice for each investigator.

## Table Setup

Draw a main timeline with a fixed number of units. Twenty units is a good default.

```text
01 -- 02 -- 03 -- 04 -- ... -- 18 -- 19 -- 20
                                      PRESENT
```

Unit 20 is the present at the start of the game. Earlier units are earlier causal states. The scale can be anything the scenario needs: hours, days, years, or centuries.

## Game Master Prep

Prepare a hidden causal table:

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | A condition that must be true | A fact that happens | Trace produced by the fact |
| F02 | F01 is true | A later fact | A file, object, witness, memory, or recording |

Keep the full table hidden. Reveal only facts that the players can prove.

Prepare an initial case file with a few clues. Use those clues to place the first confirmed facts on the main timeline.

## Character Setup

Give each investigator:

- a name and role;
- maximum Willpower;
- current Willpower equal to maximum Willpower;
- a limited set of dice representing causal energy.

For a first test, use maximum Willpower 8 and a small personal dice pool. Adjust after play.

## How a Turn Works

On a turn, a player chooses one action:

1. investigate the current timeline;
2. open a branch from a known unit;
3. continue a branch;
4. attempt a merge;
5. work on a conflict.

When a player opens a branch, they spend causal energy, draw the branch from the chosen unit, and describe what their character does in that replayed state.

## Branches

A branch is an alternate causal execution. Facts inside it are real to the character who experiences them, but they are not true on the shared main timeline until the branch merges.

Record each branch with:

- owner;
- start unit;
- new or changed facts;
- evidence produced;
- conflicts;
- status.

Do not erase branches. They matter for memory, stress, and final divergence.

## Merges

When a player attempts a merge, the Game Master checks what the branch changes:

- created facts;
- removed facts;
- modified facts;
- changed conditions;
- broken dependencies;
- evidence that appears or disappears.

If the branch still allows the present to make sense, compatible changes can be added to the main timeline.

## Conflicts

### Minor Conflict

A minor conflict changes a local or non-essential detail.

The player chooses which version they want to impose, then makes a Willpower roll:

```text
die result < current Willpower = success
die result >= current Willpower = failure
```

On success, their chosen version is applied. On failure, the opposite version is applied.

### Major Conflict

A major conflict breaks an essential fact or makes the mystery impossible.

Major conflicts cannot be solved by a roll. Players must create another cause, open an earlier corrective branch, or change the situation so the core fact becomes possible again.

## Willpower

At the start of each turn, recalculate Willpower:

```text
current Willpower
= maximum Willpower
- unresolved branches owned by the character
- unresolved conflicts owned by the character
```

Unmerged realities still exist in the character's memory. Too many unresolved branches make it harder to impose coherence.

## Ending the Game

The game ends when:

- the mystery is solved;
- all causal energy is spent;
- unresolved major conflicts make the present collapse;
- the Game Master calls final resolution.

Possible endings:

- **Complete convergence:** the mystery is solved and the present is coherent.
- **Incomplete convergence:** the present is coherent, but some truths remain unknown.
- **Psychological divergence:** reality is stable, but investigators remember too many impossible branches.
- **Causal rupture:** the group fails to preserve a coherent resulting state.
