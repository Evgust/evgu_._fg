#EX1

from functools import reduce
from operator import mul

def multiply(numbers):
    result = reduce(mul, numbers)
    return result

num_list = map(int, input("Enter numbers separated by spaces: ").split())

result = multiply(num_list)

print("Result:", result)

#EX2

def counter(string):
    cntup = sum(1 for char in string if char.isupper())
    cntlow = sum(1 for char in string if char.islower())
    return cntup, cntlow

st = input("Enter a string: ")
cnt_up, cnt_low = counter(st)

print(f"There are {cnt_up} upper case letters and {cnt_low} lower case letters")

#EX3

txt = input("Enter a string: ")
kerek = txt[::-1]

d = False
for i in kerek:
    if i.isalnum():
        d = True
    else:
        d = False 
if kerek == txt and d:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

#EX4

import time 

num = int(input("Enter the number: "))
milsec = int(input("Enter the delay time: "))
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
print(f"Square root of {num} after {milsec} miliseconds is {sqrt}")

#EX5


mytup = (True, True, False)
mytup2 = (True, True, True)

print(all(mytup))
print(all(mytup2))
