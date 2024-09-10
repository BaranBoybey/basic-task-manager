class Task:

    def __init__(self, name_init="Unnamed Task", description_init="No description provided",priority="low"):
        if priority.lower() not in ["low", "medium", "high"]:
            print("Invalid priority input")
        else:
            self.priority = priority
            self.name = name_init.upper()
            self.description = description_init
            self.status = False

    def update_status(self):

        status_update = input("Set the task status as 'completed' or 'incomplete'(C/I): ")

        if status_update.lower() == "c":
            self.status = True
            print("Status updated successfully")
        elif status_update.lower() == "i":
            self.status = False
            print("Status updated successfully")
        else:
            print("Invalid option")

    def __str__(self):

        return f"Task: {self.name}\nPriority: {self.priority}\nStatus: {self.status}\n Description: {self.description}"





