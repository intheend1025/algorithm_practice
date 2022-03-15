
# 내 풀이
def solution(id_list, report, k):
    newreport = list(set(report))

    answer = [0] * len(id_list)

    if len(newreport) < k:
        return answer
    else:
        ban_list = [[] for i in range(len(id_list))]
        for i in newreport:
            i_list = i.split()
            a = id_list.index(i_list[0])
            b = id_list.index(i_list[1])
            ban_list[b].append(a)

    for n in ban_list:
        if len(n) >= k:
            for j in n:
                answer[j] += 1

    return answer


# 다른사람풀이 중 dictionary 생성방법이 인상깊음 이렇게 만들수있었나? 너무 까먹었나;
#     reports = {x : 0 for x in id_list}
