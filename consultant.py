#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from employee import Employee
class Consultant(Employee):
    def __init__(self,empname, empaddress, vdata, prtype, hrwork):
        super().__init__(empname, empaddress, vdata)
        self.__projecttype= prtype
        self.__hourwork= hrwork
        
    def get__hourwork(self):
        return self.__hourwork
    
    def set__hourwork(self,hrwork):
        self.__hourwork= hrwork
        
    def get__projecttype(self):
        return self.__projecttype
    
    def set__projecttype(self,prtype):
        self.__projecttype= prtype
    
    def computesalary(self):
        prtype = self.__projecttype
        hrwork = self.__hourwork
        if prtype ==1 :
            return hrwork*55
        elif prtype ==2 :
            return hrwork*70
        elif prtype ==3 :
            return hrwork*85
        
    def __str__(self):
        print("\nDetails of Consultant Employee are:")
        childdata= super().__str__()
        childdata+="\nHour Rate: "+str(self.__hourwork)+"\nProject Type: "+str(self.__projecttype)
        return childdata
        
        

