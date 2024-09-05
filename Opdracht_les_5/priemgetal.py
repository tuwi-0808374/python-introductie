numbers = list(range(1, 100))

for i in numbers:
    is_prime = True
    for j in numbers:
        if j == 1:
            continue
        elif i % j == 0 and i != j:
            is_prime = False
            break
    if is_prime and i != 1:
        print(i)