class TotalLegitClass:
    name = 'legit name'

    def __init__(self):
        self.name = 'legit name'

    def print_name(self):
        print(self.name)

    @classmethod
    def print_name_twice(cls):
        print(cls.name*2)


TotalLegitClass.print_name_twice()