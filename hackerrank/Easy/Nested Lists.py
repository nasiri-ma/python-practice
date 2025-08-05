#Problem: Nested Lists
#Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


#Answer:
if __name__ == '__main__':
    
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    scores = []
    
    for student in students:
        scores.append(student[1])
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]
    
    result = []
    
    for student in students:
        if student[1] == second_lowest:
            result.append(student[0])
    
    result.sort()
    for name in result:
        print(name)
