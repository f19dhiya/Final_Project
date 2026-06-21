# Student Cyber Security Management System

**Final Task 06 – Python Programming Internship (White Band Associates)**

## Objective

The goal of this final project was to bring together everything I learned during the internship — variables, input/output, conditionals, loops, functions, lists, and file handling — into one working application instead of a bunch of separate small programs. The application manages student records along with a basic cyber security assessment for each student, and it stores everything persistently in a text file so the data isn't lost when the program closes.

## Features

The application is fully menu-driven and supports:

1. **Add Student** – stores Student ID, Name, Branch, and Email
2. **View Students** – displays every saved record along with their security score and status
3. **Search Student** – search by either Name or Student ID
4. **Delete Student** – removes a record after a yes/no confirmation
5. **Security Assessment** – asks about MFA, password length, system updates, and antivirus, then calculates a Security Score out of 100 and assigns a status (Excellent / Good / Moderate / Poor)
6. **Generate Report** – shows total students, every student's score, the average score, and a list of students with a "Poor" rating
7. **Password Strength Checker** – checks a password and rates it Weak / Moderate / Strong
8. **Username Generator** – generates a simple username from a name and birth year
9. **Login Validation** – a basic username/password check to simulate a login system
10. **Exit** – closes the program

All records are saved to and loaded from `students.txt`, so adding, updating, or deleting a student updates the file immediately.

## Technologies Used

- **Python 3** (core language)
- Built-in `re` module – used for the password strength checker (to detect special characters)
- Plain text file storage (`students.txt`) – no external database needed
- Standard library only — no third-party packages required to run it

## Program Flow

```
Program starts
      |
      v
Load students.txt into memory (if it exists)
      |
      v
Show main menu in a loop
      |
      v
User picks an option (1-10)
      |
      +--> Add / View / Search / Delete student
      +--> Run Security Assessment (updates that student's record)
      +--> Generate Report (reads current in-memory list)
      +--> Password Strength Checker / Username Generator / Login Validation
      |
      v
Any change (add, assess, delete) is saved back to students.txt immediately
      |
      v
Loop continues until user selects Exit (option 10)
```

In short: everything revolves around one list of student dictionaries that's loaded once at startup, kept updated in memory as the user works, and written back to the file every time something actually changes.

## Challenges Faced

- **Keeping the file format simple but reliable.** I went with a pipe-separated (`|`) text format for `students.txt` instead of something like JSON, since it's easier to read/write line by line with basic file handling — but I had to be careful that none of the stored fields (like email) would ever contain a `|` character.
- **Handling "unassessed" students.** Not every student has gone through the Security Assessment yet, so I had to make sure View Students, Generate Report, and the average score calculation could all handle a score of `"None"` without crashing.
- **Validating user input.** Things like password length needed to be a number, so I added a loop that keeps asking until the user enters a valid integer instead of letting the program crash on bad input.
- **Designing the scoring logic.** Deciding how many points each security factor (MFA, password length, updates, antivirus) should be worth so the score range (0–100) actually felt meaningful and matched categories like Excellent/Good/Moderate/Poor.
- **Avoiding duplicate Student IDs.** Since IDs are typed in manually rather than auto-generated, I had to add a check before adding a new student so two records can't accidentally share the same ID.

## Learning Outcomes

This project really tied together everything from the earlier tasks into one place. A few specific things that clicked while building it:

- How to design a program around **one shared data structure** (a list of dictionaries) that every function reads from and writes to, instead of isolated scripts.
- Practical **file handling** — not just reading/writing once, but keeping a text file in sync with in-memory data across multiple operations.
- Writing functions that are **reusable and focused** on one job each (e.g., `calculate_security_score()` is separate from the function that asks the questions), which made the code much easier to debug.
- A better appreciation of **basic security concepts** like MFA, password strength, and patch/antivirus status, and how something as simple as a weighted scoring system can be used to flag risk.
- How important **input validation and error handling** are once a program is interactive instead of just running with the same fixed data every time.

## How to Run

```
python student_security_manager.py
```

The program will create `students.txt` automatically the first time you add a student — no setup needed beforehand.

## Project Structure

```
Final_Project_YourName/
├── Python Version/
│   └── student_security_manager.py
├── C Version/
│   └── student_security_manager.c
├── Documentation/
│   ├── Final_Project_Report.pdf
│   ├── README.md
│   └── Screenshots/
```
