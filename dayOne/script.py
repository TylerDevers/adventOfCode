#! /usr/bin/python3

module_mass = []
with open ("input.txt", "r") as input_file:
    for line in input_file:
        module_mass.append(int(line.strip()))

def Fuel_equation(mass):
    fuel_needed = int((mass/3)) - 2 
    return fuel_needed


accumulated_fuel = 0
for mass in module_mass:
    fuel_needed = Fuel_equation(mass)

    accumulated_fuel += fuel_needed
    while(Fuel_equation(fuel_needed) > 0):
        fuel_needed = Fuel_equation(fuel_needed)
        accumulated_fuel += fuel_needed

print(accumulated_fuel)