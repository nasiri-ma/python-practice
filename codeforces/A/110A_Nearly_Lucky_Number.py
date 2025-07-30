"""
Problem: Nearly Lucky Number
Link: https://codeforces.com/problemset/problem/110/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
In this problem, we first take the input number as a list of characters. Then, we count how many times digits 4 and 7 appear and add them together.
If the total count is either 4 or 7, it means the number is “lucky” and we print “YES”; otherwise, we print “NO”.
"""


#Answer:
num = list(input())
x = int(num.count('4') + num.count('7'))
if x == 4 or x == 7:
	print("YES")
else:
	print("NO")
