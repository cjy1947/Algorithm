#갱신O

import sys

input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
minlist = temp
maxlist = temp

for _ in range(n-1):
    a,b,c = map(int, input().split())
    minlist = [a+min(minlist[0], minlist[1]), b+min(minlist), c+min(minlist[1], minlist[2])]
    maxlist = [a+max(maxlist[0], maxlist[1]), b+max(maxlist), c+max(maxlist[1], maxlist[2])]

print(max(maxlist),min(minlist))

