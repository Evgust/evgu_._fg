#Ex1

def ggg(N):
    for i in range(N+1):
        yield i**2
gen = ggg(int(input("Enter: ")))

for san in gen:
    print(san)
    
#Ex2

def gg(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i
N = int(input("Enter: "))
gon = []
for i in gg(N):
    gon.append(i)
print(gon)

#Ex3

def both3and4(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
A = int(input("Enter: "))
for i in both3and4(A):
    print(i)
    
#Ex4

def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a, b = int(input("Enter1: ")), int(input("Enter2: "))
for i in squares(a, b):
    print(i)
    
#Ex5

def reverse(N):
    while N>=0:
        yield N
        N-=1
B = int(input("Enter: "))
for i in reverse(B):
    print(i)