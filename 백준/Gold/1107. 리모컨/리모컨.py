target = int(input())
n = int(input())
if n :
    broken = list(map(int, input().split()))
else :
    broken = set()
    
#target의 모든 숫자가 고장나서 리얼 ++ 또는 --으로 이동하는 경우
cnt = abs(100-target)

#직접 누르는 경우 => 최솟값 찾기
for num in range(1000001) :
    number = str(num)
    for N in number:
        #해당 숫자가 고장이라면 더이상 비교하지 않고 넘어감
        if int(N) in broken :
            break
    else :
        #번호를 눌러서 입력할 수 있는 경우
        #최솟값 : cnt VS 이동에 필요한 버튼을 누르는 횟수 + 이동 후 target까지 남은 거리
        cnt = min(cnt, len(str(num))+abs(num-target))
print(cnt)