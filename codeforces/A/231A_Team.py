"""
Problem: Team
Link: https://codeforces.com/problemset/problem/231/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
In a loop, we receive the opinions of the team members for `num` problems.  
We use the `map` function to convert each opinion to an integer and unpack them into the defined variables.  
The opinions work like this: if a team member is confident about the solution, they input 1; otherwise, they input 0.  
So by summing up the values, we can decide whether the team is ready to solve the problem.  
Each time the team is ready, we increase the counter by one.
"""


#Answer:
num = int(input())
counter = 0
for i in range(num):
    x, y, z = map(int, input().split())
    result = x + y + z
    if result >= 2:
        counter += 1
print(counter)
