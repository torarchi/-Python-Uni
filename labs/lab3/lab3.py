# 1
product = 0

while product < 100:
    num = float(input("Введите число: "))
    
    product = num * 10
    
    print("Результат умножения на 10:", product)

print("Произведение превысило 100. Цикл завершен.")

# 2
continue_calculation = True

while continue_calculation:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    result = num1 + num2
    
    print("Сумма:", result)
    
    answer = input("Желаете выполнить операцию еще раз? (да/нет): ")
    
    if answer.lower() != 'да':
        continue_calculation = False

print("Программа завершена.")

# 3
for num in range(0, 1001, 10):
    print(num, end=", ")

# 4
total = 0

for i in range(10):
    num = float(input("Введите число: "))
    total += num

print("Накопленная сумма:", total)

# 5
total = 0

for i in range(1, 31):
    total += i + (31 - i)

print("Сумма числового ряда:", total)

# 6
а) x += 1

б) x *= 2

в) x /= 10

г) x -= 100

# 7
for i in range(10):
    for j in range(15):
        print("#", end="")
    print()

# 8
number = float(input("Введите положительное ненулевое число: "))

if number > 0:
    print("Введенное число допустимо.")
else:
    print("Введенное число не является положительным ненулевым.")

# 9
number = int(input("Введите число от 1 до 100: "))

if 1 <= number <= 100:
    print("Введенное число находится в допустимом диапазоне.")
else:
    print("Введенное число не находится в допустимом диапазоне от 1 до 100.")


# 6 - Таблица соответствия между градусами Цельсия и градусами Фаренгейта.

print("Температура по Цельсию | Температура по Фаренгейту")
print("---------------------------------------------")

# Цикл для температур от 0 до 20 по Цельсию
for celsius in range(21):
    fahrenheit = (9 / 5) * celsius + 32
    print("{:^21} | {:^21}".format(celsius, fahrenheit))



