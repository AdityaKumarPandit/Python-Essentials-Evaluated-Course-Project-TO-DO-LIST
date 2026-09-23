# Project Statement

## Project Title

**To-Do List Manager Using Python**

## Problem Statement

Managing multiple daily tasks can become difficult when users do not have a simple way to organize, track, and update their work.

A basic list can store task names, but it does not provide information such as task priority, due date, or completion status. It may also lose all task information when the program is closed if permanent storage is not used.

The purpose of this project is to develop a Python-based To-Do List Manager that allows users to create, organize, update, search, and track their tasks through a simple command-line interface.

## Scope of the Project

The project is a command-line task management application developed using Python.

The application allows users to:

- Add new tasks
- View all tasks
- Edit existing tasks
- Delete individual tasks
- Mark tasks as completed
- Search tasks using keywords
- Filter tasks according to status or priority
- View task statistics
- Clear all stored tasks
- Save tasks permanently using JSON storage

Each task can contain a title, priority, due date, and completion status.

The project uses separate Python modules for task creation, task management, data storage, validation, display, and the main program flow.

## Target Users

The application is designed for users who need a simple way to manage everyday tasks from a terminal.

Possible users include:

- Students managing assignments and study tasks
- Individuals managing personal activities
- Beginners who need a lightweight task-management application

## High-Level Features

### 1. Task Management

Users can add, view, edit, delete, and clear tasks.

### 2. Task Status

Tasks can be marked as completed while unfinished tasks remain in pending status.

### 3. Priority Management

Each task can be assigned one of the following priorities:

- High
- Medium
- Low

### 4. Due Dates

Users can assign a due date to a task using the DD-MM-YYYY format.

### 5. Search

Users can search for a task using keywords contained in the task title.

### 6. Filtering

Tasks can be filtered according to:

- Completed
- Pending
- High priority
- Medium priority
- Low priority

### 7. Task Statistics

The program displays:

- Total tasks
- Completed tasks
- Pending tasks

### 8. Permanent Storage

Task information is stored in a JSON file so that saved tasks remain available after the program is closed and restarted.

### 9. Input Validation

The application validates important user inputs such as menu options, task numbers, priority values, and due dates.

### 10. Testing

Unit tests are included to verify important project functionality such as task creation, task searching, and task statistics.

## Technologies Used

- Python 3
- JSON
- Python `unittest`
- Git
- GitHub

## Project Type

**Command-Line Interface (CLI) Application**