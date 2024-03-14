#dp[n] : n번째 계단에 올랐을 때 얻을 수 있는 최대 점수

#n-1번째 에서 오는 경우
#dp[n] = dp[n-3] + stairs[n-1] + stairs[n]

#n-2에서 오는 경우
#dp[n]=stairs[n]+dp[n-2] #stair[n] : 자기 자신, dp[n-2] : 전전칸까지 왔을 때의 최댓값

import sys

input = sys.stdin.readline

n=int(input()) #n=6

stairs = [0]*301 #계단 개수 <= 300 #계단 정보 초기화
for i in range(1,n+1) : #계단 1층 = 1로 설정
    stairs[i] = int(input()) #계단의 점수 배열

dp=[0]*301 #dp초기화
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3]=max(stairs[1]+stairs[3], stairs[2]+stairs[3]) #연속 3계단 불가

#i까지 오는 것을 생각하면, 한 계단 전에서 오는 방법 / 두 계단 전에서 오는 방법이 존재
#이 중 최댓값을 고르기
for i in range(4, n+1):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i]) 
    
print(dp[n])


