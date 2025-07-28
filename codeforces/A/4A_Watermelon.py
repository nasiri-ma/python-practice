"""
Problem: Watermelon
Link: https://codeforces.com/problemset/problem/4/A
Difficulty: A
"""


#Answer:
w = int(input())
if w % 2 == 0 and w > 2:
	print("YES")
else:
	print("NO")

  
#Answer:
w = int(input())
print("YES" if w % 2 == 0 and w > 2 else "NO")
