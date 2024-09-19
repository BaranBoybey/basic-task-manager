from task import Task

class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self):
        task_name = input("Please enter the name of the task you would like to remove: ").upper()

        for task in self.tasks:
            if task_name == task.name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' has been removed.")
                return

        print("The task name provided doesn't exist.")

    def view_tasks(self):

      for task in self.tasks:
          print(task)

    def update_task(self):

        task_name = input("Please enter the name of the task you would like to update: ")

        options = ("1. Update Name", "2. Update Description", "3. Update priority", "4. Update Status")

        for task in self.tasks:
            if task_name.upper() == task.name:
                for option in options:
                    print(option)
                choice = int(input("Please choose one of the above options(1-4): "))
                if choice == 1:
                    new_name = input("Please enter the new name for the task: ")
                    task.name = new_name.upper()
                    print("The name of the task has been changed successfully")
                    return
                elif choice == 2:
                    new_description = input("Please enter the new description for the task: ")
                    task.description = new_description.upper()
                    print("The description of the task has been changed successfully")
                    return
                elif choice == 3:
                    new_priority = input("Please enter the new priority for the task (low/medium/high): ").lower()
                    if new_priority not in ["low", "medium", "high"]:
                        print("Invalid input. Please enter 'low', 'medium', or 'high'.")
                    else:
                        task.priority = new_priority.upper()
                        print("The priority of the task has been changed successfully")
                        return
                elif choice == 4:
                    task.update_status()
                    return
                else:
                    print("Invalid option!")
                    return

        print("The task name provided doesn't exist")

    def find_task(self):

        task_name = input("Please enter the task name to obtain details: ")

        for task in self.tasks:
            if task_name.upper() == task.name:
                print(task)

    def new_task(self):

        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_priority = input("Enter task priority(low/medium/high): ")
        if task_priority.lower() not in ["low", "medium", "high"]:
            print("Invalid input")
            return
        new_task_ = Task(task_name,task_description,task_priority)

        self.tasks.append(new_task_)

        print(f"The new task '{task_name}' has been created.")
        return




