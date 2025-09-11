# main.py

import my_programs as mp

def menu():
    print("\n------ FUNCTION MENU ------")
    print("1. Armstrong Number")
    print("2. Swap Two Numbers")
    print("3. Count Vowels in String")
    print("4. GCD of Two Numbers")
    print("5. Reverse a Number")
    print("6. Sum of Digits")
    print("7. Count Words in Sentence")
    print("8. Convert String to Title Case")
    print("9. Palindrome Checker")
    print("10. Fibonacci Sequence")
    print("11. Factorial of a Number")
    print("12. Prime Number Checker")
    print("13. Find Maximum in List")
    print("14. Convert Decimal to Binary")
    print("15. Sort List in Descending Order")
    print("0. Exit")
    print("----------------------------")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        mp.armstrong_number()
    elif choice == "2":
        mp.swap_numbers()
    elif choice == "3":
        mp.count_vowels()
    elif choice == "4":
        mp.gcd_two_numbers()
    elif choice == "5":
        mp.reverse_number()
    elif choice == "6":
        mp.sum_of_digits()
    elif choice == "7":
        mp.count_words()
    elif choice == "8":
        mp.title_case()
    elif choice == "9":
        mp.palindrome_checker()
    elif choice == "10":
        mp.fibonacci_sequence()
    elif choice == "11":
        mp.factorial_number()
    elif choice == "12":
        mp.prime_checker()
    elif choice == "13":
        mp.max_in_list()
    elif choice == "14":
        mp.decimal_to_binary()
    elif choice == "15":
        mp.sort_descending()
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 0 and 15.")
1