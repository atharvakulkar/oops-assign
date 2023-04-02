#!/usr/bin/env python
# coding: utf-8

# Q.1> Create a vehicle class with an init method having instance variables as name_of_vehicle,max_speed and average_of_vehicle.

# In[8]:


class Vehicle:
    def __init__(self,name_of_vehicle, max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle =  average_of_vehicle
        
car = Vehicle("Car",200,20)
print(car.name_of_vehicle) # 'Car'
print(car.max_speed) # 200
print(car.average_of_vehicle) #20
        
                 
                 


# '''Q.2> Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.'''

# In[9]:


class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity}."
    
my_car = Car("My Car", 150, 15)
print(my_car.seating_capacity(5))  # "The My Car has a seating capacity of 5."


# Q.3> What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# In[11]:


Multiple Ineheritance is feature of Object Oreinted Programming that 
allows that allows a class to inherit 
        attributes and behaviors from multiple parent classes.
    This allows for greater flexibility and 
        code reuse, as a single class can inherit the 
        characteristics of multiple 


# In[12]:


class Engine:
    def start(self):
        return "Engine started."

class FuelSystem:
    def fill_fuel(self, fuel_amount):
        return f"Fuel tank filled with {fuel_amount} liters."

class Car(Engine, FuelSystem):
    def drive(self):
        return "Car is driving."

my_car = Car()
print(my_car.start())  # "Engine started."
print(my_car.fill_fuel(50))  # "Fuel tank filled with 50 liters."
print(my_car.drive())  # "Car is driving."


# What are getter and setter in python? Create a class and create a getter and a setter method in this class

# In[13]:


Getters and setters are methods in object-oriented programming 
  that allow you to control access to the 
      attributes of an object. A getter method is used to 
      retrieve the value of an attribute, while a setter 
      method is used to set the value of an attribute.


# In[14]:


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        self._age = value

person = Person("John Doe", 30)
print(person.name)  # "John Doe"
person.name = "Jane Doe"
print(person.name)  # "Jane Doe"
print(person.age)  # 30
person.age = 35
print(person.age)  # 35


# In[ ]:




