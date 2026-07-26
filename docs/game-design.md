# Causality Game Design

This document is the main English design reference for **Causality**, a cooperative causal-investigation tabletop RPG.

## Inspiration

Causality is inspired by [Continuum: Roleplaying in the Yet](http://www.aetherco.com/continuum/), the time-travel role-playing game published by Aetherco/Dreamcatcher.

The main influence is Continuum's serious treatment of temporal consequence, coherence, paradox pressure, and player responsibility across altered events. Causality uses that inspiration as a starting point, then changes the core premise: Investigators do not physically travel through time. They use the System to open the Time Flow, rewind causality, create Branched Timelines, and try to merge coherent resulting states back into the Now.

## 1. General Concept

**Causality** is a collaborative investigation role-playing game where the Investigators do not physically travel through time.

The setting is based on one rule:

> Time is not a dimension that can be crossed. The Now is the present observable state of the universe, produced by past causality.

The player characters are **Investigators**. They use a device called the **System**, which opens the **Time Flow**. The Time Flow is made of the Main Timeline and every Branched Timeline currently maintained by the System, all leading toward the Now.

Inside the Time Flow, every possible state of the universe on a given Time Unit is superposed. A Branched Timeline uses one possible state on that Time Unit, then lets an Investigator modify the evolution of causality from there.

Investigators can:

- rewind causality to a previous Time Unit;
- use a possible state on that Time Unit;
- create a Branched Timeline;
- act inside that Branched Timeline;
- try to merge the Branched Timeline back into the Now.

The goal is not to change the past. The goal is to understand and reconstruct the causes that explain the present while preserving the coherence of the observable world.

## 2. Core Vocabulary

Core game terms stay in English in every language version. In particular, use **Main Timeline**, **Branched Timeline**, **Time Flow**, **Now**, **Time Unit**, **System**, **Investigators**, **rewind**, **Branched**, **Merged**, and **causality** in both English and French documents.

### Time Flow

The **Time Flow** is the complete temporal structure opened and maintained by the System.

It contains:

- the Main Timeline;
- every active Branched Timeline;
- every accessible Time Unit;
- the Now, which is the present endpoint of the Time Flow.

### Now

The **Now** is the present observable state of the universe.

It is the state produced by past causality. At the beginning of the game, the Now is the original present state the Investigators must explain and preserve.

### Time Unit

A **Time Unit** is a numbered state inside the Time Flow.

The default Time Flow uses 20 Time Units. Time Unit 20 is the Now at the start of play.

### Main Timeline

The **Main Timeline** is the shared and currently observable timeline. It is the only timeline that persists after the System can no longer maintain the Time Flow.

### Branched Timeline

A **Branched Timeline** is an alternate causal execution created from a possible state on a Time Unit.

It is **Branched** on a Time Unit of the Time Flow and later attempts to be **Merged** on the Now.

### State

A **state** is an observable configuration of the world.

In play, each Time Unit on the causal map represents one state.

### Causality

**Causality** is the chain of relationships through which elements, actions, or facts transform one state into another.

```text
State A -> causality -> State B
```

### Past

The past is the set of causes that produced the Now.

### Present

The present is the Now: the single state currently observable by the Investigators.

It is not necessarily chosen or stable. It is simply the resulting state that observers can perceive.

### Future

The future is made of causes that have not happened yet.

It cannot be explored. Investigators can only explore existing causes or rewind past causality.

### Superposed States

When the System opens the Time Flow, it maintains several **possible states in superposition** on each accessible Time Unit.

Those states come from different causal chains. The causes themselves are not superposed; the possible states produced by those causes are.

### Resulting State

When the Time Flow closes, only one observable state remains: the **resulting state** on the Main Timeline.

## 3. The System

The **System** is the device that lets Investigators explore causality.

It can:

- open the Time Flow;
- rewind causality to a chosen Time Unit;
- inject Investigators into one possible state of that Time Unit;
- keep several causal Branched Timelines active;
- display the known Time Flow;
- compare a Branched Timeline with the Main Timeline;
- rerun causality toward the Now during a merge;
- detect conflicts;
- calculate remaining divergences during final resolution.

The System does not send characters into the physical past. It uses limited energy to keep the Time Flow open, rewind causality to specific Time Units, and maintain possible states that would otherwise be unobservable.

When an Investigator opens a Branched Timeline, the System selects one possible state on the target Time Unit. From that state, the Investigator changes the future evolution of causality toward the Now.

## 4. Investigator Rings

Each investigator has a ring connected to the System.

The rings allow Investigators to:

- consult the known causal map;
- know where the other investigators are;
- see active Branched Timelines;
- communicate with each other;
- identify facts validated on the Main Timeline;
- track conflicts and merges;
- measure remaining System energy and available Rewind Dice;
- track current Willpower.

The rings explain why the players share a collective view of the board.

## 5. Three Levels of Reality

### The Game Master's Hidden Structure

The Game Master prepares a hidden causal structure containing:

- prepared facts;
- conditions for those facts;
- causal relationships;
- evidence produced by facts;
- undiscovered elements.

This structure represents the mystery and its hidden causal logic. It is not the same thing as the visible Main Timeline.

### The Shared Main Timeline

The **Main Timeline** is the shared state currently observable by the players. It sits at the center of the table, for example on a whiteboard.

It contains a fixed number of Time Units, such as twenty:

- Time Unit 20 is the Now at the start of play;
- earlier Time Units represent earlier states;
- the real-world scale depends on the scenario. Twenty Time Units may represent a day, ten years, or several centuries.

Everything written on the Main Timeline is true in the current shared state.

Facts can come from two sources:

- a fact revealed and written by the Game Master;
- a fact created by a player and integrated through a successful merge.

A fact on the Main Timeline can later be modified by an earlier Branched Timeline and a new merge.

### Branched Timelines

A **Branched Timeline** is a temporary alternate causal state maintained by the System.

It is a proposed modification of the Main Timeline.

Facts in a Branched Timeline are real for the character who experiences them, but they do not automatically become shared facts. They must be merged.

## 6. Game Master Preparation

### Causal Map

The Game Master prepares a Main Timeline with a chosen number of Time Units and places important facts on the relevant Time Units.

Evidence can be placed where it is produced or discovered.

### Causal Table

The Game Master prepares a table like this:

| ID | Conditions | Fact | Evidence |
|---|---|---|---|
| F01 | The bomb is present and the detonator works | The laboratory explodes | Article, debris, witness accounts |
| F02 | F01 is true and the official investigation opens | A police investigation begins | Police file |
| F03 | Alice has the correct code | Alice defuses the bomb | Intact bomb, Alice's journal |

### Conditions

A condition defines what must be true for a fact to exist.

There are two main kinds of conditions.

**Simple conditions** describe the state of the world:

- the door is open;
- the bomb is present;
- Alice has the code;
- the laboratory is occupied.

**Dependency conditions** connect one fact to another:

- F02 requires F01 to be true;
- the report can only be published if the researcher is alive;
- the testimony requires the witness to have seen the event.

In graph form:

- nodes are facts;
- edges are dependencies between facts;
- simple conditions can be attached to nodes or relationships;
- each fact has a list of evidence.

### Facts

A fact is something that happens in a state:

- an explosion occurs;
- Alice opens the safe;
- a witness disappears;
- a report is published.

A consequence does not need to be a separate category. One fact can become a condition for a later fact.

### Evidence

Evidence is an observable trace produced by a fact:

- a photograph;
- a newspaper article;
- an object;
- a file;
- a witness statement;
- debris;
- a recording;
- a scar;
- a memory.

Players discover the hidden reality through evidence. They can also create new evidence through their actions.

## 7. Start of Play

The game starts at the Time Unit that represents the Now, such as Time Unit 20.

At the start:

- no Branched Timeline exists yet;
- the visible Main Timeline is partially empty;
- the Game Master gives the players an initial case file;
- the case file contains several pieces of evidence;
- the evidence reveals or places some facts on the Main Timeline.

The Game Master writes confirmed facts on the Main Timeline, not simple hypotheses.

Temporary facts created inside a Branched Timeline can be written on that Branched Timeline.

## 8. System Energy and Rewind Dice

The System has limited energy. That energy is distributed to the Investigators as **Rewind Dice**.

Each Rewind Die plays causality backward to reach a precise state of the universe on a Time Unit of the Time Flow. A Rewind Die can be spent to open a Branched Timeline and replay a shorter or longer portion of past causality.

### Rewind Dice

The Time Flow has **20 Time Units** by default. Rewind Dice correspond to the number of Time Units they can reach from the Now.

| Rewind Die | Maximum rewind distance |
|---|---|
| d4 | 4 Time Units |
| d6 | 6 Time Units |
| d8 | 8 Time Units |
| d10 | 10 Time Units |
| d20 | 20 Time Units |

To open a Branched Timeline, the player must spend a Rewind Die whose maximum value is equal to or higher than the number of Time Units between the Now and the target Time Unit. The player usually spends the smallest available die that can reach the target.

Example: from Time Unit 20, opening a Branched Timeline at Time Unit 16 requires a rewind of 4 Time Units, so a d4 is enough. Opening a Branched Timeline at Time Unit 11 requires a rewind of 9 Time Units, so it requires at least a d10.

### Branched Timeline Opening Roll

After choosing and spending the Rewind Die, the player rolls it. This is an inverted roll because the die represents playing causality backward: lower is better.

| Result | Outcome |
|---|---|
| 1 | Critical success |
| Lower than or equal to half the die maximum | Mitigated success with a consequence |
| Above half the die maximum | Mitigated failure |
| Maximum die result | Critical failure |

Examples:

| Die | Critical success | Mitigated success | Mitigated failure | Critical failure |
|---|---|---|---|---|
| d4 | 1 | 2 | 3 | 4 |
| d6 | 1 | 2-3 | 4-5 | 6 |
| d8 | 1 | 2-4 | 5-7 | 8 |
| d10 | 1 | 2-5 | 6-9 | 10 |
| d20 | 1 | 2-10 | 11-19 | 20 |

### Mitigated Success Consequences

When a Branched Timeline opening roll produces a mitigated success, the Branched Timeline opens, but the player rolls a d10 on this table.

| d10 | Negative consequence |
|---|---|
| 1 | **Frightened bystanders:** nearby people panic, flee, scream, call for help, or refuse to cooperate. |
| 2 | **Attention drawn:** local authorities, guards, witnesses, or security systems start reacting to the investigator's presence. |
| 3 | **Pursuit:** the investigator is actively pursued by authorities, security, or another local force as the Branched Timeline begins. |
| 4 | **Wrong entry point:** the Investigator arrives in the right Time Unit, but in the wrong place. They must reach the relevant scene. |
| 5 | **Separated or unprepared:** the investigator arrives separated from allies or without immediate access to an expected tool, object, or contact. |
| 6 | **Closer to the Now:** the Branched Timeline opens closer to the Now than planned. Move the starting Time Unit toward Time Unit 20 by the Rewind Die result, without passing Time Unit 20. |
| 7 | **Visible trace:** the investigator's first action leaves evidence of their intervention. This may complicate the merge. |
| 8 | **Minor conflict:** the investigator's first action creates a minor conflict with the known Main Timeline. |
| 9 | **Changed witness:** an important witness sees the investigator act and changes behavior inside this Branched Timeline. |
| 10 | **Major conflict:** the investigator's first action creates a major conflict with the known Main Timeline. The merge is blocked until a corrective cause is created. |

### Limited Resource

Spent Rewind Dice are not recovered while the Time Flow is open unless a specific rule allows it.

When all investigators have spent all Rewind Dice:

- the System can no longer maintain the Time Flow;
- non-observable states are no longer accessible;
- alternate states stop being observable;
- only the Main Timeline persists;
- final resolution begins.

This limit is the strategic clock of the game.

## 9. Turn Structure

On a turn, a player may:

1. act in their current Branched Timeline;
2. open a new Branched Timeline from an earlier Time Unit;
3. continue an existing Branched Timeline;
4. attempt to resolve a conflict;
5. request a merge for their Branched Timeline.

A Branched Timeline does not necessarily limit the number of narrative actions a player can take there. The main limit is the energy needed to open and maintain causal exploration.

To avoid downtime, narration can rotate between players even when they are in different Branched Timelines.

## 10. Creating a Branched Timeline

To create a Branched Timeline:

1. the player chooses a known or accessible Time Unit;
2. the player calculates the rewind distance from the Now to the target Time Unit;
3. the player spends a Rewind Die that can reach that distance;
4. the player rolls the Rewind Die and applies the Branched Timeline opening outcome;
5. the System rewinds causality to that Time Unit;
6. the Branched Timeline is Branched on the chosen Time Unit;
7. the character is injected into that causal execution;
8. the character acts;
9. the Game Master determines the facts and evidence produced.

### Local Coherence

While a Branched Timeline is played, the Game Master maintains **local coherence**.

The Game Master determines:

- what exists in that state;
- which conditions are satisfied;
- which facts can happen;
- which effects can be perceived;
- which evidence is produced.

The Branched Timeline may diverge from the Main Timeline. That is not immediately a failure; that divergence is the point of the exploration.

## 11. Branched Timeline Priority

Branched Timelines are ordered by the Time Units where they are Branched.

A Branched Timeline opened at Time Unit 14 can change a condition for an action performed in a Branched Timeline opened at Time Unit 15.

Example:

1. Alice opens a Branched Timeline at Time Unit 15.
2. She retrieves a code from a safe to defuse a bomb.
3. Another investigator opens a Branched Timeline at Time Unit 14.
4. They replace the paper in the safe with a fake code.
5. When causality is replayed, Alice now retrieves the fake code.
6. The bomb can explode as required by the current Main Timeline.

Branching earlier can change the conditions of later facts or later Branched Timelines.

## 12. Merge

A **merge** is an attempt to integrate facts from a Branched Timeline into the Main Timeline.

A Branched Timeline is Branched on a Time Unit and Merged on the Now.

Narratively, the System:

1. takes the modifications produced in the Branched Timeline;
2. replays causality from the starting Time Unit;
3. recalculates successive states;
4. compares the resulting state with the current Main Timeline;
5. detects incompatibilities;
6. integrates compatible changes.

The merge always moves back toward the Now, meaning the last Time Unit of the Main Timeline.

This is not travel into the future. The System simply re-executes causality up to the Now.

## 13. Merge Analysis

During a merge, the Game Master does not compare every narrative action.

The Game Master mainly compares:

- created facts;
- deleted facts;
- modified facts;
- modified conditions;
- invalidated causal dependencies;
- evidence that must appear or disappear.

### Causal Propagation

If a fact's condition is no longer met:

1. the fact becomes incompatible;
2. its evidence may disappear;
3. facts depending on it must be checked;
4. the conflict may propagate through the causal chain.

## 14. Major Conflicts

A conflict is **major** when a Branched Timeline modification contradicts a fact or causal structure prepared by the Game Master, or makes an essential element of the mystery impossible.

A major conflict:

- blocks the merge;
- cannot be overwritten by simple choice;
- cannot be solved by a die roll;
- requires additional causal action;
- must be handled in the current Branched Timeline or in a corrective Branched Timeline.

Example:

The Main Timeline contains this fact:

```text
Unit 16: the laboratory explodes.
```

Alice defuses the bomb in her Branched Timeline.

The Branched Timeline cannot merge until another compatible cause for the explosion has been created.

An investigator may open an earlier Branched Timeline to:

- replace Alice's code;
- add a second bomb;
- prevent Alice from reaching the safe;
- cause the explosion another way.

The major conflict disappears when the established fact becomes causally possible again.

## 15. Minor Conflicts

A conflict is **minor** when it opposes two facts that remain compatible with the essential structure of the scenario, such as:

- two player Branched Timelines modifying the same Time Unit;
- two possible versions of a non-structural event;
- a local modification that does not threaten the Game Master's core causal table.

In a minor conflict, the player chooses which version to impose:

- keep the Branched Timeline version;
- keep the current Main Timeline version.

The player then makes a Willpower roll.

If the roll succeeds, the player's choice is applied. If the roll fails, the opposite decision is applied.

If two Branched Timelines touch the same Time Unit or modify the same fact, the incompatibility is usually minor unless it affects a structural fact of the mystery.

## 16. Willpower

Each character has:

- **maximum Willpower**;
- **current Willpower**.

Willpower represents the character's ability to maintain coherence between what they experienced in Branched Timelines and the currently observable state.

By default, a human investigator starts with **maximum Willpower 100**.

At the start of each turn, current Willpower is recalculated:

```text
Current Willpower
= Maximum Willpower
- unresolved Branched Timelines belonging to that character
- unresolved conflicts belonging to that character
```

Only the character's own unresolved Branched Timelines and conflicts directly reduce their Willpower.

Example:

Alice has maximum Willpower 100. She has 2 unresolved Branched Timelines and 1 unresolved conflict.

```text
100 - 2 - 1 = 97
```

### Willpower Roll

To resolve a minor conflict, the player rolls a d100.

- If the result is strictly lower than current Willpower, the roll succeeds.
- If the result is equal to or higher than current Willpower, the roll fails.

Example with current Willpower 97 on a d100:

- 1 to 96: success;
- 97 to 100: failure.

A tie is a failure.

### Zero Willpower

If Willpower reaches zero, no roll can normally succeed with the strict lower-than rule.

This may represent:

- an inability to distinguish the observable state from divergent states;
- psychological rupture;
- an inability to impose a version during a merge.

The exact handling of zero Willpower still needs to be defined.

## 17. Human Scale and Fast Combat

By default, all investigators have normal human characteristics. The game does not use complex tactical combat by default, because combat is not the core challenge. When violence happens, it should resolve quickly and return attention to the investigation, the causal map, and the consequences of the action.

Each investigator starts with:

- **10 Health**;
- ordinary human physical limits unless the scenario says otherwise.

### Attack Resolution

Every attack that is declared and accepted by the fiction hits automatically. There is no roll to hit.

The attacker rolls only the damage die associated with the weapon category.

| Attack category | Damage die | Examples |
|---|---|---|
| Bare hands | d4 | punch, kick, shove into a wall |
| Improvised object | d6 | chair, bottle, tool, heavy book |
| Blade or non-lethal weapon | d8 | knife, baton, taser, trained restraint tool |
| Lethal weapon | d10 | firearm, explosive at close range, deadly industrial hazard |

Damage is subtracted from Health.

At 0 Health, the target is removed from the scene. The narrative consequence depends on the weapon and intent:

- bare hands or non-lethal force may knock the target out or disable them;
- blades and lethal weapons may leave the target dying or dead;
- the Game Master should turn the outcome into facts and evidence on the timeline or Branched Timeline.

## 18. Unresolved Branched Timelines and Psychological Divergence

No Branched Timeline is simply erased or forgotten.

All Branched Timelines stay drawn and visible until the end of the game.

A Branched Timeline can be:

- open;
- waiting for merge;
- merged;
- unresolved;
- blocked by a conflict.

An unmerged Branched Timeline remains a reality experienced by the character, but it is not part of the shared state.

The character keeps memories of facts that do not match the observable world. This divergence is the source of psychological degradation.

## 19. Final Resolution

When all System energy represented by Rewind Dice is consumed by the Time Flow:

1. the System can no longer maintain the Time Flow;
2. non-observable states are no longer accessible;
3. alternate Branched Timelines close;
4. only the Main Timeline persists;
5. the resulting state on the Now becomes the only observable state;
6. each character's divergences are calculated;
7. psychological consequences are applied;
8. the investigation is evaluated.

Facts experienced in unmerged Branched Timelines remain in the investigators' memories.

The number or weight of divergent facts may create final Willpower penalties or determine whether a character breaks psychologically.

If the final state of the Main Timeline is no longer coherent with the original Now defined at the beginning of the game, according to the Game Master's core events, the observed state is no longer the original Now. Reality diverges from the origin, and the Investigators' reality is lost.

## 20. Victory Conditions and Endings

### Complete Convergence

- The investigation is solved.
- The causes required by the Now are coherent.
- The resulting state matches the original Now or a coherent accepted Now.
- All investigators retain enough psychological continuity.
- Remaining divergences are absent or tolerable.

This is the best ending.

### Incomplete Convergence

- A coherent state remains observable.
- Part of the investigation remains unresolved.
- Some Branched Timelines or conflicts were not understood.

### Psychological Divergence

- The resulting state is coherent.
- One or more investigators remember too many states that are no longer observable.
- Their Willpower collapses or they break psychologically.

### Causal Rupture

- The players fail to produce a coherent resulting state.
- Major conflicts remain when the Time Flow closes.
- The final Main Timeline is no longer coherent with the original Now.
- Reality diverges from the origin, and the Investigators' reality is lost.

## 21. Table Layout

### Central Main Timeline

The shared Main Timeline is drawn at the center of the table.

```text
01 -- 02 -- 03 -- 04 -- ... -- 18 -- 19 -- 20
                                      PRESENT
```

The Game Master writes facts that have become true and observable.

### Branched Timelines

Players draw Branched Timelines above or below the Main Timeline.

```text
MAIN:      01 -- 02 -- 03 -- 04 -- 05 -- 06 -- ... -- 20
                          \
BRANCH A:                  A1 -- A2 -- A3 -- MERGE
                     \
BRANCH B:             B1 -- B2 -- MERGE
```

Branched Timelines are never erased. They are:

- the memory of the game;
- the history of attempts;
- traces of lived realities;
- the basis for calculating divergences.

Each Branched Timeline should show:

- owner;
- starting unit;
- created or modified facts;
- conflicts;
- status;
- energy cost;
- merge point, if any.

## 22. Game Master Role

The Game Master:

- prepares the causal table;
- prepares the fact graph;
- places initial evidence;
- keeps hidden information hidden;
- reveals discovered facts;
- writes validated facts on the Main Timeline;
- evaluates local Branched Timeline coherence;
- resolves damage and injury as facts when combat occurs;
- turns actions into facts;
- determines produced evidence;
- analyzes merges;
- identifies major and minor conflicts;
- propagates causal modifications;
- keeps the table readable.

The Game Master should not improvise everything or simulate everything. They focus on structural facts and their conditions.

## 23. Player Role

Players:

- study evidence;
- reconstruct facts;
- choose starting points;
- spend System energy through Rewind Dice;
- act inside Branched Timelines;
- create or modify facts;
- accept that violence creates facts, evidence, and possible causal consequences;
- cooperate to resolve conflicts;
- attempt merges;
- open corrective Branched Timelines;
- watch their Willpower;
- try to solve the investigation before the Time Flow closes.

Players can see:

- the shared Main Timeline;
- active Branched Timelines;
- other players' Branched Timelines;
- known facts;
- visible conflicts;
- remaining resources.

Players cannot see:

- hidden undiscovered facts;
- secret conditions;
- unknown evidence;
- the full causal graph prepared by the Game Master.

## 24. Main Loop

```text
1. Observe evidence and the Main Timeline.
2. Choose an investigation goal.
3. Pick a Time Unit.
4. Spend a Rewind Die to open a Branched Timeline.
5. Act in the Branched Timeline.
6. Create or modify facts.
7. Evaluate local coherence.
8. Attempt a merge.
9. Detect conflicts.
10. Resolve minor conflicts with choice and Willpower.
11. Resolve major conflicts through actions or corrective Branched Timelines.
12. Update the Main Timeline.
13. Recalculate Willpower.
14. Continue until resolution or Rewind Dice exhaustion.
15. Close the Time Flow and determine the resulting Main Timeline.
```

## 25. Mechanics Summary

| Element | Function |
|---|---|
| Time Unit | A state on the causal map inside the Time Flow |
| Main Timeline | Shared and currently observable state |
| GM structure | Hidden causal graph and facts of the investigation |
| Simple condition | World state required by a fact |
| Dependency condition | Causal link requiring another fact |
| Fact | Event or reality produced in a state |
| Evidence | Observable trace produced by a fact |
| Branched Timeline | Exploration of an alternate state |
| Rewind Die | Energy die used to open a Branched Timeline, from d4 to d20 |
| Health | Human physical resilience, default 10 |
| Damage die | The only die rolled in combat |
| Merge | Re-execution of causality up to the Now with modifications |
| Major conflict | Structural incompatibility requiring a corrective Branched Timeline |
| Minor conflict | Local opposition between versions, resolved by choice and Willpower |
| Willpower | Individual capacity to impose coherence |
| Unresolved Branched Timeline | Lived reality not integrated into the shared state |
| Closure | End of energy and disappearance of perceptible alternatives |
| Resulting state | The only observable state after closure |

## 26. Formulas

### Current Willpower

```text
Character current Willpower
= character maximum Willpower
- character unresolved Branched Timelines
- character unresolved conflicts
```

Default human investigator:

```text
Maximum Willpower = 100
```

### Minor Conflict Roll

```text
d100 result < current Willpower: success
d100 result >= current Willpower: failure
```

### Minor Conflict Resolution

```text
1. The player chooses the version they want to impose.
2. The player makes a Willpower roll.
3. On success, the player's choice is applied.
4. On failure, the opposite version is applied.
```

### Branched Timeline Opening

```text
rewind distance = Now Time Unit - target Time Unit
Required Rewind Die maximum >= rewind distance
```

```text
1 on Rewind Die: critical success
result <= half the die maximum: mitigated success with a consequence
result > half the die maximum: mitigated failure
maximum result on Rewind Die: critical failure
```

## 27. Short Example

The Main Timeline says:

```text
Time Unit 16: the laboratory explodes.
Time Unit 20: the Investigators begin their mission.
```

Evidence reveals that Alice had access to a defusal code.

### Alice's Branched Timeline

Alice opens a Branched Timeline at Time Unit 15.

She:

1. opens a safe;
2. retrieves the code;
3. defuses the bomb.

Her Branched Timeline creates this fact:

```text
Fact A: the bomb is defused.
```

But that makes this core fact impossible:

```text
Main fact: the laboratory explodes.
```

The merge is blocked by a major conflict.

### Corrective Branched Timeline

Another Investigator opens a Branched Timeline at Time Unit 14.

They:

1. enter the room with the safe;
2. replace the code with a fake;
3. leave the fake document in place.

When causality is replayed:

1. Alice retrieves the fake code;
2. she fails to defuse the bomb;
3. the explosion happens;
4. the fact at Time Unit 16 becomes possible again.

The corrective Branched Timeline resolves the major conflict.

## 28. Open Design Questions

These rules still need testing:

1. Does zero Willpower immediately cause psychological collapse?
2. How should divergent facts be weighted during final resolution?
3. Do all divergent facts count equally?
4. Are Rewind Dice personal, shared, or partly shared?
5. Does a Branched Timeline spend only one Rewind Die when opened, or does it also cost energy to maintain?
6. How should narrative time inside one Branched Timeline be limited?
7. How should several characters inside the same Branched Timeline be handled?
8. Can a player join another player's Branched Timeline?
9. What happens if a minor conflict becomes structural through propagation?
10. Can already observed evidence disappear from the Main Timeline?
11. How are player memories affected after a merge?
12. What are the exact consequences of each psychological divergence level?
13. Are the proposed Rewind Die outcomes balanced enough for repeated play?
14. Are the proposed combat damage dice balanced enough for repeated play?

## 29. Game Manifesto

> Time does not exist.
>
> The Now is the observable state produced by past causality.
>
> The future cannot be reached because its causes do not exist yet.
>
> The System does not travel back in time. It re-executes causality.
>
> A Branched Timeline explores another causal chain and produces another possible state.
>
> A merge re-executes causality up to the Now.
>
> When energy is exhausted, superposition stops being perceptible.
>
> Only one resulting state remains observable.
>
> The Investigators must discover the truth before the Time Flow closes.
