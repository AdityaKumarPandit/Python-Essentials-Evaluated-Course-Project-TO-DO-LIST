from task import create_task
from storage import save_tasks


def add_task(tasks, title, priority, due_date):
    task = create_task(title, priority, due_date)
    tasks.append(task)
    save_tasks(tasks)


def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)


def edit_task(tasks, index, title, priority, due_date):
    tasks[index]["title"] = title
    tasks[index]["priority"] = priority
    tasks[index]["due_date"] = due_date

    save_tasks(tasks)


def mark_completed(tasks, index):
    tasks[index]["completed"] = True
    save_tasks(tasks)


def search_tasks(tasks, keyword):
    results = []

    for task in tasks:
        if keyword.lower() in task["title"].lower():
            results.append(task)

    return results


def filter_tasks(tasks, filter_type):
    results = []

    for task in tasks:

        if filter_type == "completed" and task["completed"]:
            results.append(task)

        elif filter_type == "pending" and not task["completed"]:
            results.append(task)

        elif filter_type.lower() == task["priority"].lower():
            results.append(task)

    return results


def get_statistics(tasks):
    total = len(tasks)

    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed

    return total, completed, pending


def clear_tasks(tasks):
    tasks.clear()
    save_tasks(tasks)