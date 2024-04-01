#수빈이가 지금 보고 있는 채널은 100번이다.
#첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.
# 채널 0에서 -를 누른 경우에는 채널이 변하지 않고,

#abs() : 절댓값 함수
#수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)
#++으로 이동하는 경우 && --로 이동하는 경우 => 1,000,000 가지 경우의 수 생각
#모든 수를 확인하는 방법

target = int(input())
n = int(input())

#런타임에러 해결 ##############################
if n :
    broken = list(map(int, input().split()))
else :
    broken = set()
##############################
    
    
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