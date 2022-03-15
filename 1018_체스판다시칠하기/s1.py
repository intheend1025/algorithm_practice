import sys
sys.stdin = open('input.txt')

T = int(input())


def switch(temp):
    if temp == 'W':
        return 'B'
    else:
        return 'W'


for tc in range(1, T+1):
    N, M = map(int, input().split())  # M * N
    board = [list(input()) for _ in range(N)]
    answer = 64
    stack = ['W', 'B']

    for i in range(N):
        for j in range(M):
            if i+8 <= N and j+8 <= M:
                for tri in range(2):
                    result = 0
                    temp = stack[tri]
                    for n in range(i, i+8):
                        temp = switch(temp)
                        for m in range(j, j+8):
                            if temp != board[n][m]:
                                result += 1
                            temp = switch(temp)
                    if answer > result:
                        answer = result

    print(answer)
