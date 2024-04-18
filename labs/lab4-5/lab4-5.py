# 1. Функция times_ten
def times_ten(number):
    result = number * 10
    print(result)

# Вызов функции с аргументом 12
times_ten(12)

# 3. Значения переменных при вызове функции my_function
# a = 3, b = 2, c = 1

# 5. Вызов функции my_function с использованием именованных аргументов
def my_function(a, b, c):
    d = (a + c) / b
    print(d)

my_function(a=2, b=4, c=6)

# 6. Генерация случайного числа в диапазоне от 1 до 100
import random
rand = random.randint(1, 100)

# 7. Код для функции half
def half(number):
    return number / 2

result = half(number)

# 8. Вызов функции cube и присвоение возвращаемого значения переменной result
def cube(num):
    return num * num * num

result = cube(4)

# 9. Функция times_ten
def times_ten(number):
    return number * 10

# 10. Функция get_first_name
def get_first_name():
    first_name = input("Введите ваше имя: ")
    return first_name


# 6. Калории за счет жиров и углеводов.
fat_grams = float(input("Введите количество граммов жиров, употребленных за день: "))
carb_grams = float(input("Введите количество граммов углеводов, употребленных за день: "))

calories_from_fat = fat_grams * 9
calories_from_carbs = carb_grams * 4

print("Калории от жиров:", calories_from_fat)
print("Калории от углеводов:", calories_from_carbs)
