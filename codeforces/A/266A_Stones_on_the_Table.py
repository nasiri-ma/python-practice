"""
Problem: Stones on the Table
Link: https://codeforces.com/problemset/problem/266/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
We count on the stones based on the number received from input.  
Each time, we compare the stone at index i with the stone at index i+1.  
If both are equal, we increment the counter by one.  
Since indexing starts at zero, we subtract one from the total number of stones in the range function.
"""


#Answer:
num = int(input())
stones = input()
counter = 0
	for i in range (num - 1):
		if stones[i] == stones[i + 1]:
			counter += 1
print(counter)
