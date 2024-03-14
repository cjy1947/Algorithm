def solution(n, computers):
    def dfs(v) :
        visited[v] = True
        for next in range(n):
            if not visited[next] and computers[v][next] :
                dfs(next)
    count = 0
    visited = [False]*(n)
    
    #끊어진 관계 확인
    for node_ind in range(n):
        if not visited[node_ind] :
            dfs(node_ind)
            count += 1
    return count