import random
random_integer = random.randint(0, 1)          #random integer
random_number_0_to_1 = random.random()                #random number 0 - 1
random_float = random.uniform(1, 10)            #random float
if random_integer == 0:
    print("Heads")
else:
    print("Tails")
