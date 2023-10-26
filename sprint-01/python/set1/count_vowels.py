def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = sum(1 for char in string if char in vowels)
    return f"Number of vowels: {count}"

string = "Hello"
output = count_vowels(string)
print(output)
