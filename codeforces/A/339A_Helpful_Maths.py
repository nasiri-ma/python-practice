"""
Problem: Helpful Maths
Link: https://codeforces.com/problemset/problem/339/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we get an input and use the split method with the "+" operator to separate the numbers.  
Then, we use the sorted function to sort the numbers and convert them into a list.  
When printing the output, we use the join method to add the plus sign back between the numbers.
"""


#Method1:
x = input()
numbers_list = x.split("+")
numbers_list.sort()
print('+'.join(numbers_list))


#Method2:
numbers_list = sorted(list(input().split('+')))
print('+'.join(numbers_list))
