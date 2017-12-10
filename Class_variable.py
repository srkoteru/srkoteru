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
        self.salary= self.salary* self.pay_raise
        #self.salary= self.salary* employee.pay_raise
        return self.salary 
         
print('Number of employees:' ,employee.num_of_emp)

emp1=employee('Rajesh','k',100000)
emp2=employee('Sagar','koteru',90000)
emp3=employee('John','Taylor',130000)

print('Number of employees:' ,employee.num_of_emp)

emp2.pay_raise= 1.50

print('employee1 :')
print(emp1.first)
print(emp1.second)
print(emp1.salary)
print(emp1.email)
print('salary after hike:', emp1.hike())
print('employee2 :')
print(emp2.first)
print(emp2.second)
print(emp2.salary)
print( 'salary after hike:',emp2.hike())
print(emp2.email)

print('employee3 :')
print(emp3.first)
print(emp3.second)
print(emp3.salary)
print('salary after hike:',emp3.hike())
print(emp3.email)