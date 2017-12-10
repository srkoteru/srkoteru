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
        
    

employee.set_raise_amount(6)
         
print('Number of employees:' ,employee.num_of_emp)

str1="Rajesh-K-100000"
str2="Sagar-koteru-90000"
str3="John-Taylor-130000"

emp1=employee.from_string(str1)
emp2=employee.from_string(str2)
emp3=employee.from_string(str3)

print('Number of employees:' ,employee.num_of_emp)

emp2.pay_raise= 3

print('employee1 :')
print(emp1.first)
print(emp1.second)
print(emp1.salary)

print('salary after hike:', emp1.hike())
print(emp1.email,"\n")

print('employee2 :')
print(emp2.first)
print(emp2.second)
print(emp2.salary)
print( 'salary after hike:',emp2.hike())
print(emp2.email,"\n")

print('employee3 :')
print(emp3.first)
print(emp3.second)
print(emp3.salary)
print('salary after hike:',emp3.hike())
print(emp3.email,"\n")