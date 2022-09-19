import sys
input = sys.stdin.readline

n = int(input())
video = [list(input().strip()) for _ in range(n)]

# x: row, y: col, n: 분할 사분면
def divide_conq(x, y, n):   
    color = video[x][y]

    for row in range(x, x+n):
        for col in range(y, y+n):

            # video의 row, col 인덱스가 color와 같지 않다면 재귀함수 호출 
            if color != video[row][col]:

                k = n // 2
                
                # 처음 색상과 다른 결과가 시작될 때만 "(" 출력
                print("(", end='')
                divide_conq(x, y, k)
                divide_conq(x, y+k, k)
                divide_conq(x+k, y, k)
                divide_conq(x+k, y+k, k)
                print(")", end='')
                
                # 재귀 종료 
                return 0

    # color가 모두 같다면, 값을 출력
    print(color, end='')

divide_conq(0, 0, n)