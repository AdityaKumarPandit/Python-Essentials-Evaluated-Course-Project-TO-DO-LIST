import unittest

from task import create_task
from task_manager import search_tasks, get_statistics


class TestTaskManager(unittest.TestCase):

    def test_create_task(self):
        task = create_task(
            "Complete Assignment",
            "High",
            "25-09-2026"
        )

        self.assertEqual(task["title"], "Complete Assignment")
        self.assertEqual(task["priority"], "High")
        self.assertFalse(task["completed"])


    def test_search_task(self):
        tasks = [
            create_task("Study Python", "High", ""),
            create_task("Complete Maths", "Medium", "")
        ]

        result = search_tasks(tasks, "Python")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Study Python")


    def test_statistics(self):
        tasks = [
            create_task("Task 1", "High", ""),
            create_task("Task 2", "Low", "")
        ]

        tasks[0]["completed"] = True

        total, completed, pending = get_statistics(tasks)

        self.assertEqual(total, 2)
        self.assertEqual(completed, 1)
        self.assertEqual(pending, 1)


if __name__ == "__main__":
    unittest.main()