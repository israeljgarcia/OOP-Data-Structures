from collections import deque


class Student:
    def __init__(self):
        self.name = ''
        self.course = ''

    def prompt(self):
        self.name = input('Name: ')
        self.course = input('Course: ')

    def display(self):
        print(f'{self.name} in {self.course}')


class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
        else:
            return False

    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)

    def help_next_student(self):
        if self.is_student_waiting():
            self.waiting_list.popleft()
            print('Helped Student')
        else:
            print('No one to help')


def main():
    option = 0
    system = HelpSystem()

    while option != 3:
        option = int(
            input('Options:\n1. Add new student\n2. Help next\n3. Quit'))

        if option == 1:
            student = Student()
            student.prompt()
            system.add_to_waiting_list(student)

        elif option == 2:
            system.help_next_student()

        elif option == 3:
            print('Quitting')


if __name__ == "__main__":
    main()
