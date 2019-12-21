#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from employee import Employee
class HourlyEmployee(Employee):
    def __init__(self,empname, empaddress, vdata, hrwork, hrrate):
        super().__init__(empname, empaddress, vdata)
        self.__hourwork= hrwork
        self.__hourrate= hrrate

    def get__hourwork(self):
        return self.__hourwork

    def set__hourwork(self,hrwork):
        self.__hourwork= hrwork

    def get__hourrate(self):
        return self.__hourrate

    def set__hourrate(self,hrrate):
        self.__hourrate= hrrate
        

    def computesalary(self):
        
        hrwork= self.__hourwork
        hrrate = self.__hourrate
        if hrwork>40:
            return 40*hrrate + (hrwork- 40)*(hrrate*1.8)
        else:
            return hrwork*hrrate

    def __str__(self):
        print("\nDetails of Hourly Employee are:")
        childdata= super().__str__()
        childdata+="\nHour Rate: "+str(self.__hourrate)+"\nHour Work: "+str(self.__hourwork)
        return childdata

