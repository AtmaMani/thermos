from random import randint

def generate_unique_random_integers(num_random=20, upper_limit=40):
    unique_random_list = set()
    if num_random > upper_limit:
        num_random = upper_limit
    while len(unique_random_list) < num_random:
        unique_random_list.add(randint(0, upper_limit))
    return list(unique_random_list)