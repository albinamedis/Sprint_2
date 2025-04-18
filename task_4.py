class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls,name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls,name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
        
    def set_hourly_payment(self,hourly_payment):
        self.hourly_payment = hourly_payment
    
    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary


test = EmployeeSalary.get_hours('имя',2,'test@mail')
print(test.hours)

test2 = EmployeeSalary.get_email('Fedy',40, 2)
print(test2.email)

test2.set_hourly_payment(200)

print(test2.hourly_payment)
print(test2.hours)
print(test2.salary())