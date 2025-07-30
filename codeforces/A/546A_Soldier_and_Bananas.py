"""
Problem: Soldier and Bananas
Link: https://codeforces.com/problemset/problem/546/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
To calculate the cost of the bananas, we use a loop that goes through the range of the number of bananas to buy (starting the range at 1, so we add one to the total number of bananas).  
Each time a banana is added, its number is multiplied by its price.
"""


#Answer:
k, n, w = map(int, input().split())
total = 0
for i in range(1, w + 1):
	total += i * k
if n >= total:
	print(0)
else:
	print(total - n)
