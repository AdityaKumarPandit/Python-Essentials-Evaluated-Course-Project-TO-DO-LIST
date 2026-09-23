from datetime import datetime


def valid_priority(priority):
    priorities = ["High", "Medium", "Low"]
    return priority.capitalize() in priorities


def valid_date(date):
    if date == "":
        return True

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def valid_task_number(number, tasks):
    return 1 <= number <= len(tasks)