from itertools import combinations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    # 3개 숫자의 조합을 구함
    comb = combinations(nums, 3)
    
    for c in comb:
        if is_prime(sum(c)):
            count += 1
    
    return count