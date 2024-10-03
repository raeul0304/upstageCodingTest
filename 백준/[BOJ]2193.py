N = int(input())

# DP 테이블 초기화
dp = [[0] * 2 for _ in range(N + 1)]

# 초기 조건
dp[1][0] = 0  # 1자리 이친수는 0으로 끝날 수 없음
dp[1][1] = 1  # 1자리 이친수는 1밖에 없음

# 점화식에 따른 DP 테이블 채우기
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] 
    dp[i][1] = dp[i - 1][0] 

# N자리 이친수의 개수는 dp[N][0] + dp[N][1] 
print(dp[N][0] + dp[N][1])
