num = input("Enter a number: ")

sum_digits = sum(int(d) for d in num)
product_digits = 1
for d in num:
    product_digits *= int(d)

print("Spy Number" if sum_digits == product_digits else "Not a Spy Number")
