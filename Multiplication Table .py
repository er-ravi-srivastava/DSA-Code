# Program to print the multiplication table of a number

# Input from user
num = int(input("Enter a number: "))

# Generate and print the multiplication table
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
