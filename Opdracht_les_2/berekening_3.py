t = 4
v = 179875474.8
c = 299792458

term1 = v ** 2
term2 = c ** 2
term4 = term1 / term2
term5 = v * (1 - term4)
term6 = 1 / term5
delta = t * term6

print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.')