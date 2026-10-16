import json
from pathlib import Path
tasks = []


def load_tasks():
    tasks_file_path = Path("tasks.json")
    if not tasks_file_path.exists():
        tasks_file_path.write_text("[]", encoding="utf-8")

    with open(tasks_file_path, "r", encoding="utf-8") as file:
        tasks = json.load(file)
    return tasks


def save_tasks():
    tasks_file_path = Path("tasks.json")
    with open(tasks_file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    if tasks:
        task_id = tasks[-1]["id"]+1
    else:
        task_id = 1
    tasks.append({
        "id": task_id,
        "title": task
    })


def update_task(task_id, task_title):
    for task in tasks:
        if str(task["id"]) == str(task_id):
            task["title"] = task_title
            return True

    print("Task not found.")
    return False


def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']} : {task['title']}")


def delete_task(task_id):
    new_tasks = [
        task
        for task in tasks
        if str(task["id"]) != str(task_id)
    ]
    if len(new_tasks) != len(tasks):
        tasks[:] = new_tasks
        print("Task deleted successfully.")
        return True
    else:
        print("Task not found.")
        return False


def menu():
    print("""--- Task Manager ---
    1. Add Task
    2. Show Tasks
    3. Update Task
    4. Delete Task
    5. Exit""")
    result = input("=> ")
    return result


tasks = load_tasks()
while True:
    choice = menu()
    if choice == "1":
        new_task = input("Write your new task: ")
        add_task(new_task)
        save_tasks()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_id = input("Write your task id: ")
        task_title = input("Write your task title: ")
        result = update_task(task_id, task_title)
        if result:
            save_tasks()
    elif choice == "4":
        task_id = input("Write your task id: ")
        result = delete_task(task_id)
        if result:
            save_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please try again.")
