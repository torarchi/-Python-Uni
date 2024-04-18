# 12. Среднее количество шагов.

with open('steps.txt', 'r') as file:
    steps_per_month = [0] * 12
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    average_steps_per_month = [0] * 12
    month_index = 0

    for line in file:
        steps = int(line.strip())
        steps_per_month[month_index] += steps
        if (month_index + 1) % 12 != 2:
            month_index += 1
        else:
            if (int(line.strip()) % 365) > 0:
                month_index = 0
            else:
                month_index += 1
    
    for month in range(12):
        average_steps_per_month[month] = steps_per_month[month] / days_in_month[month]
        print("Среднее количество шагов в месяце", month + 1, ":", average_steps_per_month[month])
