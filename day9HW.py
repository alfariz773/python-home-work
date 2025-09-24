class account:
    def __init__(self,name,balance=1000):
        self._name=name
        self._balance=balance
    
    def __add__(self, other):
        return self._balance + other._balance
    
class savingsaccount(account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
    
    def calculate(self):
        return self._balance * 0.05
    
class currentaccount(account):
    def __init__(self, name, balance):
        super().__init__(name, balance) 
        
    def calculate(self):
        return self._balance * 0.02
    
acc1 = savingsaccount("ravi", 10000)
acc2 = currentaccount("anjali", 15000)

print(f"Account Holder: {acc1._name}, Balance: {acc1._balance}, Interest: {acc1.calculate()}")
print(f"Account Holder: {acc2._name}, Balance: {acc2._balance}, Interest: {acc2.calculate()}")


print(f"total balance (ravi + anjali): {acc1 + acc2} ")
           
        
        
