```markdown
# Task Manager System

A lightweight Python application for managing tasks and users.  
This project simulates a real-world task assignment system where users can log in, add tasks, track progress, and generate reports.  
It is built using **only standard Python libraries**, making it simple, portable, and easy to run anywhere.

---

## Why This Project?
The Task Manager was designed to practice:
- Building a **user authentication system**
- Managing data with **file handling**
- Implementing **role-based permissions** (Admin vs. User)
- Generating reports and statistics from raw data
- Applying problem-solving and clean coding principles

Think of it as a mini productivity tool, perfect for small teams or individual use.

---

## Features

### General Users
- Secure login  
- Add tasks with due dates and descriptions  
- View all tasks in the system  
- View only their assigned tasks  

### Admin Users
- Register new users  
- Manage tasks (add, delete, or review completed tasks)  
- Generate detailed reports on task progress  
- Display user and task statistics  

---

## How It Works

### File Structure
- **`task_manager.py`** → Main program script  
- **`user.txt`** → Stores user credentials (`username, password`)  
- **`tasks.txt`** → Stores task records  
- **`task_overview.txt`** → Auto-generated task report  
- **`user_overview.txt`** → Auto-generated user report  

### Task Format
```

username, title, description, date_assigned, due_date, completed

```

Example:
```

alex, Prepare Sales Report, Summarize Q3 performance, 2025-09-25, 2025-10-05, No

````

---

## Getting Started

### Prerequisites
- Python 3.x installed
- No additional libraries required

### Run the Program
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
python task_manager.py
````

The first time you run the program, it will create default files (`user.txt`, `tasks.txt`) if they don’t exist.

---

## Skills Showcased

* **Python Core** (functions, conditionals, loops)
* **File Handling** (text read/write)
* **User Authentication**
* **Admin Privilege Management**
* **Date Handling** with `datetime`
* **Report Generation** (user and task statistics)
* **Problem-Solving and Algorithm Design**

---

## Future Roadmap

* Secure password storage with hashing
* Task search and filtering by deadlines
* Mark tasks as complete from the user menu
* Export reports in CSV/Excel formats
* Replace text files with SQLite database

---

## Why Use It?

This project is not just a task manager.
It’s a demonstration of **fundamental software engineering concepts** — modular code, clean structure, and practical functionality.
It can be adapted for real workflows or serve as a foundation for bigger projects.

---



