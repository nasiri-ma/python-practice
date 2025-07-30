"""
Problem: Elephant
Link: https://codeforces.com/problemset/problem/617/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
Greedy approach: At each step, we try to move the maximum possible distance to reach the destination faster.  
If we move less than five units in some steps, we might end up taking more steps overall.  

Divisibility logic by five: If x is divisible by five, meaning x is a multiple of five,  
the elephant can reach the destination in (x/5) steps of five units each.  
For example, if x is 10, the elephant can reach the destination in two steps of five units.  

If x is not divisible by five, meaning x has a remainder,  
the elephant can reach the destination by taking (x//5) steps of five units and 1 additional step.  
For example, if x is 12, the elephant can reach the destination by taking two steps of five units and one step of two units.
"""


#Answer:
x = int(input())
if x % 5 == 0:
	print(x // 5)
else:
	print(x // 5 + 1)
