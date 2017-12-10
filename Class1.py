class employee:
    
    def __init__(self,fname,sname,pay):
        self.first= fname
        self.second= sname
        self.salary= pay
        self.email=fname +"."+sname +"@"'company.com'
        
emp1=employee('Rajesh','k',100000)
emp2=employee('Sagar','koteru',90000)
emp3=employee('John','Taylor',130000)


print(emp1.first)
print(emp1.second)
print(emp1.salary)
print(emp1.email)
print(emp2.first)
print(emp2.second)
print(emp2.salary)
print(emp2.email)
print(emp3.first)
print(emp3.second)
print(emp3.salary)
print(emp3.email)