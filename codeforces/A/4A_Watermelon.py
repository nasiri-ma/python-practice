"""
Problem: Watermelon
Link: https://codeforces.com/problemset/problem/4/A
Difficulty: A
"""


#Method1:
w = int(input())
if w % 2 == 0 and w > 2:
	print("YES")
else:
	print("NO")

  
#Method2:
w = int(input())
print("YES" if w % 2 == 0 and w > 2 else "NO")


"""
Solution Explanation:
To divide the watermelon into two even parts with at least one piece each, 
the weight must be even and greater than 2. Number 2 doesn't satisfy this.

برای اینکه هندوانه بین دو نفر تقسیم بشه و هر کدوم حداقل یک قسمت زوج رو بگیرن باید وزن هندوانه زوج و بزرگتر از 2 باشه چون وزن 2 امکان تقسیم شدن به دو قسمت زوج رو نداره
"""
