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


class Dog:
    def __init__(self, name, feature):
        self.name = name # atributebi
        self.feature = feature 
    
    def barks(self): # method 
        print(f"{self.name} is {self.feature}")


# my_dog = Dog("Buddy", "bark") # object
# print(my_dog.name) # name-s anu atribits pirdapir mivwvdi
# my_dog.barks()

# # my_dog_2 = Dog("vivi", "eating")
# # my_dog_2.barks()
# # print(my_dog_2.feature)
# # # print(f"{my_dog.name} is {my_dog.feature}ing")

# # --------------------------------------------------------------------------

# class Car:
#     def set_details(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def show_details(self):
#         print(f"{self.brand}, color: {self.color}")


# car = Car()
# # print(car.color)
# car.set_details("wrx", "black")
# print(car.color)
# car.show_details()


# ------------------------------------------------------------------------------

# __init__ - konstruqtori

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.brand} is {self.color}")

    def __str__(self): # objectis gamoprintvisas rac unda chandes aq vwert 
        return f"{self.brand} is {self.color} . ..  ."
    
    # def __repr__(self): # developerebistvis gasageb enaze 
    #     return f"Car(brand={self.brand}, color={self.color})"

car1 = Car("g_class", "white")
print(car1)
car1.drive()

car11 = Car("a-class", "pink")
print(car11)

# -----------------------------------------------------------------------------------------------------------

# ენკაფსულაცია - პირდაპირი წვდომის შეზღუდვა  
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private atributia balansi __

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough")
            # raise ValueError
    # radgan pirdapiri wvdoma Shezghudulia unda dvamato axali methodi romelshic damibrunebs balanss
    def get_balance(self):
        return self.__balance
    
account = BankAccount("B", 1000)
account.deposit(400)
account.withdraw(100)
# print(account.__balance) # pirdapiri wvdoma shezghudulia
print(account.get_balance())
      
    
# მემკვიდრეობა - მშობელი კლასის მახასიათებლები შეგიძლიათ რომ გაუზიაროთ შვილობილ კლასს

class Animal:
    def speaks(self):
        print("not speaking")


class Dog(Animal):
    def rame(self):
        super().speaks() # mshobeli klasidan super()is daxmarebit
        print("......") # es aris tviton dog klasshi damatebuli

a = Animal()
a.speaks()

d = Dog()
d.rame()


# პოლიმორფიზმი - რამდენიმე კლასსში მაქვს მეთოდის იგივე სახელები მაგრამ აქვთ სხვადასხვა დანიშნულება  

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("bark")

def animal_sound(animal):
    animal.speak()


cat = Cat()
dog = Dog()

# cat.speak()
animal_sound(cat)
# dog.speak()
animal_sound(dog)


# ------------------------------------------------------------------------------------------------------------

# აბსტრაქცია - 

# private, public, protected, final

