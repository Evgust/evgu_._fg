#Ex1
class Mycl():
    def getString(self):
        self.strng = input()
    def printString(self):
        print(self.strng.upper())

a = Mycl()
a.getString()
a.printString()
#Ух ема оңай екен ғой

#Ex2

class Shape:
    def __init__(self):
        self.area = 0
    def ff(self):
        pass
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def ff(self):
        self.area = self.length **2

square = Square(5)
square.ff()
print(square.area)

#енгізу керек емес шығар санды енді 

#Ex3

class Shape:
    def __init__(self, length):
        self.length = length
        self.shape_area = 0
        

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
        


    def area(self):
        self.shape_area = self.width * self.length
        print(self.shape_area)

rectangle = Rectangle(2,3)
rectangle.area()

#Ex4

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

point1 = Point(2, 3)
point2 = Point(5, 7)
point1.show()
point2.show()
print(f"Distance between 2 points: {point1.dist(point2)}")

#Ex5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited money {amount}. New money: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"I need {amount}. New money: {self.balance}")
        else:
            print("No enough money")

account = Account("Elana", 9999)
account.deposit(570)
account.withdraw(699)
account.withdraw(982)

#Ex6

a = [2, 3, 5, 8, 13, 17, 20, 23, 29, 31]

b = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, a))

print("A", b)
