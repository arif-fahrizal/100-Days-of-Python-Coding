import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))                               #1st options

random_list = random.randint(0, len(friends) - 1)        #2nd options
print(friends[random_list])