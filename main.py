tasks = []


def add_task(task):
    task_count = len(tasks)
    tasks.append({
        "id": task_count + 1,
        "title": task
    })


def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']} : {task['title']}")


def menu():
    print("""--- Task Manager ---
    1. Add Task
    2. Show Tasks
    3. Exit""")
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
        break
    else:
        print("Invalid option. Please try again.")
