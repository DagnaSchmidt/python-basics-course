class Employee:
    def __init__(self, fname, sname, salary):
        self.fname = fname
        self.sname = sname
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52
    