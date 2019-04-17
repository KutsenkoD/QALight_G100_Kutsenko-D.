import random
random_list = random.sample(range(1, 100),10)
print random_list

maximum = random_list[0]
for index in range(1, len(random_list)):
    if random_list[index] > maximum:
        maximum = random_list[index]
print(maximum)
