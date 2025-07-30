"""
Problem: Way Too Long Words
Link: https://codeforces.com/problemset/problem/71/A
Difficulty: A
---------------------------------------------------------------------------
Solution Explanation:
First, a function handles long words. It checks the length of the word, takes the first and last characters using index 0 and -1, and places the number of characters in between them as a string.
In the first loop, we read all words from the input and pass each one to the abbreviation function, then store the result in a list.
In the second loop, we simply print each item of the list one by one as output.
"""


#Answer:
def abbreviate_long_words(word):
	if len(word) > 10:
		a = word[0] + str(len(word[1:-1])) + word[-1]
		return a
	else:
		return word
		
words_list = []
number_of_words = int(input())

for i in range(number_of_words):
	word = input()
	words_list.append(abbreviate_long_words(word))

for i in words_list:
	print(i)
