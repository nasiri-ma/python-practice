#Problem: Write a Function
#Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true


#Answer:
def is_leap(year):
    leap = False
 
    if year % 4 == 0:
        if year % 100 == 0:
            leap = True if year % 400 == 0 else False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))
