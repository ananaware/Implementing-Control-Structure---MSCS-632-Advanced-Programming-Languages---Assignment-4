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
---

## **Execution Screenshots and Explanations**

The following screenshots show the full execution and development process for both the **Python** and **Java** implementations of the Employee Scheduling project, including commits, results, and code logic verification.You can find these screenshots over here:  https://github.com/ananaware/Implementing-Control-Structure---MSCS-632-Advanced-Programming-Languages---Assignment-4/tree/main/docs/screenshots

---

### **Python Implementation**

**Screenshot (264–272):**  
The Python version of the project successfully runs the weekly scheduling logic. The terminal output displays the **Final Weekly Schedule**, with clear separation of morning, afternoon, and evening shifts for each day (Mon–Sun). Employees such as *Alex, Blair, Casey, Dev, Eden,* and *Finn* are automatically assigned to shifts according to their ranked preferences. The weekly summary confirms that each employee works five days, with a total of 30 assignments generated. The report also lists short-staffed shifts like *Monday evening* or *Friday afternoon*, helping identify where fewer workers than required were scheduled. Export files—`schedule.csv`, `summary.csv`, and `schedule.md`—are generated automatically inside the `/docs` folder.  
The screenshots also show proper Git usage: you staged changes, committed them with clear messages (like “Finalized code and documentation for Assignment 4”), and pushed them to your GitHub repository. This confirms a clean, traceable workflow and successful upload of project outputs and screenshots to version control.

---

**Screenshot (273–281):**  
These images continue showing the process of organizing your updated project. The terminal confirms that multiple new screenshots were added under `docs/screenshots/` and pushed to GitHub. The commit “Finalized code and documentation for Assignment 4” was completed successfully. The compression and delta confirmations show that Git processed the images efficiently, and the line “working tree clean” verifies that no pending changes remain locally. This section documents the final push for your Python logic and its output verification.

---

**Screenshot (283–291):**  
The next series captures the updated scheduling results after implementing **ranked preferences with same- or next-day fallback logic** in Python. The “Final Weekly Schedule” now reflects an improved balance in employee distribution, where each person still works five days, but the code dynamically handles conflicts if a shift is already full. The summary again lists all total assignments and short-staffed shifts and confirms the creation of export files.  
After running and verifying the results, the commit message *“Bonus: implement ranked preferences with same/next-day fallback”* was added, and the push shows the update was completed successfully. The last screenshot in this set displays the terminal returning “working tree clean,” confirming that everything was properly pushed and synchronized. Together, these screenshots validate that the enhanced scheduling logic works as intended and that all visual documentation is backed up in GitHub.

---

### **Java Implementation**

**Screenshot (292–304):**  
These screenshots show the process of testing, running, and documenting the Java version of the scheduling system. The output from `./run.sh` displays a **Final Weekly Schedule** that matches the Python results, confirming consistent logic between both languages. Each day lists assigned employees for morning, afternoon, and evening shifts, maintaining fair distribution across the team. The weekly summary shows that every employee worked five days, totaling 30 assignments, with clear notes on short-staffed shifts for transparency.  
You also committed and pushed updates for the Java version using messages like *“Add Java implementation with ranked prefs and next-day fallback.”* The terminal confirms that all changes, screenshots, and compiled outputs were uploaded to GitHub.  
The screenshots of your `ScheduleApp.java` source code show constants like `DAYS`, `SHIFTS`, `MIN_PER_SHIFT`, and `MAX_DAYS_PER`, which control scheduling rules. Helper methods such as `canAssign()`, `shiftHasRoom()`, and `assign()` ensure valid and limited assignments per employee. The `tryRanked()` and `resolveConflictOrReassign()` functions replicate Python’s ranked preference logic, letting the program assign employees based on top choices and reassign them to the next available shift or day when needed. This confirms that your Java program mirrors the Python behavior accurately.

---

**Screenshot (305–307):**  
These final screenshots show the closing section of the Java code. The `fillMinimumStaff()` function guarantees that every shift meets the minimum staffing requirement by selecting available employees randomly if a shift has fewer workers than required. The `scheduleWeek()` method drives the entire scheduling process by looping through each day and applying ranked assignments or conflict resolution when necessary. The `demoSeedPreferences()` method creates demo data with six employees and random shift rankings for testing, while the `printSummary()` function prints the final weekly report with total assignments, workdays per employee, and any short-staffed shifts. Together, these methods complete the Java implementation, ensuring the output matches the Python results and demonstrating a consistent, functional scheduling system across both languages.

---

**Summary:**  
All screenshots together document the complete development lifecycle — from Python implementation and testing to Java replication, enhancement with ranked preferences, and final export validation. Both versions successfully generate balanced schedules, produce reports, and meet all assignment criteria. Every step has been properly committed, pushed, and recorded in GitHub for verification and grading.



