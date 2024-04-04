#이분탐색
# # // : 정수형 나눗셈
# from sys import stdin
# n, m = map(int, stdin.readline.spilt())
# time = [int(stdin.readline) for _ in range(n)]

# #최소 심사 시간 : a, 최대 시간 b
# a, b = min(time), max(time)*m
# ans = b

# while a <= b :
#     total = 0
#     mid = (a+b)//2 #이분탐색

#     for i in range(n) :
#         #몇명을 검사할 수 있는지 계산하여 total에 저장
#         total += mid//time[i]
        
#     #모든 인원 검사완료 || 검사 가능 인원이 정원을 초과한 경우    
#     if total >= m :
#         b = mid -1
#         ans = min(mid,ans)
#     #기준 시간 갱신    
#     else :
#         a = mid +1

# print(ans)

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(n)]

l, r = min(arr), max(arr) * m
ans = r

while l <= r:
    total = 0
    mid = (l + r) // 2

    for i in range(n):
        total += mid // arr[i]

    if total >= m:
        r = mid -1
        ans = min(mid, ans)

    else:
        l = mid + 1

print(ans)