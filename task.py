def create_task(title, priority="Medium", due_date=""):
    return {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }