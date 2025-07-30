"""
Problem: String Task
Link: https://codeforces.com/problemset/problem/118/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we put the vowels inside a list.  
Then, we write a loop to compare each character of the input string with the vowels list,  
and if the character is not a vowel, we add it to a new variable.  
This way, we extract all the consonants from the input string.  

When printing the output, there will definitely be a dot at the beginning of the string, so we add it,  
and then use the join method to insert a dot between the elements of the string.
"""


#Method1:
s = input().lower()
wovels = ['a', 'e', 'i', 'o', 'u', 'y']
result = ""
for ch in s:
	if ch not in wovels:
		result += ch
print(f".{'.'.join(result)}")


#Method2:
s = input().lower()
wovels = ['a', 'e', 'i', 'o', 'u', 'y']
s = s.translate({ord(i): None for i in wovels})
print(f".{'.'.join(s)}")
