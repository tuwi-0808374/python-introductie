import math

a = 0.87
b = 22.7
c = 5.03

term1 = b ** 2
term2 = 4 * a * c
term3 = math.sqrt(term1 - term2)
term4 = -b + term3

term5 = 2 * a
y = term4 / term5
print(f"De waarde van y = {y} als a = {a}, b = {b} an c = {c}")