"""
Problem: Beautiful Year
Link: https://codeforces.com/problemset/problem/271/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
After taking the year from the input, we add 1 to it.  
To check whether the digits of the year are unique, we use a loop.  
The set data type removes duplicate digits from the year,  
so we can implement it in a way that compares the length of the year as a string  
with the length of the year converted to a set.  
If the lengths are equal, it means all digits are unique.  
If they’re not equal, it means there were repeated digits, which were removed in the set,  
making its length smaller than the string’s length.
"""


#Answer:
input_year = int(input())
year = input_year + 1
	while True:
	s_year = str(year)
	if len(s_year) == len(set(s_year)):
		print(year)
		break
	else:
	year += 1
