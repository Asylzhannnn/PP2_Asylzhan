#exer 1


def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num  # Умножаем каждый элемент
    return result
nums = [2, 3, 4, 5]
print(multiply_list(nums))  # 120

#exer 2

def count_case_letters(text):
    upper_count = sum(1 for char in text if char.isupper())  #Counting uppercase letter
    lower_count = sum(1 for char in text if char.islower())  #Counting lowercase letter
    print(f": {upper_count}")
    print(f": {lower_count}")
text = input("Input your text: ")
count_case_letters(text)


#exer 3

def is_palindrome(text):
    length = len(text)
    
    for i in range(length // 2):  # Проверяем только первую половину
        if text[i] != text[length - i - 1]:  # Сравниваем с конца
            return False 
    return True  
sentence = input("Your text: ")
print(is_palindrome(sentence))


#exer 4

import math
import time

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)  # delay time
    result = math.sqrt(number)  # square root
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
number = int(input("Input number: "))
delay_ms = int(input("Delay in milliseconds: "))
delayed_square_root(number, delay_ms)


#exer 5

def all_elements_true(my_tuple):
    return all(my_tuple)  # Проверяет, все ли элементы истинные
print(all_elements_true((True, 1, "Hello", 5)))  # True
print(all_elements_true((True, 0, "Hello")))  # False
print(all_elements_true((False, False, False)))  #false
print(all_elements_true(()))  # true