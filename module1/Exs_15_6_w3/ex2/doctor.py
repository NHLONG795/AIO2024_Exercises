# doctor.py
from human import Human


class Doctor(Human):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob, job="Doctor")
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"

    def count_doctor(person_list):
        count = 0
        for person in person_list:
            if person.job == "Doctor":
                count += 1
        return count
