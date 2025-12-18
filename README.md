# Python Todo CLI

A simple yet structured command-line Todo List application written in Python. This project was built to practice Python fundamentals, data persistence, and clean CLI design.

---

## Features

* Add new tasks with priority levels
* List tasks sorted by **priority** and **completion status**
* Delete tasks
* Mark tasks as completed
* Change the priority of existing tasks
* Persistent storage using a JSON file

---

## Task Ordering Logic

When listing tasks, the application follows these rules:

1. **Incomplete tasks** are shown first
2. Tasks are ordered by priority: **High → Medium → Low**
3. **Completed tasks** are always moved to the bottom

This makes sure important and pending tasks are always visible at the top.

---

## Technologies Used

* Python 3
* JSON (for persistent storage)

---

## How to Run

```bash
python3 todolist.py
```

---

## Example Output

```text
Select an option: 1

1. wash the dishes [High] [✘]
3. take the garbage out [Medium] [✔]
2. clean the floor [Low] [✔]
```

---

## Project Structure

```text
python-todo-cli/
├── todolist.py
├── tasks.json
├── README.md
└── .gitignore
```

---

## Author

Nafiz Meriç Yıldırım

---

This project is intended as a learning exercise and a clean GitHub portfolio entry demonstrating basic backend logic, data handling, and CLI UX principles.
