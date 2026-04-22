# Student Management System

A simple command-line application built in Python to manage student records.

## Features

- Add a student with their name and marks
- View all students with their marks and pass/fail status
- Find the topper (student with the highest marks)
- Search for a specific student and view their result
- Exit the program cleanly

## How to Run

Make sure you have Python installed, then run:

```bash
python main.py
```

## Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add a new student |
| 2 | Show all students with marks and result |
| 3 | Find the topper |
| 4 | Search for a student by name |
| 5 | Exit the program |

## Pass/Fail Criteria

- Marks **>= 50** → PASS
- Marks **< 50** → FAIL

## Example

```
--- STUDENT MANAGEMENT SYSTEM ---
1. ADD STUDENT
2. SHOW ALL STUDENTS
3. FIND TOPPER
4. SEARCH STUDENT
5. EXIT..
ENTER YOUR CHOICE: 1
ENTER STUDENT NAME: Amy
ENTER STUDENT MARKS: 85
STUDENT ADDED SUCCESSFULLY...
```

## Requirements

- Python 3.x
- No external libraries needed
