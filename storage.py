import json
import os


DATA_FILE = "data/tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)