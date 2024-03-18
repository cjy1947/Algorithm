#최소 횟수 찾기
# G는 통과할 수 있음
#heapq 를 사용하는 이유 : priority를 기준으로 append됨 => loop만 신경쓰면 됨
from heapq import heappop, heappush

def solution(board) :
    #map 을 이중배열로 수정 -> 각 자리에 도달하기까지 최소 몇번의 움직임이 필요한지 직접 작성해줄 것
    board = [list(line) for line in board]
    #시작, 끝을 찾아줌
    init_row, init_col, end_row, end_col = 0,0,0,0
    #보드 크기 설정
    max_row, max_col = len(board), len(board[0])
    
    for r_idx in range(max_row):
        for c_idx in range(max_col):
            #시작점 찾기
            if board[r_idx][c_idx] == "R" :
                init_row, init_col = r_idx, c_idx
                board[r_idx][c_idx] = 0
            elif board[r_idx][c_idx] == "G" :
                end_row, end_col = r_idx, c_idx
                #아직은 최소가 몇번인지 모르기 때문에 가장 큰 수로 초기화 => heapq를 사용하기 때문에 무한의 수로 초기화 한 것
                board[r_idx][c_idx] = float("inf")
            elif board[r_idx][c_idx] == "." :
                board[r_idx][c_idx] = float("inf")
    
    #그 위치에 도달하기 위해 몇번을 움직여야하는지 저장
    queue = [(0,init_row, init_col)]
    while queue :
        curr_mov, curr_row, curr_col = heappop(queue)
        #방향을 나타내는 값
        for dir_row, dir_col in [(-1,0), (0,1),(1,0), (0,-1)] :
            #offset : 몇칸을 이동하였는가 (최소 이동 거리를 찾기 위함)
            offset, mov_result = 1, None
            #해당 방향으로 거리만큼 이동
            while True :
                mov_row, mov_col = curr_row + dir_row*offset, curr_col + dir_col*offset
                
                #장애물을 만난 경우 => D가 존재하는 한칸 전
                if mov_row in range(max_row) and mov_col in range(max_col) :
                    if board[mov_row][mov_col] =='D':
                        mov_result = (curr_mov+1, mov_row-dir_row, mov_col-dir_col)
                        break
                        
                #맨 끝에 부딪힐 때 => 벽이 있는 한칸 전
                else :
                    mov_result = (curr_mov+1, mov_row-dir_row, mov_col-dir_col)
                    break
                #미끄러지는 동안은 한번의 이동으로 간주
                offset += 1
        #G위치에 멈추는 경우
            if mov_result[1] == end_row and mov_result[2] == end_col :
                return mov_result[0]

            #G를 못찾아 다른 경로를 탐색해야 할 때, 움직인 경로가 가장 짧은 것으로 각 위치에 움직인 경로를 저장
            if mov_result[0]<board[mov_result[1]][mov_result[2]] :
                board[mov_result[1]][mov_result[2]] = mov_result[0]
                heappush(queue, mov_result)

    #G에 도달하지 못한 경우 -1 
    return -1
            
            