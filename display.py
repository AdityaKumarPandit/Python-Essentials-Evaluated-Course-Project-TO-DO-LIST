def show_menu():
    print("\n=====================================================")
    print("                 TO-DO LIST MANAGER                  ")
    print("=====================================================")

    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. Search Task")
    print("7. Filter Tasks")
    print("8. View Statistics")
    print("9. Clear All Tasks")
    print("10. Exit")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo Tasks Added Yet.")
        return

    print("\n================ YOUR TASKS =================")

    number = 1

    for task in tasks:
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        due_date = task["due_date"]

        if due_date == "":
            due_date = "No Due Date"

        print(
            f"{number}. {task['title']} | "
            f"Priority: {task['priority']} | "
            f"Due: {due_date} | "
            f"Status: {status}"
        )

        number += 1