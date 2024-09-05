number = 0
while True:
    number = input("Geef getal of sluit af met '.' \n")
    if number == '.':
        break
    int_number = int(number)

    numbers = list(range(1, 100))

    for i in numbers:
        is_prime = True
        for j in numbers:
            if j == 1:
                continue
            elif i % j == 0 and i != j:
                is_prime = False
                break
        if int_number == i:
            if is_prime and i != 1:
                print(f"{int_number} is priemgetal")
            else:
                print(f"{int_number} is geen priemgetal")


print("Programma gestopt")