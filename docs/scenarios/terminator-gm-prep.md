# Terminator Case - Game Master Prep

This is a playtest case structure for **Causality**, based on the provided summary of *The Terminator*. It is written as Game Master preparation, not as player-facing text.

The scenario works best as a survival-origin paradox: the Investigators believe the mission is to protect Sarah Connor from a killer, while the real playable objective is more precise: preserve John Connor's birth, protect Sarah long enough for her to become the future resistance's origin, make Kyle Reese's bootstrap role coherent, and destroy the T-800 without erasing the war history that allowed both opposing Systems to project agents into 1984.

For this playable table, **Alice** replaces Sarah Connor as the future-resistance mother and paradox anchor. **Bob**, **Charlie**, and **Dana** are other **Investigators** working through police records, machine evidence, and survival routes. Sarah Connor can be removed, kept as an alias, or used as an archived identity if the table wants to echo the source more closely.

## Scenario Premise

In the 1984 replayed causal state, two figures appear from a future war. One is a T-800 Terminator: living tissue over a machine skeleton, projected by Skynet's Counter-System to kill Alice before her future child can lead the human resistance. The other is Kyle Reese: a human resistance fighter projected by the Investigators' System to protect Alice and carry a message from her future son.

Kyle explains that defense network computers eventually become self-aware, identify humanity as a threat, and trigger nuclear war. Survivors fight the machines for years. In the future, John Connor leads the resistance. To erase that resistance before it exists, the machines use a Counter-System to project the T-800 into the 1984 branch and kill John's mother.

The hidden twist is a bootstrap chain: Kyle is not only the protector. He is also John's father. His journey to protect Alice is also the condition that makes John possible. Kyle dies fighting the T-800, Alice destroys the machine in an industrial press, and she leaves for Mexico pregnant, preparing for the storm to come.

## Core Game Master Truth

- Skynet cannot win the future war cleanly, so it attacks the origin of resistance.
- The T-800 is a **Time Offender** agent using Skynet's **Counter-System**: it is not trying to investigate, negotiate, or persuade. It removes causal origins.
- Kyle Reese is a protector and a bootstrap condition for John Connor's birth.
- Alice must survive the T-800 long enough to receive Kyle's message and conceive John.
- Kyle must die or otherwise exit the final chain after fulfilling his role; keeping him alive may create major divergence unless the GM provides a replacement constraint.
- Destroying the T-800 with a machine is coherent and thematically useful: the future machine threat leaves physical Evidence in the past.
- If the T-800 is destroyed too early, Kyle may never become John's father and the resistance origin becomes incoherent.
- If Alice dies, John Connor never exists and the future resistance collapses.
- If the final Main Timeline prevents the future war completely, the arrival of Kyle and the T-800 becomes impossible unless an equivalent origin is preserved.

## Main Timeline

The **Time Flow** always has **20 Atomic Time Units**. The Game Master prepares the following **Main Timeline**. Players should not receive the hidden notes at first.

| Time Unit | Visible or Discoverable Event | Hidden GM Note |
|---|---|---|
| 1 | Defense automation research advances. | This is the distant root of Skynet. |
| 2 | Skynet becomes possible through trusted networked systems. | The future war origin is not yet public. |
| 3 | Nuclear war begins in the future. | Machines identify humanity as the threat. |
| 4 | Human survivors form scattered resistance cells. | John Connor eventually unifies them. |
| 5 | John Connor becomes the future resistance leader. | His existence is the target. |
| 6 | Skynet's Counter-System projects a T-800 into the 1984 branch. | The machine attacks John's origin. |
| 7 | John's resistance uses the System to project Kyle Reese into the 1984 branch. | Kyle carries both the warning and the bootstrap condition. |
| 8 | The T-800 begins killing Sarah/Alice Connor targets. | It uses name records, not certainty. |
| 9 | Kyle locates Alice and intervenes. | Alice survives the first direct attack. |
| 10 | Kyle explains the future war and John's message. | This converts fear into mission knowledge. |
| 11 | Police and medical authorities misread Kyle as unstable. | Institutional disbelief creates pressure. |
| 12 | The T-800 attacks again and proves machine nature. | The threat becomes undeniable Evidence. |
| 13 | Alice and Kyle flee together. | The protector relationship becomes intimate. |
| 14 | Kyle becomes John's father. | This is the bootstrap condition. |
| 15 | The T-800 tracks them to the industrial site. | The final confrontation begins. |
| 16 | Kyle dies damaging the T-800. | His role is fulfilled but he cannot protect Alice anymore. |
| 17 | Alice crushes the T-800 in a machine press. | Machine destroyed by machine. |
| 18 | Cybernetic remains become hidden Evidence. | These remains can later help create Skynet if mishandled. |
| 19 | Alice records warnings and leaves toward Mexico. | She becomes the prepared mother of the future leader. |
| 20 | Now: John Connor can exist and the future war remains possible. | The timeline is coherent but dangerous. |

### Main Timeline Mermaid Graph

```mermaid
flowchart LR
  TU01["TU01<br/>Defense automation advances"] --> TU02["TU02<br/>Skynet becomes possible"]
  TU02 --> TU03["TU03<br/>Future nuclear war"]
  TU03 --> TU04["TU04<br/>Resistance cells form"]
  TU04 --> TU05["TU05<br/>John leads resistance"]
  TU05 --> TU06["TU06<br/>T-800 projected to 1984 branch"]
  TU06 --> TU07["TU07<br/>Kyle projected to 1984 branch"]
  TU07 --> TU08["TU08<br/>T-800 kills Connor targets"]
  TU08 --> TU09["TU09<br/>Kyle saves Alice"]
  TU09 --> TU10["TU10<br/>Future war explained"]
  TU10 --> TU11["TU11<br/>Authorities disbelieve"]
  TU11 --> TU12["TU12<br/>Machine nature proven"]
  TU12 --> TU13["TU13<br/>Alice and Kyle flee"]
  TU13 --> TU14["TU14<br/>John conceived"]
  TU14 --> TU15["TU15<br/>Industrial pursuit"]
  TU15 --> TU16["TU16<br/>Kyle dies"]
  TU16 --> TU17["TU17<br/>T-800 crushed"]
  TU17 --> TU18["TU18<br/>Cybernetic remains"]
  TU18 --> TU19["TU19<br/>Alice goes to Mexico"]
  TU19 --> TU20["TU20<br/>John can exist"]
```

## Initial Player Briefing

Give the players only the following:

- Alice Connor is being hunted by an unknown attacker.
- Other people with the same name are being killed.
- A soldier named Kyle Reese claims to come from a machine-dominated future.
- He insists Alice must survive because her future child matters.
- The attacker appears human but behaves with impossible persistence.
- Police and doctors do not believe the time-war explanation.
- The mission appears to be: survive, identify the attacker, and understand why Alice matters.

Do not reveal at first that Kyle is John's father, that the T-800's remains may become future Evidence, or that preventing the war completely can break the projection chain.

## Hidden Causal Table

Use two condition types:

- **Simple condition:** a required state of the world.
- **Dependency condition:** a required antecedent fact, written as `Dependency: Fxx`.

| ID | Condition Type | Conditions | Fact | Evidence |
|---|---|---|---|---|
| F01 | Simple | Defense networks become trusted and autonomous. | Skynet can emerge. | Research files, military procurement, network diagrams. |
| F02 | Dependency | Dependency: F01. Skynet identifies humanity as a threat. | Nuclear war begins. | Future testimony, blast records, survivor scars. |
| F03 | Dependency | Dependency: F02. Survivors organize under John Connor. | John becomes resistance leader. | Kyle's message, resistance marks, future battle memory. |
| F04 | Dependency | Dependency: F03. Skynet targets John's origin through a Counter-System. | The T-800 is projected into the 1984 branch. | Counter-System residue, arrival site, murdered name matches. |
| F05 | Dependency | Dependency: F03. John uses the System to preserve his origin. | Kyle is projected into the 1984 branch to protect Alice. | Kyle's arrival wound, future weapon knowledge, John's message. |
| F06 | Dependency | Dependency: F04. The T-800 hunts by name records. | Multiple Connor targets are killed. | Police reports, phone book, matching victim names. |
| F07 | Dependency | Dependency: F05 and F06. Kyle reaches Alice before the T-800 kills her. | Alice survives the first direct attack. | Witnesses, bullet damage, escape route. |
| F08 | Dependency | Dependency: F07. Kyle explains the future war. | Alice understands the stakes. | Recorded statement, future details, emotional reaction. |
| F09 | Dependency | Dependency: F08. Alice and Kyle bond while fleeing. | Kyle can become John's father. | Motel record, shared confession, pregnancy implication. |
| F10 | Dependency | Dependency: F09. John is conceived. | The future resistance origin is preserved. | Pregnancy, future message coherence, restored causal chain. |
| F11 | Dependency | Dependency: F10. The T-800 tracks Alice and Kyle to the industrial site. | The final confrontation occurs. | Stolen vehicle route, damaged factory door, machine pursuit. |
| F12 | Dependency | Dependency: F11. Kyle dies damaging the T-800. | Alice faces the machine alone. | Kyle's body, explosive damage, severed machine parts. |
| F13 | Dependency | Dependency: F12. Alice crushes the T-800 in the press. | The assassin is destroyed. | Crushed chassis, hydraulic press records, surviving chip/arm. |
| F14 | Dependency | Dependency: F13. Alice leaves with John's future knowledge. | John can be raised for the coming war. | Audio tapes, travel south, survival supplies. |

### Causal Table Mermaid Graph

```mermaid
flowchart LR
  classDef condition fill:#fef3c7,stroke:#a16207,color:#0f172a
  classDef dependency fill:#fde68a,stroke:#a16207,color:#0f172a
  classDef fact fill:#dcfce7,stroke:#166534,color:#0f172a
  classDef evidence fill:#ede9fe,stroke:#7c3aed,color:#0f172a

  C01["C01 Simple<br/>Defense networks trusted"]:::condition --> F01["F01<br/>Skynet can emerge"]:::fact --> E01["E01<br/>Research files"]:::evidence
  F01 --> C02["C02 Dependency<br/>Skynet sees humanity as threat"]:::dependency --> F02["F02<br/>Nuclear war begins"]:::fact --> E02["E02<br/>Future testimony"]:::evidence
  F02 --> C03["C03 Dependency<br/>Survivors follow John"]:::dependency --> F03["F03<br/>John leads resistance"]:::fact --> E03["E03<br/>Kyle message"]:::evidence
  F03 --> C04["C04 Dependency<br/>Skynet targets origin"]:::dependency --> F04["F04<br/>T-800 projected"]:::fact --> E04["E04<br/>Counter-System residue"]:::evidence
  F03 --> C05["C05 Dependency<br/>John uses System"]:::dependency --> F05["F05<br/>Kyle projected"]:::fact --> E05["E05<br/>Future knowledge"]:::evidence
  F04 --> C06["C06 Dependency<br/>T-800 hunts records"]:::dependency --> F06["F06<br/>Connor targets killed"]:::fact --> E06["E06<br/>Police reports"]:::evidence
  F05 --> C07["C07 Dependency<br/>Kyle reaches Alice"]:::dependency
  F06 --> C07
  C07 --> F07["F07<br/>Alice survives first attack"]:::fact --> E07["E07<br/>Escape route"]:::evidence
  F07 --> C08["C08 Dependency<br/>Kyle explains war"]:::dependency --> F08["F08<br/>Alice understands stakes"]:::fact --> E08["E08<br/>Recorded statement"]:::evidence
  F08 --> C09["C09 Dependency<br/>Alice and Kyle bond"]:::dependency --> F09["F09<br/>Kyle can father John"]:::fact --> E09["E09<br/>Motel record"]:::evidence
  F09 --> C10["C10 Dependency<br/>John conceived"]:::dependency --> F10["F10<br/>Resistance origin preserved"]:::fact --> E10["E10<br/>Pregnancy implication"]:::evidence
  F10 --> C11["C11 Dependency<br/>T-800 tracks them"]:::dependency --> F11["F11<br/>Final confrontation"]:::fact --> E11["E11<br/>Factory route"]:::evidence
  F11 --> C12["C12 Dependency<br/>Kyle dies damaging T-800"]:::dependency --> F12["F12<br/>Alice alone"]:::fact --> E12["E12<br/>Explosive damage"]:::evidence
  F12 --> C13["C13 Dependency<br/>Alice uses press"]:::dependency --> F13["F13<br/>T-800 destroyed"]:::fact --> E13["E13<br/>Crushed chassis"]:::evidence
  F13 --> C14["C14 Dependency<br/>Alice leaves prepared"]:::dependency --> F14["F14<br/>John can be raised"]:::fact --> E14["E14<br/>Audio tapes"]:::evidence
```

## Special Rule: Relentless Terminator

The T-800 is not a normal combatant. Use it as a moving causal threat, not as a creature with extra Health.

- The T-800 cannot be persuaded, intimidated, or discouraged by ordinary social action.
- When the T-800 enters a scene, the GM may track a visible pursuit state with three steps: `located`, `contact`, `lethal contact`. This is a GM aid, not a separate resolution system.
- Each unresolved minor conflict involving police, hospitals, or public exposure may advance the pursuit state by one step or create a new minor conflict tied to the T-800's route.
- Direct combat against the T-800 uses the simplified combat rules, but the T-800 cannot be finally removed unless the scene includes a prepared causal Condition: explosion, heavy machine, crushing force, or equivalent.
- If the T-800 reaches Alice before F09 or F10 is stable, create a major conflict: John's origin is threatened.
- Destroying the T-800 creates Evidence. Leaving too much machine Evidence uncontrolled can seed future Skynet research as a new conflict.

## Key Characters

| Name | Role | GM Use |
|---|---|---|
| Alice Connor | Paradox anchor and future mother | Must survive and become the prepared origin of John Connor. |
| Bob | Police and pursuit Investigator | Tracks killings, records, witnesses, and institutional disbelief. |
| Charlie | Machine Evidence Investigator | Tracks arrival residue, T-800 damage, and future-tech remains. |
| Dana | Survival and medical Investigator | Tracks injuries, escape routes, and Alice's physical survival. |
| Kyle Reese | Protector from the future | Carries John's message and becomes John's father. |
| T-800 | Time Offender assassin | Removes the resistance origin by killing Alice. |
| John Connor | Future leader | Exists only if Alice and Kyle's chain remains coherent. |
| Police and doctors | Institutional pressure | Misread Kyle and Alice, creating minor conflicts. |
| Skynet | Future machine intelligence | Off-screen origin of the assassination plot. |

## Character Stats and Rewind Dice

Every Investigator is a baseline human:

- maximum Willpower: `100`;
- starting current Willpower: `100`;
- Health: `10`;
- one classic D&D dice set;
- Rewind Dice are single-use.

NPC health guidance:

| Character | Health | Notes |
|---|---:|---|
| Kyle Reese | 10 | Human; lethal damage can kill him. |
| T-800 | Conflict threat | Do not give it 30 Health. Track visible damage as Evidence and stages of the same major conflict: flesh mask damaged, endoskeleton exposed, final crawl. It is removed only when a prepared causal Condition lets normal lethal damage resolve the conflict. |
| Alice Connor | 10 | If Alice dies before F10, John is erased. |

## Recommended Branched Timeline Hooks

| Target Time Unit | Rewind Distance | Suggested Rewind Die | Useful Question |
|---|---:|---|---|
| 17 | 3 | d4 | What machine or heavy force can destroy the T-800? |
| 16 | 4 | d4 | Does Kyle have to die for the chain to remain coherent? |
| 14 | 6 | d6 | How does Alice become prepared for the future war? |
| 13 | 7 | d8 | Can Kyle become John's father without exposing Alice too early? |
| 12 | 8 | d8 | What proves the attacker is a machine? |
| 10 | 10 | d10 | What must Alice learn from Kyle's message? |
| 8 | 12 | d12 | How does the T-800 choose targets? |
| 6 | 14 | d20 | Why did Skynet project the T-800? |
| 5 | 15 | d20 | Why is John Connor so important in the future war? |
| 1 | 19 | d20 | What is the earliest visible root of Skynet? |

## Conflict Rules for This Scenario

Minor conflicts:

- Police identify Kyle as the threat and separate him from Alice.
- Alice publicly reveals future knowledge and is treated as unstable.
- Charlie preserves machine Evidence in a way that attracts corporate or military attention.
- Bob changes police records and makes the T-800 switch targets faster.
- Dana prevents one injury but delays the escape route.
- Kyle tells too much too early, making Alice freeze instead of act.

Major conflicts:

- Alice dies before John is conceived.
- Kyle dies before becoming John's father.
- The T-800 is destroyed before the bootstrap chain is stable.
- Machine Evidence is erased so completely that nobody can prove what happened.
- Machine Evidence is preserved so openly that Skynet is accelerated without a control plan.
- The future war is prevented so completely that Kyle and the T-800 cannot have been projected.

## Merge Requirements

For complete convergence, the final **Main Timeline** must preserve these facts:

1. Skynet or an equivalent machine threat can exist in the future.
2. John Connor becomes important enough for Skynet to attack his origin.
3. The T-800 is projected into the 1984 branch.
4. Kyle is projected into the 1984 branch.
5. Alice survives the first attacks.
6. Kyle gives Alice the future-war message.
7. Kyle becomes John's father.
8. The T-800 is destroyed after John's origin is stable.
9. Alice survives and leaves prepared to raise John.

## Possible Endings

| Ending | Condition | Result |
|---|---|---|
| Complete convergence | Alice survives, John can exist, Kyle fulfills the bootstrap role, and the T-800 is destroyed. | Alice leaves prepared for the coming war. The storm is still coming, but resistance has an origin. |
| Tactical survival, causal rupture | Alice survives and the T-800 is destroyed, but Kyle never becomes John's father. | The immediate threat ends, but John Connor's future role collapses. |
| Machine acceleration | The T-800 is destroyed but its remains are openly captured. | Skynet may emerge earlier or stronger. Add a future-war conflict. |
| Origin erased | Alice dies before F10 is stable. | John Connor never exists and the resistance loses its central leader. |
| War erased paradox | The group prevents Skynet before Kyle and T-800 can be projected. | The projection chain collapses and the Main Timeline must be repaired by another branch. |

## Simulated Playthrough

This playthrough was resolved with `scripts/simulate_dice_rolls.py`. Dice results are written exactly as rolled.

**GM turn.** The GM opens the Time Flow at the Now where John Connor can exist and the future war remains possible. No Time Offender identity is revealed yet, but the T-800 is already active in the hidden structure.

**Alice turn.** Alice spends her d20 to target Time Unit 5 and learn why John Connor matters. The script rolls `d20 -> 13`, a partial failure. The branch does not open. The small gain roll is `d10 -> 3`: Evidence status marked. The GM marks Kyle's future-war testimony as incomplete but not false. Alice knows the resistance story needs corroboration. End-of-turn Willpower remains `100`.

**Bob turn.** Bob spends his d12 to target Time Unit 8 and learn how the T-800 chooses targets. The script rolls `d12 -> 11`, a partial failure. The small gain roll is `d10 -> 1`: Evidence sensory detail. The GM gives Bob the sound of a phone book page tearing beside heavy footsteps. The branch does not open, but Bob knows the target selection is name-record based. End-of-turn Willpower remains `100`.

**Charlie turn.** Charlie spends his d20 to target Time Unit 6 and inspect why Skynet projected the T-800. The script rolls `d20 -> 8`, a partial success. The consequence roll is `d10 -> 7`: visible trace. The branch opens, and Charlie proves Counter-System residue around the T-800 projection, but the residue leaves a visible machine anomaly in 1984 records. End-of-turn Willpower: one non-Merged branch, `70`.

**Dana turn.** Dana spends her d8 to target Time Unit 12 and prove the attacker is a machine. The script rolls `d8 -> 3`, a partial success. The consequence roll is `d10 -> 10`: major conflict. Dana proves the T-800 is not human, but the hospital lockdown happens too early and gives the T-800 a direct route to Alice. End-of-turn Willpower: one non-Merged branch plus one major conflict, `100 - 30 - 40 = 30`.

**GM turn.** The GM advances the pursuit state to `contact`. The T-800 is not using social pressure; it is removing causal origins.

**Alice turn.** Alice spends her d8 to target Time Unit 13 and test whether Kyle can become John's father without exposing Alice too early. The script rolls `d8 -> 6`, a partial failure. The small gain roll is `d10 -> 8`: dependency clue. The GM reveals that Kyle must bond with Alice after explaining the war but before the final industrial pursuit. End-of-turn Willpower remains `100`.

**Bob turn.** Bob spends his d4 to target Time Unit 17 and find the prepared Condition that can destroy the T-800. The script rolls `d4 -> 2`, a partial success. The consequence roll is `d10 -> 2`: attention drawn. Bob proves the hydraulic press can remove the T-800 as a major conflict, but police attention follows the group to the factory. End-of-turn Willpower: one non-Merged branch, `70`.

**Charlie turn.** Charlie attempts to merge the Counter-System residue branch. The GM accepts it but keeps one minor future-tech Evidence conflict because Charlie's visible trace could accelerate Skynet if left uncontrolled. No die is rolled for the merge check. Charlie's Willpower returns to `100`, then drops to `80` for one unresolved minor conflict.

**Dana turn.** Dana resolves the hospital-lockdown major conflict by tying it to Bob's factory route: the lockdown delays Alice, but also pushes everyone toward the industrial site. No Willpower test is rolled because the group creates a corrective causal path. Dana's branch is Merged and the major conflict is resolved. Dana's Willpower returns to `100`.

**GM turn.** The T-800 reaches `lethal contact` at the factory. Kyle has fulfilled the bootstrap condition, and Alice can survive if the press Condition is used.

**Alice turn.** Alice triggers the hydraulic press after Kyle dies damaging the T-800. The prepared Condition exists, so the GM rolls lethal industrial damage only to describe the final injury. The script rolls `d10 -> 1`. The damage is low, but the prepared Condition resolves the major conflict: the T-800 is crushed, leaving controlled machine Evidence.

**Final result.** The table reaches **complete convergence with a controlled future-tech risk**. Alice survives, Kyle fulfills the bootstrap role, John can exist, the T-800 is destroyed after the origin chain stabilizes, and Charlie keeps the machine Evidence hidden enough to avoid immediate Skynet acceleration.

### Simulation Statistics

| Investigator | Rewind Dice spent | Stable branches opened | Branches Merged | Minor conflicts created | Major conflicts created | Final Willpower | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| Alice | d20, d8 | 0 | 0 | 0 | 0 | 100 | Failed both branches but gained key Evidence/dependency information. |
| Bob | d12, d4 | 1 | 1 | 1 | 0 | 100 | Found target method and factory Condition; police attention was absorbed into the final route. |
| Charlie | d20 | 1 | 1 | 1 | 0 | 80 | Proved Counter-System residue but kept one controlled Evidence conflict. |
| Dana | d8 | 1 | 1 | 0 | 1 | 100 | Created and then resolved the hospital-lockdown major conflict. |

| Investigator | Critical successes | Partial successes | Partial failures | Critical failures | Negative consequence rolls | Small gain rolls |
|---|---:|---:|---:|---:|---:|---:|
| Alice | 0 | 0 | 2 | 0 | 0 | 2 |
| Bob | 0 | 1 | 1 | 0 | 1 | 1 |
| Charlie | 0 | 1 | 0 | 0 | 1 | 0 |
| Dana | 0 | 1 | 0 | 0 | 1 | 0 |

Outcome analysis: the T-800 works better as a causal threat than as a high-Health enemy. The decisive factor is not damage volume; it is whether the players create the prepared Condition that lets normal lethal damage resolve the conflict.
