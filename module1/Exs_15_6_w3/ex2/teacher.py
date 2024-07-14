from human import Human


class Teacher(Human):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob, job='Teacher')
        self.subject = subject
        pass

    def describe(self):
        return f"Teacher - Name: {self.name} - YoB: {self.yob} - Specialiast: {self.subject}"
        pass

    pass
