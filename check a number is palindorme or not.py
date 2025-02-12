# Function to check if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Input from user
num = int(input("Enter a number: "))

# Check and print result
if is_palindrome(num):
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")
