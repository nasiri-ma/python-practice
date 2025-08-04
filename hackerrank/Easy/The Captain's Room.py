#Problem: The Captain's Room
#Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true


#Answer:
if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    unique_rooms = set(rooms)
    sum_unique_rooms = sum(unique_rooms)
    sum_all_rooms = sum(rooms)
    
    captain_room = (k * sum_unique_rooms - sum_all_rooms) // (k - 1)
    
    print(captain_room)
