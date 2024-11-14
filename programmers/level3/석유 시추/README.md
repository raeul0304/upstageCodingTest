### **문제 설명**

**[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]**

세로길이가 `n` 가로길이가 `m`인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 당신이 시추관을 수직으로 **단 하나만** 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.

!https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/beb862a9-5382-4f61-adae-bd6e9503c014/%E1%84%89%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B5%E1%84%8E%E1%85%AE-1.drawio.png

예를 들어 가로가 8, 세로가 5인 격자 모양의 땅 속에 위 그림처럼 석유가 발견되었다고 가정하겠습니다. 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리이며, 석유 덩어리의 크기는 덩어리에 포함된 칸의 수입니다. 그림에서 석유 덩어리의 크기는 왼쪽부터 8, 7, 2입니다.

!https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0b10a9f6-6d98-44d6-a342-f984ea47315c/%E1%84%89%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B5%E1%84%8E%E1%85%AE-2.drawio.png

시추관은 위 그림처럼 설치한 위치 아래로 끝까지 뻗어나갑니다. 만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다. 시추관을 설치한 위치에 따라 뽑을 수 있는 석유량은 다음과 같습니다.

| 시추관의 위치 | 획득한 덩어리 | 총 석유량 |
| --- | --- | --- |
| 1 | [8] | 8 |
| 2 | [8] | 8 |
| 3 | [8] | 8 |
| 4 | [7] | 7 |
| 5 | [7] | 7 |
| 6 | [7] | 7 |
| 7 | [7, 2] | 9 |
| 8 | [2] | 2 |

오른쪽 그림처럼 7번 열에 시추관을 설치하면 크기가 7, 2인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 9로 가장 많습니다.

석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 `land`가 매개변수로 주어집니다. 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.

---

### 제한사항

- 1 ≤ `land`의 길이 = 땅의 세로길이 = `n` ≤ 500
    - 1 ≤ `land[i]`의 길이 = 땅의 가로길이 = `m` ≤ 500
    - `land[i][j]`는 `i+1`행 `j+1`열 땅의 정보를 나타냅니다.
    - `land[i][j]`는 0 또는 1입니다.
    - `land[i][j]`가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미합니다.

### 정확성 테스트 케이스 제한사항

- 1 ≤ `land`의 길이 = 땅의 세로길이 = `n` ≤ 100
    - 1 ≤ `land[i]`의 길이 = 땅의 가로길이 = `m` ≤ 100

### 효율성 테스트 케이스 제한사항

- 주어진 조건 외 추가 제한사항 없습니다.

---

### 풀이

- 문제에서 n*m 2차원 배열이 주어진다고 하였으므로 dfs, bfs로 문제를 풀이하면 되는 것이고 라이브러리를 사용하지 않는 dfs를 더 선호하여 아래와 같이 dfs를 작성하였습니다.

```python
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
```

- 추가적으로 효율성이 dfs에서 저하될 수 있어 구간 합 계산(미리 열마다 석유매장의 크기를 더해줌) 방식을 사용하여 최댓값을 구하도록 작성하였습니다.

```python
size_by_col = [0] * m
'''
중략
'''
# 구간 합 계산
max_oil = 0
current_oil = 0
for col in range(m):
    current_oil += size_by_col[col]
    max_oil = max(max_oil, current_oil)
```