from student import Student
from teacher import Teacher
from doctor import Doctor
from ward import Ward

# HACK: examples
Tuan = Doctor(name="Tuan", yob=2000, specialist="Nurse")

Ngoc = Teacher(name="Ngoc", yob=1998, subject="Math")

Hieu = Student(name="Hieu", yob=2005, grade=9)


def is_yob(input_yob):
    try:
        if int(input_yob) > 1700 and int(input_yob) < 2010:
            return True
    except ValueError:
        return False


def is_number(x):
    try:
        int(x)
    except ValueError:
        return False
    return True


def add_person():
    your_name = input("Enter your name: ")
    year_of_birth = input("Enter your year of birth: ")

    if not is_number(year_of_birth):
        print("Yob must be int")
        return
    year_of_birth = int(year_of_birth)

    # NOTE: verify year_of_birth
    if not is_yob(year_of_birth):
        print("year of birth must be integer and 1700 < yob < 2010")

    your_job = input("Student | Doctor | Teacher: ")

    if your_job == "Student":
        grade = input("Enter Grade: ")
        subject = Student(name=your_name, yob=year_of_birth, grade=grade)
        print(subject.describe())

    elif your_job == "Doctor":
        specialist = input("Enter Specialist: ")
        subject = Doctor(name=your_name, yob=year_of_birth,
                         specialist=specialist)
        print(subject.describe())

    elif your_job == "Teacher":
        subject = input("Enter Subject: ")
        subject = Teacher(name=your_name, yob=year_of_birth, subject=subject)
        print(subject.describe())
    else:
        print("Job not support")
        return

    print(f"Finish add {your_job}!")
    print("------------------------")
    return subject


n_person = input("Enter n person: ")

if is_number(n_person):
    n_person = int(n_person)
    ward = Ward()
    # NOTE: add person sort as well as compute average
    for n in range(n_person):
        ward.person_list.append(add_person())

    print(f"Teacher yob average: {ward.compute_average()}")
    ward.sort_age()

    for person in ward.person_list:
        print(person.describe())
