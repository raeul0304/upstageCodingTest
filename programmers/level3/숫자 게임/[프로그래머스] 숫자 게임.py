def solution(A, B):
    A.sort()
    B.sort()

    answer = 0
    a_cnt = 0

    for i in range(len(B)):
        if B[i] > A[a_cnt]:
            answer += 1
            a_cnt += 1
        
    return answer