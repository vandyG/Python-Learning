# Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.
# For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0

for i in s:
    if i in vowels:
        num_vowels += 1

print(num_vowels)

