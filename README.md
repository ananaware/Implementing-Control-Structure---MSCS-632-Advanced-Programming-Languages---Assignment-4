# MSCS 632 – Assignment 4: Implementing Control Structures (Employee Scheduling)

## Overview
This project demonstrates implementation of control structures (conditionals, loops, and branching) across two programming languages — **Python** and **Java**.  
The program manages employee shifts for a company operating 7 days a week. Employees select preferred shifts (morning, afternoon, or evening), and the system automatically schedules them following specific constraints.

## Folder Structure
```
Implementing-Control-Structure---MSCS-632-Advanced-Programming-Languages---Assignment-4/
├─ README.md
├─ python/
│ ├─ schedule_app.py
│ └─ requirements.txt
├─ java/
│ ├─ src/
│ │ └─ ScheduleApp.java
│ └─ run.sh
└─ docs/
└─ screenshots/
```
---
## How to Run

### Python
```bash
cd python
python schedule_app.py
```

### Java
```bash
cd java
./run.sh
```

---
## Notes

Currently, both Python and Java versions print a test message confirming the environment works.

Future updates will include:

Real scheduling logic (loops, conditionals, random assignment)

Shift conflict resolution

Weekly output formatting

Optional GUI for input/output

## Reference

Sebesta, R. (2016). Concepts of Programming Languages (12th ed.). Pearson Education.

---

## Bonus & Java Implementation

- Added **ranked preference scheduling** with same-day and next-day fallback in both **Python** and **Java** versions.  
- Python script (`python/schedule_app.py`) now supports 3-level ranked preferences per day.  
- Java version (`java/src/ScheduleApp.java`) mirrors the Python logic using object-oriented structures.  
- Exported results are automatically written to `/docs`:
  - `schedule.csv`
  - `summary.csv`
  - `schedule.md`
- Execution screenshots are stored in `/docs/screenshots/` for verification and grading.

---

---

## Environment
- Python 3.10+ (standard library only; no external packages)
- Java 17+ (tested with OpenJDK)
- OS: Windows (Git Bash / Notepad), should work similarly on macOS/Linux

## Notes
- Python supports **ranked preferences** per day. Toggle input mode in `python/schedule_app.py`:
  - `USE_RANDOM_PREFS=True`  → quick demo (seeded)
  - `USE_RANDOM_PREFS=False` → manual CLI (enter names + daily rankings: `m>a>e`)
- Exports are written to `docs/`: `schedule.md`, `schedule.csv`, `summary.csv`.
- Screenshots of final outputs are stored in `docs/screenshots/`.

## Java Run Notes
- The script `java/run.sh` compiles the Java program and runs it automatically.
- It builds the compiled files under `java/out` and executes `ScheduleApp`.
- To run manually:
  ```bash
  cd java
  javac -d out src/ScheduleApp.java
  java -cp out ScheduleApp
  ```



