## Project Overview

Generates randomized punch combinations by difficulty and stance. Each combo includes a number sequence (the standard boxing shorthand), full punch names, and a coaching tip. Optional drill mode runs timed rounds so you can actually train with it.

```
  Boxing Combo Generator  Orthodox / Intermediate
  ------------------------------------------------

  Jab-cross-uppercut-cross

  1 Jab  ->  2 Cross  ->  5 Lead uppercut  ->  2 Cross

  Tip: Bend your knees for the uppercut. Drive up from the legs.
```

Power punches (2, 4, 6) are highlighted in red in the terminal.

## Usage

```bash
python combo.py
```

```bash
# options
-d, --difficulty    beginner | intermediate | advanced   (default: beginner)
-s, --stance        orthodox | southpaw                  (default: orthodox)
-n, --count         number of combos to generate         (default: 1)
--drill             run a timed drill after the combo
--all               show every combo for the difficulty
```

**Examples**

```bash
python combo.py -d advanced                 # one advanced combo
python combo.py -d intermediate -n 5        # five intermediate combos
python combo.py -s southpaw -d beginner     # southpaw stance
python combo.py -d intermediate --drill     # combo + 3x30s timed drill
python combo.py --all -d beginner           # all beginner combos
```

## Punch numbering

Standard boxing notation used worldwide:

| Number | Punch |
|--------|-------|
| 1 | Jab |
| 2 | Cross |
| 3 | Lead hook |
| 4 | Rear hook |
| 5 | Lead uppercut |
| 6 | Rear uppercut |

Southpaw stance mirrors hooks and uppercuts (3/4 and 5/6 swap sides).

## Drill mode

```bash
python combo.py -d intermediate --drill
```

Runs 3 rounds of 30 seconds work / 15 seconds rest with a live countdown. Gives you one combo to drill for the full session rather than randomizing mid-workout.

## No dependencies

Standard library only. No installs.

```bash
git clone https://github.com/mostafa-ehab22/Boxing-Combo-Generator
cd Boxing-Combo-Generator
python combo.py
```

---
