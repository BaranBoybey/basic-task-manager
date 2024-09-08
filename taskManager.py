class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self,task_name):

        for task in self.tasks:
            if task_name == task.name:
                self.tasks.remove(task)

