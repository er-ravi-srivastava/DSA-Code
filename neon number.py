num = int(input("Enter a number: "))
square = num * num
sum_digits = sum(int(digit) for digit in str(square))

print("Neon Number" if sum_digits == num else "Not a Neon Number")
