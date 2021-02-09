class Student:
    def __init_(self):
        self.first_name = ""
        self.last_name = ""
        self.student_id = 0

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_student_id(self, stu_id):
        self.student_id = stu_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_id(self):
        return self.student_id


def main():
    user = prompt_student()
    display_student(user)


def prompt_student():
    student = Student()

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    student_id = int(input("Please enter your id number: "))

    student.set_first_name(first_name)
    student.set_last_name(last_name)
    student.set_student_id(student_id)

    return student


def display_student(student_obj):
    print("\nYour information:")
    print(f'{student_obj.get_student_id()} - {student_obj.get_first_name()} {student_obj.get_last_name()}')


if __name__ == "__main__":
    main()
