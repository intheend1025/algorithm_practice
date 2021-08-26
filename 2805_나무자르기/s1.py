import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))

    total = 0
    tree.sort()
    n = len(tree)
    i = 0
    total = 0
    cut = tree[n//2]

    if n % 2 == 1:
        m = n//2
    else:
        m = n//2 - 1

    print(sum(tree[n//2+1:n+1]) - cut * m)
    #
    while i < n:
        if sum(tree[n//2+1:n+1]) - cut * m < M:
            cut -= 1
        print()
        sum(tree[n//2+1:n])

        else:
            if total >= M:
                break
            else:
                cut -= 1
                total = 0
                i = 0

        i += 1


