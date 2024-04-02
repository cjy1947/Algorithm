#최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함
# 사전 순으로 오름차순 정렬해서 return 해주세요.

# 가능한 모든 조합 확인 -> 2명 이상 주문 확인
# 조합 중에서 가장 많이 나온 조합 -> course의 개수마다 저장
# 사전 오름차순으로 정렬 (sort)

#product('abc', repeat=2) = aa,ab,ac,ba,bb,bc,ca,cb,cc => 2^n개
#combinations('abc', 2) =ab,ac,bc => 3C2개
### append VS extend ###
#append : 자료형 그대로 추가
#extend : 항목들을 추가 (ex. list형의 항목만 추가하는 경우 []가 통째로 들어가는 것 X []안의 항목만 들어감)


from itertools import combinations
def solution(orders, course):
    answer = []
    
    for course_cnt in course :
        order_comb =[]
        comb_cnt = {}
        order_max = []
        
        #가능한 모든 조합 찾기
        for order in orders :
            order_comb = combinations(list(order), course_cnt)
            #사전순으로 정렬
            for order in order_comb :
                order_str = "".join(sorted(order))
                
                #조합의 개수 count
                if comb_cnt.get(order_str) :
                    comb_cnt[order_str] += 1
                else : 
                    comb_cnt[order_str] =1
                    
        #2명 이상 주문 && max 주문 확인
        order_max = [k for k,v in comb_cnt.items() if ((v==max(comb_cnt.values()) and v >= 2)) ]
        
        
        answer.extend(order_max)
        #사전순으로 정렬
        answer = sorted(answer)
    return answer