#EX1
import re

with open('row.txt', 'r', encoding='utf-8') as file:
    ex = file.read()
first = re.compile(r'ab*')
first1 = first.findall(ex)
print(first1)

#EX2cd 

second = re.compile(r'ab{2, 3}')
second2 = second.findall(ex)
print(second2)

#EX3

ex1 = "My_good_friends_Result_blala-lalala"
third = re.compile(r'[a-z]+_[a-z]+_')
third3 = third.findall(ex1)
print(third3)

#EX4

fourth = re.compile(r'[A-Z][a-z]+')
fourth4 = fourth.findall(ex)
print(fourth4)

#EX5

f = re.compile(r'a.*b$')
f5 = f.findall(ex)
print(f5)

#EX6

s = re.compile(r'[ ,.]')
s6 = re.sub(s, ":", ex)
print(s6)

#EX7

str = "some_random_snake_case"
obj = re.compile(r'([a-zA-Z0-9]+)_([a-zA-Z0-9]+)')
p = obj.findall(str)
res = ""
for i in p:
    for j in i:
        res += j.capitalize()
a = res[0].lower() + res[1:]
print(a)

#EX8

eight = re.findall('[A-Z][a-z]*', ex)
print(eight)

#EX9

nine = re.compile(r'([a-z])([A-Z])')
nine9 = re.sub(nine, r'\1\2', ex)
print(nine9)

#EX10

ten = re.compile(r'([a-z0-9])([A-Z])')
ten1 = "caseandCase"
ten10 = ten.sub( r'\1_\2', ten1).lower()
print(ten10)