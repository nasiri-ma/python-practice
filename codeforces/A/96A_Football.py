"""
Problem: Football
Link: https://codeforces.com/problemset/problem/96/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
We define a counter and set its initial value to 1 because it doesn’t matter which team the player is from — for now, we have one player at the start.  
The reason we start from 1 is that we want to compare each player with the one before them, so there needs to be a previous player.  
In the first iteration, `i` is equal to 1 and is compared with `i - 1`, meaning the first and second players.  
If they are the same, we increment the counter by one; otherwise, we reset the counter back to 1.
"""


#Answer:
players = input()
counter = 1
for i in range(1, len(players)):
	if players[i] == players[i - 1]:
		counter += 1
	else:
		counter = 1
if counter >= 7:
	print("YES")
exit()
	print("NO")
