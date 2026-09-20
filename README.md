# To-Do List Using Python

## About the Project

This is a simple To-Do List program that I made using Python.

The main purpose of this project is to keep track of tasks. A user can add a task, see all the tasks that have been added, delete a particular task or clear the complete list.

I made this project to practice the basic concepts of Python and understand how they can be used together in a working program.

## What Can This Program Do?

The program has 5 options:

1. Add Task
2. View All Tasks
3. Delete any Task
4. Clear all Task
5. Exit

The program keeps running until the user selects the Exit option.

## How It Works

At the start, an empty list called `tasks` is created.

```python
tasks = []
```

When the user adds a task, it is stored inside this list using `append()`.

For example:

```python
tasks.append(task)
```

I used a `while` loop so that the menu keeps appearing after every operation. The program only stops when option 5 is selected.

For different menu options, I used `if`, `elif` and `else` conditions.

## Adding a Task

When option 1 is selected, the program asks the user to enter a task.

The entered task is added to the list and then all the currently available tasks are displayed with their task numbers.

## Viewing Tasks

Option 2 shows all the tasks.

If the list is empty, the program displays:

```text
No Tasks Added Yet.
```

Otherwise, it displays each task along with its number.

## Deleting a Task

For deleting a task, first the program displays all available tasks.

The user enters the number of the task that they want to delete.

For example, if the tasks are:

```text
1. Complete Python Assignment
2. Study Maths
3. Complete Lab Work
```

and the user enters `2`, the second task will be removed.

I used:

```python
tasks.remove(task)
```

for removing the selected task.

The program also checks whether the entered task number actually exists or not.

## Clearing All Tasks

Option 4 removes every task from the list.

For this I used:

```python
tasks.clear()
```

If there are no tasks already present, the program tells the user that there are no tasks to clear.

## Exiting the Program

Option 5 is used to exit the program.

The `break` statement stops the `while` loop and ends the program.

## Python Concepts I Used

While making this project, I used the following Python concepts:

* Lists
* Variables
* `while` loop
* `for` loop
* `if`, `elif` and `else`
* `input()`
* `int()`
* `len()`
* `append()`
* `remove()`
* `clear()`
* `break`

## How to Run

Python 3 should be installed on the computer.

Open the project folder in VS Code or terminal and run the Python file.

```bash
python3 todo.py
```

If your Python file has a different name, use that filename instead of `todo.py`.

## Project Files

```text
To-Do-List/
│
├── todo.py
└── README.md
```

## One Limitation

Currently the tasks are stored only while the program is running.

If I close the program and run it again, the previous tasks will not be available because I have not used a file or database to permanently save them.

## What I Can Add in Future

I can improve this project later by adding things like:

* Saving tasks in a file
* Editing an existing task
* Marking tasks as completed
* Adding task priority
* Adding due dates
* Making a graphical interface instead of only using the terminal

## Conclusion

This was a basic Python project, but it helped me understand how lists, loops and conditions work together.

Before making this, I had practiced these concepts separately. In this project I tried to combine them into one program where the user can actually add, view and manage tasks.

## Author

**Aditya Kumar Pandit**
B.Tech Computer Science and Engineering
VIT Bhopal University
