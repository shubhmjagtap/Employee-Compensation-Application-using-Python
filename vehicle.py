class Vehicle:
    def __init__(self,make,model,year,mlg):
        self.__make= make
        self.__model= model
        self.__year= year
        self.__mileage=mlg
    
    def get__make(self):
        return self.__make
    def get__model(self):
        return self.__model
    def get__year(self):
        return self.__year
    def get__mileage(self):
        return int(self.__mileage)
    def set__make(self, mk):
        self.__make = mk
    def set__model(self, md):
        self.__model = md
    def set__year(self, yr):
        self.__year = yr
    def set__mileage(self, mg):
        self.__mileage = mg
    def __str__(self):
        return "Make: " + self.__make + "; Model: " + self.__model+ ":Year: " + str(self.__year) + "; Mileage: " + str(self.__mileage) 
    