#Randomisation and Python lists

#Random module

import random
''' import my_module

random_integer = random.randint(1, 10)
print(random_integer)

#module - set of instructions which perform some functions.
print(my_module.my_favourite_number) '''

#generate a random floating point number
#random_number_0_to_1 = random.random() * 10 #1st refers to module and 2nd refers to function random.
#print(random_number_0_to_1)

#random_float = random.uniform(1, 10)
#print(random_float)

#Coin toss
random_coin = random.randint(0, 1)
if random_coin == 0:
    print("Head")
else:
    print("Tails")