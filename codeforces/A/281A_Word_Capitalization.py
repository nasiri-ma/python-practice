"""
Problem: Word Capitalization
Link: https://codeforces.com/problemset/problem/281/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
After getting the word from input, we separate the first character and convert it to uppercase, then store it in another variable.  
When printing the output, we combine it with the rest of the characters from the input word.
"""


#Method1:
word = input()
first_char = word[0].upper()
print(first_char + word[1:])


#Method2:
word = input()
word = word[0].upper() + word[1:]
print(word)
