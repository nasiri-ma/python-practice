"""
Problem: Vanya and Fence
Link: https://codeforces.com/problemset/problem/677/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we take the number of friends and the maximum allowed height as input.
Then, we get a list containing the heights of all friends.
We use a loop to go through this list and check each friend's height.
If a friend is taller than the allowed height, it means they need to bend, so we count 2 units of width.
If the height is less than or equal to the allowed limit, only 1 unit of width is needed.
Finally, we print the total width required.
"""


#Answer:
n, h = map(int, input().split())
friends = list(map(int, input().split()))
width = 0
for i in friends:
	if i > h:
		width += 2
	else:
		width += 1
print(width)
