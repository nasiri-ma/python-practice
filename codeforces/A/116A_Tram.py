"""
Problem: Tram
Link: https://codeforces.com/problemset/problem/116/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we write a loop to take input for the number of passengers getting off and on at each station.  
Then we calculate how many passengers remain inside the tram after each station.  
We store the number of passengers after the first station in the variable that keeps track of the tram's maximum capacity.  
At every new station, we compare the current number of passengers with this variable to update it if needed,  
until we reach the last station.
"""


#Answer:
num_of_stations = int(input())
max = 0
total = 0
	for i in range(num_of_stations):
		x, y = map(int, input().split())
		total = (total - x) + y
		if max < total:
			max = total
print(max)
