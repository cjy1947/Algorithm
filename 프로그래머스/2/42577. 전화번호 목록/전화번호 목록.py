def solution(phone_book):
    hash_map = {}
    for nums in phone_book: #전화번호를 해시맵에 추가
        hash_map[nums] =1
    
    for nums in phone_book: 
        arr=""
        for n in nums : #번호의 각 숫자를 arr에 추가
            arr += n
            
            if arr in hash_map and arr != nums: #arr이 접두어이면 false반환
                return False
    return True
