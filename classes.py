import json

class Address:
    def __init__(self, street, city, zip_code):
        self.street, self.city, self.zip_code = street,city, zip_code
class Person:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age,address

class Car:
    def __init__(self, make, model, year, owner):
        self.make, self.model, self.year, self.owner = make, model, year,   owner
# relating
address = Address("123 Main St", " Cityville", "12345")
person = Person("John", 30, address)
car = Car("Toyota", "Camry", 2022,  person)

# convert to jsonn
address_json = json.dumps(address.__dict__)
person_json = json.dumps(person.__dict__)
car_json = json.dumps(car.__dict__)

print("Address JSON:", address_json)

print("Person JSON:", person_json)

print("Car JSON: ", car_json)

