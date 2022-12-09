class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class MonthlyEmployee(Employee):
    
    def __init__ (self,name,salary):
        super().__init__(name)
        self.salary = salary
     
    def get_pay(self):
        return (self.salary)
    
    def __str__(self):
        string = f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}$'

        return string

class MonthlyBonus(MonthlyEmployee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    

    def get_pay(self):
        return self.salary + self.bonus


    def __str__(self):
        string = f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}$'
        return string


class MonthlyContract(MonthlyEmployee):

    def __init__(self,name,salary,contracts, contractPay):
        super().__init__(name,salary)
        self.contracts = contracts
        self.contractPay = contractPay
        self.contractEarning = contracts*contractPay

    

    def get_pay(self):
        return self.salary + self.contractEarning


    def __str__(self):
        string = f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.contractPay}/contract. Their total pay is {self.get_pay()}$'
        return string



class HourlyEmployee(Employee):
    
    def __init__ (self,name,wage,wageHours):
        super().__init__(name)
        self.wage = wage
        self.wageHours = wageHours
        self.wageEarnings = wage*wageHours

    
    def get_pay(self):
        return self.wageEarnings
        

    def __str__(self):
        string = f'{self.name} works on a contract of {self.wageHours} hours at {self.wage}/hour.  Their total pay is {self.get_pay()}$'
        return string
        

class HourlyContract(HourlyEmployee):

    def __init__(self,name,wage,wageHours,contracts, contractPay):
        super().__init__(name,wage,wageHours)
        self.contracts = contracts
        self.contractPay = contractPay
        self.contractEarning = contracts*contractPay

    

    def get_pay(self):
        return self.wageEarnings + self.contractEarning


    def __str__(self):
        string = f'{self.name} works on a contract of {self.wageHours} hours at {self.wage}/hour and receives a commission for {self.contracts} contract(s) at {self.contractPay}/contract. Their total pay is {self.get_pay()}$.'
        return string



class HourlyBonus(HourlyEmployee):

    def __init__(self,name,wage,wageHours,bonus):
        super().__init__(name,wage,wageHours)
        self.bonus = bonus
    

    def get_pay(self):
        return self.wageEarnings + self.bonus


    def __str__(self):
        string = f'{self.name} works on a contract of {self.wageHours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}$'
        return string

# # Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie',4000)

# # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie',25,100)

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyContract('Renee',3000,4,200)
print(str(renee))

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContract('Jan',25,150,3,220)
print(str(jan))

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyBonus('Robbie',2000,1500)


# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonus('Ariel',30,120,600)