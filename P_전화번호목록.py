from collections import defaultdict

def solution3(phone_book):
    answer = True
    idx = 0

    while idx < len(phone_book):
        temp = phone_book.pop(0)
        length = len(temp)
        for i in phone_book:
            if i[:length] == temp:
                return False
        phone_book.append(temp)
        idx += 1

    return answer

def solution2(phone_book):
    answer = True
    length_list = list(map(len, phone_book))

    while len(phone_book):
        a = length_list.index(min(length_list))
        length_list.pop(a)
        temp = phone_book.pop(a)
        for i in phone_book:
            if i[:len(temp)] == temp:
                return False
    return answer


def solution4(phone_book):
    answer = True
    phone_book.sort()
    dict = defaultdict(list)
    idx = 1

    print(phone_book)
    for i in phone_book:
        dict[len(i)].append(i)
    print(dict)

    while len(dict):
        if idx in dict:
            temp = dict.pop(idx)
            for k in temp:
                print(k)
                for key, val in dict.items():
                    for l in val:
                        if l.startswith(k):
                            return False
        idx += 1
    return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        a = len(phone_book[i-1])
        if phone_book[i-1][:a] == phone_book[i][:a]:
            return False

    return answer

def solution6(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        a = len(phone_book[i-1])
        if phone_book[i-1][:a] == phone_book[i][:a]:
            return False

    return answer

def solution(phone_book):
    answer = True
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_book and temp != phone_number:
                return False
    return answer

def solution7(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer



print(solution(["12","123","1235","567","88"]))
print(solution(["119", "97674223", "1195524421"]))