import sys
sys.stdin = open('input.txt')

T = int(input())


def binary_search(a, b):
    global answer
    while a <= b:
        total = 0
        c = (a + b) // 2
        for i in range(N):
            if tree[i] > c:
                total += (tree[i] - c)
            if total > M:
                break

        # if total == M:
        #     answer = c
        #     return
        if total < M:
            b = c-1
        else:
            a = c+1
    answer = b
    return


for tc in range(1, T+1):
    N, M = map(int, input().split())  # 나무수 N, 필요한 나무길이 M
    tree = list(map(int, input().split()))
    answer = 0

    a = max(tree)-M
    b = max(tree)
    binary_search(a, b)
    print(answer)

