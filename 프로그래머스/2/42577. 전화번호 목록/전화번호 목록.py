def solution(phone_book):
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] =1
    
    for nums in phone_book:
        arr=""
        for n in nums :
            arr += n
            
            if arr in hash_map and arr != nums:
                return False
    return True