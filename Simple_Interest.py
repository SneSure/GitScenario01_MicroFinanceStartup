# Program to calculate and display Simple Interest

p = int(input('Enter Principal : '))
r = float(input('Enter Rate of Interest (per annum): '))
t = int(input('Enter Time (in years) : '))
si = (p * r * t) / 100
print('Simple Interest =', si)
