import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
count = [0] * 10001  # 수의 범위가 1부터 10,000까지이므로 크기 10001의 리스트 사용

# 입력 받은 N개 만큼 반복, 입력받은 숫자를 인덱스로 값을 추가시킴 count[3]=10 -> 3이 10번 입력받은 것
for _ in range(N):
    number = int(sys.stdin.readline().strip())
    count[number] += 1 #

# 출력 조건에 따라 1,10001에서 i(입력받은 숫자)값을 돌게 된다. 입력 받지 않았을 경우에 0보다 큰 조건을 명시
for i in range(1, 10001):
    if count[i] > 0:
        sys.stdout.write((str(i) + '\n') * count[i])
