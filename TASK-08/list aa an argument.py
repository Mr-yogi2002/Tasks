locations = [10,501,22,37,100,999,87,351]

class argument:
    def __init__(self, locations):
        self.locations = locations

    def platforms(self):
        print(self.locations)

argument = argument(locations)
argument.platforms()