# Python Task Manager

A simple command-line task manager built with Python to practice Python fundamentals and software development basics.

## About

This project is a CLI application for managing daily tasks. It was built as a hands-on learning project to practice writing clean, modular, and maintainable Python code.

Tasks are stored locally in a JSON file, allowing them to persist between application runs.

## Features

- [x] Add new tasks
- [x] View all tasks
- [x] Edit existing tasks
- [x] Delete tasks
- [x] Mark tasks as completed or pending
- [x] Save and load tasks using JSON
- [x] Validate user inputs
- [x] Validate loaded task data
- [x] Handle invalid JSON data
- [x] Add automated tests with `pytest`

## Tech Stack

- Python
- JSON for local data persistence
- `pytest` for testing
- Git and GitHub for version control

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/TheNimaDev/python-task-manager.git
cd python-task-manager
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run the Project

Run the application:

```bash
python main.py
```

On the first run, the application creates `tasks.json` if it does not exist.

### Run Tests

Run the automated tests:

```bash
python -m pytest -v
```

## Project Structure

```text
python-task-manager/
├── main.py
├── test_main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/          # Local virtual environment (not committed)
```

`tasks.json` is created automatically at runtime if it does not exist.

The project structure may evolve as new features are implemented.

## Learning Goals

- Practice Python data structures, functions, and comprehensions
- Understand modular programming and application entry points
- Work with files and JSON serialization
- Validate user input and application data
- Handle exceptions properly
- Write automated tests
- Learn Git and GitHub workflows

## License

This project is for educational purposes.
