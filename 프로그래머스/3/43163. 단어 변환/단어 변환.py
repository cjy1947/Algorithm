#가장 짧은 변환 과정
#일단 words 안에 target가 존재하는지 확인
from collections import deque

def solution(begin, target, words):
    if target in words :
        return bfs(begin, target, words)
    else :
        return 0
        
def bfs(begin, target, words) :
    queue = deque()
    #queue 초기화 : 단어-begin / step-0
    queue.append([begin,0])
    
    while queue :
        now, step = queue.popleft()
        if now == target :
            return step
        
        for w in words :
            count = 0
            for i in range(len(now)) :
                #일치하지 않는 알파벳이 나오면 step 증가, now = w가 되어 target과 동일할 때까지 bfs 진행
                if now[i] != w[i] :
                    count += 1
            if count == 1 :
                queue.append([w,step+1])
    