class Task:

    def __init__(self, name_init="Unnamed Task", description_init="No description provided",priority="low", status=False):
        self.name = name_init
        self.description = description_init
        self.priority = priority

    def getStatus(self):
        return self.priority




