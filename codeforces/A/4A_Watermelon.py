"""
Problem: Watermelon
Link: https://codeforces.com/problemset/problem/4/A
Difficulty: A
"""


#Method1:
w = int(input())
if w % 2 == 0 and w > 2:
	print("YES")
else:
	print("NO")

  
#Method2:
w = int(input())
print("YES" if w % 2 == 0 and w > 2 else "NO")
