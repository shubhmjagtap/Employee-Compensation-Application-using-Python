#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vehicle import Vehicle
class Employee:
    def __init__(self, empname, empaddress, vdata):
        self.__name = empname
        self.__address = empaddress
        self.__vehicledata = vdata
    def get__name(self):
        return self.__name
    def get__address(self):
        return self.__address
    def get__vehicledata(self):
        return self.__vehicledata
    def set__name(self, empname):
        self.__name =empname
    def set__address(self, empaddress):
        self.__address = empaddress
    def set__vehicledata(self, vdata):
        self.__vehicledata = vdata
       
    def get_option4_data(self):
        if self.__vehicledata.get__mileage() > 78000:
            print("Employee name is :{0} {1}".format(self.get__name(),self.get__vehicledata()))
        
    
        
    def __str__(self):
        allData = "\nEmployee Name: " + self.__name + "; Employee Address: " + self.__address
        allData +=  "\n" + self.__vehicledata.__str__()
        return allData
    

