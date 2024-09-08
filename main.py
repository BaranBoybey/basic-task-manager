from task import Task
from taskManager import TaskManager

def main():

    task_1 = Task("Buy groceries", "Buy bread and egg", "medium")
    task_2 = Task("Do Homework", "MATH 107, section 1.1 practice problems", "high")

    task_manager = TaskManager()

    task_manager.add_task(task_1)
    task_manager.add_task(task_2)

    print("Welcome to Your Task Manager Program")

    options = ("1. Create New Task", "2. Remove Task", "3. View All Tasks", "4. Update a Task", "5. Find a Task", "6. Exit")

    while True:

        for option in options:
            print(option)

        choice = input("Please choose from the above options(1-6): ")
        if choice == "1":
            task_manager.new_task()
        elif choice == "2":
            task_manager.remove_task()
        elif choice == "3":
            task_manager.view_tasks()
        elif choice == "4":
            task_manager.update_task()
        elif choice == "5":
            task_manager.find_task()
        elif choice == "6":
            print("Good Bye!")
            break
        else:
            print("Invalid input!")



if __name__ == "__main__":
    main()