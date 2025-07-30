"""
Problem: Boy or Girl
Link: https://codeforces.com/problemset/problem/236/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
To remove the duplicate characters, we convert the data type to a set and divide its length by two.  
Based on whether the result is even or odd, we determine whether the user is female or male.
"""


#Method1:
name = input()
if len(set(name)) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")


#Method2:
user_name = set(input())
if len(user_name) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
