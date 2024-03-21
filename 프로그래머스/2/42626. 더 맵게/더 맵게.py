#heapq로 오름차순 정렬되도록 스코빌지수를 저장 => .heapify : 이미 배열을 heap으로 변경
#맨 앞에 것 선택
#heappop으로 앞에서부터 제거
#그 후의 맨 앞에 것 선택(즉, 두번째 것)
#더하기
#더한 값 다시 배열에 추가 : heappush
#맨 앞의 값 >= k 확인
#아닐 경우 ctn +=1 으로 카운트 
#반복
#while로 계속 반복 => 만족하면 break

import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer = 0
    
    while True :
        first = heapq.heappop(scoville)
        if first >= K :
            return answer
        second = heapq.heappop(scoville)
        mix = first+(second*2)
        heapq.heappush(scoville, mix)
        answer +=1 
        if len(scoville) == 1 and scoville[0] < K :
            return -1
            

