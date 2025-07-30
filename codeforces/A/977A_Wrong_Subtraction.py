"""
Problem: Wrong Subtraction
Link: https://codeforces.com/problemset/problem/977/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
We define a counter to track the number of operations, initially set to zero.  
In each iteration, we increment the counter by one and compare it with the number of operations input by the user.  
First, we check whether the number is divisible by 10, which lets us know if the last digit is zero.  
If this condition is true, we divide the number by ten; otherwise, we subtract one from the number.
"""


#Method1:
n, k = map(int, input().split())
counter = 0
while counter != k:
	if n % 10 == 0:
		n = n / 10
	else:
		n = n - 1
	counter += 1
print(int(n))


#Method2:
n, k = map(int, input().split())
for i in range(k):
	if n % 10 == 0:
		n /= 10
	else:
		n -= 1
print(int(n))
