class Task:

    def __init__(self, name_init="Unnamed Task", description_init="No description provided",priority="low"):
        self.name = name_init.upper()
        self.description = description_init
        self.priority = priority
        self.status = False

    def update_status(self):

        status_update = input("Set the task status as 'completed' or 'incomplete'(C/I): ")

        if status_update.lower() == "c":
            self.status = True
        elif status_update.lower() == "i":
            self.status = False
        else:
            print("Invalid option")

    def __str__(self):

        return f"Task: {self.name}\nPriority: {self.priority}\nStatus: {self.status}\n Description: {self.description}"





