"""
Problem: Theatre Square
Link: https://codeforces.com/contest/1/problem/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
To solve this, we divide the length and width of the rectangle by the length and width of the paving stones and take the ceiling of the result.  
If the length and width of the rectangle are multiples of the stone dimensions, this step is not necessary. But if not, to cover the entire rectangular area, we need to extend beyond the field's borders.
"""


#Method1:
n, m, a = map(int, input().split())
stones_in_length = (n + a - 1) // a
stones_in_width = (m + a - 1) // a
total_stones = stones_in_length * stones_in_width
print(total_stones)


#Method2:
import math
n, m, a = map(int, input().split())
l_stones = math.ceil(n / a)
w_stones = math.ceil(m / a)
total_stones = l_stones * w_stones
print(total_stones)
