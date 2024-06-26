import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        self.tasks.append({"name": name, "description": description})

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task["name"] != name]

    def list_tasks(self):
        return self.tasks
    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
   @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            task_manager = cls()
            task_manager.tasks = data
            return task_manager

# Example usage:
task_manager = TaskManager()
task_manager.add_task("Task 1", "Description of Task 1")
task_manager.add_task("Task 2", "Description of Task 2")
task_manager.save_to_json("tasks.json")

# Later, you can load the tasks from the JSON file
task_manager_loaded = TaskManager.load_from_json("tasks.json")
print(task_manager_loaded.list_tasks())



