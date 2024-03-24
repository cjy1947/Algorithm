
###### (처음 아이디어) 효율성 테스트 실패 ######
# def solution(board, skill):
#     ctn = 0
#     for sk in skill:
#         miny, minx, maxy, maxx = sk[1], sk[2], sk[3], sk[4]
#         degree = sk[5]
        
#         if sk[0] == 1 :
#             for i in range(miny, maxy+1) :
#                 for j in range(minx, maxx+1):
#                     board[i][j] -= degree
        
#         elif sk[0] == 2 :
#             for i in range(miny, maxy+1) :
#                 for j in range(minx, maxx+1):
#                     board[i][j] += degree

#     for i in range(len(board)) :
#         for j in range(len(board[i])) :
#             if board[i][j] > 0 :
#                 ctn += 1
        
#     return ctn





###### 누진법 활용(공부필요) ######
# skill을 누진법용 배열에 담아 board 배열에 더하여 건물의 파괴 여부 판단

def solution(board, skill):  
    visited = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    
    for t, r1, c1, r2, c2, degree in skill:
        visited[r1][c1] += degree if t==2 else -degree
        visited[r1][c2+1] += degree if t==1 else -degree
        visited[r2+1][c1] += degree if t==1 else -degree
        visited[r2+1][c2+1] += degree if t==2 else -degree
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            visited[i+1][j] += visited[i][j]
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j+1] += visited[i][j]
    
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += visited[i][j]
            if board[i][j] > 0:
                answer += 1
            
    return answer
