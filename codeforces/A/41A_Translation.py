"""
Problem: Translation
Link: https://codeforces.com/problemset/problem/41/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
In this problem, we take two strings as input: the first word and the second word.  
Then we reverse the first string using slicing (`[::-1]`) and check if the reversed version is equal to the second string.  
If they are equal, it means the second word is exactly the reverse of the first, so we print "YES".  
Otherwise, we print "NO".
"""


#Answer:
first_word = input()
second_word = input()
if first_word[::-1] == second_word:
	print("YES")
else:
	print("NO")
