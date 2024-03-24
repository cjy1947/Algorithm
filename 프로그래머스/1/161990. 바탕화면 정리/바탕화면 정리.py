# #인 경우의 좌표를 추출
#그들 중 max, min 좌표 확인
#y작x작y큰x큰 순으로 return

#x는 0부터 시작
#y는 1부터 시작


def solution(wallpaper):
    x, y = [], []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                y.append(i) 
                x.append(j)
                
    return [min(y), min(x), max(y)+1, max(x)+1]