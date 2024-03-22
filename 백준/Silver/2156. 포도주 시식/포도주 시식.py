#계단 오르기와 유사한 문제
#n번째까지 도달하는 경우
#    1) n-1, n, 최대(n-3)
#    2) n, 최대(n-2)
#    3) n을 마시지 않는 경우 => 최대(n-1)
#이중에서 최댓값을 추출

n = int(input()) #전체 와인잔의 개수
arr = [0]*10000 #와인의 양 arr 초기화
for i in range(n): #와인 양 저장
    arr[i] = int(input())
    
d=[0]*10000 #각 경우의 수 저장 arr 초기화
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[2]+arr[1], arr[2]+d[0], d[1]) #i-3음수 가능성으로 for문에서 제외
for i in range(3,n):
    d[i] = max(arr[i]+arr[i-1]+d[i-3], arr[i]+d[i-2], d[i-1])

print(max(d))