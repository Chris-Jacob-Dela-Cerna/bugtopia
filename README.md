# Bugtopia
**Version 1.0.0** · Python terminal bug battle game

Bugtopia is a terminal program. It is a text-based, deck-building, turn-based bug battle game. Yes, that is a lot of words — and every one of them is accurate.

Two players each pick 3 bugs from a roster of 45, build their deck, and fight. The last player with bugs standing wins. Everything happens in the command line, in black and white, and somehow it still feels like a battle.

---

## The Bug Roster

There are **15 bug families**, each with **3 distinct species** — 45 bugs total, every one of them unique in stats and abilities.

Bugs are designed around real archetypes: glass cannons, sustains, tanks, balanced fighters. The inspiration is loosely grounded in reality — a Hercules beetle really is tougher than an ant — but this is a game, so balance comes first. That said, if you find yourself curious about what a real bug can actually do, look it up. It makes the battles hit differently.

---

## Battle System

### Turn Structure
- **Turn-based, 1v1.** Player 1 always goes first.
- Each turn has **2 instances** — one per player. Using an ability or skipping uses up your instance for that turn.
- **Ticking abilities** (damage over time, buffs, debuffs) tick every turn. Some take effect at end of turn, others take effect immediately and persist.

### Deck System
- Each player selects **3 bugs** for their deck before battle.
- All bugs are **immediately visible** — both players can see each other's full deck and choose who to target.

### Stats
| Stat | Description |
|------|-------------|
| Health | Base and max health of the bug |
| Defence | Reduces incoming damage |
| Attack | Raw attack damage |

### Damage Types
| Type | How it works |
|------|--------------|
| Damage | Reduced by defence: `Damage - Defence = Damage Dealt` |
| Raw Damage | Attack damage before defence reduction |
| True Damage | Ignores defence entirely |

---

## Abilities

Every bug has between 1 and 4 abilities. Abilities are either **Active** (manually triggered, uses your instance) or **Passive** (triggers automatically, no instance cost).

### Active — Inflicting (Instant)
| Ability | Effect |
|---------|--------|
| Attack | Deals attack as damage |
| Leech | Deals 10% of enemy's remaining health as true damage, heals that amount |
| Sacrifice | Deals 30% of your bug's remaining health as damage; costs 30% of your own health |
| Sting | Deals 20% of enemy's remaining health as true damage |

### Active — Inflicting (Ticking)
| Ability | Duration | Effect |
|---------|----------|--------|
| Burn | 2 turns | 25% of enemy's base health as damage per turn |
| Corrode | 5 turns | Permanently reduces 1 defence per turn |
| Pierce | 4 turns | Reduces enemy's defence by 50% |
| Rupture | 4 turns | Enemy takes 25% more damage from all sources |
| Sap | 4 turns | Reduces all enemy healing by 50% |
| Venom | 3 turns | Progressive true damage: 9% → 12% → 15% of base health per turn |
| Weaken | 4 turns | Reduces enemy's attack by 30% |
| Wither | 5 turns | Deals 5% of remaining health as damage per turn and reduces base health by the same amount |

### Active — Self (Instant)
| Ability | Effect |
|---------|--------|
| HealSelf | Heals 1–30% of base health based on how much health is lost; cures Rupture, Venom, and Weaken |
| Shed | Permanently drains all defence, converting and adding it to attack |

### Active — Self (Ticking)
| Ability | Duration | Effect |
|---------|----------|--------|
| Enrage | 5 turns | +30% attack |
| Harden | 5 turns | +40% defence |
| Regen | 3 turns | Heals 10% of base health per turn |
| Shell | 4 turns | 70% chance to block incoming damage |

### Passive
| Ability | Effect |
|---------|--------|
| Ambush | Once only — first attack ignores all defence |
| LastStand | +50% attack when remaining health drops below 25% |
| Molt | Once only — when remaining health drops below 10%, removes all debuffs and restores half base health |
| Thorns | Returns 50% of raw damage received back to the attacker as damage |

> **Note:** Healing is capped at 30HP regardless of source.

---

## How to Play

### Installation

1. Make sure Python 3.x is installed — download from [python.org](https://python.org). During installation, check **"Add Python to PATH"** or the run command won't work.
2. Download or clone the `bugtopia` folder.
3. Navigate into the folder and install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python main.py
```

If `python` doesn't work, try `py main.py` instead.

### Navigation

The **Enter key** is your best friend. Every pause screen in the game just requires Enter to continue — this pacing is intentional, so the battle information doesn't blur together.

### Game Flow

1. **Main Menu** — Choose Play or Quit. (`Ctrl+C` also exits at any point.)
2. **Deck Building** — Both players go through this separately.
   - Create a new deck or load a saved one.
   - A page system lets you browse all 15 families and their 3 species, with full stats and abilities shown.
   - Press `H` for controls: page switching, selecting, undo, and randomize.
   - Press `F` when your deck is ready. You'll be asked if you want to save it and what to name it.
3. **Battle** — Refer to the ability tables above. The game does not explain ability descriptions mid-battle, so knowing what Burn, Venom, Rupture, etc. do before you play will make a real difference.
4. **Result** — After a win or a tie (yes, ties are possible), the game returns to the main menu.

> **Before your first game:** Read through the abilities section. The game trusts you to know what your bugs do.

---

## Mobile (Pydroid 3)

Bugtopia runs on Android via Pydroid 3. Install the app, open the Bugtopia folder, run `main.py`. Note: horizontal line rendering may appear off in Pydroid — this is a terminal rendering difference, not a bug. It displays correctly on desktop.

---

## Built With

- **Python 3.x**
- `json` — bug data storage and loading
- `os` — file path and directory handling
- `sys` — program exit
- `re` — input validation
- `random` — ability and game logic randomization
- `millify` — health display
- `copy` — deepcopy of class variables

---

## How It's Built

The core of Bugtopia is OOP. Every bug is an instance of a `Bug` class that handles everything — family name, species name, stat calculations, damage and defence logic, what counts as a buff or debuff, separating ticking abilities from instant ones, and running per-instance and per-turn methods that calculate everything before the battle screen renders.

Bug data (stats, abilities, families) lives in JSON files rather than hardcoded into classes, which means adding a new bug or tweaking a stat doesn't require touching the class logic. This was one of the bigger structural decisions made mid-build, and it paid off.

Inheritance is used so bug family classes can borrow shared behavior from a base class. Instance variables, class variables, properties, and methods all appear across the codebase — not for the sake of using them, but because the game mechanics genuinely needed them.

Almost every concept covered in CS50P ended up somewhere in this project: exception handling, file I/O, regex for input validation, external libraries, and OOP as the backbone of the entire system. The damage math — while not complex — turned out to be one of the most creatively interesting parts: figuring out how damage is calculated, what gets reduced, what gets ignored, and how healing interacts with all of it created real design space.

---

## Planned Features (v2.0.0)

- **Improved code structure** — the current codebase is clean and readable, but there's a higher standard to get to. This is the first thing on the list.
- **More ability types** — the current system has room to expand: team abilities, conditional triggers, combo interactions between abilities.
- **More bugs** — 45 is a start. More families, more species, more ability combinations.

---

## Background

This is my second personal portfolio project, and the most ambitious thing I've built so far.

I started coding from scratch on March 27, 2026 — zero experience, zero background. Bugtopia began as a class exercise while studying OOP in CS50P Week 8, originally called Battlopia. When the Final Project deadline approached, I pivoted the concept, rebuilt the foundations, and turned it into something I actually wanted other people to play.

It took **64 hours across 15 days** to finish.

Halfway through, my laptop broke. It became 10x slower and stayed that way. I spent hours trying to fix it and couldn't. So I kept working on it anyway. My motivation came from looking back at how far I'd come since March — starting from nothing, getting through CS50P week by week, building projects that kept getting more complex. That context made the broken laptop feel like a smaller problem than it actually was.

I have a genuine interest in bugs — not an obsession, but real fascination with what certain insects are actually capable of. That interest is what made this game possible. It gave me a reason to care about the design beyond just making it functional.

If you play this: I hope you feel the battle, even in black and white.