from employee import SalaryEmployee, CommissionEmployee, HourlyEmployee

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

    employee1 = SalaryEmployee('Sarah', 'Johnes', 40000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Ola', 'Hess', 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Leo', 'Black', 30000, 5, 200)
    my_company.add_employee(employee3)

    my_company.current_employees()
    my_company.pay_employees()

main()