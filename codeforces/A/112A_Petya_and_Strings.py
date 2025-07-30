"""
Problem: Petya and Strings
Link: https://codeforces.com/problemset/problem/112/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we get two strings from input and convert both of them to lowercase so that the comparison becomes case-insensitive.  
Then, using comparison operators, we check whether the first string is smaller than the second one or vice versa.  
If the first string is smaller, we print -1. If it's greater, we print 1. And if they are equal, we print 0.
"""


#Answer:
str1 = input().lower()
str2 = input().lower()
if str1 < str2:
	print("-1")
elif str2 < str1:
	print("1")
else:
	print("0")
