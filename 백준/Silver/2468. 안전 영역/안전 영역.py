import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n= int(input())
graph = [list(map(int, input().split()))for _ in range(n)] #주어진 땅의 높이 정보 저장
dx = (1,-1,0,0) #x좌표 초기화
dy = (0,0,1,-1) #y좌표 최기화
cnt = 0 #잠기지 않은 땅의 개수 초기화

def dfs(x,y,h) :
    visited[x][y] = True #방문한 지점 표시
    
    #주변 탐색
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        
        #물의 높이보다 높지만 아직 방문하지 않은 경우 탐색
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] >h and not visited[nx][ny]:
            dfs(nx, ny, h)
    
#모든 물의 높이에 대해 확인
for h in range(101) :
    cnt2 = 0
    visited=[[False for _ in range(n)]for _ in range(n)]
    for i in range(n) :
        for j in range(n):
            if graph[i][j] >h and not visited[i][j] :
                dfs(i,j,h)
                cnt2 +=1
    cnt = max(cnt,cnt2) #그 비의 양에서 최대로 나올 수 있는 영역의 개수 업데이트
    
print(cnt)
        