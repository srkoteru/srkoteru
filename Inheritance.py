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
    
class Devaloper(employee):
    
    pay_raise= 1.10
    def __init__(self,fname,sname,pay,prog_lang):
         super().__init__(fname,sname,pay)
         self.prog_lang= prog_lang
         
class Manager(employee):
    def __init__(self,fname,sname,pay,employees= None):
         super().__init__(fname,sname,pay)
         if employees is None:
           self.employees=()
         else:
            self.employees= employees
             
    def print_emp(self):
        for emp in self.employees:
           print("--->",emp.first +","+emp.second)
        
            
    def add_emp(self,emp):
        if emp not in self.employees:
         self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
         self.employees.remove(emp)
         
         
    
         
print('Number of employees:' ,employee.num_of_emp)

dev1=Devaloper('Rajesh','k',100000,'.Net')
dev2=Devaloper('Sagar','koteru',90000,"Rpgle")
dev3=Devaloper('John','Taylor',130000,'CL')

mgr2=Manager('Scot','s',120000,[dev3])
mgr1=Manager('Sue',"Smith",90000,[dev1,dev2,mgr2])
#mgr1.add_emp(dev2)

print('Number of employees:' ,employee.num_of_emp)

print(dev1.email)
print(dev1.salary)
print("salary after hike:", dev1.hike())
print(dev2.email)
print(dev2.salary)
print("salary after hike:", dev2.hike())

print(mgr1.email)
print(mgr1.salary)
print("--->", mgr1.print_emp())
print("salary after hike:", mgr1.hike())
print(mgr2.email)
print(mgr2.salary)
print("--->", mgr2.print_emp())
print("salary after hike:", mgr2.hike())

