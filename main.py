tasks = []


def add_task(task):
    if tasks:
        task_id = tasks[-1]["id"]+1
    else:
        task_id = 1
    tasks.append({
        "id": task_id,
        "title": task
    })


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
    else:
        print("Task not found.")


def menu():
    print("""--- Task Manager ---
    1. Add Task
    2. Show Tasks
    3. Delete Task
    4. Exit""")
    result = input("=> ")
    return result


while True:
    choice = menu()
    if choice == "1":
        new_task = input("Write your new task: ")
        add_task(new_task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_id = input("Write your task id: ")
        delete_task(task_id)
    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")
