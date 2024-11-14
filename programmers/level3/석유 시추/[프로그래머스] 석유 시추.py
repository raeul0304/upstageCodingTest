def dfs(land, visited, x, y, n, m):
    # 이동할 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    stack = [(x, y)]
    visited[x][y] = True
    size = 0
    min_col, max_col = y, y
    
    while stack:
        cx, cy = stack.pop()
        size += 1
        min_col = min(min_col, cy)
        max_col = max(max_col, cy)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return size, min_col, max_col

def solution(land):
    n = len(land) # 세로
    m = len(land[0]) # 가로
    
    visited = [[False] * m for _ in range(n)]
    size_by_col = [0] * m  # 각 열에 석유량을 구간 덧셈 방식으로 기록
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size, min_col, max_col = dfs(land, visited, i, j, n, m)
                
                # 구간 덧셈 방식으로 석유 덩어리 크기를 기록
                size_by_col[min_col] += size
                if max_col + 1 < m:
                    size_by_col[max_col + 1] -= size

    # 구간 합 계산
    max_oil = 0
    current_oil = 0
    for col in range(m):
        current_oil += size_by_col[col]
        max_oil = max(max_oil, current_oil)
    
    return max_oil