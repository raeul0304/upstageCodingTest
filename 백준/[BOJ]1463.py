# 동적 계획법으로 다시 작성
X = int(input())

# DP 테이블 초기화 (0부터 X까지 계산할 것이므로 X+1 크기)
dp = [0] * (X + 1)

for i in range(2, X + 1):
    # 1을 빼는 연산
    dp[i] = dp[i - 1] + 1

    # 2로 나눌 수 있을 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나눌 수 있을 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])



""" => 런타임 에러
X = int(input())
tmp = []

def make_1(x):
    if x == 1:
        return 0  
    
    cnt = 1 + make_1(x - 1)
    
    if x % 2 == 0:
        cnt = min(cnt, 1 + make_1(x // 2))
    
    if x % 3 == 0:
        cnt = min(cnt, 1 + make_1(x // 3))
    
    return cnt

print(f'{make_1(X)}')
"""
