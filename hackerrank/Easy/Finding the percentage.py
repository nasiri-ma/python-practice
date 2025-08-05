#Problem: Finding the percentage
#Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


#Answer:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores = student_marks[query_name]
    average = sum(scores) / len(scores)
    print(f"{average:.2f}")
  
