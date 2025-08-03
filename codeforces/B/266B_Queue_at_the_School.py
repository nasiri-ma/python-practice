"""
Problem: Queue at the School
Link: https://codeforces.com/problemset/problem/266/B
Difficulty: B
---------------------------------------------------------------------------
Solution Explanation:
In this code, we first read `n` (number of kids in the queue) and `t` (number of seconds) from input.  
Then we store the initial queue as a list.  
For each second, we go through the queue from start to end.  
If we find a boy ('B') standing in front of a girl ('G'), we swap their positions.  
Since they just moved, we skip the next index to avoid re-checking them.  
Otherwise, we just move one step forward.  
At the end, we join the list into a string and print the final queue.
"""


#Method1:
n, t = map(int, input().split())
queue = input()
queue = list(queue)
for i in range(t):
    a = 0
    while a < n - 1:
        if queue[a] == 'B' and queue[a + 1] == 'G':
            queue[a], queue[a + 1] = queue[a + 1], queue[a]
            a += 2
        else:
            a += 1

final_queue = ""
for x in queue:
    final_queue += x

print(final_queue)


#Method2:
n, t = map(int, input().split())
queue = input()
queue = list(queue)
for i in range(t):
    a = 0
    while a < n - 1:
        if queue[a] == 'B' and queue[a + 1] == 'G':
            queue[a], queue[a + 1] = queue[a + 1], queue[a]
            a += 2
        else:
            a += 1

final_queue = "".join(queue)
print(final_queue)
