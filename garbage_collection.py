import gc

""" 
class Node():
    def __init__(self,name):
        self.name = name
        self.next = None
    def __del__(self):
        print(f"{self.name} is deleted")

a = Node("A")
b = Node("B")

a.next = b
b.next = a

print('Collecting garbage...')
gc.collect() 

class A:
    def __init__(self):
        self.b = None

a = A()
b = A()

a.b = b
b.b = a
"""
# Python program showing 
# a use of with keyword

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())