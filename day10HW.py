from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self,name,joinedyear):
        self.name=name
        self.joinedyear=joinedyear
        
    def accountage(self):
        currentyear=2025
        return currentyear - self.joinedyear
    
    @abstractmethod
    def get_role(self):
        pass
    
    
class admin(user):
    def get_role(self):
        return "admin"
    
    def __str__(self):
        return f"admin: {self.name},account age: {self.accountage()} years"

class guest(user):
    def get_role(self):
        return "guest"
    
    def __str__(self):
        return f"guest: {self.name},account age: {self.accountage()} years"
    
adminuser= admin("shibin",2020)
guestuser= guest("james",2023)


print(adminuser.get_role())
print(adminuser.accountage())
print(adminuser)

print(guestuser.get_role())
print(guestuser.accountage())
print(guestuser)
print(globals())
        
        
        
        
       