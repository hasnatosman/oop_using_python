# class variables.................

class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp = Employee.num_of_emp + 1
        # Employee.num_of_emp = self.num_of_emp + 1

    # class methods..............
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)


# creating class instance.............
print(Employee.num_of_emp)
emp_1 = Employee('hasnat', 'osman', 50000)
emp_2 = Employee('oalid', 'islam', 60000)
print(Employee.num_of_emp)

print(Employee.__dict__)
print()

print(emp_1.__dict__)
print(emp_1.fullname())
print(emp_1.email)
emp_1.apply_raise()
print(emp_1.pay)
print()

print(emp_2.__dict__)
print(emp_2.fullname())
print(emp_2.email)
emp_2.apply_raise()
print(emp_2.pay)
