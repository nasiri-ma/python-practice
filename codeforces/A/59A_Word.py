"""
Problem: Word
Link: https://codeforces.com/problemset/problem/59/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we store lowercase and uppercase letters inside variables as sets.  
Then, we loop through the input word and each time check which group the character belongs to (uppercase or lowercase),  
and based on that, increment the corresponding counter.  
In the second method, we can use the string library so we don’t have to write all uppercase and lowercase English letters manually; they are provided for us.  
(Note: It doesn’t compare ASCII codes; it just means that only alphabet characters are included, without any other characters.)
"""


#Method1:
word = input()

lowercase_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
					'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
					's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
a = str(lowercase_letters)
capital_letters = set(a.upper())
l_counter = 0
c_counter = 0
for i in word:
	if i in lowercase_letters:
		l_counter += 1
	else:
		c_counter += 1
if l_counter >= c_counter:
	print(word.lower())
else:
	print(word.upper())


#Method2:
from string import ascii_lowercase, ascii_uppercase
s = input()
upper, lower = 0, 0
for ch in s:
	if ch in ascii_lowercase:
		lower += 1
	elif ch in ascii_uppercase:
		upper += 1
if upper > lower:
	print(s.upper())
else:
	print(s.lower())
