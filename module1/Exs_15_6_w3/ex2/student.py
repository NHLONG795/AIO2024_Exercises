from human import Human


class Student(Human):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob, job='Student')
        self.grade = grade
        pass

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Specialiast: {self.grade}"
        pass

    pass
