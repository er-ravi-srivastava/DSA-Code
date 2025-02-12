word = input("Enter a word: ").lower()
vowels = "aeiou"

count = sum(1 for letter in word if letter in vowels)

print("Number of vowels:", count)
