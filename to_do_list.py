tasks = []

while True:

    print(" ")
    print("=====================================================")
    print("                     TO-DO LIST                      ")
    print("=====================================================")

    print(" ")

    print("Select from the below options:")

    print(" ")

    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Delete any Task")
    print("4. Clear all Task")
    print("5. EXIT")

    print(" ")

    option = int(input("Enter the option to be done (1-5) only: "))

    print(" ")

    if option == 1:

        print(" ")
        print("=====================================================")
        print("                      ADD TASK                       ")
        print("=====================================================")

        print(" ")

        task = input("Enter the Task to be added : ")

        tasks.append(task)

        print(" ")
        print("Task Added Successfully")

        print(" ")

        number = 1

        for task in tasks:
            print(number, ".", task)
            number = number + 1

        print(" ")

    elif option == 2:

        print(" ")
        print("=====================================================")
        print("                 YOUR ALL THE TASKS                  ")
        print("=====================================================")

        print(" ")

        if len(tasks) == 0:

            print("No Tasks Added Yet.")

        else:

            number = 1

            for task in tasks:
                print(number, ".", task)
                number = number + 1

        print(" ")

    elif option == 3:

        print(" ")
        print("=====================================================")
        print("                   DELETE ANY TASK                   ")
        print("=====================================================")

        print(" ")

        if len(tasks) == 0:

            print("There are no tasks to delete.")

        else:

            number = 1

            for task in tasks:
                print(number, ".", task)
                number = number + 1

            print(" ")

            task_delete = int(input("Enter the number of task you want to delete : "))

            if task_delete >= 1 and task_delete <= len(tasks):

                task = tasks[task_delete - 1]

                tasks.remove(task)

                print(" ")
                print("Task Deleted Successfully.")

                print(" ")
                print("Your Remaining Tasks Are:")

                print(" ")

                number = 1

                for task in tasks:
                    print(number, ".", task)
                    number = number + 1

            else:

                print(" ")
                print("Task number does not exist.")

        print(" ")

    elif option == 4:

        print(" ")
        print("=====================================================")
        print("                   CLEAR ALL TASKS                   ")
        print("=====================================================")

        print(" ")

        if len(tasks) == 0:

            print("There are no tasks to clear.")

        else:

            tasks.clear()

            print("All Tasks Deleted Successfully.")

        print(" ")

    elif option == 5:

        print(" ")
        print("Exiting :(")
        print(" ")

        break

    else:

        print(" ")
        print("Hmm....")
        print("Please select only from (1-5). 👺")
        print(" ")