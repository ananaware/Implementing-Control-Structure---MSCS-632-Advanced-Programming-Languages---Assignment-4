# MSCS 532 – Assignment 4: Implementing Control Structures (Employee Scheduling)

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
## How to Run

### Python
```bash
cd python
python schedule_app.py
cd java
./run.sh
```
##Notes

Currently, both Python and Java versions print a test message confirming the environment works.

Future updates will include:

Real scheduling logic (loops, conditionals, random assignment)

Shift conflict resolution

Weekly output formatting

Optional GUI for input/output

##Reference

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
