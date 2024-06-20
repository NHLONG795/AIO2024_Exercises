from quick_sort import quicksort
from teacher import Teacher


class Ward:
    def __init__(self):
        self.name = "Your warp"
        self.person_list = []
        pass

    def sort_age(self):
        quicksort(self.person_list, 0, len(self.person_list) - 1)

    def compute_average(self):
        count_teacher = 0
        sum_yob = 0

        # NOTE: get all teacher from person list
        # and get sum all yob of teacher

        for person in self.person_list:
            if isinstance(person, Teacher):
                print(f"Teacher{person}")
                count_teacher += 1
                sum_yob += person.yob
        return sum_yob / count_teacher
