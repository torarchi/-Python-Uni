# 1
my_car.go()

# 2
class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author
    
    def get_publisher(self):
        return self.publisher
    
    def set_publisher(self, publisher):
        self.publisher = publisher
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}"

# 3
# Потенциальные классы:
# BankAccount (родительский класс)
# SavingsAccount (наследует от BankAccount)
# CheckingAccount (наследует от BankAccount)
# MoneyMarketAccount (наследует от BankAccount)
# Обязанности классов:
# BankAccount: содержит общие атрибуты и методы для всех видов счетов (например, остаток на счете, процентная ставка, методы для внесения и снятия денег)
# SavingsAccount, CheckingAccount, MoneyMarketAccount: содержат специфические методы (например, методы для начисления процентов) и, возможно, дополнительные атрибуты (например, минимальный баланс для сберегательного счета)


# 1. Класс Pet.

class Pet:
    def __init__(self):
        self._name = ""
        self._animal_type = ""
        self._age = 0
    
    def set_name(self, name):
        self._name = name
    
    def set_animal_type(self, animal_type):
        self._animal_type = animal_type
    
    def set_age(self, age):
        self._age = age
    
    def get_name(self):
        return self._name
    
    def get_animal_type(self):
        return self._animal_type
    
    def get_age(self):
        return self._age

my_pet = Pet()

name = input("Введите имя вашего домашнего животного: ")
animal_type = input("Введите тип вашего домашнего животного (например, собака, кот, птица): ")
age = int(input("Введите возраст вашего домашнего животного: "))

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

print("Имя:", my_pet.get_name())
print("Тип:", my_pet.get_animal_type())
print("Возраст:", my_pet.get_age())
