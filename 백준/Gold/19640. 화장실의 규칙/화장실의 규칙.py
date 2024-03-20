########## 다시 공부 필요 #############

import sys, heapq
from collections import deque
input = sys.stdin.readline

#n : 직원수, m: 줄의 수, k:데카의 위치
n, m, k = map(int, input().split())
#줄 초기화
person = [deque([]) for _ in range(m)]
#직원 정보 입력
for i in range(n):
    #a:근무일, b:긴급도
    a, b = map(int, input().split())
    # - : 오름차순 정렬
    #데카인 경우 1
    #0부터 시작 -> 데카 위치 == k
    person[i % m].append((-a, -b, i % m, 1 if i == k else 0))
    
#카운트 초기화
cnt = 0
#각 줄의 대표자 확인을 위한 우선순위 큐 초기화
pq = []

#각 줄의 대표자를 우선순위 큐에 넣기
for i in range(m):
    if person[i]:
        heapq.heappush(pq, person[i][0])
       
#데카의 차례가 될 때까지 대표자 처리
while True:
    x = heapq.heappop(pq)
    person[x[2]].popleft()
    
    #데카인 경우 loop 중지
    if x[3]:
        break
    else:
        cnt += 1
        #아직 줄에 직원이 남아 있다면 새로운 큐에 넣기
        if person[x[2]]:
            heapq.heappush(pq, person[x[2]][0])
print(cnt)