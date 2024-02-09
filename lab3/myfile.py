
from function1 import ounces, Fahrenheit, solution, filterprime
from function1 import stringpermutations, reverse_words, has_33, spy_game
from function1 import sphere_volume, remove_duplicates, is_palindrome, histogram
from function1 import guess_the_number_game

def main():
    grams_weight = 500
    ounces_weight = ounces(grams_weight)
    print(f"{grams_weight} grams is equal to {ounces_weight:.2f} ounces.")

    fahrenheit_temp = 98.6
    celsius_temp = Fahrenheit(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {celsius_temp:.2f} Celsius.")

    numheads = 35
    numlegs = 94
    solutionn = solution(numheads, numlegs)
    print(f"The number of chickens is {solutionn[0]} and the number of rabbits is {solutionn[1]}.")

    numbers = [2, 5, 8, 11, 15, 20]
    prime_numbers = filterprime(numbers)
    print(f"Prime numbers in the list are: {prime_numbers}")

    input_str = "abc"
    permutations = stringpermutations(input_str)
    print(f"Permutations of '{input_str}': {permutations}")

    sentence = "We are ready"
    reversed_sentence = reverse_words(sentence)
    print(f"Reversed words in '{sentence}': {reversed_sentence}")

    nums1 = [1, 3, 3]
    nums2 = [1, 3, 1, 3]
    nums3 = [3, 1, 3]
    print(has_33(nums1)) 
    print(has_33(nums2)) 
    print(has_33(nums3))  

    spy_sequence = [1, 2, 4, 0, 0, 7, 5]
    print(spy_game(spy_sequence)) 

    radius = 5
    volume = sphere_volume(radius)
    print(f"Volume of a sphere with radius {radius} is {volume:.2f} cubic units.")

    original_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = remove_duplicates(original_list)
    print(f"Original list: {original_list}, Unique list: {unique_list}")

    word = "madam"
    print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

    numbers_for_histogram = [4, 9, 7]
    histogram(numbers_for_histogram)

    guess_the_number_game()

if __name__ == "__main__":
    main()
