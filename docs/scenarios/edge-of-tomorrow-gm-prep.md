# Edge of Tomorrow Case - Game Master Prep

This is a playtest case structure for **Causality**, based on the provided summary of *Edge of Tomorrow*. It is written as Game Master preparation, not as player-facing text.

The scenario works best as a tactical investigation loop: the Investigators believe the mission is to survive a beach assault, while the real playable objective is to understand the Mimic command structure, identify the Omega as a Time Offender using a Counter-System, reject the false target, identify the Omega location, and preserve a coherent final Now after the loop breaks.

For this playable table, **Alice** is the **Loop Bearer Investigator**. She replaces the William Cage role as the unwilling public-relations officer forced into the front line. **Bob**, **Charlie**, and **Dana** are other Investigators embedded with J-Squad and the coalition command structure. William Cage can be removed, kept as an alias, or used as an off-screen propaganda file.

## Scenario Premise

The Mimics have invaded Europe. Germany has fallen, France is close to collapse, and London will be next if the coalition fails. General Brigham is confident that **Operation Twilight** will break the alien front. He sends Alice to cover the operation as a public-relations symbol, but she refuses front-line duty. Brigham has her arrested, labels her a deserter, and transfers her to J-Squad.

The assault is an ambush. The Mimics know the attack is coming because their command organism, the **Omega**, is a Time Offender using a Counter-System through Alpha Mimics. Alice kills an Alpha and is soaked in its blood. From that moment, her death lets the Omega's Counter-System force the same Branched Timeline state open again: Alice returns to the morning before deployment with memories of previous attempts.

Rita Vrataski and Doctor Carter know enough to identify the pattern. Rita had the same loop power after Verdun and lost it after a transfusion. Carter understands that the Alpha is not the leader: it is a node. The Omega is the head. The first apparent location, Switzerland, is a false signal. The real Omega is hidden beneath the Louvre.

## Core Game Master Truth

- Operation Twilight is not a breakthrough; it is an ambush.
- The Mimics are not merely predicting the coalition. The Omega is correcting failed outcomes through a Counter-System network.
- Alice becomes the Loop Bearer after killing an Alpha and receiving its blood.
- The loop always returns Alice to the same Branched Timeline starting point until the power is lost.
- Rita Vrataski had the same power at Verdun and lost it after a transfusion.
- Doctor Carter knows the enemy is a distributed organism: Drones act, Alphas signal, and Omega uses the Counter-System to reopen failed branches.
- The Switzerland vision is a trap or false signal created by the Omega network.
- The Omega is hidden beneath the Louvre.
- A transfusion severs Alice from the loop. After that, there is no automatic reset.
- Killing the Omega neutralizes the Mimic Counter-System and allows the Investigators to attempt a final Merge into a victory Now.
- If the final Main Timeline kills the Omega but makes Alice's loop impossible, reality diverges unless the Alpha-blood loop anchor or an equivalent causal explanation is preserved.

## Main Timeline

The **Time Flow** has **20 Atomic Time Units** numbered from **Time Unit 20** as the oldest prepared event to **Time Unit 1** as the latest prepared event before the present. **Now** is **Time Unit 0**. The Game Master prepares the following **Main Timeline**. Players should not receive the hidden notes at first.

| Time Unit | Visible or Discoverable Event | Hidden GM Note |
|---|---|---|
| 20 | The Mimics invade Europe. | The Omega network is already active. |
| 19 | Germany falls. | Coalition strategy becomes desperate and overconfident. |
| 18 | France weakens and London becomes the next strategic target. | Brigham needs a public victory before collapse spreads. |
| 17 | General Brigham prepares Operation Twilight. | The operation is based on false confidence. |
| 16 | Alice is ordered to the front as public-relations cover. | Refusal allows Brigham to remove her authority. |
| 15 | Alice is arrested, labeled a deserter, and assigned to J-Squad. | Her identity and credibility are damaged before the loop begins. |
| 14 | J-Squad deploys in exoskeletons. | Alice does not know how to use her suit. |
| 13 | The beach assault becomes a massacre. | The Mimics knew the assault plan. |
| 12 | Alice kills an Alpha and dies in its blood. | This links Alice to the Omega's Counter-System and creates the Blood Loop. |
| 11 | The Omega's Counter-System reopens the deployment-morning Branched Timeline state. | Alice remembers. The rest of the world does not. |
| 10 | Alice repeats the assault and improves through failure. | Treat repeated attempts as loop Evidence, not full scenes every time. |
| 9 | Rita recognizes Alice's impossible knowledge. | Rita is the credibility bridge for the loop. |
| 8 | Carter explains the Alpha/Omega structure. | The enemy can be beaten only by finding Omega. |
| 7 | Alice trains with Rita through many deaths. | Willpower pressure rises because Alice remembers each failure. |
| 6 | Alice follows the Switzerland signal. | The signal is false or incomplete. |
| 5 | Alice is injured and transfused. | The Blood Loop is lost. No more automatic reset. |
| 4 | Carter identifies the Louvre as the real Omega location. | This is the key dependency for the final assault. |
| 3 | Alice, Rita, Bob, Charlie, Dana, and J-Squad assault the Louvre. | This is the no-error final branch. |
| 2 | Rita dies and Alice reaches the Omega. | Alice must accept a coherent sacrifice. |
| 1 | Alice destroys the Omega and is exposed to Alpha blood again. | The final Merge can produce a coherent victory Now before Brigham's meeting. |
| 0 | Now: the victory state is observed before Brigham's meeting. | The Mimic network has collapsed and Alice remembers enough to seek Rita. |

### Main Timeline Mermaid Graph

```mermaid
flowchart LR
  TU20["TU20<br/>The Mimics invade Europe"] --> TU19["TU19<br/>Germany falls"]
  TU19 --> TU18["TU18<br/>France weakens and London becomes the nex..."]
  TU18 --> TU17["TU17<br/>General Brigham prepares Operation Twilight"]
  TU17 --> TU16["TU16<br/>Alice is ordered to the front as public-r..."]
  TU16 --> TU15["TU15<br/>Alice is arrested, labeled a deserter, an..."]
  TU15 --> TU14["TU14<br/>J-Squad deploys in exoskeletons"]
  TU14 --> TU13["TU13<br/>The beach assault becomes a massacre"]
  TU13 --> TU12["TU12<br/>Alice kills an Alpha and dies in its blood"]
  TU12 --> TU11["TU11<br/>The Omega's Counter-System reopens the de..."]
  TU11 --> TU10["TU10<br/>Alice repeats the assault and improves th..."]
  TU10 --> TU09["TU09<br/>Rita recognizes Alice's impossible knowledge"]
  TU09 --> TU08["TU08<br/>Carter explains the Alpha/Omega structure"]
  TU08 --> TU07["TU07<br/>Alice trains with Rita through many deaths"]
  TU07 --> TU06["TU06<br/>Alice follows the Switzerland signal"]
  TU06 --> TU05["TU05<br/>Alice is injured and transfused"]
  TU05 --> TU04["TU04<br/>Carter identifies the Louvre as the real..."]
  TU04 --> TU03["TU03<br/>Alice, Rita, Bob, Charlie, Dana, and J-Sq..."]
  TU03 --> TU02["TU02<br/>Rita dies and Alice reaches the Omega"]
  TU02 --> TU01["TU01<br/>Alice destroys the Omega and is exposed t..."]
  TU01 --> TU00["TU00 / Now<br/>Now - the victory state is observed befor..."]
```

## Initial Player Briefing

Give the players only the following:

- Europe is collapsing under the Mimic invasion.
- Germany has fallen and London will soon be threatened.
- General Brigham believes Operation Twilight will be decisive.
- Alice has been forced into J-Squad after refusing front-line propaganda duty.
- Rita Vrataski is a legendary soldier from Verdun.
- Doctor Carter is discredited, but still tracks unusual Mimic behavior.
- The mission appears to be: survive the landing, expose why it failed, and find a way to stop the Mimics.

Do not reveal at first that Alice's death lets the Omega reopen the same branch, that Switzerland is false, or that the Omega is beneath the Louvre.

## Hidden Causal Table

Use two condition types:

- **Simple condition:** a required state of the world.
- **Dependency condition:** a required antecedent fact, written as `Dependency: Fxx`.

| ID | Condition Type | Conditions | Fact | Evidence |
|---|---|---|---|---|
| F01 | Simple | Mimics control continental Europe. | London is under strategic threat. | War map, refugee reports, ruined German front. |
| F02 | Dependency | Dependency: F01. Brigham trusts Operation Twilight. | The coalition commits to the beach assault. | Briefing file, invasion schedule, propaganda order. |
| F03 | Dependency | Dependency: F02. Alice refuses front-line duty. | Alice is stripped of status and assigned to J-Squad. | Arrest order, deserter label, squad transfer record. |
| F04 | Dependency | Dependency: F02. Mimics know the assault plan. | The beach landing is an ambush. | Repeated landing deaths, enemy positions, impossible response timing. |
| F05 | Dependency | Dependency: F04. Alice kills an Alpha while dying. | Alice becomes linked to the Omega's Counter-System and receives the Blood Loop. | Alpha corpse, black blood exposure, reset memory. |
| F06 | Dependency | Dependency: F05. Alice dies after the Alpha blood transfer. | The Omega's Counter-System reopens the deployment-morning Branched Timeline state. | Repeated wake-up scene, unchanged barracks, retained memory. |
| F07 | Dependency | Dependency: F06. Alice demonstrates impossible knowledge. | Rita identifies the loop pattern. | Rita test, predicted battlefield events, training reaction. |
| F08 | Dependency | Dependency: F07. Carter explains the enemy organism. | Alphas are signal nodes and Omega is the command source. | Carter notes, Verdun data, alien biology diagrams. |
| F09 | Dependency | Dependency: F08. Alice follows the Switzerland signal. | Switzerland is false, incomplete, or manipulated. | Failed route, empty target site, contradictory vision. |
| F10 | Dependency | Dependency: F08. Alice is transfused after injury. | Alice loses the Blood Loop. | Hospital record, mixed blood, failed reset test. |
| F11 | Dependency | Dependency: F09 and F10. Carter reinterprets the signal after the loop is lost. | The Omega is beneath the Louvre. | Map overlay, underwater access, Mimic movement pattern. |
| F12 | Dependency | Dependency: F11. J-Squad reaches the Louvre after the loop is lost. | The final assault has no automatic reset. | J-Squad route, stolen transport, no-loop risk. |
| F13 | Dependency | Dependency: F12. Alice reaches the Omega after Rita dies. | Alice can destroy the Omega. | Rita's last stand, explosive payload, Omega chamber. |
| F14 | Dependency | Dependency: F13. Alpha blood reaches Alice during the Omega death event. | The final Merge can produce a coherent victory Now. | Mimic collapse, pre-meeting continuity, Rita alive at barracks. |

### Causal Table Mermaid Graph

```mermaid
flowchart LR
  classDef condition fill:#fef3c7,stroke:#a16207,color:#0f172a
  classDef dependency fill:#fde68a,stroke:#a16207,color:#0f172a
  classDef fact fill:#dcfce7,stroke:#166534,color:#0f172a
  classDef evidence fill:#ede9fe,stroke:#7c3aed,color:#0f172a

  C01["C01 Simple<br/>Mimics control Europe"]:::condition --> F01["F01<br/>London threatened"]:::fact --> E01["E01<br/>War map"]:::evidence
  F01 --> C02["C02 Dependency<br/>Brigham trusts Operation Twilight"]:::dependency --> F02["F02<br/>Coalition commits assault"]:::fact --> E02["E02<br/>Briefing file"]:::evidence
  F02 --> C03["C03 Dependency<br/>Alice refuses duty"]:::dependency --> F03["F03<br/>Alice joins J-Squad"]:::fact --> E03["E03<br/>Arrest order"]:::evidence
  F02 --> C04["C04 Dependency<br/>Mimics know plan"]:::dependency --> F04["F04<br/>Beach ambush"]:::fact --> E04["E04<br/>Repeated deaths"]:::evidence
  F04 --> C05["C05 Dependency<br/>Alice kills Alpha"]:::dependency --> F05["F05<br/>Blood Loop begins"]:::fact --> E05["E05<br/>Alpha blood"]:::evidence
  F05 --> C06["C06 Dependency<br/>Alice dies"]:::dependency --> F06["F06<br/>Counter-System reopens branch"]:::fact --> E06["E06<br/>Retained memory"]:::evidence
  F06 --> C07["C07 Dependency<br/>Impossible knowledge"]:::dependency --> F07["F07<br/>Rita identifies loop"]:::fact --> E07["E07<br/>Rita test"]:::evidence
  F07 --> C08["C08 Dependency<br/>Carter explains organism"]:::dependency --> F08["F08<br/>Omega is command source"]:::fact --> E08["E08<br/>Carter notes"]:::evidence
  F08 --> C09["C09 Dependency<br/>Switzerland signal followed"]:::dependency --> F09["F09<br/>False target"]:::fact --> E09["E09<br/>Empty site"]:::evidence
  F08 --> C10["C10 Dependency<br/>Alice transfused"]:::dependency --> F10["F10<br/>Loop lost"]:::fact --> E10["E10<br/>Hospital record"]:::evidence
  F09 --> C11["C11 Dependency<br/>Signal reinterpreted"]:::dependency
  F10 --> C11
  C11 --> F11["F11<br/>Omega under Louvre"]:::fact --> E11["E11<br/>Map overlay"]:::evidence
  F11 --> C12["C12 Dependency<br/>J-Squad final route"]:::dependency --> F12["F12<br/>No-reset assault"]:::fact --> E12["E12<br/>Stolen transport"]:::evidence
  F12 --> C13["C13 Dependency<br/>Alice reaches Omega"]:::dependency --> F13["F13<br/>Omega can be destroyed"]:::fact --> E13["E13<br/>Explosive payload"]:::evidence
  F13 --> C14["C14 Dependency<br/>Alpha blood in Omega death"]:::dependency --> F14["F14<br/>Victory Now Merge"]:::fact --> E14["E14<br/>Mimic collapse"]:::evidence
```

## Special Rule: Blood Loop

The Blood Loop is a scenario rule, not a default power. It represents the Omega's Counter-System forcing a known Branched Timeline state to reopen around Alice.

- Only the Loop Bearer has automatic memory continuity.
- Before transfusion, the Loop Bearer's death does not end the scenario. The Omega's Counter-System reopens the Loop Bearer's state at Time Unit 10.
- Each loop can reveal one new **Evidence**, confirm one **Condition**, or test one combat route.
- Do not play every repeated loop in full. Use montage unless the loop introduces a new **Fact**, **Evidence**, or conflict.
- Every three remembered deaths create one temporary `-5` Willpower penalty for the Loop Bearer until the next clean **Merge**.
- The transfusion at Time Unit 16 ends the Blood Loop. After that point, death is final unless another explicit scenario rule or the final Omega Merge preserves a coherent Now.
- A loop reopening does not automatically **Merge** facts. The group must still prove the causal chain through Evidence.

## Key Characters

| Name | Role | GM Use |
|---|---|---|
| Alice | Loop Bearer Investigator | Starts unwilling and untrained, then becomes the memory carrier. |
| Bob | J-Squad tactical Investigator | Tracks beach routes, enemy positions, and final assault logistics. |
| Charlie | Scientific Investigator | Works with Carter to interpret Alpha/Omega evidence. |
| Dana | Medic and morale Investigator | Tracks injuries, transfusion risk, and squad survival. |
| Rita Vrataski | Veteran soldier | Recognizes the loop and trains Alice. |
| Doctor Carter | Discredited scientist | Explains the enemy organism and translates evidence into strategy. |
| General Brigham | Coalition commander | Creates the initial pressure and can become an obstacle to J-Squad access. |
| J-Squad | Assault squad | Provides human stakes and final-assault resources. |
| Alpha Mimic | Signal node | Creates the Blood Loop and can protect Omega's network. |
| Omega | Time Offender command source | Hidden final target beneath the Louvre; uses a Counter-System through Alpha Mimics. |

## Character Stats and Rewind Dice

Every Investigator is a baseline human:

- maximum Willpower: `100`;
- starting current Willpower: `100`;
- Health: `10`;
- one classic D&D dice set;
- Rewind Dice are single-use.

Recommended simple handling: the Blood Loop reopens scene position and knowledge, but not spent Rewind Dice. This keeps System energy meaningful and prevents infinite mechanical attempts.

| Investigator | Role | Max Willpower | Current Willpower | Health | Rewind Dice Available |
|---|---|---:|---:|---:|---|
| Alice | Loop Bearer | 100 | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Bob | Tactical routes | 100 | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Charlie | Science and Evidence | 100 | 100 | 10 | d4, d6, d8, d10, d12, d20 |
| Dana | Medicine and squad survival | 100 | 100 | 10 | d4, d6, d8, d10, d12, d20 |

## Recommended Branched Timeline Hooks

| Target Time Unit | Rewind Distance | Suggested Rewind Die | Useful Question |
|---|---:|---|---|
| 18 | 18 | d4 | Can J-Squad reach the Louvre chamber after the loop is lost? |
| 17 | 17 | d4 | What proves the Louvre location? |
| 16 | 16 | d4 | What exactly breaks the Blood Loop? |
| 15 | 15 | d6 | Why is Switzerland the wrong target? |
| 14 | 14 | d6 | What training route keeps Alice alive longest? |
| 12 | 12 | d8 | Why does Rita believe Alice? |
| 10 | 10 | d10 | What reopens when Alice dies? |
| 9 | 9 | d12 | What did the Alpha blood do? |
| 8 | 8 | d12 | Why was the beach assault an ambush? |
| 4 | 4 | d20 | Why did Brigham commit to Operation Twilight? |

## Conflict Rules for This Scenario

Minor conflicts:

- Alice exposes impossible knowledge too early and is restrained.
- J-Squad treats Alice as a coward, deserter, or unstable officer.
- A training loop changes Rita's trust but not the external Main Timeline.
- The group follows the Switzerland signal without proving the Louvre dependency.
- Carter's notes are seized before Charlie can preserve them.
- Dana prevents the transfusion, but Alice remains too injured to continue.

Major conflicts:

- The coalition cancels Operation Twilight before the Blood Loop exists.
- Alice never kills the Alpha and never becomes Loop Bearer.
- Rita dies before identifying the loop.
- Carter is removed before explaining the Alpha/Omega structure.
- Alice avoids the transfusion but the group uses loop reopenings forever instead of reaching final convergence.
- Omega is destroyed without a coherent explanation for the final victory Now.

## Merge Requirements

For complete convergence, the final **Main Timeline** must preserve these facts:

1. Operation Twilight happens or an equivalent assault exposes the Mimic ambush.
2. Alice kills an Alpha and becomes Loop Bearer.
3. Rita and Carter identify the Alpha/Omega structure.
4. Switzerland is rejected as the final target.
5. The Blood Loop is lost before the final assault.
6. The Louvre location is proven through Evidence.
7. J-Squad reaches Omega without relying on another reset.
8. Omega is destroyed.
9. The final Now remains coherent: Mimics collapse, and Alice returns to a stable pre-meeting state or another equivalent victory state.

## Possible Endings

| Ending | Condition | Result |
|---|---|---|
| Complete convergence | Omega is destroyed and the final Now remains coherent. | Mimics collapse, Alice remembers enough to find Rita again, and the coalition victory becomes observable. |
| Tactical victory, causal rupture | Omega is destroyed, but no stable loop anchor explains the final Now. | The war is won, but the Investigators' reality diverges from origin. |
| Loop exhaustion | Alice loses Willpower or System energy before proving the Louvre. | The loop becomes psychological collapse rather than victory. |
| False target failure | The group commits to Switzerland as final truth. | Omega survives, the beach defeat remains inevitable, and London falls. |
| Final assault failure | The loop is lost and J-Squad cannot reach Omega. | Death is final; the Mimic network continues. |

## Simulated Playthrough

This replay was recalculated under the **Time Unit 20** to **Time Unit 0 / Now** convention. Every Rewind roll uses `distance = target Time Unit`.

**GM turn.** The GM opens the Time Flow on the invasion Now. The visible Main Timeline shows Operation Twilight, the beach disaster, and Rita's reputation. The Omega is hidden as a Time Offender.

**Alice turn.** Alice spends her d20 to target Time Unit `12`. The replay result is `d20 -> 13`, so `r = 108.33%`: critical success. Alice proves that killing an Alpha while dying connects her to the Omega's Counter-System and creates the Blood Loop. Willpower `70`.

**Bob turn.** Bob spends his d12 to target Time Unit `13`. The replay result is `d12 -> 10`, so `r = 76.92%`: partial success. The new consequence roll is `d10 -> 9`: a witness changes behavior. Bob still proves the beach assault is an ambush, but a soldier who saw him later changes squad movement. Willpower `70`.

**Charlie turn.** Charlie spends his d12 to target Time Unit `9`. The replay result is `d12 -> 2`, so `r = 22.22%`: partial failure. No branch opens. The existing gain roll is `d10 -> 10`: immediate lead. The GM gives Carter as the concrete lead tied to Rita and the Alpha/Omega theory. Willpower `100`.

**Dana turn.** Dana spends her d8 to target Time Unit `5`. The replay result is `d8 -> 4`, so `r = 80%`: critical success. Dana proves that mixed blood severs Alice from the Blood Loop. Willpower `70`.

**GM turn.** The GM summarizes the proven chain: Alpha blood creates the loop, the beach assault is an ambush, Carter is the lead, and transfusion ends the loop. The final target is still hidden.

**Alice turn.** Alice spends her d10 to target Time Unit `6`. The replay result is `d10 -> 4`, so `r = 66.67%`: partial success. The new consequence roll is `d10 -> 3`: pursuit. Alice proves Switzerland is a false or manipulated signal, but Mimic pressure follows the branch. With two non-Merged branches, her Willpower reaches `40`.

**Bob turn.** Bob spends his d8 to target Time Unit `3` and solve the final J-Squad route. The replay result is `d8 -> 1`, so `r = 33.33%`: partial failure. No branch opens. The new gain roll is `d10 -> 3`: Evidence status marked. The GM marks Bob's route evidence as incomplete rather than false. Bob has only one open branch, so Willpower is `70`.

**Charlie turn.** Charlie spends his d10 to target Time Unit `4`. The replay result is `d10 -> 2`, so `r = 50%`: partial success. The consequence roll is `d10 -> 3`: pursuit. Charlie proves the Omega is beneath the Louvre through Carter's map overlay, but Mimic pressure follows him. Willpower `70`.

**Dana turn.** Dana spends her d6 to target Time Unit `3`. The replay result is `d6 -> 2`, so `r = 66.67%`: partial success. The new consequence roll is `d10 -> 3`: pursuit. Dana proves the squad survival route, but the approach to the chamber is under active Mimic pressure. Her lowest Willpower is `40`.

**GM turn.** The GM checks dependencies. Bob's final route branch failed, but his gain marked the route evidence as incomplete rather than false. Charlie proves the Louvre and Dana proves the survival route, so the group can still merge every stable branch.

**Alice turn.** Alice accepts that the Blood Loop is gone and commits to the final Omega action. The prepared explosive payload is resolved with the damage die only. The replay result is `d10 -> 10`. The Omega is destroyed; the Alpha-blood death event gives the GM enough causal material to merge the victory Now.

**Final result.** The table reaches **complete convergence**. The Mimic network collapses, the final Now is stable, and the Omega's Counter-System is neutralized without needing another reset.

### Scenario GitGraph

```mermaid
%%{init: { 'theme': 'base', 'themeVariables': { 'git0': '#4b5563', 'git1': '#f97316', 'git2': '#2563eb', 'git3': '#2563eb', 'git4': '#7c3aed', 'git5': '#16a34a', 'git6': '#7c3aed' }, 'gitGraph': { 'showCommitLabel': true, 'mainBranchName': 'main' } } }%%
gitGraph LR:
  commit id: "TU20 The Mimics invade Europe"
  commit id: "TU19 Germany falls"
  commit id: "TU18 France weakens and London becomes the next strategic ta..."
  commit id: "TU17 General Brigham prepares Operation Twilight"
  commit id: "TU16 Alice is ordered to the front as public-relations cover"
  commit id: "TU15 Alice is arrested, labeled a deserter, and assigned to..."
  commit id: "TU14 J-Squad deploys in exoskeletons"
  commit id: "TU13 The beach assault becomes a massacre"
  branch Bob_TU13
  commit id: "Bob proves beach ambush"
  checkout main
  commit id: "TU12 Alice kills an Alpha and dies in its blood"
  branch Alice_TU12
  commit id: "Alice proves Blood Loop"
  checkout main
  commit id: "TU11 The Omega's Counter-System reopens the deployment-morni..."
  commit id: "TU10 Alice repeats the assault and improves through failure"
  commit id: "TU09 Rita recognizes Alice's impossible knowledge"
  commit id: "TU08 Carter explains the Alpha/Omega structure"
  commit id: "TU07 Alice trains with Rita through many deaths"
  commit id: "TU06 Alice follows the Switzerland signal"
  branch Alice_TU06
  commit id: "Alice proves Switzerland false target"
  checkout main
  commit id: "TU05 Alice is injured and transfused"
  branch Dana_TU05
  commit id: "Dana proves transfusion loss"
  checkout main
  commit id: "TU04 Carter identifies the Louvre as the real Omega location"
  branch Charlie_TU04
  commit id: "Charlie proves Louvre location"
  checkout main
  commit id: "TU03 Alice, Rita, Bob, Charlie, Dana, and J-Squad assault th..."
  branch Dana_TU03
  commit id: "Dana proves J-Squad survival route"
  checkout main
  commit id: "TU02 Rita dies and Alice reaches the Omega"
  commit id: "TU01 Alice destroys the Omega and is exposed to Alpha blood..."
  merge Bob_TU13 id: "Merge beach ambush"
  merge Alice_TU12 id: "Merge Blood Loop"
  merge Alice_TU06 id: "Merge false target"
  merge Dana_TU05 id: "Merge transfusion loss"
  merge Charlie_TU04 id: "Merge Louvre proof"
  merge Dana_TU03 id: "Merge final route"
  commit id: "Now - the victory state is observed before Brigham's me..." type: HIGHLIGHT
```

### Simulation Statistics

| Investigator | Rewind Dice spent | Stable branches opened | Branches Merged | Minor conflicts created | Major conflicts created | Final Willpower | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| Alice | d20, d10 | 2 | 2 | 0 | 0 | 100 | Proved the Blood Loop and rejected Switzerland under pursuit. |
| Bob | d12, d8 | 1 | 1 | 0 | 0 | 100 | Proved the beach ambush; failed the late route but marked Evidence incomplete. |
| Charlie | d12, d10 | 1 | 1 | 0 | 0 | 100 | Failed Rita's branch but gained Carter, then proved the Louvre. |
| Dana | d8, d6 | 2 | 2 | 0 | 0 | 100 | Proved transfusion loss and squad survival under pursuit. |

| Investigator | Total Branched Timelines | Merged Branched Timelines | Open Branched Timelines | Minor Conflicts Created | Minor Conflicts Resolved | Major Conflicts Created | Major Conflicts Resolved | Critical Successes | Partial Successes | Partial Failures | Critical Failures | Consequence Rolls | Gain Rolls | Willpower Tests | Willpower Test Successes | Lowest Willpower | Final Health |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Alice | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 40 | 10 |
| Bob | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 70 | 10 |
| Charlie | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 70 | 10 |
| Dana | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 40 | 10 |
| **Total** | **6** | **6** | **0** | **0** | **0** | **0** | **0** | **2** | **4** | **2** | **0** | **4** | **2** | **0** | **0** | **40** | **40** |

Outcome analysis: long rewinds are now harsher, and Bob's late route attempt no longer opens a branch. The scenario still converges because partial failure produces useful Evidence status and the other stable branches satisfy the final dependencies.
