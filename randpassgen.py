import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "012345678"
symbols = "[]{}()*;/,_-"

all = lower + upper + numbers + symbols
len = 16

password = "".join(random.sample(all,len))

print(password)