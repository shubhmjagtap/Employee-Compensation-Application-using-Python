#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self,empname, empaddress, vdata, salary):
        super().__init__(empname, empaddress, vdata)
        self.__salary= salary
        
    def get__salary(self):
        return self.__salary
    def set__salary(self,salary):
        self.__salary= salary
   
        
    def computesalary(self):
        sal = self.__salary
        if sal <= 45000 and sal > 0:
            compensation= sal - (.18 *sal)
        elif sal>= 45000 and sal <= 82000:
            compensation = sal - (.28*(sal-45000) + .18*45000)
        elif sal >82000:
            compensation = sal - .18*45000 - .28*37000 - .33*(sal-82000)
        return compensation
            
    def __str__(self):
        print('\n Details of Full time Employee are:')
        childdata= super().__str__()
        childdata+="\nSalary: "+str(format(self.__salary,'.2f'))
        return childdata
    
        

