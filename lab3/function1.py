#Бсмлаа бастайын
#Ex1

def ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

print(ounces(45))

#Ex2

def Fahrenheit(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

print(Fahrenheit(2))

#Ex3

def solution(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if (2 * i + 4 * j) == legs:
            return i, j
    return None

#Ex4

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filterprime(numbers):
    return [num for num in numbers if is_prime(num)]

#Ex5

from itertools import permutations

def stringpermutations(input_str):
    return [''.join(perm) for perm in permutations(input_str)]


#Ex6

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

#Ex7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

#Ex8

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
        if index == len(code):
            return True
    return False

#Ex9

import math

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius**3)
    return volume

#Ex10

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#Ex11

def is_palindrome(word):
    return word == word[::-1]

#Ex12

def histogram(numbers):
    for num in numbers:
        print('*' * num)

#Ex13

import random

def guess_the_number_game():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

#Ex14
