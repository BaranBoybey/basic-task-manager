from task import Task

class TaskManager:

    def __init__(self):
        self.tasks = []


    def remove_task(self):
        task_name = input("Please enter the name of the task you would like to remove: ")

        for task in self.tasks:
            if task_name.upper() == task.name:
                self.tasks.remove(task)
            else:
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
                elif choice == 2:
                    new_description = input("Please enter the new description for the task: ")
                    task.description = new_description.upper()
                    print("The description of the task has been changed successfully")
                elif choice == 3:
                    new_priority = input("Please enter the new name for the task(low/medium/high): ")
                    if new_priority.lower() != "low" or new_priority != "medium" or new_priority != "high":
                        print("Invalid input")
                    else:
                        task.priority = new_priority.upper()
                        print("The name of the task has been changed successfully")
                elif choice == 4:
                    task.update_status()

    def find_task(self):

        task_name = input("Please enter the task name to obtain details: ")

        for task in self.tasks:
            if task_name.upper() == task.name:
                print(task)

    def new_task(self):

        task_name = input("Enter task name: ")
        task_description = input("Enter task description")
        task_priority = input("Enter task priority(low/medium/high): ")
        if task_priority.lower() != "low" or task_priority != "medium" or task_priority != "high":
            print("Invalid input")

        new_task_ = Task(task_name,task_description,task_priority)

        self.tasks.append(new_task_)




