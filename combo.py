import random
import time
import argparse
import sys

ORTHODOX = {1: "Jab", 2: "Cross", 3: "Lead hook", 4: "Rear hook", 5: "Lead uppercut", 6: "Rear uppercut"}
SOUTHPAW = {1: "Jab", 2: "Cross", 3: "Rear hook", 4: "Lead hook", 5: "Rear uppercut", 6: "Lead uppercut"}
POWER_PUNCHES = {2, 4, 6}

COMBOS = {
    "beginner": [
        {"nums": [1, 2],       "name": "Jab-cross",            "tip": "Foundation of everything. Keep your guard up on the return."},
        {"nums": [1, 1, 2],    "name": "Double jab-cross",     "tip": "First jab probes, second sets up the cross. Stay light on your feet."},
        {"nums": [1, 2, 3],    "name": "Jab-cross-hook",       "tip": "Classic 1-2-3. Pivot slightly after the hook to reset."},
        {"nums": [2, 3],       "name": "Cross-hook",           "tip": "Cross lands on the chin, hook on the temple."},
        {"nums": [1, 3],       "name": "Jab-lead hook",        "tip": "Both from the same side. Snap the jab then immediately hook."},
    ],
    "intermediate": [
        {"nums": [1, 2, 3, 2], "name": "Jab-cross-hook-cross", "tip": "End with the cross to keep your power hand active."},
        {"nums": [1, 2, 5, 2], "name": "Jab-cross-uppercut-cross", "tip": "Bend your knees for the uppercut. Drive up from the legs."},
        {"nums": [3, 2, 3],    "name": "Hook-cross-hook",      "tip": "Vary head and body on the hooks to open up targets."},
        {"nums": [1, 2, 1, 2], "name": "Double 1-2",           "tip": "Move your head between the pairs. This is Ali territory."},
        {"nums": [1, 6, 3, 2], "name": "Uppercut-setup combo", "tip": "Uppercut lifts their chin for the hook. Time the transitions."},
    ],
    "advanced": [
        {"nums": [1, 2, 3, 4, 2],    "name": "Five-punch rapid fire",   "tip": "Head movement after every two punches. Breathe out on each shot."},
        {"nums": [1, 2, 5, 6, 3],    "name": "Double uppercut finisher", "tip": "Two uppercuts set up a wide hook. Rotate your whole body."},
        {"nums": [2, 3, 2, 3, 2],    "name": "Cross-hook repeater",      "tip": "Brutal in combos. Stay balanced, reset feet between exchanges."},
        {"nums": [1, 1, 2, 3, 2, 3], "name": "Six-punch wall",           "tip": "Keep elbows in and chin down the entire time. No telegraph."},
        {"nums": [6, 3, 2, 5, 2],    "name": "Uppercut-to-cross flow",   "tip": "Start from inside. Uppercut creates the angle, rest follows."},
    ],
}

RED   = "\033[91m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
RESET = "\033[0m"
CYAN  = "\033[96m"
YELLOW = "\033[93m"

def supports_color():
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

def fmt(text, *codes):
    if not supports_color():
        return text
    return "".join(codes) + text + RESET

def print_combo(combo, punch_names, drill_mode=False):
    print()
    print(fmt(f"  {combo['name']}", BOLD))
    print()

    parts = []
    for n in combo["nums"]:
        label = punch_names[n]
        num_str = fmt(str(n), RED, BOLD) if n in POWER_PUNCHES else fmt(str(n), BOLD)
        parts.append(f"{num_str} {fmt(label, DIM)}")
    print("  " + fmt("  ->  ", DIM).join(parts))

    print()
    print(f"  {fmt('Tip:', CYAN)} {combo['tip']}")
    print()

    if drill_mode:
        run_drill(combo, punch_names)

def run_drill(combo, punch_names):
    sequence = " - ".join(punch_names[n] for n in combo["nums"])
    rounds = 3
    work = 30
    rest = 15

    print(fmt(f"  Drill: {rounds} rounds x {work}s work / {rest}s rest", YELLOW))
    print(fmt(f"  Sequence: {sequence}", DIM))
    print()

    input("  Press Enter to start...")

    for r in range(1, rounds + 1):
        print(f"\n  {fmt(f'Round {r}', BOLD, CYAN)} — GO!")
        countdown(work)
        if r < rounds:
            print(f"\n  {fmt('Rest', BOLD)} — {rest}s")
            countdown(rest)

    print(f"\n  {fmt('Done. Good work.', BOLD)}\n")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r  {i:3d}s ", end="", flush=True)
        time.sleep(1)
    print("\r        ", end="")

def main():
    parser = argparse.ArgumentParser(
        description="Boxing punch combination generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python combo.py                         random combo, beginner
  python combo.py -d advanced             random advanced combo
  python combo.py -d intermediate -n 5   5 intermediate combos
  python combo.py -s southpaw            southpaw stance
  python combo.py --drill                combo with timed drill
        """
    )
    parser.add_argument("-d", "--difficulty", choices=["beginner", "intermediate", "advanced"],
                        default="beginner", help="difficulty level (default: beginner)")
    parser.add_argument("-s", "--stance", choices=["orthodox", "southpaw"],
                        default="orthodox", help="fighting stance (default: orthodox)")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="number of combos to generate (default: 1)")
    parser.add_argument("--drill", action="store_true",
                        help="run a timed drill after generating combo")
    parser.add_argument("--all", action="store_true",
                        help="show all combos for the given difficulty")

    args = parser.parse_args()

    punch_names = ORTHODOX if args.stance == "orthodox" else SOUTHPAW
    pool = COMBOS[args.difficulty]

    print()
    stance_label = args.stance.capitalize()
    diff_label = args.difficulty.capitalize()
    print(fmt(f"  Boxing Combo Generator", BOLD) + fmt(f"  {stance_label} / {diff_label}", DIM))
    print(fmt("  " + "-" * 36, DIM))

    if args.all:
        for combo in pool:
            print_combo(combo, punch_names)
        return

    if args.drill and args.count > 1:
        print("  --drill only works with a single combo (-n 1). Ignoring -n.\n")
        args.count = 1

    seen = set()
    generated = 0
    while generated < args.count:
        combo = random.choice(pool)
        key = combo["name"]
        if args.count > 1 and key in seen and len(seen) < len(pool):
            continue
        seen.add(key)
        print_combo(combo, punch_names, drill_mode=args.drill)
        generated += 1

if __name__ == "__main__":
    main()
