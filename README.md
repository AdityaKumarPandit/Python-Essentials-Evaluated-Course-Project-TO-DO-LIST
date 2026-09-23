# To-Do List Manager Using Python

## About the Project

This is a command-line To-Do List Manager developed using Python.

The purpose of this project is to provide a simple task management system where users can create and manage their daily tasks. The project started as a basic To-Do List and was later developed into a modular application with permanent data storage, task priorities, due dates, searching, filtering, statistics, validation, and testing.

This project was developed as part of the Python Essentials Evaluated Course Project.

## Features

The program currently provides the following options:

1. Add Task
2. View All Tasks
3. Edit Task
4. Delete Task
5. Mark Task Completed
6. Search Task
7. Filter Tasks
8. View Statistics
9. Clear All Tasks
10. Exit

## How the Project Works

When the program starts, previously saved tasks are loaded from the JSON data file.

Each task contains:

- Task title
- Priority
- Due date
- Completion status

A task is represented in Python using a dictionary.

For example:

```python
{
    "title": "Complete Python Assignment",
    "priority": "High",
    "due_date": "25-09-2026",
    "completed": False
}
```

The program continues running until the user selects the Exit option.

## Adding a Task

The user can create a new task by entering:

- Task title
- Priority: High, Medium, or Low
- Due date in DD-MM-YYYY format

The program validates the entered information before adding the task.

After a task is added, it is saved to the JSON file so that it remains available even after the program is closed.

## Viewing Tasks

The View All Tasks option displays all saved tasks.

For every task, the program shows:

- Task number
- Title
- Priority
- Due date
- Status

The status is displayed as either `Pending` or `Completed`.

## Editing a Task

An existing task can be edited by selecting its task number.

The user can update:

- Task title
- Priority
- Due date

If the user does not enter a new value, the existing value is retained.

## Deleting a Task

The user can delete a particular task by entering its task number.

The program validates the task number before deleting the selected task.

The updated task list is then saved automatically.

## Marking a Task as Completed

A task can be marked as completed by selecting its task number.

Its completion status is updated from Pending to Completed and saved permanently.

## Searching Tasks

The Search option allows the user to search for tasks using a keyword.

The search is case-insensitive and checks the task title for matching text.

## Filtering Tasks

Tasks can be filtered according to:

- Completed tasks
- Pending tasks
- High priority
- Medium priority
- Low priority

This allows users to quickly view tasks belonging to a particular category.

## Task Statistics

The program can calculate and display:

- Total number of tasks
- Number of completed tasks
- Number of pending tasks

## Permanent Data Storage

Tasks are stored in:

```text
data/tasks.json
```

JSON storage allows tasks to remain available after the program is closed and restarted.

The program automatically loads the saved tasks when it starts.

## Input Validation and Error Handling

The program includes validation for:

- Menu selections
- Task numbers
- Priority values
- Due-date format
- Empty task titles
- Non-numeric input where numbers are required

This helps prevent invalid input from causing unexpected program errors.

## Modular Project Structure

The project is divided into separate Python modules so that different responsibilities are handled independently.

```text
Python-Essentials-Evaluated-Course-Project-TO-DO-LIST/
│
├── data/
│   └── tasks.json
│
├── tests/
│   └── test_task_manager.py
│
├── .gitignore
├── display.py
├── main.py
├── requirements.txt
├── statement.md
├── storage.py
├── task.py
├── task_manager.py
├── validation.py
└── README.md
```

### Purpose of the Main Files

- `main.py` - Runs the application and controls the main program flow.
- `task.py` - Creates the task data structure.
- `task_manager.py` - Handles task-management operations.
- `storage.py` - Loads and saves tasks using JSON.
- `validation.py` - Handles input validation.
- `display.py` - Displays menus and task information.
- `data/tasks.json` - Stores task data permanently.
- `tests/test_task_manager.py` - Contains unit tests for important functionality.
- `statement.md` - Contains the project problem statement, scope, target users, and high-level features.

## Python Concepts Used

This project uses several Python concepts, including:

- Variables
- Lists
- Dictionaries
- Functions
- Modules
- Loops
- Conditional statements
- User input
- File handling
- JSON
- Exception handling
- String operations
- Imports
- Functions with parameters and return values
- Unit testing

## Testing

The project includes unit tests for important functionality.

To run the tests from the project root directory:

```bash
python3 -m unittest discover -s tests
```

A successful test run should display:

```text
Ran 3 tests

OK
```

The tests currently check:

- Task creation
- Task searching
- Task statistics

## How to Run the Project

Python 3 must be installed on the computer.

Open the project folder in VS Code or Terminal and run:

```bash
python3 main.py
```

The main menu will then appear in the terminal.

## Future Enhancements

The project can be further improved in the future by adding features such as:

- Task categories
- Sorting tasks by due date
- Overdue-task identification
- Recurring tasks
- Additional automated tests
- Graphical User Interface (GUI)

## Conclusion

This project demonstrates how basic and intermediate Python concepts can be combined to build a functional task-management application.

The project uses a modular structure to separate task management, storage, validation, and display responsibilities. JSON-based storage provides data persistence, while validation and unit testing improve the reliability of the application.

## Author

**Aditya Kumar Pandit**

B.Tech Computer Science and Engineering  
VIT Bhopal University