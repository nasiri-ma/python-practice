"""
Problem: Young Physicist
Link: https://codeforces.com/problemset/problem/69/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we define three variables to store the sum of each component every time a new force is entered.  
Then, we create a loop to read the vectors from input, and in each iteration, we add each component to its corresponding variable.
"""


#Answer:
n = int(input())
x_s = 0
y_s = 0
z_s = 0
	for i in range(n):
		x, y, z = map(int, input().split())
		x_s += x
		y_s += y
		z_s += z
if x_s == 0 and y_s == 0 and z_s == 0:
	print("YES")
else:
	print("NO")
