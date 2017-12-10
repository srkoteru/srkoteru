
class employee:
    
    num_of_emp=0
    pay_raise= 1.05
    def __init__(self,fname,sname,pay):
        self.first= fname
        self.second= sname
        self.salary= pay
        self.email=fname +"."+sname +"@"'company.com'
        employee.num_of_emp +=1
        
     
    def hike(self):  
        self.salary= int(self.salary) * self.pay_raise
        #self.salary= self.salary* employee.pay_raise
        return self.salary 
    
    @classmethod
    
    def set_raise_amount(cls, amount):
        cls.pay_raise= amount
    
    @classmethod
    
    def from_string(cls,str):
        fname,sname,pay= str.split('-')
        return cls(fname,sname,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday()== 6:
           return False
        return True
    
import  datetime

    
mydate= datetime.date(2017,10,6)

print(employee.is_workday(mydate))