# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random

random_01 = random.random()
random_110 = random.randint(1,10)

print(random_01)

print(random_110)

# 2) Use the datetime library together with the random number to generate a random, unique value.

import datetime

random_datetime = datetime.datetime.now()

print(random_datetime)

print((str(random_datetime) + (str(random_01))))