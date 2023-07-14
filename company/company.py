from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def current_employees(self):
        print('Current employees:')
        for i in self.employees:
            print(i.fname, i.sname)
            print('--------------')

    def pay_employees(self):
        print('Paying employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.sname)
            print(f'Amount:, ${i.calculate_paycheck():,.2f}')
            print('-----------')

def main():
    my_company = Company()

    employee1 = Employee('Sarah', 'Johnes', 40000)
    my_company.add_employee(employee1)
    employee2 = Employee('Ola', 'Hess', 35000)
    my_company.add_employee(employee2)
    employee3 = Employee('Leo', 'Black', 45000)
    my_company.add_employee(employee3)

    my_company.current_employees()
    my_company.pay_employees()

main()