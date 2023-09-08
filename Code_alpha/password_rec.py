import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%^&*()+[]{}\?<>;'
number = '0123456789'

create = lower + upper + number + symbol
len = 16
password = "".join(random.sample(create,len))
print("The Generated Password is:", password)