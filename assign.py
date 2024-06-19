
# Q1: Write a program that takes two numbers as input and prints their sum.
# Ans:

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

# Q2: Write a python program that checks whether a given number is even or odd
#Ans: 

num = int(input("Enter a number: "))

if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))    

# Q3: Write a python program that calculates the factorial of a given number.
# Ans:
def factorial(n):
    if n < 0:
      return "Factorial is not defined for negative number"
    elif n == 0 or n == 1:
      return 1
    else:
        result = 1 
        for i in range (2, n+1):
             result *= i
        return result 
num = int(input("Enter a number to calculate its factorial: "))
fact = factorial(num)
print(factorial(num))
 
    
# Q4: Write a program that asks the user for their name and then prints a greeting message.
#Ans:
user_name = input("Enter your name")
print(f"Hello, {user_name}! Welcome!")

# Q5: Write a program that takes a string input from the user and writes it to a text file.
#Ans:
user_input = input("Enter some text:")
with open('user_input.txt','w') as file:
    file.write(user_input)
print("your input has written to 'user_input.txt'.")

# Q6: Write a program that reads the content of a text file and prints it to the console.
#Ans:
with open('user_input.txt', 'r') as file:
   content = file.read()
print(content)

# Q7: Write a python program that takes a string as input and returns its length.
#Ans:
user_string = input("Please enter a string: ")
length = len(user_string)
print(f"The length of the input string is: {length}")

# Q8: Write a python program that concatenates two strings and returns the result.
#Ans:
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
result = first_string + second_string
print(f"The concatenated string is: {result} ")

# Q9: Write a python program that checks if a substring is present in a given string.
#Ans:
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
if substring in main_string:
    print(f"The substring '{substring}'is present in the main string.")
    print(f"The substring '{substring}' is not present in the main string.")
print(result)

# Q10: Write a python program that converts a given string to uppercase.
#Ans:
input_string = input("Enter the string to convert to uppercase: ")
uppercase_string = input_string.upper()
print(f"The string in uppercase is: {uppercase_string}")

# Q11: Write a python program that generates the first n numbers in the Fibonacci sequence.
#Ans:
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence
n = int(input("Enter the value of 'n': "))
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")

# Q12: Write a python program that calculates the sum of the digits of a given number.
#Ans:
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total
user_number = int(input("Enter a positive integer: "))
result = sum_of_digits(user_number)
print(f"The sum of the digits in {user_number} is: {result}")

# Q13: Write a program that asks the user for their birth year and calculates their age.
#Ans:
birth_year = int(input("Enter your birth year: "))
import datetime
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are approximately {age} years old.")

# Q14: Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
#Ans:
def read_lines():
    print("Enter multiple lines of text (enter an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines
def main():
    lines = read_lines()
    print("\nYou entered:")
    for line in lines:
        print(line)
if __name__ == "__main__":
    main()

# Q15: Write a program that reads data from a CSV file and prints it to the console.
#Ans:
import csv
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(", ".join(row))  # Print each row as a comma-separated string
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Q16: Write a program in python that counts the frequency of each character in a string.
#Ans:
def count_characters(input_string):
    char_count = {}  
    for char in input_string:
        if char.isalpha():  
            char_count[char] = char_count.get(char, 0) + 1
    return char_count
user_input = input("Enter a string: ")
result = count_characters(user_input)
for char, count in result.items():
    print(f"'{char}' occurs {count} times")

# Q17:  Write a program in python that converts a given string to title case (first letter of each word capitalized).
#Ans:
def convert_to_title_case(input_string):
    return input_string.title()
user_input = input("Enter a string: ")
title_case_string = convert_to_title_case(user_input)
print(f"The string in title case is: {title_case_string}")


# Q18: Write a python program that checks if two strings are anagrams of each other.
#Ans:
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Q19: Write a python program that removes all punctuation from a given string.
# Ans:    
import string
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string
user_input = input("Enter a string: ")
result = remove_punctuation(user_input)
print(f"The string without punctuation is: {result}")

# Q20: Write a python program that takes a list of numbers and returns their sum.
#Ans:
def calculate_sum(numbers):
    return sum(numbers)
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in user_input.split()]
total_sum = calculate_sum(numbers_list)
print(f"The sum of the numbers is: {total_sum}")

# Q21: Write a python program that counts the occurrences of a specific element in a list.
#Ans:
def count_occurrences(lst, target):
    return lst.count(target)
result = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {result} times in the list.")

# Q22: Write a python program that returns the minimum and maximum values in a list of numbers.
#Ans: 
def find_min_max(numbers):
    if not numbers:
        return None, None  
    min_value = float('inf')
    max_value = float('-inf')
    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    return min_value, max_value
min_value, max_value = find_min_max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Q23: Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
#Ans:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
if choice.upper() == 'C':
    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp:.2f}°C is equivalent to {fahrenheit_temp:.2f}°F.")
elif choice.upper() == 'F':
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp:.2f}°F is equivalent to {celsius_temp:.2f}°C.")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")

# Q24: Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
#Ans:
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
result = calculate(num1, num2, operator)
print(f"Result: {result}")

# Q25: Write a program that copies the contents of one text file to another.
#Ans:
def copy_file(source_file, target_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        with open(target_file, 'w') as target:
            target.write(content)
        print(f"Contents copied from '{source_file}' to '{target_file}'.")
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
source_path = input("Enter the path of the source file: ")
target_path = input("Enter the path of the target file: ")
copy_file(source_path, target_path)

# Q26: Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
#Ans:
def check_prefix_suffix(string, prefix, suffix):
    return string.startswith(prefix) or string.endswith(suffix)
result = check_prefix_suffix(input_string, input_prefix, input_suffix)
print(f"Result: {result}")

# Q27: Write a program in python that converts a string into a list of its characters.
#Ans:
def string_to_list(input_string):
    return list(input_string)
input_string = "Hello, world!"
result_list = string_to_list(input_string)
print(result_list)




















