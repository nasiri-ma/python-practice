"""
Problem: Beautiful Matrix
Link: https://codeforces.com/problemset/problem/263/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we define an empty list which represents our matrix, and it will contain 5 lists, each one representing a row — making 5 rows in total.  
We use a nested loop where for each iteration of the outer loop, the inner loop runs five times.  
This allows us to check every row and column to find the number one.  
The index `i` represents the row, and `j` represents the column.  
Whenever the value at those indices is equal to one, we store those indices.
To center the matrix visually, we need to move the number one to the center cell, which is in the third row and third column — but since indexing starts from zero, that’s index 2.  
We subtract 2 from both the row and column indices of the number one, take the absolute value, and add them together to get the minimum number of moves required.
"""


#Answer:
matrix = []
for i in range(5):
	row = list(map(int, input().split()))
	matrix.append(row)
for i in range(5):
	for j in range(5):
		if matrix[i][j] == 1:
			one_row = i
			one_col = j
result = abs(one_row - 2) + abs(one_col - 2)
print(result)
