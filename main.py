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


new_task = input("Write your new task: ")

add_task(new_task)
show_tasks()
