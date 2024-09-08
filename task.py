class Task:

    def __init__(self, name_init="Unnamed Task", description_init="No description provided",priority="low", status=False):
        self.name = name_init
        self.description = description_init
        self.priority = priority
        self.status = status

    def updateStatus(self):

        status_update = input("Set the task status as 'completed' or 'incomplete'(C/I): ")

        if status_update.lower() == "c":
            self.status = True
        elif status_update.lower() == "i":
            self.status = True
        else:
            print("Invalid option")




