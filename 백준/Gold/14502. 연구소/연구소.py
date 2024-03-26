#런타임 에러로 pypy3로 제출

from collections import deque
import copy
import sys
input = sys.stdin.readline


#감염을 위한 방향
d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    #감염된 구역 저장
    #이진배열 저장을 위해 deepcopy사용
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue:
        r,c = queue.popleft()

        #주변 감염 시작
        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]
            
            #새로운 감염 지역 저장
            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] =2
                    queue.append((dr,dc))

    global result
    count = 0
    
    #감염 안된 구역 count
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)

#벽 세우기
def make_wall(count):
    #3개가 다 세워졌다면 bfs 시행
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                #재귀 탐색
                make_wall(count+1)
                #벽 초기화
                #다시 벽을 세우는 과정에서 그 자리에 벽을 세울 수 있으니 초기화
                lab_map[i][k] = 0

                
                
n, m = map(int,input().split())
#연구소 상황 저장
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
make_wall(0)

print(result)