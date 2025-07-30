"""
Problem: Domino Piling
Link: https://codeforces.com/problemset/problem/50/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we get the length and width of the rectangular area.  
We should note that each domino covers two squares, so we calculate the maximum number of dominoes that can be placed on the board using the following formula:  
`(m * n) / 2`  
If the area is an odd number, we take the floor of the result.
"""


#Method1:
m, n = map(int, input().split())
max_dominoes = (m * n) // 2
print(max_dominoes)


#Method2:
import math
m, n = map(int, input().split())
max_dominoes = math.floor(m * n) / 2
print(int(max_dominoes))
