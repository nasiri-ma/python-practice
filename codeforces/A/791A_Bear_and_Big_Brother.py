"""
Problem: Bear and Big Brother
Link: https://codeforces.com/problemset/problem/791/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
After getting the weights of the two bears, since it is guaranteed that Limak’s weight is less than or equal to Bob’s weight,  
we use a while loop to calculate the yearly growth of each.  
As long as Limak’s weight is less than or equal to his brother’s, the loop continues,  
and with each iteration, one year is added to the count of years needed for Limak’s weight to become greater than Bob’s.  
Finally, the number of years is printed.
"""


#Answer:
a, b = map(int, input().split())
years = 0
while a <= b:
	a *= 3
	b *= 2
	years += 1
print(years)
