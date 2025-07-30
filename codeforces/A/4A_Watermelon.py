"""
Problem: Watermelon
Link: https://codeforces.com/problemset/problem/4/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
To divide the watermelon into two even parts with at least one piece each, 
the weight must be even and greater than 2. Number 2 doesn't satisfy this.
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
