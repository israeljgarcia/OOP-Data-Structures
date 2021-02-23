class Employee(ABC):
    def __init__(self):
        self.name = ''

    @abstractmethod
    def display(self):
        print(self.name)

    @abstractmethod
    def get_paycheck(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_wage = 8
        self.hours = 0

    def display(self):
        print(f'{self.name} - {self.hourly_wage}/hour')

    def get_paycheck(self):
        print(f'{self.hours * self.hourly_wage}')


class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 50000

    def display(self):
        print(f'{self.name} - {self.salary}/year')

    def get_paycheck(self):
        print(f'{self.salary / 24}')

    def display_employee_data(self, employee: Employee):
        print(f'{employee.display()}')


def main():
    employees = []
    loop_key = 'a'

    while loop_key != 'q':

        loop_key = input('Hourly(h) or Salary(s)? \n')

        if loop_key == 'h':
            name = input('Name: ')
            hourly_wage = int(input('Hourly Rate:'))
            hours = int(input('Hours Worked: '))

            employee = HourlyEmployee()
            employee.name = name
            employee.hourly_wage = hourly_wage

            employees.append(employee)

        if loop_key == 's':
            name = input('Name: ')
            salary = int(input('Salary: \n'))

            employee = SalaryEmployee()
            employee.name = name
            employee.salary = salary

            employees.append(employee)

    for employee in employees:
        employee.display()


if __name__ == '__main__':
    main()
