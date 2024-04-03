#수신 받지 못하면 => 0
#수신 받았을 경우 => 1
#높이 비교 => 현재보다 작으면 0 / 현재보다 높으면 || 동일하면 1

#stack : LIFO => (인덱스, 높이)튜플
#* : 반복 가능 항목(ex. list, tuple)을 개별 인수로 압축 해제


n = int(input())
tops = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(len(tops)) :
    
    while stack :
        if tops[stack[-1][0]]<tops[i]:
            stack.pop()
        else :
            ans[i] = stack[-1][0]+1
            break
    stack.append((i, tops[i]))

#ans의 항목만 print 해야 함 => *활용
print(*ans)