from collections import defaultdict
import random
import csv
import os

# ---------------- Constants ----------------
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
SHIFTS = ["morning", "afternoon", "evening"]

MIN_PER_SHIFT = 2          # company rule: at least 2 employees per shift
MAX_DAYS_PER_EMP = 5       # company rule: an employee works at most 5 days/week
SHIFT_CAP = 3              # a shift cannot exceed this capacity (you can tweak)
RANDOM_SEED = 42           # seed for reproducibility

# Toggle: set to False to enter employees + preferences manually
USE_RANDOM_PREFS = True

# ---------------- Data containers ----------------
# schedule[day][shift] -> list of employee names assigned
schedule = {d: {s: [] for s in SHIFTS} for d in DAYS}

# worked_days[name] -> count of distinct days this person has been assigned
worked_days = defaultdict(int)

# assigned_today[day] -> set of names assigned on that day (enforce 1 shift/day)
assigned_today = {d: set() for d in DAYS}

# preferences[name][day] -> preferred shift (basic single-choice preference)
preferences = {}

# ---------------- Core helpers ----------------
def can_assign(name, day):
    return (name not in assigned_today[day]) and (worked_days[name] < MAX_DAYS_PER_EMP)

def shift_has_room(day, shift):
    return len(schedule[day][shift]) < SHIFT_CAP

def assign(name, day, shift):
    if not can_assign(name, day):
        return False
    if not shift_has_room(day, shift):
        return False
    schedule[day][shift].append(name)
    assigned_today[day].add(name)
    worked_days[name] += 1
    return True

def try_preferred(name, day):
    pref = preferences.get(name, {}).get(day)
    if pref is None:
        return False
    return assign(name, day, pref)

def resolve_conflict_or_reassign(name, day):
    pref = preferences.get(name, {}).get(day)
    for s in SHIFTS:
        if s == pref:
            continue
        if assign(name, day, s):
            return True
    return False

def fill_minimum_staff(day, all_emps):
    # pool of candidates who *could* be assigned today
    pool = [e for e in all_emps if can_assign(e, day)]
    for s in SHIFTS:
        while len(schedule[day][s]) < MIN_PER_SHIFT:
            elig = [e for e in pool if (e not in assigned_today[day]) and (worked_days[e] < MAX_DAYS_PER_EMP)]
            if not elig:
                break  # short-staffed; no one left to place
            pick = random.choice(elig)
            if assign(pick, day, s):
                continue
            else:
                pool = [e for e in pool if e != pick]

# ---------------- Scheduling driver ----------------
def schedule_week(all_emps):
    for day in DAYS:
        for name in all_emps:
            if not can_assign(name, day):
                continue
            if try_preferred(name, day):
                continue
            resolve_conflict_or_reassign(name, day)
        fill_minimum_staff(day, all_emps)

# ---------------- Input modes ----------------
def demo_seed_preferences():
    """Random preferences for quick testing."""
    emps = ["Alex", "Blair", "Casey", "Dev", "Eden", "Finn"]
    for e in emps:
        preferences[e] = {day: random.choice(SHIFTS) for day in DAYS}
    return emps

def collect_prefs_from_input():
    """
    Simple CLI input:
      - ask for names (comma-separated)
      - for each day, for each person, ask m/a/e (or full word)
    Press Enter at 'names' prompt to fall back to demo data.
    """
    raw = input("Enter employee names, comma-separated (or press Enter to use demo): ").strip()
    if not raw:
        return demo_seed_preferences()

    emps = [x.strip() for x in raw.split(",") if x.strip()]
    print(f"\nGreat—captured {len(emps)} employees: {', '.join(emps)}")
    print("Enter preference per day: m = morning, a = afternoon, e = evening")
    print("(you can also type the full word). Example inputs: m / morning / A / evening\n")

    def normalize(choice):
        c = choice.strip().lower()
        if c in ("m", "morning"): return "morning"
        if c in ("a", "afternoon"): return "afternoon"
        if c in ("e", "evening"): return "evening"
        return None

    for e in emps:
        preferences[e] = {}
        for d in DAYS:
            while True:
                ans = input(f"{e} preference for {d} (m/a/e): ").strip()
                norm = normalize(ans)
                if norm:
                    preferences[e][d] = norm
                    break
                print("  Sorry, please enter m / a / e (or morning/afternoon/evening).")
        print()
    return emps

# ---------------- Output helpers ----------------
def pretty_print_schedule():
    print("\n============================")
    print("      Final Weekly Schedule")
    print("============================")
    for d in DAYS:
        print(f"\n{d}:")
        for s in SHIFTS:
            names = ", ".join(schedule[d][s]) if schedule[d][s] else "-"
            # include count for quick read
            print(f"  {s:10s} ({len(schedule[d][s])}) -> {names}")

def print_summary(all_emps):
    print("\n----------------------------")
    print("         Weekly Summary")
    print("----------------------------")
    # Sort by most days worked
    items = sorted(worked_days.items(), key=lambda kv: (-kv[1], kv[0]))
    for name, days in items:
        print(f"{name:10s} : {days} day(s)")
    # total assigned per day/shift
    total_assigned = sum(sum(len(schedule[d][s]) for s in SHIFTS) for d in DAYS)
    print(f"\nTotal assignments placed: {total_assigned}")
    # find any short-staffed shifts (< MIN_PER_SHIFT)
    shortages = []
    for d in DAYS:
        for s in SHIFTS:
            if len(schedule[d][s]) < MIN_PER_SHIFT:
                shortages.append((d, s, len(schedule[d][s])))
    if shortages:
        print("\nShort-staffed shifts (below minimum):")
        for d, s, c in shortages:
            print(f"  {d:3s} {s:10s} -> {c}/{MIN_PER_SHIFT}")
    else:
        print("\nAll shifts meet the minimum staffing requirement ✅")
def export_schedule_csv(out_path):
    """
    Write schedule to a CSV with columns: Day, Shift, Count, Employees.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Day", "Shift", "Count", "Employees"])
        for d in DAYS:
            for s in SHIFTS:
                names = schedule[d][s]
                writer.writerow([d, s, len(names), ", ".join(names)])

def export_summary_csv(out_path):
    """
    Write per-employee days worked to a CSV.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    rows = sorted(worked_days.items(), key=lambda kv: (-kv[1], kv[0]))
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Employee", "DaysWorked"])
        writer.writerows(rows)

def export_markdown(out_path):
    """
    Write a GitHub-friendly Markdown file of the schedule for easy viewing in the repo.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    lines = []
    lines.append("# Final Weekly Schedule\n")
    for d in DAYS:
        lines.append(f"## {d}\n")
        lines.append("| Shift | Count | Employees |")
        lines.append("|------:|:-----:|-----------|")
        for s in SHIFTS:
            names = schedule[d][s]
            lines.append(f"| {s} | {len(names)} | {', '.join(names) if names else '-'} |")
        lines.append("")  # blank line

    lines.append("\n## Weekly Summary\n")
    lines.append("| Employee | Days Worked |")
    lines.append("|----------|-------------|")
    for name, days in sorted(worked_days.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {name} | {days} |")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ---------------- Main ----------------
if __name__ == "__main__":
    random.seed(RANDOM_SEED)
    if USE_RANDOM_PREFS:
        employees = demo_seed_preferences()
    else:
        employees = collect_prefs_from_input()

    schedule_week(employees)
    pretty_print_schedule()
    print_summary(employees)
    # --- exports for your submission ---
    base_dir = os.path.dirname(__file__)                        # /python
    docs_dir = os.path.normpath(os.path.join(base_dir, "..", "docs"))

    export_schedule_csv(os.path.join(docs_dir, "schedule.csv"))
    export_summary_csv(os.path.join(docs_dir, "summary.csv"))
    export_markdown(os.path.join(docs_dir, "schedule.md"))

    print("\nFiles written to /docs:")
    print(" - docs/schedule.csv")
    print(" - docs/summary.csv")
    print(" - docs/schedule.md")

