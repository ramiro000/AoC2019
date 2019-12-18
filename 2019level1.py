#AoC 2019 level 1 - 18/12/2019 - Python
import math, re
from decimal import Decimal

fueltotal = 0
module_mass = []

def calculate_fuel(mass):
	i = math.floor(mass / 3) - 2
	i_future = math.floor(i / 3) - 2
	if i_future <= 0:
		module_mass.append(Decimal(i).normalize())
		return 0
	else:
		module_mass.append(Decimal(i).normalize())
		calculate_fuel(i)

listofmasses = open("2019level1.txt", "r")

numbers = re.findall('([0-9]+)', listofmasses.read())

for number in numbers:

	calculate_fuel(int(number))

print sum(module_mass)
