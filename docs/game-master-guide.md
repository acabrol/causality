# Game Master Guide

This guide explains how to create and run a **Causality** scenario. It is written for the Game Master and assumes the main rules in [Game Design](./game-design.md).

Use [Glass Fever Protocol](./scenarios/glass-fever-protocol-gm-prep.md) as the recommended starter scenario. It contains a simple playthrough without a `Time Offender`, then a complete playthrough that demonstrates the full rules surface.

## Design Goal

A Causality scenario is a causal investigation, not a scripted plot. The Game Master prepares the hidden structure of what caused the `Now`; the `Investigators` discover, test, damage, repair, and merge pieces of that structure through `Branched Timelines`.

The goal is to prepare enough truth for the table to reason about:

- what is visible on the `Main Timeline`;
- what is hidden in the `Causal Table`;
- what `Evidence` can prove each `Fact`;
- which `Conditions` and dependencies make each `Fact` possible;
- which changes create `Minor Conflict` or `Major Conflict`;
- what must remain coherent when a branch is `Merged` on the `Now`.

Do not prepare every possible player solution. Prepare causal pressure, evidence, and constraints, then let the players create replacement causes.

## Scenario Creation Workflow

1. Define the `Now`: the present observable state the scenario must explain.
2. Define the central mystery: what do the `Investigators` need to understand, prove, prevent, preserve, or expose?
3. Choose the scenario scale: the 20 `Atomic` `Time Units` may represent hours, days, years, or centuries.
4. Build the `Main Timeline`: exactly 20 `Atomic` `Time Units`, from `TU20` as the oldest prepared event to `TU01` as the latest event before the present, plus `TU00 / Now`.
5. Build the hidden `Causal Table`: each important `Fact` gets `Conditions`, dependencies, and `Evidence`.
6. Prepare the initial player briefing: give enough clues to start action, but not the hidden solution.
7. Build important NPCs: give each one a causal role, what they know, what they want, and how they can produce or hide `Evidence`.
8. Decide whether the scenario uses one or more `Time Offenders`.
9. Prepare expected conflicts and merge requirements.
10. Run turns, update branches, recalculate Willpower, and audit the final `Main Timeline`.

## Build The Main Timeline

The `Main Timeline` is the shared visible table map. It always has 20 `Atomic` `Time Units` before the present, plus the `Now`.

```text
TU20 -- TU19 -- TU18 -- ... -- TU02 -- TU01 -- TU00 / Now
oldest                                      latest   present
```

Every `Time Unit` is `Atomic`. Players cannot enter a smaller period inside a `Time Unit`. If `TU08` represents "the laboratory access window", the player can rewind to `TU08`, not to "five minutes before the freezer opens" unless that smaller moment is the whole scale of `TU08`.

A good `Time Unit` entry contains:

- a visible or discoverable event;
- a hidden causal role;
- at least one route toward `Evidence`;
- a reason the event matters to the final `Now`.

Use this table format:

| Time Unit | Visible or Discoverable Event | Hidden GM Purpose | Starting Visibility |
|---|---|---|---|
| TU20 | The earliest prepared causal event. | Establishes the first condition. | Hidden, suspected, or confirmed. |
| TU08 | The suspect gains access to the critical object. | Enables a later disaster. | Hidden until evidence is found. |
| TU00 / Now | The present observable state. | The state that must remain coherent. | Confirmed. |

Keep the starting `Main Timeline` incomplete. The players should see confirmed facts, strong clues, and blank spaces, not the full answer.

## Build The Causal Table

The `Causal Table` is the Game Master's hidden truth. It is not player-facing. It tells you what must be true for each important `Fact` to exist and what `Evidence` can prove it.

Use this format:

| ID | Time Unit | Condition Type | Conditions | Fact | Evidence | GM Notes |
|---|---|---|---|---|---|---|
| F01 | TU18 | Simple | The lab door is unlocked. | The virologist enters the lab. | Badge log, camera frame. | Opens access chain. |
| F02 | TU12 | Dependency | Dependency: F01. The sample freezer is active. | The sample is removed. | Inventory gap, freezer alarm. | Required for final outbreak. |
| F03 | TU05 | Dependency | Dependency: F02. Airport security misses the container. | The sample reaches the departure chain. | Ticket record, baggage scan. | Blocking this may create a Major Conflict. |

There are two condition types.

**Simple conditions** describe a required state of the world:

- the door is open;
- the witness is alive;
- the sample exists;
- the police file is falsified;
- the `Time Offender` has access to a place, person, or object.

**Dependency conditions** connect one `Fact` to an earlier `Fact`:

- `F02` requires `F01`;
- the testimony exists only if the witness saw the event;
- the outbreak exists only if the sample left containment;
- the `Now` exists only if the historical catastrophe still happened.

Write `Facts` as playable statements. A good `Fact` can be prevented, replaced, proven, protected, hidden, or made dangerous to alter. Avoid vague facts like "things get worse"; write "security records identify Alice as the attacker".

## Prepare Evidence

Players discover the hidden structure through `Evidence`. Every important `Fact` should have at least two evidence routes, so a failed branch or missed witness does not stop the game.

Useful `Evidence` types include:

- physical traces: object, scar, debris, weapon, biological sample;
- documents: file, article, badge log, ticket, inventory record;
- witnesses: testimony, memory, behavior change, contradiction;
- recordings: camera frame, audio, radio traffic, corrupted archive;
- System traces: impossible timestamp, `Counter-System` residue, repeated name, altered route;
- negative evidence: missing file, erased camera gap, impossible absence.

At the start of play, give the table 3 to 6 clues. Good starting clues point to action:

- one confirmed `Fact` on the `Main Timeline`;
- one suspicious blank `Time Unit`;
- one person, place, object, or record to investigate;
- one contradiction between evidence sources;
- one phrase, symbol, or event that might be a false lead;
- one unstable memory, archive, or System trace.

During play, reveal evidence through:

- investigation on the current `Main Timeline`;
- successful `Branched Timelines`;
- partial failure gains;
- consequences of partial successes;
- failed merge analysis;
- `Time Offender` traces;
- NPC reactions.

Do not reveal internal `Fact` IDs to players during play. Say what the characters can learn in the fiction: "the ticket proves the suspect changed gates after the lab alarm", not "this confirms F07".

## Build NPCs

Most NPCs do not need a full character sheet. Build them as causal tools first: they know things, want things, block things, produce evidence, or embody consequences.

Use this table:

| NPC | Role | Linked Facts | Conditions They Affect | Evidence They Can Provide | What They Know | What They Want | Health | Willpower |
|---|---|---|---|---|---|---|---:|---:|
| Witness | Saw the event. | F03, F04 | Must be alive and reachable. | Statement, memory, photo. | Partial truth. | Safety. | 10 | 100 or not tracked. |
| Suspect | False lead. | F05 | Distracts from true cause. | Manifesto, symbol, alibi. | Wrong but useful truth. | Avoid arrest. | 10 | 100 or scenario value. |

Baseline human NPCs usually have `10 Health`. Only change this when the fiction clearly requires it.

NPCs do not have `Rewind Dice`. Their Willpower is only tracked when the story exposes them to `Branched Timelines`, contradictions, memory pressure, or direct scenario effects. If you do track it, calculate it from what the NPC has actually experienced or witnessed.

Good NPC roles:

- clue source;
- obstacle;
- false culprit;
- victim;
- witness;
- institutional pressure;
- emotional anchor;
- keeper of a condition;
- person whose survival or death controls a dependency.

## Build Time Offenders

A `Time Offender` is a Game Master-controlled NPC adversary with one or more objectives opposed to the `Investigators`. A scenario may have one `Time Offender`, several collaborating `Time Offenders`, or several competing `Time Offenders`.

A `Time Offender` uses a `System` that works exactly like the Investigators' `System`. It is usually called a `Counter-System` to keep adversary actions distinct at the table.

Create a `Time Offender` with this table:

| Field | Preparation Question |
|---|---|
| Identity | Who are they in the visible story? |
| True Role | What causal problem do they create or protect? |
| Objectives | What do they want that opposes the players? |
| Protected Facts | Which `Facts` do they need to preserve? |
| Targeted Facts | Which `Facts` do they want to erase, falsify, or corrupt? |
| Counter-System Resources | Which `Rewind Dice` do they have, and are they single-use? |
| Awareness | What do they know at the start? |
| Identification Triggers | What player actions reveal temporal abnormality? |
| Methods | How do they apply pressure through facts, evidence, witnesses, or conflicts? |
| Traces | What `Evidence` proves their interference? |
| Limits | What can they not know or do? |

Do not make a `Time Offender` omniscient. Track their awareness.

| Awareness State | Trigger | GM Use |
|---|---|---|
| Unaware of identities | Start of play or before evidence connects players to anomalies. | Follow their plan and protect key facts. |
| Alerted | Players create visible contradictions, impossible timing, or abnormal knowledge. | Hide evidence, change a route, mislead witnesses, or prepare pressure. |
| Identified target | The `Time Offender` links a player to temporal interference. | Target that Investigator with conflicts, framing, route changes, or forced resource pressure. |

## How To Play Time Offenders

Play a `Time Offender` as an adversary inside the rules, not as unlimited GM force. They should create pressure that the table can investigate and answer.

On each relevant GM turn, ask:

1. What does the `Time Offender` currently know?
2. Which objective is at risk?
3. Which `Fact`, `Evidence`, NPC, or `Investigator` can they affect?
4. Does the action require the `Counter-System`, or is it mundane?
5. If it requires the `Counter-System`, which `Rewind Die` is spent and what is the `Rewind Percentage`?
6. What trace or contradiction does the action leave?
7. Which player choice becomes more interesting after this action?

Fair `Time Offender` actions:

| Action | Mechanical Use | Evidence Left Behind |
|---|---|---|
| Hide evidence | Delay proof of a `Fact`. | Missing file, camera gap, changed witness statement. |
| Contaminate evidence | Make one clue unusable for a merge until repaired. | Contradictory timestamp, altered record. |
| Frame an Investigator | Add a `Minor Conflict` to that Investigator. | Police report, witness description, security alert. |
| Escalate a conflict | Turn an unresolved `Minor Conflict` into a `Major Conflict` if fiction supports it. | Official record, dependency break, false proof. |
| Protect a dependency | Move, replace, or shield a required cause. | Route change, object substitution, new guard. |
| Force resource pressure | Make a clean resolution require a new branch. | Lead points to a different `Time Unit`. |

The best `Time Offender` moves both hurt and reveal. If the adversary erases a file, the erased file should leave a missing record, a witness with inconsistent memory, or `Counter-System` residue.

## Run The Start Of Play

At the table:

1. State the `Now`.
2. Draw the 20 `Atomic` `Time Units`.
3. Place only confirmed opening facts on the `Main Timeline`.
4. Give the initial case file.
5. Give each Investigator `100 Willpower`, `10 Health`, and one classic D&D dice set.
6. Mark available `Rewind Dice`: d4, d6, d8, d10, d12, d20.
7. Explain that the percentile d10 is for Willpower tests and that `00` is worth `0`.
8. Keep the hidden `Causal Table` private.
9. Ask the players which clue they investigate first.

## Run Turns

The recommended table order is:

```text
GM as needed, then Alice, Bob, Charlie, Dana, then repeat.
```

Replace the names with your actual table. The GM does not need a rigid full turn every round; the GM acts whenever the game state, NPCs, `Time Offender`, conflict analysis, or merge procedure requires it.

On a player turn:

1. Restate the player's current branch, conflicts, Health, Willpower, and remaining `Rewind Dice`.
2. Ask for one clear action.
3. If they investigate, reveal only evidence they can reach.
4. If they open a `Branched Timeline`, choose the target `Time Unit`, spend a `Rewind Die`, roll it, calculate `Rewind Percentage`, and apply the result.
5. If the branch opens, maintain local coherence and play the scene.
6. Record every important new `Visible or Discoverable Event` created inside the branch. A single branch can create several events.
7. Mark produced evidence and conflicts.
8. If the player requests a merge, compare changed facts, conditions, dependencies, and evidence.
9. Resolve `Minor Conflicts` by choice and Willpower roll.
10. Block `Major Conflicts` until a corrective cause exists.
11. Recalculate the active player's Willpower at the end of the turn.

Use the visible calculation:

```text
Current Willpower
= 100
- 30 x non-Merged Branched Timelines
- 40 x unresolved Major Conflicts
- 20 x unresolved Minor Conflicts
- other active Willpower penalties
```

If the result is `0` or less, the character falls into madness.

## Manage Branches And Merges

Track every `Branched Timeline`. Do not erase failed pressure from the fiction just because a branch did not merge.

Use this tracker:

| Branch | Owner | Start Time Unit | Rewind Die | Rewind Result | Events Created | Evidence Produced | Conflicts | Status |
|---|---|---:|---|---|---|---|---|---|
| Alice_TU14 | Alice | 14 | d12 | 75%, partial success | Witness moved; file recovered. | Witness statement, file copy. | Minor: public alarm. | Open. |
| Bob_TU08 | Bob | 8 | d20 | 100%, critical success | Cause replaced. | Clean lab log. | None. | Merged. |

Branch status should be one of:

- Open;
- Merged;
- blocked by `Minor Conflict`;
- blocked by `Major Conflict`;
- closed without merge;
- failed to open.

A `Major Conflict` can be resolved by another player's branch. Once the corrective cause exists, the previous branch may become mergeable even if the original owner cannot act anymore. This is important for cooperative play.

## Merge Checklist

When a player asks to merge, check:

- Which `Facts` were created?
- Which `Facts` were removed?
- Which `Facts` were modified?
- Which `Conditions` changed?
- Which dependency conditions are now broken?
- Which `Evidence` appears, disappears, or becomes contradictory?
- Does the `Now` still make sense?
- Does this create a `Minor Conflict` or `Major Conflict`?
- Can another branch provide a replacement cause?
- What does the System show the players?

Merge only what is coherent. A branch can partially succeed in the fiction but remain blocked from the `Main Timeline`.

## Best Practices

- Start with a clear `Now`. If the present state is vague, the players cannot reason about causality.
- Build facts as causes, not lore. Every important entry should affect another entry.
- Keep the visible `Main Timeline` readable. Use hidden notes for complexity.
- Give players evidence, not answers.
- Give at least two evidence routes for every critical `Fact`.
- Make partial failures useful. They should fail the action but point to `Condition`, `Fact`, `Evidence`, or `Time Offender` information.
- Use `Major Conflicts` for structural contradictions only. Too many major blocks make play feel stuck.
- Use `Minor Conflicts` to create pressure, witnesses, records, reputation problems, and local contradictions.
- Show Willpower math at the end of each player turn.
- Let players solve major problems with replacement causes.
- Let one player's branch repair another player's conflict.
- Keep `Time Offenders` fair, limited, and traceable.
- Do not punish players for not guessing the hidden table. Give new leads when they test a wrong theory.
- Prefer concrete evidence: a ticket, a scar, a log, a file, a person, a route, a missing object.
- Use the [Rewind Dice Abacus](./abacus/README.md) during play to avoid slowing the table.
- Use the starter `Glass Fever Protocol` before running more complex scenarios.
- End decisively when the `System` energy is spent, the mystery is solved, the final `Main Timeline` diverges from the original `Now`, or the table reaches a strong final state.

## Scenario Template

Copy this structure when preparing a new case.

```markdown
# Scenario Name - Game Master Prep

## Scenario Premise

## Core Game Master Truth

## Now

## Mystery Question

## Main Timeline

| Time Unit | Visible or Discoverable Event | Hidden GM Note |
|---|---|---|
| 20 |  |  |
| 19 |  |  |
| ... |  |  |
| 1 |  |  |
| 0 | Now:  |  |

## Initial Player Briefing

## Hidden Causal Table

| ID | Time Unit | Condition Type | Conditions | Fact | Evidence |
|---|---|---|---|---|---|

## Key Characters

| Character | Public Role | Real Function | Health | Willpower |
|---|---|---|---:|---:|

## Time Offenders

| Time Offender | Objectives | Counter-System Resources | Awareness | Traces |
|---|---|---|---|---|

## Expected Conflicts

| Trigger | Conflict Type | Why It Matters | How It Can Be Resolved |
|---|---|---|---|

## Merge Requirements

## Ending Conditions

## Play Trackers
```

## Minimal Prep Checklist

Before running, make sure you have:

- one clear `Now`;
- 20 `Atomic` `Time Units`;
- 8 to 15 important hidden `Facts`;
- at least one `Evidence` route for every `Fact`, and two for every critical `Fact`;
- clear `Simple conditions` and `Dependency conditions`;
- 3 to 6 starting clues;
- NPCs with roles in the causal structure;
- optional `Time Offenders` with limited `Counter-System` resources;
- expected `Minor Conflicts` and `Major Conflicts`;
- a branch tracker;
- a Willpower tracker;
- a final resolution rule for success, rupture, madness, or unresolved divergence.
