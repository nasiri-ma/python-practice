"""
Problem: Bit++
Link: https://codeforces.com/problemset/problem/282/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we get the number of commands, then we receive the commands through a loop.  
According to the type of command, we update the variable’s value, and finally print the variable.
"""


#Answer:
num = int(input())
x = 0
	for i in range(num):
		command = input()
		if "--" in command:
			x -= 1
		elif "++" in command:
			x += 1
print(x)
