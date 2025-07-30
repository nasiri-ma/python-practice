"""
Problem: Next Round
Link: https://codeforces.com/contest/158/problem/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, we get the number of participants and the value of k, and then the scores of the participants.  
To get the score of the k-th participant, we subtract one from its index.  
We iterate through the list of scores, and each time a score is equal to or greater than the k-th score and greater than zero, we increase the counter by one.
"""


#Answer:
n, k = map(int, input().split())
scores = list(map(int, input().split()))
kth_score = scores[k - 1]
counter = 0
for i in scores:
	if i >= kth_score and i > 0:
	counter += 1
print(counter)
