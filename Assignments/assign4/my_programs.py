# my_programs.py

def armstrong_number():
    print("Program: Armstrong Number")
    print(""" 
def is_armstrong(num):
    temp = num
    s = 0
    while temp > 0:
        digit = temp % 10
        s += digit ** len(str(num))
        temp //= 10
    return s == num
    """)
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: An Armstrong number equals the sum of its digits raised to the power of the number of digits.")

def swap_numbers():
    print("Program: Swap Two Numbers")
    print(""" 
def swap(a, b):
    a, b = b, a
    return a, b
    """)
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(5, -1) -> (-1, 5)")
    print("Explanation: This uses tuple unpacking to swap values without a temporary variable.")

def count_vowels():
    print("Program: Count Vowels in String")
    print(""" 
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
    """)
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('xyz') -> 0")
    print("Explanation: Iterates through the string and counts vowels using membership check.")

def gcd_two_numbers():
    print("Program: GCD of Two Numbers")
    print(""" 
import math
def gcd(a, b):
    return math.gcd(a, b)
    """)
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(100, 85) -> 5")
    print("Explanation: Uses Python's built-in gcd function to compute greatest common divisor.")

def reverse_number():
    print("Program: Reverse a Number")
    print(""" 
def reverse_num(n):
    return int(str(n)[::-1])
    """)
    print("Test Case 1: reverse_num(1234) -> 4321")
    print("Test Case 2: reverse_num(9870) -> 789")
    print("Explanation: Converts number to string, reverses it, and converts back to integer.")

def sum_of_digits():
    print("Program: Sum of Digits")
    print(""" 
def digit_sum(n):
    return sum(int(d) for d in str(n))
    """)
    print("Test Case 1: digit_sum(1234) -> 10")
    print("Test Case 2: digit_sum(999) -> 27")
    print("Explanation: Iterates over each digit, converts to int, and sums them up.")

def count_words():
    print("Program: Count Words in Sentence")
    print(""" 
def word_count(s):
    return len(s.split())
    """)
    print("Test Case 1: word_count('Hello World') -> 2")
    print("Test Case 2: word_count('Python is awesome') -> 3")
    print("Explanation: Uses string split() method to count words separated by spaces.")

def title_case():
    print("Program: Convert String to Title Case")
    print(""" 
def to_title_case(s):
    return s.title()
    """)
    print("Test Case 1: to_title_case('hello world') -> 'Hello World'")
    print("Test Case 2: to_title_case('python programming') -> 'Python Programming'")
    print("Explanation: Uses Python’s built-in title() method to capitalize each word.")

def palindrome_checker():
    print("Program: Palindrome Checker")
    print(""" 
def is_palindrome(s):
    return s == s[::-1]
    """)
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Checks if a string is equal to its reverse.")

def fibonacci_sequence():
    print("Program: Fibonacci Sequence")
    print(""" 
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
    """)
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]")
    print("Explanation: Generates sequence by summing last two elements iteratively.")

def factorial_number():
    print("Program: Factorial of a Number")
    print(""" 
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    """)
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Uses recursion: n! = n × (n-1)! with base case 0! = 1.")

def prime_checker():
    print("Program: Prime Number Checker")
    print(""" 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    """)
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(12) -> False")
    print("Explanation: Checks divisibility up to sqrt(n). If divisible, not prime.")

def max_in_list():
    print("Program: Find Maximum in List")
    print(""" 
def find_max(lst):
    return max(lst)
    """)
    print("Test Case 1: find_max([1, 5, 3]) -> 5")
    print("Test Case 2: find_max([-1, -9, -3]) -> -1")
    print("Explanation: Uses Python’s built-in max() to return largest element.")

def decimal_to_binary():
    print("Program: Convert Decimal to Binary")
    print(""" 
def dec_to_bin(n):
    return bin(n).replace("0b", "")
    """)
    print("Test Case 1: dec_to_bin(10) -> '1010'")
    print("Test Case 2: dec_to_bin(7) -> '111'")
    print("Explanation: Uses Python’s built-in bin() function and strips '0b' prefix.")

def sort_descending():
    print("Program: Sort List in Descending Order")
    print(""" 
def sort_desc(lst):
    return sorted(lst, reverse=True)
    """)
    print("Test Case 1: sort_desc([3, 1, 4]) -> [4, 3, 1]")
    print("Test Case 2: sort_desc([10, -2, 0]) -> [10, 0, -2]")
    print("Explanation: Uses sorted() with reverse=True to arrange values in descending order.")
