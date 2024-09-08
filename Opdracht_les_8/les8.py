import time

def zeef_van_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2
    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
        current_prime += 1

    prime_numbers = []
    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)

    return prime_numbers

cache = {}

def add_to_dict(number):
    if number in cache:
        print(f"{number} is already present")
        return cache[number]
    else:
        prime_numbers = zeef_van_eratosthenes(number)
        cache[number] = prime_numbers
        return cache[number]

# lim = 10000000
lm_str = ""
while lm_str != "x":
    lm_str = input("Geef limiet")
    if lm_str != "x":
        start_time = time.time()
        lm  = int(lm_str)
        add_to_dict(lm)
        print(cache)
        time_elapsed = time.time() - start_time
        print(time_elapsed)


# start_time = time.time()
# add_to_dict(lim)
# # print(cache)
# time_elapsed = time.time() - start_time
# print(time_elapsed)
# add_to_dict(lim)
# # print(cache)
# time_elapsed = time.time() - start_time
# print(time_elapsed)
