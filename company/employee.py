class Employee:
    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname

class SalaryEmployee(Employee):
    def __init__(self, fname, sname, salary):
        super().__init__(fname, sname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, sname, weekly_hours, hourly_rate):
        super().__init__(fname, sname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, sname, salary, sales_number, commission_rate):
        super().__init__(fname, sname, salary)
        self.sales_number = sales_number
        self.commission_rate = commission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_number*self.commission_rate
        return regular_salary+total_commission

