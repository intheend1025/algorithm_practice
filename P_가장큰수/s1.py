import sys
sys.stdin = open('input.txt')

T = int(input())


def solution(numbers):
    max_num = 0
    answer = ''
    cnt = 0
    numbers2 = numbers[:]

    while len(numbers):
        for i in range(len(numbers)):
            a = str[numbers[i]]
            b = str(max_num)
            if int(a[0]) > int(b[0]):
                max_num = numbers[i]
                cnt = i
            elif a[0] == b[0]:
                if len(a) == len(b):
                    if numbers[i] > max_num:
                        max_num = numbers[i]

        answer += str(max_num)
        max_num = 0
        del numbers[cnt]

    return answer

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    print(solution(numbers))


