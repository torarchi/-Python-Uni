# 1
class Poodle(Dog):

# 2
# Я - планета.
# Я - дерево.

# 3
class Cola(Beverage):
    def __init__(self):
        super().__init__('кока-кола')


# Классы Employee и ProductionWorker.
class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def get_name(self):
        return self.name

    def get_employee_number(self):
        return self.employee_number


class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_rate):
        super().__init__(name, employee_number)
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate

    def get_shift_number(self):
        return self.shift_number

    def get_hourly_rate(self):
        return self.hourly_rate


def main():
    name = input("Введите имя сотрудника: ")
    employee_number = input("Введите номер сотрудника: ")
    shift_number = int(input("Введите номер смены (1 для дневной, 2 для вечерней): "))
    hourly_rate = float(input("Введите почасовую ставку оплаты труда: "))

    worker = ProductionWorker(name, employee_number, shift_number, hourly_rate)

    print("\nИмя сотрудника:", worker.get_name())
    print("Номер сотрудника:", worker.get_employee_number())
    print("Номер смены:", worker.get_shift_number())
    print("Почасовая ставка оплаты труда:", worker.get_hourly_rate())


if __name__ == "__main__":
    main()

