# Since lotto deals with random numbers
# I will import random


import random


# Now I will create a variable for the lotto numbers


mylotto = []
for x in range(6):
    x = random.randint(1, 50)
    mylotto.append(x)
    mylotto.sort()

# Do not add the print in the same loop


print("Your lotto numbers are as follows: ")
print(mylotto)
