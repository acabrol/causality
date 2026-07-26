# Causality Game Design

This document is the main English design reference for **Causality**, a cooperative causal-investigation tabletop RPG.

## Inspiration

Causality is inspired by [Continuum: Roleplaying in the Yet](http://www.aetherco.com/continuum/), the time-travel role-playing game published by Aetherco/Dreamcatcher.

The main influence is Continuum's serious treatment of temporal consequence, coherence, paradox pressure, and player responsibility across altered events. Causality uses that inspiration as a starting point, then changes the core premise: investigators do not physically travel through time. They replay causality, create branches, and try to merge coherent resulting states.

## 1. General Concept

**Causality** is a collaborative investigation role-playing game where characters do not physically travel through time.

The setting is based on one rule:

> Time is not a dimension that can be crossed. The present is the observable state of the world, produced by all past causal chains.

The player characters are **causal investigators**. They use a device called **the System**, which can temporarily open a **probability window**. Inside that window, several possible states can coexist, each produced by a different chain of causes.

Investigators can:

- replay part of the past causal chain;
- return to an earlier state;
- create a causal branch;
- act inside that branch;
- try to merge the branch back into the present.

The goal is not to change the past. The goal is to understand and reconstruct the causes that explain the present while preserving the coherence of the observable world.

## 2. Core Vocabulary

### State

A **state** is an observable configuration of the world.

In play, each unit on the causal map represents one state.

### Cause

A **cause** is a relationship through which an element, action, or fact transforms one state into another.

```text
State A -> cause -> State B
```

### Past

The past is the set of causes that produced the present state.

### Present

The present is the single state currently observable by the investigators.

It is not necessarily chosen or stable. It is simply the resulting state that observers can perceive.

### Future

The future is made of causes that have not happened yet.

It cannot be explored. Investigators can only explore existing causes or replay past causal chains.

### Superposed States

When the System opens a probability window, it maintains several **possible states in superposition**.

Those states come from different causal chains. The causes themselves are not superposed; the possible states produced by those causes are.

### Resulting State

When the probability window closes, only one observable state remains: the **resulting state**.

## 3. The System

The **System** is the device that lets investigators explore causality.

It can:

- open a probability window;
- replay a portion of past causes;
- inject investigators into a reproduction of an earlier state;
- keep several causal branches active;
- display the known causal map;
- compare a branch with the main timeline;
- rerun causes toward the present during a merge;
- detect conflicts;
- calculate remaining divergences during final resolution.

The System does not send characters into the physical past. It **re-executes past causal chains from a chosen state**, then lets investigators intervene in that new execution.

## 4. Investigator Rings

Each investigator has a ring connected to the System.

The rings allow investigators to:

- consult the known causal map;
- know where the other investigators are;
- see active branches;
- communicate with each other;
- identify facts validated on the main timeline;
- track conflicts and merges;
- measure remaining causal energy;
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

This structure represents the mystery and its hidden causal logic. It is not the same thing as the visible main timeline.

### The Shared Main Timeline

The **main timeline** is the shared state currently observable by the players. It sits at the center of the table, for example on a whiteboard.

It contains a fixed number of units, such as twenty:

- unit 20 is the present at the start of play;
- earlier units represent earlier states;
- the real-world scale depends on the scenario. Twenty units may represent a day, ten years, or several centuries.

Everything written on the main timeline is true in the current shared state.

Facts can come from two sources:

- a fact revealed and written by the Game Master;
- a fact created by a player and integrated through a successful merge.

A fact on the main timeline can later be modified by an earlier branch and a new merge.

### Branches

A **branch** is a temporary alternate causal state maintained by the System.

It is a proposed modification of the main timeline.

Facts in a branch are real for the character who experiences them, but they do not automatically become shared facts. They must be merged.

## 6. Game Master Preparation

### Causal Map

The Game Master prepares a main timeline with a chosen number of units and places important facts on the relevant units.

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

The game starts at the unit that represents the present, such as unit 20.

At the start:

- no branch exists yet;
- the visible main timeline is partially empty;
- the Game Master gives the players an initial case file;
- the case file contains several pieces of evidence;
- the evidence reveals or places some facts on the main timeline.

The Game Master writes confirmed facts on the main timeline, not simple hypotheses.

Temporary facts created inside a branch can be written on that branch.

## 8. Causal Energy and Dice

Dice represent the energy required to keep the probability window open.

Each character has a limited number of dice. A die can be spent to open a branch and replay a shorter or longer portion of past causality.

### Jump Range

The size or value of a die can represent a budget of causal units.

One possible approach:

- each die provides a unit budget;
- the cost depends on the distance between the present and the target unit;
- the farther the causal point is, the stronger the required die must be.

The exact scale must be balanced through playtesting.

### Limited Resource

Spent dice are not recovered during the probability window unless a specific rule allows it.

When all investigators have spent all dice:

- the System can no longer maintain superpositions;
- the probability window closes;
- alternate states stop being observable;
- final resolution begins.

This limit is the strategic clock of the game.

## 9. Turn Structure

On a turn, a player may:

1. act in their current branch;
2. open a new branch from an earlier unit;
3. continue an existing branch;
4. attempt to resolve a conflict;
5. request a merge for their branch.

A branch does not necessarily limit the number of narrative actions a player can take there. The main limit is the energy needed to open and maintain causal exploration.

To avoid downtime, narration can rotate between players even when they are in different branches.

## 10. Creating a Branch

To create a branch:

1. the player chooses a known or accessible unit;
2. the player spends the required die or energy;
3. the System replays causes up to that state;
4. a branch is drawn from the chosen unit;
5. the character is injected into that causal execution;
6. the character acts;
7. the Game Master determines the facts and evidence produced.

### Local Coherence

While a branch is played, the Game Master maintains **local coherence**.

The Game Master determines:

- what exists in that state;
- which conditions are satisfied;
- which facts can happen;
- which effects can be perceived;
- which evidence is produced.

The branch may diverge from the main timeline. That is not immediately a failure; that divergence is the point of the exploration.

## 11. Branch Priority

Branches are ordered by the units where they begin.

A branch opened at unit 14 can change a condition for an action performed in a branch opened at unit 15.

Example:

1. Alice opens a branch at unit 15.
2. She retrieves a code from a safe to defuse a bomb.
3. Another investigator opens a branch at unit 14.
4. They replace the paper in the safe with a fake code.
5. When causality is replayed, Alice now retrieves the fake code.
6. The bomb can explode as required by the current main timeline.

Branching earlier can change the conditions of later facts or later branches.

## 12. Merge

A **merge** is an attempt to integrate facts from a branch into the main timeline.

Narratively, the System:

1. takes the modifications produced in the branch;
2. replays causality from the branch point;
3. recalculates successive states;
4. compares the resulting state with the current main timeline;
5. detects incompatibilities;
6. integrates compatible changes.

The merge always moves back toward the present, meaning the last unit of the main timeline.

This is not travel into the future. The System simply re-executes causality up to the present state.

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

A conflict is **major** when a branch modification contradicts a fact or causal structure prepared by the Game Master, or makes an essential element of the mystery impossible.

A major conflict:

- blocks the merge;
- cannot be overwritten by simple choice;
- cannot be solved by a die roll;
- requires additional causal action;
- must be handled in the current branch or in a corrective branch.

Example:

The main timeline contains this fact:

```text
Unit 16: the laboratory explodes.
```

Alice defuses the bomb in her branch.

The branch cannot merge until another compatible cause for the explosion has been created.

An investigator may open an earlier branch to:

- replace Alice's code;
- add a second bomb;
- prevent Alice from reaching the safe;
- cause the explosion another way.

The major conflict disappears when the established fact becomes causally possible again.

## 15. Minor Conflicts

A conflict is **minor** when it opposes two facts that remain compatible with the essential structure of the scenario, such as:

- two player branches modifying the same unit;
- two possible versions of a non-structural event;
- a local modification that does not threaten the Game Master's core causal table.

In a minor conflict, the player chooses which version to impose:

- keep the branch version;
- keep the current main timeline version.

The player then makes a Willpower roll.

If the roll succeeds, the player's choice is applied. If the roll fails, the opposite decision is applied.

If two branches touch the same unit or modify the same fact, the incompatibility is usually minor unless it affects a structural fact of the mystery.

## 16. Willpower

Each character has:

- **maximum Willpower**;
- **current Willpower**.

Willpower represents the character's ability to maintain coherence between what they experienced in branches and the currently observable state.

At the start of each turn, current Willpower is recalculated:

```text
Current Willpower
= Maximum Willpower
- unresolved branches belonging to that character
- unresolved conflicts belonging to that character
```

Only the character's own unresolved branches and conflicts directly reduce their Willpower.

Example:

Alice has maximum Willpower 8. She has 2 unresolved branches and 1 unresolved conflict.

```text
8 - 2 - 1 = 5
```

### Willpower Roll

To resolve a minor conflict, the player rolls the system's Willpower die.

- If the result is strictly lower than current Willpower, the roll succeeds.
- If the result is equal to or higher than current Willpower, the roll fails.

Example with current Willpower 5 on a d10:

- 1 to 4: success;
- 5 to 10: failure.

A tie is a failure.

### Zero Willpower

If Willpower reaches zero, no roll can normally succeed with the strict lower-than rule.

This may represent:

- an inability to distinguish the observable state from divergent states;
- psychological rupture;
- an inability to impose a version during a merge.

The exact handling of zero Willpower still needs to be defined.

## 17. Unresolved Branches and Psychological Divergence

No branch is simply erased or forgotten.

All branches stay drawn and visible until the end of the game.

A branch can be:

- open;
- waiting for merge;
- merged;
- unresolved;
- blocked by a conflict.

An unmerged branch remains a reality experienced by the character, but it is not part of the shared state.

The character keeps memories of facts that do not match the observable world. This divergence is the source of psychological degradation.

## 18. Final Resolution

When all causal energy represented by dice is spent:

1. the System can no longer maintain the probability window;
2. the superposition of possible states stops being perceptible;
3. alternate branches close;
4. the resulting state becomes the only observable state;
5. each character's divergences are calculated;
6. psychological consequences are applied;
7. the investigation is evaluated.

Facts experienced in unmerged branches remain in the investigators' memories.

The number or weight of divergent facts may create final Willpower penalties or determine whether a character breaks psychologically.

The exact final scale still needs to be defined.

## 19. Victory Conditions and Endings

### Complete Convergence

- The investigation is solved.
- The causes required by the present are coherent.
- The resulting state matches the desired present.
- All investigators retain enough psychological continuity.
- Remaining divergences are absent or tolerable.

This is the best ending.

### Incomplete Convergence

- A coherent state remains observable.
- Part of the investigation remains unresolved.
- Some branches or conflicts were not understood.

### Psychological Divergence

- The resulting state is coherent.
- One or more investigators remember too many states that are no longer observable.
- Their Willpower collapses or they break psychologically.

### Causal Rupture

- The players fail to produce a coherent resulting state.
- Major conflicts remain when the window closes.
- The present can no longer be explained by the remaining causes.
- Investigators or elements of the initial state may disappear.

## 20. Table Layout

### Central Main Timeline

The shared main timeline is drawn at the center of the table.

```text
01 -- 02 -- 03 -- 04 -- ... -- 18 -- 19 -- 20
                                      PRESENT
```

The Game Master writes facts that have become true and observable.

### Branches

Players draw branches above or below the main timeline.

```text
MAIN:      01 -- 02 -- 03 -- 04 -- 05 -- 06 -- ... -- 20
                          \
BRANCH A:                  A1 -- A2 -- A3 -- MERGE
                     \
BRANCH B:             B1 -- B2 -- MERGE
```

Branches are never erased. They are:

- the memory of the game;
- the history of attempts;
- traces of lived realities;
- the basis for calculating divergences.

Each branch should show:

- owner;
- starting unit;
- created or modified facts;
- conflicts;
- status;
- energy cost;
- merge point, if any.

## 21. Game Master Role

The Game Master:

- prepares the causal table;
- prepares the fact graph;
- places initial evidence;
- keeps hidden information hidden;
- reveals discovered facts;
- writes validated facts on the main timeline;
- evaluates local branch coherence;
- turns actions into facts;
- determines produced evidence;
- analyzes merges;
- identifies major and minor conflicts;
- propagates causal modifications;
- keeps the table readable.

The Game Master should not improvise everything or simulate everything. They focus on structural facts and their conditions.

## 22. Player Role

Players:

- study evidence;
- reconstruct facts;
- choose branch points;
- spend causal energy;
- act inside branches;
- create or modify facts;
- cooperate to resolve conflicts;
- attempt merges;
- open corrective branches;
- watch their Willpower;
- try to solve the investigation before the window closes.

Players can see:

- the shared main timeline;
- active branches;
- other players' branches;
- known facts;
- visible conflicts;
- remaining resources.

Players cannot see:

- hidden undiscovered facts;
- secret conditions;
- unknown evidence;
- the full causal graph prepared by the Game Master.

## 23. Main Loop

```text
1. Observe evidence and the main timeline.
2. Choose an investigation goal.
3. Pick a causal unit.
4. Spend a die to open a branch.
5. Act in the branch.
6. Create or modify facts.
7. Evaluate local coherence.
8. Attempt a merge.
9. Detect conflicts.
10. Resolve minor conflicts with choice and Willpower.
11. Resolve major conflicts through actions or corrective branches.
12. Update the main timeline.
13. Recalculate Willpower.
14. Continue until resolution or dice exhaustion.
15. Close the window and determine the resulting state.
```

## 24. Mechanics Summary

| Element | Function |
|---|---|
| Unit | A state on the causal map |
| Main timeline | Shared and currently observable state |
| GM structure | Hidden causal graph and facts of the investigation |
| Simple condition | World state required by a fact |
| Dependency condition | Causal link requiring another fact |
| Fact | Event or reality produced in a state |
| Evidence | Observable trace produced by a fact |
| Branch | Exploration of an alternate state |
| Die | Energy required to open or maintain alternatives |
| Merge | Re-execution of causality up to the present with modifications |
| Major conflict | Structural incompatibility requiring a corrective branch |
| Minor conflict | Local opposition between versions, resolved by choice and Willpower |
| Willpower | Individual capacity to impose coherence |
| Unresolved branch | Lived reality not integrated into the shared state |
| Closure | End of energy and disappearance of perceptible alternatives |
| Resulting state | The only observable state after closure |

## 25. Formulas

### Current Willpower

```text
Character current Willpower
= character maximum Willpower
- character unresolved branches
- character unresolved conflicts
```

### Minor Conflict Roll

```text
Die result < current Willpower: success
Die result >= current Willpower: failure
```

### Minor Conflict Resolution

```text
1. The player chooses the version they want to impose.
2. The player makes a Willpower roll.
3. On success, the player's choice is applied.
4. On failure, the opposite version is applied.
```

## 26. Short Example

The main timeline says:

```text
Unit 16: the laboratory explodes.
Unit 20: the investigators begin their mission.
```

Evidence reveals that Alice had access to a defusal code.

### Alice's Branch

Alice opens a branch at unit 15.

She:

1. opens a safe;
2. retrieves the code;
3. defuses the bomb.

Her branch creates this fact:

```text
Fact A: the bomb is defused.
```

But that makes this core fact impossible:

```text
Main fact: the laboratory explodes.
```

The merge is blocked by a major conflict.

### Corrective Branch

Another investigator opens a branch at unit 14.

They:

1. enter the room with the safe;
2. replace the code with a fake;
3. leave the fake document in place.

When causality is replayed:

1. Alice retrieves the fake code;
2. she fails to defuse the bomb;
3. the explosion happens;
4. the fact at unit 16 becomes possible again.

The corrective branch resolves the major conflict.

## 27. Open Design Questions

These rules still need testing:

1. Which die is used for Willpower rolls?
2. What is the exact scale of maximum Willpower?
3. Does zero Willpower immediately cause psychological collapse?
4. How should divergent facts be weighted during final resolution?
5. Do all divergent facts count equally?
6. What is the exact branch cost based on distance?
7. Are dice personal, shared, or partly shared?
8. Does a branch spend only one die when opened, or does it also cost energy to maintain?
9. How should narrative time inside one branch be limited?
10. How should several characters inside the same branch be handled?
11. Can a player join another player's branch?
12. What happens if a minor conflict becomes structural through propagation?
13. Can already observed evidence disappear from the main timeline?
14. How are player memories affected after a merge?
15. What are the exact consequences of each psychological divergence level?

## 28. Game Manifesto

> Time does not exist.
>
> The present is the observable state produced by past causes.
>
> The future cannot be reached because its causes do not exist yet.
>
> The System does not travel back in time. It re-executes causality.
>
> A branch explores another causal chain and produces another possible state.
>
> A merge re-executes causality up to the present.
>
> When energy is exhausted, superposition stops being perceptible.
>
> Only one resulting state remains observable.
>
> The investigators must discover the truth before the window closes.
