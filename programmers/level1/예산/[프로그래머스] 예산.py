def solution(d, budget):
    answer = 0
    d_sort = sorted(d)
    sum_d = 0
    for d in d_sort:
        sum_d += d
        if budget < sum_d:
            break
        answer += 1
    return answer