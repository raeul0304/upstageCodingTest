def solution(grid):
    answer = []
    
    # 방향 벡터(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(grid)        # 행 길이
    m = len(grid[0])     # 열 길이
    
    # 방문 여부를 기록하는 3차원 리스트(총 4번 방문을 담을 수 있다.)
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    
    # S일 때를 제외하고 L, R에 대해서 방향을 바꾸어 이동을 도와준다.
    def move(x, y, d):
        if grid[x][y] == 'L':
            # L이 나왔을 때 좌회전
            if d == 0:  # 상 -> 좌
                d = 2
            elif d == 1:  # 하 -> 우
                d = 3
            elif d == 2:  # 좌 -> 하
                d = 1
            elif d == 3:  # 우 -> 상
                d = 0
        elif grid[x][y] == 'R':
            # R이 나왔을 때 우회전
            if d == 0:  # 상 -> 우
                d = 3
            elif d == 1:  # 하 -> 좌
                d = 2
            elif d == 2:  # 좌 -> 상
                d = 0
            elif d == 3:  # 우 -> 하
                d = 1
        
        # 다음 위치로 이동
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        
        return x, y, d
    
    # 특정 방향에서 방문한 적이 없는 노드일 때까지 사이클 반복한다.
    def find_cycle(x, y, d):
        cnt = 0
        while not visited[x][y][d]:
            visited[x][y][d] = True
            cnt += 1
            x, y, d = move(x, y, d)
        return cnt
    
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if not visited[i][j][d]:
		                # 방문하지 않은 노드들의 사이클 길이를 구한다.
                    cycle_length = find_cycle(i, j, d)
                    if cycle_length > 0:
                        answer.append(cycle_length)
    
    return sorted(answer)
