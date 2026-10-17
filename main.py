import json
from pathlib import Path
tasks = []


def load_tasks(file_path=None):
    tasks_file_path = Path(file_path) if file_path else Path("tasks.json")

    if not tasks_file_path.exists():
        tasks_file_path.write_text("[]", encoding="utf-8")

    try:
        with open(tasks_file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            raise ValueError()

        if any(not isinstance(task, dict) for task in tasks):
            raise ValueError()

        required_keys = {"id", "title", "completed"}

        if any(not required_keys.issubset(task) for task in tasks):
            raise ValueError()

        if any(
            not (
                type(task["id"]) is int
                and type(task["title"]) is str
                and type(task["completed"]) is bool
            )
            for task in tasks
        ):
            raise ValueError()

        if any(
            not (task["title"].strip() and task["id"] > 0)
            for task in tasks
        ):
            raise ValueError()

        tasks_set = {task["id"] for task in tasks}

        if len(tasks_set) != len(tasks):
            raise ValueError()

        return tasks

    except (json.JSONDecodeError, ValueError):
        print(
            "Invalid tasks data in tasks.json. "
            "Starting with an empty task list."
        )
        return []


def save_tasks():
    tasks_file_path = Path("tasks.json")

    with open(tasks_file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    if tasks:
        task_id = tasks[-1]["id"] + 1
    else:
        task_id = 1

    tasks.append({
        "id": task_id,
        "title": task,
        "completed": False
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
            status = "Completed" if task.get("completed", False) else "Pending"
            print(f"{task['id']} : {task['title']} - {status}")


def change_completed(task_id):
    for task in tasks:
        if str(task["id"]) == str(task_id):
            task["completed"] = not task["completed"]
            return True

    print("Task not found.")
    return False


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

    print("Task not found.")
    return False


def menu():
    print("""--- Task Manager ---
    1. Add Task
    2. Show Tasks
    3. Update Task
    4. Mark as completed
    5. Delete Task
    6. Exit""")

    result = input("=> ")
    return result


def input_creator(input_title, input_type=str):
    result = input(input_title)

    if not result.strip():
        print("Input cannot be empty.")
        return None

    try:
        result = input_type(result)
    except ValueError:
        print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        return None

    if input_type is int and result <= 0:
        print("ID must be a positive integer.")
        return None

    return result


def main():
    global tasks
    tasks = load_tasks()

    while True:
        choice = menu()

        if choice == "1":
            new_task = input_creator("Write your new task: ")

            if new_task:
                add_task(new_task)
                save_tasks()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            task_id = input_creator("Write your task id: ", int)
            task_title = input_creator("Write your task title: ")

            if task_id and task_title:
                result = update_task(task_id, task_title)

                if result:
                    save_tasks()

        elif choice == "4":
            task_id = input_creator("Write your task id: ", int)

            if task_id:
                result = change_completed(task_id)

                if result:
                    save_tasks()

        elif choice == "5":
            task_id = input_creator("Write your task id: ", int)

            if task_id:
                result = delete_task(task_id)

                if result:
                    save_tasks()

        elif choice == "6":
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
