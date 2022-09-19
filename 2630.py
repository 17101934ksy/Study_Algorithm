import sys
input = sys.stdin.readline

N = int(input())

# 입력받는 색종이 색상을 리스트에 저장
paper = [list(map(int, input().split())) for _ in range(N)]
answers = [0, 0]

# 재귀함수 설정(row: 행, col: 열, N: 인덱스 시작 포인트)
def divide_conq(row, col, N):
    
    # 처음 시작하는 색상을 비교 대상으로 설정 
    color = paper[row][col]

    for r in range(row, row+N):
        for c in range(col, col+N):
            
            # 처음 색상과 다른 색상 체크 
            if color != paper[r][c]:

                n = N // 2

                # 분할 재귀 함수 적용 
                divide_conq(row, col, n)
                divide_conq(row, col+n, n)
                divide_conq(row+n, col, n)
                divide_conq(row+n, col+n, n)

                # 함수를 끝내기 위한 return
                return 0

    # color가 동일하다    
    if color == 0:
        answers[0] += 1
    else:
        answers[1] += 1

# 재귀 시작 
divide_conq(0, 0, N)

for answer in answers:
    print(answer)                           