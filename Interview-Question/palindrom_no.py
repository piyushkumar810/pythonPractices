def palindrome(str):
    original_str = str
    reversed_str = ""
    
    # Reversing the string manually without built-in functions
    n = len(str)
    for i in range(n-1, -1, -1):  # Fix: Stop value is -1 to include index 0
        reversed_str += str[i]

    print("Reversed String:", reversed_str)
    
    # Check if the string is a palindrome
    if original_str == reversed_str:
        print(f"Yes, '{original_str}' is a palindrome.")
    else:
        print(f"No, '{original_str}' is not a palindrome.")

# Input from the user
str = input("Enter the string you want to check = ")
palindrome(str)
