def solution(priorities, location):

    queue = list(range(len(priorities)))
    cnt = 0
    while len(priorities):
        pri = max(priorities)
        temp1 = priorities.pop(0)
        temp2 = queue.pop(0)
        if pri != temp1:
            priorities.append(temp1)
            queue.append(temp2)
        else:
            cnt += 1
            if temp2 == location:
                answer = cnt
                break
    return answer