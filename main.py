from storage import load_tasks
from task_manager import (
    add_task,
    delete_task,
    edit_task,
    mark_completed,
    search_tasks,
    filter_tasks,
    get_statistics,
    clear_tasks
)
from display import show_menu, show_tasks
from validation import valid_priority, valid_date, valid_task_number


tasks = load_tasks()


while True:

    show_menu()

    try:
        option = int(input("\nEnter your choice (1-10): "))
    except ValueError:
        print("Please enter a number only.")
        continue


    # ADD TASK
    if option == 1:

        title = input("Enter task title: ").strip()

        if title == "":
            print("Task title cannot be empty.")
            continue

        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()

        if not valid_priority(priority):
            print("Invalid priority.")
            continue

        due_date = input("Enter due date (DD-MM-YYYY) or press Enter to skip: ").strip()

        if not valid_date(due_date):
            print("Invalid date. Please use DD-MM-YYYY.")
            continue

        add_task(tasks, title, priority, due_date)

        print("Task Added Successfully.")


    # VIEW TASKS
    elif option == 2:

        show_tasks(tasks)


    # EDIT TASK
    elif option == 3:

        show_tasks(tasks)

        if len(tasks) == 0:
            continue

        try:
            number = int(input("\nEnter task number to edit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not valid_task_number(number, tasks):
            print("Task number does not exist.")
            continue

        task = tasks[number - 1]

        title = input(
            f"New title [{task['title']}]: "
        ).strip()

        if title == "":
            title = task["title"]

        priority = input(
            f"New priority [{task['priority']}]: "
        ).strip().capitalize()

        if priority == "":
            priority = task["priority"]

        if not valid_priority(priority):
            print("Invalid priority.")
            continue

        due_date = input(
            f"New due date [{task['due_date']}]: "
        ).strip()

        if due_date == "":
            due_date = task["due_date"]

        if not valid_date(due_date):
            print("Invalid date.")
            continue

        edit_task(
            tasks,
            number - 1,
            title,
            priority,
            due_date
        )

        print("Task Updated Successfully.")


    # DELETE TASK
    elif option == 4:

        show_tasks(tasks)

        if len(tasks) == 0:
            continue

        try:
            number = int(input("\nEnter task number to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if valid_task_number(number, tasks):

            delete_task(tasks, number - 1)

            print("Task Deleted Successfully.")

        else:
            print("Task number does not exist.")


    # MARK COMPLETED
    elif option == 5:

        show_tasks(tasks)

        if len(tasks) == 0:
            continue

        try:
            number = int(
                input("\nEnter task number to mark completed: ")
            )
        except ValueError:
            print("Please enter a valid number.")
            continue

        if valid_task_number(number, tasks):

            mark_completed(tasks, number - 1)

            print("Task Marked as Completed.")

        else:
            print("Task number does not exist.")


    # SEARCH
    elif option == 6:

        keyword = input("Enter task name to search: ").strip()

        results = search_tasks(tasks, keyword)

        print("\nSearch Results:")

        show_tasks(results)


    # FILTER
    elif option == 7:

        print("\nFilter By:")
        print("1. Completed")
        print("2. Pending")
        print("3. High Priority")
        print("4. Medium Priority")
        print("5. Low Priority")

        filter_choice = input("\nEnter choice: ")

        if filter_choice == "1":
            results = filter_tasks(tasks, "completed")

        elif filter_choice == "2":
            results = filter_tasks(tasks, "pending")

        elif filter_choice == "3":
            results = filter_tasks(tasks, "High")

        elif filter_choice == "4":
            results = filter_tasks(tasks, "Medium")

        elif filter_choice == "5":
            results = filter_tasks(tasks, "Low")

        else:
            print("Invalid filter option.")
            continue

        show_tasks(results)


    # STATISTICS
    elif option == 8:

        total, completed, pending = get_statistics(tasks)

        print("\n================ STATISTICS =================")
        print("Total Tasks     :", total)
        print("Completed Tasks :", completed)
        print("Pending Tasks   :", pending)


    # CLEAR ALL
    elif option == 9:

        if len(tasks) == 0:
            print("There are no tasks to clear.")
            continue

        confirm = input(
            "Are you sure you want to clear all tasks? (yes/no): "
        ).lower()

        if confirm == "yes":

            clear_tasks(tasks)

            print("All Tasks Deleted Successfully.")

        else:
            print("Operation Cancelled.")


    # EXIT
    elif option == 10:

        print("\nThank you for using To-Do List Manager.")
        print("Goodbye!")

        break


    else:

        print("Please select only from options 1-10.")