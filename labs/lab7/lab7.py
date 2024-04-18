# 9. Данные о населении.
with open('USPopulation.txt', 'r') as file:
    population_data = [int(line.strip()) for line in file]

average_change = (population_data[-1] - population_data[0]) / (len(population_data) - 1)

max_increase_year = population_data.index(max(population_data))

min_increase_year = population_data.index(min(population_data))

print("Среднегодовое изменение численности населения:", average_change)
print("Год с наибольшим увеличением численности населения:", max_increase_year + 1950)
print("Год с наименьшим увеличением численности населения:", min_increase_year + 1950)
