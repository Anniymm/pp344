# OOP - class, objects, attribute
# object-oriented programming
#
# class ClassName - charcho saidanac unda vawarmoot objectebi - 
# modeli, dzravis moculoba, sawvavis tipi - classhi vwert - atributebi
# wrx, 2.0, dizeli - object 1
# 2_modeli, 3.5, sawvavi - object 2 

# object - classis instance 

# cvladi - atributi
# method = function (def)

# --------------------------------------------------------------------------

# atributebi - name, feature 
# __init__ - konstruqtori - methodi romelic gamoiyeneba inicializaciistvis 

# class Dog:
#     def __init__(self, name, feature):
#         self.name = name # atributebi
#         self.feature = feature 

# my_dog = Dog("Buddy", "bark") # object
# print(f"{my_dog.name} is {my_dog.feature}ing")

# class (atributebi) --konstruqtori-> object


# # ---------------------------------------------------------------------


# class Dog:
#     def __init__(self, name, feature):
#         self.name = name # atributebi
#         self.feature = feature 
    
#     def barks(self): # method 
#         print(f"{self.name} is {self.feature}")


# my_dog = Dog("Buddy", "bark") # object
# my_dog.barks()

# my_dog_2 = Dog("vivi", "eating")
# my_dog_2.barks()
# print(my_dog_2.feature)
# # print(f"{my_dog.name} is {my_dog.feature}ing")

# --------------------------------------------------------------------------

class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"{self.brand}, color: {self.color}")


car = Car()
# print(car.color)
car.set_details("wrx", "black")
print(car.color)
car.show_details()

# ------------------------------------------------------------------------------
