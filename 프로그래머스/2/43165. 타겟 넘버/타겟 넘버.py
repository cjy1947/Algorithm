ctn = 0

def dfs(numbers, target, temp, ind):
    global ctn
    if ind == len(numbers):
        if temp == target :
            ctn += 1
        return
    
    dfs(numbers, target, temp+numbers[ind], ind+1)
    dfs(numbers, target, temp-numbers[ind], ind+1)
    
def solution(numbers, target):
    dfs(numbers, target, 0,0)
    return ctn