"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee():

    def __init__(self, name):
        self.name = name
        
        self.contract_type = None
        self.contract_pay = None
        self.hours = None

        self.commision_type = None
        self.commision_pay = None
        self.commision_contract_no = None


    def set_contract_as_salary(self, pay):
       self.contract_type = 'salary'
       self.contract_pay = pay

    def set_contract_as_hourly(self, hours, pay):
       self.contract_type = 'hourly'
       self.contract_pay = pay
       self.hours = hours

    def set_commission_as_bonus(self, bonus):
       self.commission_type = 'bonus'
       self.commision_pay = bonus

    def set_commission_as_contract(self, bonus, contracts):
       self.contract_type = 'contract'
       self.contract_pay = bonus
       self.commision_contract_no = contracts

    def get_pay(self):
        pay = 0

        if self.contract_type == 'salary':
            pay = self.contract_pay
        elif self.contract_type == 'hourly':
            pay = (self.contract_pay*self.hours)

        if self.commision_type == 'bonus':
            pay += self.commision_pay
        elif self.commision_type == 'contract':
            pay += (self.commision_pay*self.commision_contract_no)

        return pay

    def __str__(self):
        string = f'{self.name}'

        if self.contract_type == 'salary':
            string += f' works on a monthly salary of {self.contract_pay}'
        elif self.contract_type == 'hourly':
            string += f' works on a contract of {self.contract_pay} hours at {self.hours}/hour'

        if self.commision_type == 'bonus':
            string += f' and receives a bonus commission of {self.commision_pay}.'
        elif self.commision_type == 'contract':
            string += f' and receives a commission for {self.commision_contract_no} contract(s) at {self.commision_pay}/contract.'
        else:
            string += '.'

        string += f' Their total pay is {self.get_pay()}.'
        return string




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_contract_as_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_contract_as_hourly(100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_contract_as_salary(3000)
renee.set_commission_as_contract(200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_contract_as_hourly(150, 25)
jan.set_commission_as_contract(220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_contract_as_salary(2000)
robbie.set_commission_as_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_contract_as_hourly(120, 30)
ariel.set_commission_as_bonus(600)

