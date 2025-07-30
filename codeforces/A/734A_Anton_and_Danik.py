"""
Problem: Anton and Danik
Link: https://codeforces.com/problemset/problem/734/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we take the number of games from the input, and then a string that shows who won each game.  
We define two variables named `anton` and `danik` to store each player's score.  
We loop through the input string and check each character. If it's `A`, we increment Anton’s score by one;  
if it's `D`, we increment Danik’s score by one.  
At the end, we compare the scores. If one of them has a higher score, we print their name.  
If their scores are equal, it means the match ended in a tie and we print "Friendship".
"""


#Answer:
number_of_games = int(input())
results = input()
anton = 0
danik = 0
	for i in range(number_of_games):
		if results[i] == 'A':
			anton += 1
		elif results[i] == 'D':
			danik += 1
if anton > danik:
	print("Anton")
elif danik > anton:
	print("Danik")
else:
	print("Friendship")
